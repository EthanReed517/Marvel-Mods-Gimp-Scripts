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
#   v1.1: 30Aug2023: Add support for transparency, add support for next-gen MUA1 (Steam, PS3, and Xbox 360), and add support for MUA2 PS2. Improve efficiency
#   v1.2: 06Sep2023: Now checks if image dimensions are a power of 2 and gives an error if not.
#   v1.3: 10Jan2024: Removed some functions and replaced them with common/basic processes

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
def sizeCheck(currentWidth, currentHeight, skinType, texType):
    # Determine how many primaries and secondaries
    type = skinType + texType
    # Determine the max size based on the texture type
    if type == 0:
        # primary skin and primary texture
        criteria = 256
    elif type == 1:
        # secondary skin or secondary texture
        criteria = 128
    else:
        # secondary skin and secondary texture
        criteria = 64
    # compare the criteria to the current texture size
    if (currentWidth > criteria) or (currentHeight > criteria):
        oversized = True
    else:
        oversized = False
    return oversized

# Define the function for RGB-BGR swapping
def RGB_BGR(image, layer):
    # Perform the swap
    pdb.plug_in_colors_channel_mixer(image, layer, FALSE, 0, 0, 1, 0, 1, 0, 1, 0, 0)
    
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
    
# Define the function for resizing to the max size for PNG8
def resizeMax(image, layer, skinType, texType):
    # Determine how many primaries and secondaries
    type = skinType + texType
    # Determine the max size based on the texture type
    if type == 0:
        # primary skin and primary texture
        maxSize = 256
    elif type == 1:
        # secondary skin or secondary texture
        maxSize = 128
    else:
        # secondary skin and secondary texture
        maxSize = 64
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
    
# Define the function for exporting as a png
def exportPNG(image, layer, dirname, newFolder, fileName, transparency, colors):
    # Check if the export folder exists and create it if needed
    outFolder = pdb.python_fu_marvelmods_basic_folderCheck(dirname, newFolder)
    # Get the new file name
    outFileName = fileName[0:-3] + "png"
    # Get the full save file path
    outFilePath = os.path.join(outFolder, outFileName)
    # Create a duplicate image that can be exported
    exportImage = pdb.gimp_image_duplicate(image)
    # Get the active layer of the new image
    exportLayer = pdb.gimp_image_get_active_layer(exportImage)
    # Determine if the image should be transparent
    if transparency == 1:
        # Not transparent
        # Flatten the Image
        exportLayer = pdb.gimp_image_flatten(exportImage)
        # Index the colors
        exportLayer = pdb.python_fu_marvelmods_basic_indexcolors(exportImage, colors)
    # Export the image
    pdb.file_png_save(exportImage, exportLayer, outFilePath, outFilePath, 0, 9, 0, 0, 0, 0, 0)
    
# Define the function for exporting as a dds
def exportDDS(image, layer, dirname, newFolder, fileName, transparency, BGR):
    # Check if the export folder exists and create it if needed
    outFolder = pdb.python_fu_marvelmods_basic_folderCheck(dirname, newFolder)
    # Get the new file name
    outFileName = fileName[0:-3] + "dds"
    # Get the full save file path
    outFilePath = os.path.join(outFolder, outFileName)
    # Create a duplicate image that can be exported
    exportImage = pdb.gimp_image_duplicate(image)
    # Get the active layer of the new image
    exportLayer = pdb.gimp_image_get_active_layer(exportImage)
    # Determine if the image should be transparent
    if transparency == 1:
        # Not transparent
        # Flatten the Image
        exportLayer = pdb.gimp_image_flatten(exportImage)
        # set the compression (DXT1)
        compression = 1
    else:
        # transparent
        # set the compression (DXT5)
        compression = 3
    # Determine if the image needs to be RGB-BGR swapped
    if BGR == True:
        # RGB-BGR needed
        RGB_BGR(exportImage, exportLayer)
    # Export the image
    pdb.file_dds_save(exportImage, exportLayer, outFilePath, outFilePath, compression, 0, 4, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0)

