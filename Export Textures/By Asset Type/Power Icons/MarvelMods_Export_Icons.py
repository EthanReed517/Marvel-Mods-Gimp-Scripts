#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export power icons
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 01Feb2023: First published version.

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.


# ####### #
# IMPORTS #
# ####### #
# Import the OS module to be able to check file paths
import os
# Import the gimpfu module so that scripts can be executed
from gimpfu import*


# ######### #
# FUNCTIONS #
# ######### #
# Define the function for RGB-BGR swapping
def RGB_BGR(image, layer):
    # Perform the swap
    pdb.plug_in_colors_channel_mixer(image, layer, FALSE, 0, 0, 1, 0, 1, 0, 1, 0, 0)
    # Display the changes
    pdb.gimp_displays_flush()
    
# Define the function for indexing colors
def convertIndexed(image, colors):
    # Index the colors
    pdb.gimp_image_convert_indexed(image, CONVERT_DITHER_NONE, CONVERT_PALETTE_GENERATE, colors, FALSE, FALSE, "")
    # Display the changes
    pdb.gimp_displays_flush()
    # Get the active layer
    layer = pdb.gimp_image_get_active_layer(image)
    # return the new layer
    return layer
    
# Define the function for resizing to half size
def resizeHalf(image, layer, newSize):
    # scale the image accordingly
    pdb.gimp_image_scale(image, newSize, newSize)
    # Resize the layer to the image size
    pdb.gimp_layer_resize_to_image_size(layer)
    # Display the changes
    pdb.gimp_displays_flush()

# Define the folder checking operation
def folderCheck(dirname, newFolder):
    # Append the paths
    outFolder = os.path.join(dirname, newFolder)
    # Check if the path exists
    outFolderExists = os.path.exists(outFolder)
    # If the path doesn't exist, create the new folder
    if outFolderExists == False:
        os.mkdir(outFolder)
    # Return the new path
    return outFolder
    
# Define the function for exporting as a png
def exportPNG(image, layer, dirname, newFolder, fileName, icons2):
    # Check if the export folder exists and create it if needed
    outFolder = folderCheck(dirname, newFolder)
    # Get the new file name
    if icons2 == True:
        outFileName = fileName[0:-5] + "2.png"
    else:
        outFileName = fileName[0:-3] + "png"
    # Get the full save file path
    outFilePath = os.path.join(outFolder, outFileName)
    # Export the image
    pdb.file_png_save(image, layer, outFilePath, outFilePath, 0, 9, 0, 0, 0, 0, 0)

# Define the function for exporting as a DXT1 dds
def exportDXT1(image, layer, dirname, newFolder, fileName, icons2):
    # Check if the export folder exists and create it if needed
    outFolder = folderCheck(dirname, newFolder)
    # Get the new file name
    if icons2 == True:
        outFileName = fileName[0:-5] + "2.dds"
    else:
        outFileName = fileName[0:-3] + "dds"
    # Get the full save file path
    outFilePath = os.path.join(outFolder, outFileName)
    # Export the image
    pdb.file_dds_save(image, layer, outFilePath, outFilePath, 1, 0, 4, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0)

