#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a skin, 3D head, or mannequin texture.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 30Jan2023: First published version.

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
# Define the size checking operation
def sizeCheck(currentWidth, currentHeight, texType):
    if texType == 0:
        criteria = 256
    else:
        criteria = 128
    if (currentWidth > criteria) or (currentHeight > criteria):
        oversized = True
    else:
        oversized = False
    return oversized
    
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

# Define the function for RGB-BGR swapping
def RGB_BGR(image, layer):
    # Perform the swap
    pdb.plug_in_colors_channel_mixer(image, layer, FALSE, 0, 0, 1, 0, 1, 0, 1, 0, 0)
    # Display the changes
    pdb.gimp_displays_flush()
    
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
    
# Define the function for resizing to the max size for PNG8
def resizeMax(image, layer, texType):
    # Determine the max size based on the texture type:
    if texType == 0:
        # primary texture
        maxSize = 256
    else:
        # secondary texture
        maxSize = 128
    # Get the current dimensions of the image
    currentWidth = float(image.width)
    currentHeight = float(image.height)
    # Check which is bigger
    if currentWidth >= currentHeight:
        # Wide image or square
        scaleFactor = maxSize / currentWidth
    else:
        # Tall image
        scaleFactor = maxSize / currentHeight
    # Get the new sizes
    newWidth = scaleFactor * currentWidth
    newHeight = scaleFactor * currentHeight
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