# Define the main operation
def exportSkin(image, layer, console, skinType, texType, charSize, alchemyVersion, transparency, PSPFormat):
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
    # Check if the dimensions are powers of 2
    powerOf2 = pdb.python_fu_marvelmods_basic_p02check(image, layer)
    if powerOf2 == True:
        # Both dimensions are powers of 2
        # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
        pdb.gimp_selection_none(image)
        # Determine if the image is oversized
        oversized = sizeCheck(currentWidth, currentHeight, skinType, texType)
        # Create a duplicate image that can be manipulated
        modImage = pdb.gimp_image_duplicate(image)
        # Get the active layer of the new image
        modLayer = pdb.gimp_image_get_active_layer(modImage)
        # Begin the export
        # Determine the console
        if console == 1:
            # PC
            # Determine if the image is oversized or transparent
            if (oversized == True) or (transparency == 0):
                # The image is oversized or transparent
                # Determine the version of Alchemy
                if alchemyVersion == 0:
                    # Alchemy 2.5
                    # Export for XML2 PC
                    exportDDS(modImage, modLayer, dirname, "XML2 PC", fileName, transparency, False)
                    # Export for MUA1 PC and Steam
                    exportDDS(modImage, modLayer, dirname, "MUA1 PC and Steam", fileName, transparency, True)
                else:
                    # Alchemy 5
                    # Export for MUA1 PC and Steam
                    exportDDS(modImage, modLayer, dirname, "MUA1 PC and Steam", fileName, transparency, False)
            else:
                # The image is neither oversized nor transparent
                # Export for PC (same folder name regardless of Alchemy version because it'll work for XML2 and MUA1 PC no matter what)
                exportPNG(modImage, modLayer, dirname, "PC", fileName, transparency, 256)
                # Determine the version of Alchemy
                if alchemyVersion == 0:
                    # Alchemy 2.5
                    # Export for MUA1 Steam
                    exportDDS(modImage, modLayer, dirname, "MUA1 Steam", fileName, transparency, True)
                else:
                    # Alchemy 5
                    # Export for MUA1 Steam
                    exportDDS(modImage, modLayer, dirname, "MUA1 Steam", fileName, transparency, False)
        else:
            # all consoles
            # Determine if the image is oversized or transparent
            if (oversized == True) or (transparency == 0):
                # The image is oversized or transparent
                # Determine the version of Alchemy
                if alchemyVersion == 0:
                    # Alchemy 2.5
                    # The secondary skin property should not reduce the threshold for png vs dds on PC, Xbox, and 360.
                    if skinType == 1:
                        # secondary skin
                        oversized2 = sizeCheck(currentWidth, currentHeight, 0, texType)
                        # check if oversized under new conditions
                        if oversized2 == True:
                            # Export for Wii, Xbox, and XML2 PC
                            exportDDS(modImage, modLayer, dirname, "Wii, Xbox, and XML2 PC", fileName, transparency, False)
                            # Export for MUA1 PC, Steam, PS3, and 360
                            exportDDS(modImage, modLayer, dirname, "MUA1 PC, Steam, PS3, and 360", fileName, transparency, True)
                        else:
                            # export for PC, Xbox, and 360
                            exportPNG(modImage, modLayer, dirname, "PC, Xbox, and MUA1 360", fileName, transparency, 256)
                            # Export for Wii
                            exportDDS(modImage, modLayer, dirname, "Wii", fileName, transparency, False)
                            # Export for Steam and PS3
                            exportDDS(modImage, modLayer, dirname, "MUA1 Steam and PS3", fileName, transparency, True)
                    else:
                        # Export for Wii, Xbox, and XML2 PC
                        exportDDS(modImage, modLayer, dirname, "Wii, Xbox, and XML2 PC", fileName, transparency, False)
                        # Export for MUA1 PC, Steam, PS3, and 360
                        exportDDS(modImage, modLayer, dirname, "MUA1 PC, Steam, PS3, and 360", fileName, transparency, True)
                else:
                    # Alchemy 5
                    # The secondary skin property should not reduce the threshold for png vs dds on PC, Xbox, and 360.
                    if skinType == 1:
                        # secondary skin
                        oversized2 = sizeCheck(currentWidth, currentHeight, 0, texType)
                        # check if oversized under new conditions
                        if oversized2 == True:
                            # Export for Wii
                            exportDDS(modImage, modLayer, dirname, "Wii", fileName, transparency, False)
                            # Export for MUA1 PC, Steam, PS3, and 360
                            exportDDS(modImage, modLayer, dirname, "MUA1 PC, Steam, PS3, and 360", fileName, transparency, True)
                        else:
                            # export for PC and 360
                            exportPNG(modImage, modLayer, dirname, "PC, and MUA1 360", fileName, transparency, 256)
                            # Export for Wii
                            exportDDS(modImage, modLayer, dirname, "Wii", fileName, transparency, False)
                            # Export for Steam and PS3
                            exportDDS(modImage, modLayer, dirname, "MUA1 Steam and PS3", fileName, transparency, True)
                    else:
                        # Export for Wii, MUA1 PC, Steam, PS3, and 360
                        exportDDS(modImage, modLayer, dirname, "Wii, MUA1 PC, Steam, PS3, and 360", fileName, transparency, False)
                # resizing should only apply to oversized images
                if oversized == True:
                    # image is oversized
                    # Determine the character size
                    if charSize == 0:
                        # standard size character
                        # Resize to max size for texture type
                        resizeMax(modImage, modLayer, skinType, texType)
                # In the case of oversized or transparent textures, PS2 needs to be exported separately
                exportPNG(modImage, modLayer, dirname, "PS2", fileName, transparency, 256)
            else:
                # The image is neither oversized nor transparent
                # Determine the version of Alchemy
                if alchemyVersion == 0:
                    # Alchemy 2.5
                    # Export for PC, PS2, Xbox, and 360
                    exportPNG(modImage, modLayer, dirname, "PC, PS2, Xbox, and MUA1 360", fileName, transparency, 256)
                    # Export for Wii
                    exportDDS(modImage, modLayer, dirname, "Wii", fileName, transparency, False)
                    # Export for MUA1 Steam and PS3
                    exportDDS(modImage, modLayer, dirname, "MUA1 Steam and PS3", fileName, transparency, True)
                else:
                    # Alchemy 5
                    # Export for PC and 360
                    exportPNG(modImage, modLayer, dirname, "PC, PS2, and MUA1 360", fileName, transparency, 256)
                    # Export for Wii, MUA1 Steam and PS3
                    exportDDS(modImage, modLayer, dirname, "Wii, MUA1 Steam and PS3", fileName, transparency, False)
            # Based on previous steps, image is now at ideal size for PS2. Resize to half size for remaining consoles
            resizeHalf(modImage, modLayer)
            # Non-transparent PNG4 will always have PSP separate
            if (PSPFormat == 0) and (transparency == 1):
                # PSP is separate
                # export PSP
                exportPNG(modImage, modLayer, dirname, "PSP", fileName, transparency, 16)
                # Determine the version of Alchemy
                if alchemyVersion == 0:
                    # Alchemy 2.5
                    # Export for GameCube and MUA2 PS2
                    exportPNG(modImage, modLayer, dirname, "GameCube and MUA2 PS2", fileName, transparency, 256)
                else:
                    # Alchemy 5
                    # Export for MUA2 PS2
                    exportPNG(modImage, modLayer, dirname, "MUA2 PS2", fileName, transparency, 256)
            else:
                # Transparent textures or PSP is PNG8
                if alchemyVersion == 0:
                    # Alchemy 2.5
                    # Export for GameCube, PSP, and MUA2 PS2
                    exportPNG(modImage, modLayer, dirname, "GameCube, PSP, and MUA2 PS2", fileName, transparency, 256)
                else:
                    # Alchemy 5
                    # Export for PSP and MUA2 PS2
                    exportPNG(modImage, modLayer, dirname, "PSP and MUA2 PS2", fileName, transparency, 256)
    else:
        # One or both image dimensions are not powers of 2
        pdb.gimp_message("One or both image dimensions are not a power of 2. Alchemy only supports image dimensions that are powers of 2.\n\nPowers of 2: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, and so on.")

# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_skin",
    "Exports a skin texture in multiple formats. Also\nworks on 3D head textures and mannequin textures.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports a skin texture in multiple formats. Also works on 3D head textures and mannequin textures.",
    "BaconWizard17",
    "BaconWizard17",
    "September 2023",
    "Export Skin",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, 'drawable', 'Layer, mask or channel', None),
        (PF_OPTION,"p1","Console:", 0, ["All","PC Only"]),
        (PF_OPTION,"p1","Skin Type:", 0, ["Primary Skin","Secondary Skin"]),
        (PF_OPTION,"p1","Texture Type:", 0, ["Primary Texture","Secondary Texture"]),
        (PF_OPTION,"p1","Character Size:", 0, ["Standard","Large"]),
        (PF_OPTION,"p1","Alchemy Version:", 0, ["Alchemy 2.5","Alchemy 5"]),
        (PF_OPTION,"p1","Requires Transparency:", 1, ["Yes","No"]),
        (PF_OPTION,"p1","PSP Texture Compression:", 1, ["PNG4","PNG8"])
    ],
    [],
    exportSkin,
    menu='<Image>/Marvel Mods/Export Textures/By Asset Type'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()