# Define the main operation
def exportIcons(baseImage, baseLayer, console, game):
    # Get the file path of the original image
    filePath = pdb.gimp_image_get_filename(baseImage)    
    # Save the file in its original format before proceeding
    pdb.gimp_file_save(baseImage, baseLayer, filePath, filePath)
    # Get the folder and file name from the file path
    dirname = os.path.dirname(filePath)
    fileName = os.path.basename(filePath)
    # Create a duplicate image that can be manipulated
    image = pdb.gimp_image_duplicate(baseImage)
    # Get the active layer of the new image
    layer = pdb.gimp_image_get_active_layer(image)
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Flatten the Image
    layer = pdb.gimp_image_flatten(image)
    # Begin the Export
    # Pick the console
    if game == 0:
        # XML1
        # Ensure that the image is the proper size
            # Get the current dimensions of the image
        currentWidth = image.width
        currentHeight = image.height
        # Determine if the image is oversized
        if (currentWidth > 128) or (currentHeight > 128):
            resizeHalf(image, layer, 128)
        # Index the colors
        layer = convertIndexed(image, 256)
        # Export the image
        exportPNG(image, layer, dirname, "All", fileName, False)
    elif game == 1:
        # XML2
        # Get the current dimensions of the image
        currentWidth = image.width
        currentHeight = image.height
        # Determine if an icons2 file is needed
        if (currentWidth > 128) or (currentHeight > 128):
            icons2 = True
        else:
            icons2 = False
        # Decide what icons are needed
        if icons2 == True:
            # Export icons2
            # Pick the console
            if console == 1:
                # PC Only
                # Determine if PC needs high res icons
                if (currentWidth > 256) or (currentHeight > 256):
                    # 512x512 icons, export the PC as a dds
                    exportDXT1(image, layer, dirname, newFolder, "icons2 (PC)", True)
                else:
                    # 256x256 icons, export as PNG8
                    # Index the colors
                    layer = convertIndexed(image, 256)
                    # Export the image
                    exportPNG(image, layer, dirname, "icons2 (PC)", fileName, True)
                    # Color mode back to RGB
                    pdb.gimp_image_convert_rgb(image)
                # Resize to 128x128
                resizeHalf(image, layer, 128)
                # Index the colors
                layer = convertIndexed(image, 256)
                # Export the image
                exportPNG(image, layer, dirname, "icons1 (PC)", fileName, False)
            else:
                # All consoles
                # Determine if PC needs high res icons
                if (currentWidth > 256) or (currentHeight > 256):
                    # 512x512 icons, export the PC as a dds
                    exportDXT1(image, layer, dirname, newFolder, "icons2 (PC)", True)
                    # Scale to 256x256
                    resizeHalf(image, layer, 256)
                    # Index the colors
                    layer = convertIndexed(image, 256)
                    # Export the image
                    exportPNG(image, layer, dirname, "icons2 (PSP, XB)", fileName, True)
                else:
                    # 256x256 icons, export the PC with Xbox
                    # Index the colors
                    layer = convertIndexed(image, 256)
                    # Export the image
                    exportPNG(image, layer, dirname, "icons2 (All)", fileName, True)
                # Color mode back to RGB
                pdb.gimp_image_convert_rgb(image)
                # Resize to 128x128
                resizeHalf(image, layer, 128)
                # Index the colors
                layer = convertIndexed(image, 256)
                # Export the image
                exportPNG(image, layer, dirname, "icons1 (All)", fileName, False)
        else: 
            # Do not export icons2
            # Index the colors
            layer = convertIndexed(image, 256)
            # Determine the console
            if console == 1:
                # PC only
                # Export the image
                exportPNG(image, layer, dirname, "icons1 (PC)", fileName, False)
            else:
                # All consoles
                # Export the image
                exportPNG(image, layer, dirname, "icons1 (All)", fileName, False)
    elif game == 2:
        # MUA1
        # Determine if the image is oversized
        if (currentWidth > 256) or (currentHeight > 256):
            resizeHalf(image, layer, 256)
        # Determine the console
        if console == 0:
            # All
            # Export the image
            exportPNG(image, layer, dirname, "NG", fileName, False)
            # Resize the image
            resizeHalf(image, layer, 128)
            # Export the image
            exportPNG(image, layer, dirname, "LG", fileName, False)
        if console == 1:
            # PC only
            # Export the image
            exportPNG(image, layer, dirname, "PC", fileName, False)            
    else:
        # MUA2
        # Determine if the image is oversized
        if (currentWidth > 128) or (currentHeight > 128):
            resizeHalf(image, layer, 128)
        # Export the image
        exportPNG(image, layer, dirname, "All", fileName, False)

# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_icons",
    "Exports a power icons texture in multiple formats.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports a power icons texture in multiple formats.",
    "BaconWizard17",
    "BaconWizard17",
    "February 2023",
    "Export Power Icons",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, 'drawable', 'Layer, mask or channel', None),
        (PF_OPTION,"p1","Console:", 0, ["All","PC Only"]),
        (PF_OPTION,"p1","Game:", 0, ["XML1","XML2","MUA1","MUA2"])
    ],
    [],
    exportIcons,
    menu='<Image>/Marvel Mods/Export Textures/By Asset Type'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()