# Define the main operation
def exportSkinQuick(image, layer):
    # Define the remaining variables
    console = 0
    skinType = 0
    texType = 0
    charSize = 0
    alchemyVersion = 0
    PSPFormat = 1
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
    # Start an undo group so that the entire operation can be undone at once
    pdb.gimp_image_undo_group_start(image)
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Flatten the Image
    layer = pdb.gimp_image_flatten(image)
    # Determine if the image is oversized
    oversized = sizeCheck(currentWidth, currentHeight, texType)
    # Begin the export
    if oversized == True:
        # The original texture size is above 256x256 for primary textures of 128x128 for secondary textures
        # Choose the console
        if console == 1:
            # PC only
            # Pick the version of Alchemy being used for skin creation
            if alchemyVersion == 0:
                # Alchemy 2.5
                # Export the image
                exportDXT1(image, layer, dirname, "XML2 PC", fileName)
                # RGB-BGR swap the image
                RGB_BGR(image, layer)
                # Export the image
                exportDXT1(image, layer, dirname, "MUA1 PC", fileName)
                # return from BGR to RGB
                RGB_BGR(image, layer)
            else:
                # Alchemy 5
                # RGB-BGR swap the image
                RGB_BGR(image, layer)
                # Export the image
                exportDXT1(image, layer, dirname, "MUA1 PC", fileName)           
        else: 
            # All consoles
            # Pick the version of Alchemy
            if alchemyVersion == 0:
                # Alchemy 2.5
                # Export the image
                exportDXT1(image, layer, dirname, "Wii, Xbox, and XML2 PC", fileName)
                # RGB-BGR swap the image
                RGB_BGR(image, layer)
                # Export the image
                exportDXT1(image, layer, dirname, "MUA1 PC", fileName)
                # BGR back to RGB
                RGB_BGR(image, layer)
                # Check if the character is oversized or standard
                if charSize == 0:
                    # standard size character
                    # Resize to max size for texture type
                    resizeMax(image, layer, texType)
                # Check if the skin is primary or secondary
                if skinType == 1:
                    # secondary skin, resize further
                    # resize to half size
                    resizeHalf(image, layer)
                # Convert to PNG8
                layer = convertIndexed(image, 256)
                # Export the image
                exportPNG(image, layer, dirname, "PS2", fileName)
                # Color mode back to RGB
                pdb.gimp_image_convert_rgb(image)
                # Resize to half size
                resizeHalf(image, layer)
                # Convert to PNG8
                layer = convertIndexed(image, 256)
                # Check which format is being used for PSP
                if PSPFormat == 0:
                    # Use PNG4 for PSP
                    # Export the image
                    exportPNG(image, layer, dirname, "GameCube", fileName)
                    # Color mode back to RGB
                    pdb.gimp_image_convert_rgb(image)
                    # Convert to PNG4
                    layer = convertIndexed(image, 16)
                    # Export the image
                    exportPNG(image, layer, dirname, "PSP", fileName)
                else:
                    # use PNG8 for PSP
                    # Export the image
                    exportPNG(image, layer, dirname, "GameCube and PSP", fileName)
            else:
                # Alchemy 5
                # Export the image
                exportDXT1(image, layer, dirname, "Wii and MUA1 PC", fileName)
                # Check if the character is oversized or standard
                if charSize == 0:
                    # standard size character
                    # Resize to max size for texture type
                    resizeMax(image, layer, texType)
                # Convert to PNG8
                layer = convertIndexed(image, 256)
                # Export the image
                exportPNG(image, layer, dirname, "PS2", fileName)
                # Color mode back to RGB
                pdb.gimp_image_convert_rgb(image)
                # Resize to half size
                resizeHalf(image, layer)
                # Check which format is being used for PSP
                if PSPFormat == 0:
                    # Use PNG4 for PSP
                    # Convert to PNG4
                    layer = convertIndexed(image, 16)
                else:
                    # use PNG8 for PSP
                    # Convert to PNG8
                    layer = convertIndexed(image, 256)
                # Export the image
                exportPNG(image, layer, dirname, "PSP", fileName)
    else: 
        # The original texture is 256x256 or less for primary textures or 128x128 for secondary textures
        # Choose the console
        if console == 1:
            # PC only
            # Alchemy version doesn't matter
            # Convert to PNG8
            layer = convertIndexed(image, 256)
            # Export the image
            exportPNG(image, layer, dirname, "PC", fileName)
        else:
            # All consoles
            # Pick the version of Alchemy
            if alchemyVersion == 0:
                # Alchemy 2.5
                # Export the image
                exportDXT1(image, layer, dirname, "Wii", fileName)
                # Convert to PNG8
                layer = convertIndexed(image, 256)
                # Check if it is a primary or secondary skin
                if skinType == 0:
                    # Primary skin
                    # Export the image
                    exportPNG(image, layer, dirname, "PC, PS2, and Xbox", fileName)
                    # Color mode back to RGB
                    pdb.gimp_image_convert_rgb(image)
                    # Resize to half size
                    resizeHalf(image, layer)
                    # Convert to PNG8
                    layer = convertIndexed(image, 256)
                    # Check the texture format used by PSP
                    if PSPFormat == 1:
                        # PSP uses PNG8 format
                        # Export the image
                        exportPNG(image, layer, dirname, "GameCube and PSP", fileName)
                    else:
                        # PSP uses PNG4 format
                        # Export the image
                        exportPNG(image, layer, dirname, "GameCube", fileName)
                        # Color mode back to RGB
                        pdb.gimp_image_convert_rgb(image)
                        # Convert to PNG4
                        layer = convertIndexed(image, 16)
                        # Export the image
                        exportPNG(image, layer, dirname, "PSP", fileName)
                else:
                    # secondary skin
                    # Export the image
                    exportPNG(image, layer, dirname, "PC and Xbox", fileName)
                    # Color mode back to RGB
                    pdb.gimp_image_convert_rgb(image)
                    # Resize to half size
                    resizeHalf(image, layer)
                    # Convert to PNG8
                    layer = convertIndexed(image, 256)
                    # Export the image
                    exportPNG(image, layer, dirname, "PS2", fileName)
                    # Color mode back to RGB
                    pdb.gimp_image_convert_rgb(image)
                    # Resize to half size
                    resizeHalf(image, layer)
                    # Convert to PNG8
                    layer = convertIndexed(image, 256)
                    # Check the texture format used by PSP
                    if PSPFormat == 1:
                        # PSP uses PNG8 format
                        # Export the image
                        exportPNG(image, layer, dirname, "GameCube and PSP", fileName)
                    else:
                        # PSP uses PNG4 format
                        # Export the image
                        exportPNG(image, layer, dirname, "GameCube", fileName)
                        # Color mode back to RGB
                        pdb.gimp_image_convert_rgb(image)
                        # Convert to PNG4
                        layer = convertIndexed(image, 16)
                        # Export the image
                        exportPNG(image, layer, dirname, "PSP", fileName)
            else:
                # Alchemy 5
                # Export the image
                exportDXT1(image, layer, dirname, "Wii", fileName)
                # Check if it is a primary or secondary skin
                if skinType == 0:
                    # Primary skin
                    # Convert to PNG8
                    layer = convertIndexed(image, 256)
                    # Export the image
                    exportPNG(image, layer, dirname, "PS2", fileName)
                    # Color mode back to RGB
                    pdb.gimp_image_convert_rgb(image)
                    # Resize to half size
                    resizeHalf(image, layer)
                    # Check the texture format used by PSP
                    if PSPFormat == 1:
                        # PSP uses PNG8 format
                        # Convert to PNG8
                        layer = convertIndexed(image, 256)
                    else:
                        # PSP uses PNG4 format
                        # Convert to PNG4
                        layer = convertIndexed(image, 16)
                    # Export the image
                    exportPNG(image, layer, dirname, "PSP", fileName)
                else:
                    # secondary skin
                    # Color mode back to RGB
                    pdb.gimp_image_convert_rgb(image)
                    # Resize to half size
                    resizeHalf(image, layer)
                    # Convert to PNG8
                    layer = convertIndexed(image, 256)
                    # Export the image
                    exportPNG(image, layer, dirname, "PS2", fileName)
                    # Color mode back to RGB
                    pdb.gimp_image_convert_rgb(image)
                    # Resize to half size
                    resizeHalf(image, layer)
                    # Check the texture format used by PSP
                    if PSPFormat == 1:
                        # PSP uses PNG8 format
                        # Convert to PNG8
                        layer = convertIndexed(image, 256)
                    else:
                        # PSP uses PNG4 format
                        # Convert to PNG4
                        layer = convertIndexed(image, 16)
                    # Export the image
                    exportPNG(image, layer, dirname, "PSP", fileName)
    # End the undo group
    pdb.gimp_image_undo_group_end(image)

# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_skin_quick",
    "Exports a skin texture in multiple formats. Also\nworks on 3D head textures and mannequin textures.\nThis is an optimized version that runs without\noptions and with my preferred settings.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports a skin texture in multiple formats. Also works on 3D head textures and mannequin textures.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2023",
    "Export Skin (Quick)",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, 'drawable', 'Layer, mask or channel', None)
    ],
    [],
    exportSkinQuick,
    menu='<Image>/Marvel Mods/Export Textures/By Asset Type'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()