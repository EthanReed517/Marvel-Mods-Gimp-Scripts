#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a single skin preview in 3 different formats.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 22Apr2023: First published version.

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
# Define the function for resizing to correct dimensions
def resize(image, layer, widthFactor):
    # Get the current dimensions of the image
    currentWidth = image.width
    currentHeight = image.height
    # Get the new dimensions
    newWidth = currentHeight * widthFactor
    # scale the image accordingly
    pdb.gimp_image_scale(image, newWidth, currentHeight)
    # Resize the layer to the image size
    pdb.gimp_layer_resize_to_image_size(layer)
    # Display the changes
    pdb.gimp_displays_flush()

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
def resizeHalf(image, layer):
    # Get the current dimensions of the image
    currentWidth = image.width
    currentHeight = image.height
    # Get the new dimensions by dividing old dimensions by 2
    newWidth = currentWidth/2
    newHeight = currentHeight/2
    # scale the image accordingly
    pdb.gimp_image_scale(image, newWidth, newHeight)
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
    
# Define the function for exporting as a DXT1 dds
def exportDXT1(image, layer, dirname, newFolder, fileName):
    # Check if the export folder exists and create it if needed
    outFolder = folderCheck(dirname, newFolder)
    # Get the new file name
    outFileName = fileName[0:-3] + "dds"
    # Get the full save file path
    outFilePath = os.path.join(outFolder, outFileName)
    # Export the image
    pdb.file_dds_save(image, layer, outFilePath, outFilePath, 1, 0, 4, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0)
    
# Define the function for exporting as a png
def exportPNG(image, layer, dirname, newFolder, fileName):
    # Check if the export folder exists and create it if needed
    outFolder = folderCheck(dirname, newFolder)
    # Get the new file name
    outFileName = fileName[0:-3] + "png"
    # Get the full save file path
    outFilePath = os.path.join(outFolder, outFileName)
    # Export the image
    pdb.file_png_save(image, layer, outFilePath, outFilePath, 0, 9, 0, 0, 0, 0, 0)
    

# Define the operation
def exportLoading(image, layer, game, console, asset):
    # Get the file path of the original image
    filePath = pdb.gimp_image_get_filename(image)
    # Save the file in its original format before proceeding
    pdb.gimp_file_save(image, layer, filePath, filePath)
    # Get the folder and file name from the file path
    dirname = os.path.dirname(filePath)
    fileName = os.path.basename(filePath)
    # Get the current dimensions of the image
    currentWidth = image.width
    currentHeight = image.height
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Create a duplicate image that can be manipulated
    exportImage = pdb.gimp_image_duplicate(image)
    # Get the active layer of the new image
    exportLayer = pdb.gimp_image_get_active_layer(exportImage)
    # Flatten the Image
    exportLayer = pdb.gimp_image_flatten(exportImage)
    # Determine the game
    if game == 0:
        # The game is XML1/XML2
        # Determine the console
        if console == 0:
            # Cross-compatible
            # Check the size
            if currentHeight > 1024:
                # Too big for consoles but will work for PC
                # Resize the texture correctly
                resize(exportImage, exportLayer, 1)
                # Export the image
                exportDXT1(exportImage, exportLayer, dirname, "PC", fileName)
                # Resize the image
                resizeHalf(exportImage, exportLayer)
                # Export the image
                exportDXT1(exportImage, exportLayer, dirname, "Xbox", fileName)
            else:
                # Size works for PC and consoles
                # Resize the texture correctly
                resize(exportImage, exportLayer, 1)
                # Export the image
                exportDXT1(exportImage, exportLayer, dirname, "PC and Xbox", fileName)
            # Resize the image
            resizeHalf(exportImage, exportLayer)
            # Export the image
            exportDXT1(exportImage, exportLayer, dirname, "GameCube", fileName)
            # Index colors
            convertIndexed(exportImage, 256)
            # Export the image
            exportPNG(exportImage, exportLayer, dirname, "PS2", fileName)
        elif console == 1:
            # PC-only
            # Resize the texture correctly
            resize(exportImage, exportLayer, 1)
            # Export the image
            exportDXT1(exportImage, exportLayer, dirname, "PC", fileName)
        else:
            # PSP
            print("temp")
    else:
        # The game is MUA1
        # Determine the console
        if console == 0:
            # Cross-compatible
            # Check the size
            if currentHeight > 1024:
                # Too big for consoles but will work for PC
                # Resize the texture correctly
                resize(exportImage, exportLayer, 2)
                # RGB-BGR swap the image
                RGB_BGR(exportImage, exportLayer)
                # Export the image
                exportDXT1(exportImage, exportLayer, dirname, "PC", fileName)
                # Resize the image
                resizeHalf(exportImage, exportLayer)
                # Export the image
                exportDXT1(exportImage, exportLayer, dirname, "NG", fileName)
            else:
                # Size works for PC and consoles
                # Resize the texture correctly
                resize(exportImage, exportLayer, 2)
                # RGB-BGR swap the image
                RGB_BGR(exportImage, exportLayer)
                # Export the image
                exportDXT1(exportImage, exportLayer, dirname, "PC and NG", fileName)
            # Resize the texture correctly
            resize(exportImage, exportLayer, 1)
            # RGB-BGR swap the image
            RGB_BGR(exportImage, exportLayer)
            # Export the image
            exportDXT1(exportImage, exportLayer, dirname, "Wii and Xbox", fileName)
            # Resize the image
            resizeHalf(exportImage, exportLayer)
            # Index colors
            convertIndexed(exportImage, 256)
            # Export the image
            exportPNG(exportImage, exportLayer, dirname, "PS2", fileName)
        elif console == 1:
            # PC-only
            # Resize the texture correctly
            resize(exportImage, exportLayer, 2)
            # RGB-BGR swap the image
            RGB_BGR(exportImage, exportLayer)
            # Export the image
            exportDXT1(exportImage, exportLayer, dirname, "PC", fileName)
        else:
            # PSP
            print("temp")

# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_loading",
    "Exports a loading screen, comic book cover, or\nconcept art texture to different formats and\nsizes.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports a loading screen, comic book cover, or concept art texture to different formats and sizes.",
    "BaconWizard17",
    "BaconWizard17",
    "April 2024",
    "Export Loading Screen, Comic, or Concept Art",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, 'drawable', 'Layer, mask or channel', None),
        (PF_OPTION,"p1","Game:", 0, ["XML1/XML2","MUA1"]),
        (PF_OPTION,"p1","Console:", 0, ["All (Except PSP)","PC Only","PSP Only"]),
        (PF_OPTION,"p1","Asset Type:", 0, ["Loading Screen","Comic Cover","Concept Art"])
    ],
    [],
    exportLoading,
    menu='<Image>/Marvel Mods/Export Textures/By Asset Type'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()