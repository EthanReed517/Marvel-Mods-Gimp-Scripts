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
#   v2.0: 24Jan2024: Full rewrite. More use of basic procedures. Alchemy 2.5 transparency now uses plain png only. Better logic for different texture types.
#   v2.1: 01Mar2024: Focused purely on primary textures to simplify the code

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
# To be able to check file paths
import os
# To be able to execute GIMP scripts
from gimpfu import*


# ######### #
# FUNCTIONS #
# ######### #
# Define the function to check for image errors
def errorCheck(image, layer):
    # Get the current dimensions of the image
    currentWidth = image.width
    currentHeight = image.height
    # Set the initial error state
    canProceed = False
    # Check if the dimensions are powers of 2
    powerOf2 = pdb.python_fu_marvelmods_basic_p02check(image, layer)
    # Determine next steps based on power of 2 check
    if powerOf2 == True:
        # Image dimensions are powers of 2, can proceed
        canProceed = True
    else:
        # Image dimensions are not powers of 2
        # Give error message
        pdb.gimp_message("ERROR: One or both image dimensions are not a power of 2. Alchemy only supports image dimensions that are powers of 2.\n\nPowers of 2: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, and so on.")
    # Return whether or not the script can proceed, as well as the width and height
    return canProceed, currentWidth, currentHeight

# Define the size checking operation
def sizeCheck(currentWidth, currentHeight):
    # compare the criteria to the current texture size
    if (currentWidth > 256) or (currentHeight > 256):
        oversized = True
    else:
        oversized = False
    return oversized
    
# Define the function for resizing to the max size for PNG8
def resizeMax(image, layer, skinType):
    # Determine the max size based on the texture type
    if skinType == 0:
        # primary skin
        maxSize = 256
    else:
        # secondary skin
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

# Define the main operation
def exportSkin(image, layer, console, skinType, charSize, alchemyVersion, transparency, pspFormat):
    # Save the file and get its path and name
    (folderName, fileName) = pdb.python_fu_marvelmods_basic_get_path_save(image, layer)
    # Check for errors
    (canProceed, currentWidth, currentHeight) = errorCheck(image, layer)
    # Determine if it's okay to proceed
    if canProceed == True:
        # No errors, can proceed
        # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
        pdb.gimp_selection_none(image)
        # Determine if the image is oversized
        oversized = sizeCheck(currentWidth, currentHeight)
        # Create a duplicate image that can be manipulated
        exportImage = pdb.gimp_image_duplicate(image)
        # Get the active layer of the new image
        exportLayer = pdb.gimp_image_get_active_layer(exportImage)
        # Begin the export
        # Determine if the image is oversized
        if oversized == True:
            # The image is oversized
            # Determine the console
            if console == 1:
                # PC Only
                # Determine if the image needs transparency
                if transparency == 0:
                    # The image is transparent
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for PC and MUA1 Steam
                        pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC and MUA1 Steam", fileName, 0)
                    else:
                        # Alchemy 5
                        # Export for MUA1 PC and Steam
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 PC and Steam", fileName, 2, 0)
                else:
                    # The image is not transparent
                    # Flatten the image
                    exportLayer = pdb.gimp_image_flatten(exportImage)
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for XML2 PC
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "XML2 PC", fileName, 0, 0)
                        # Export for MUA1 PC and Steam
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 PC and Steam", fileName, 0, 1)
                    else:
                        # Alchemy 5
                        # Export for MUA1 PC and Steam
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 PC and Steam", fileName, 0, 0)
            else:
                # All consoles
                # Determine if the image needs transparency
                if transparency == 0:
                    # The image is transparent
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Determine the character size
                        if charSize == 0:
                            # Standard size character
                            # Export for many consoles
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC, Wii, Xbox, MUA1 Steam, PS3, and 360", fileName, 0)
                            # Reduce to the max size for PS2 per the parameters
                            resizeMax(exportImage, exportLayer, skinType)
                            # Export for PS2
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PS2", fileName, 0)
                        else:
                            # Big character
                            # Export for many consoles
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC, PS2, Wii, Xbox, MUA1 Steam, PS3, and 360", fileName, 0)
                        # Resize to half size
                        pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                        # Export for GameCube, PSP, and MUA2 PS2
                        pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "GameCube, PSP, and MUA2 PS2", fileName, 0)
                    else:
                        # Alchemy 5
                        # Export for Wii
                        pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "Wii", fileName, 0)
                        # Export for MUA1 PC, Steam, PS3, and 360
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 PC, Steam, PS3, and 360", fileName, 2, 0)
                        # Determine the character size
                        if charSize == 0:
                            # Standard size character
                            # Reduce to the max size for PS2 per the parameters
                            resizeMax(exportImage, exportLayer, skinType)
                        # Resize to half size
                        pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                        # Export for PSP and MUA2 PS2
                        pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PSP and MUA2 PS2", fileName, 0)
                else:
                    # The image is not transparent
                    # Flatten the image
                    exportLayer = pdb.gimp_image_flatten(exportImage)
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for Wii, Xbox, and XML2 PC
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "Wii, Xbox, and XML2 PC", fileName, 0, 0)
                        # Export for next-gen MUA1
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 PC, Steam, PS3, and 360", fileName, 0, 1)
                        # Determine the character size
                        if charSize == 0:
                            # Standard size character
                            # Reduce to the max size for PS2 per the parameters
                            resizeMax(exportImage, exportLayer, skinType)
                        # Export for PS2
                        pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PS2", fileName, 2)
                        # Resize to half size
                        pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                        # Determine the PSP format
                        if pspFormat == 0:
                            # PNG4
                            # Export for PSP
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PSP", fileName, 1)
                            # Export for GameCube and MUA2 PS2
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "GameCube and MUA2 PS2", fileName, 2)
                        else:
                            # PNG8
                            # Export for GameCube, PSP, and MUA2 PS2
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "GameCube, PSP, and MUA2 PS2", fileName, 2)
                    else:
                        # Alchemy 5
                        # Export for Wii and next-gen MUA1
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "Wii, MUA1 PC, Steam, PS3, and 360", fileName, 0, 0)
                        # Determine the character size
                        if charSize == 0:
                            # Standard size character
                            # Reduce to the max size for PS2 per the parameters
                            resizeMax(exportImage, exportLayer, skinType)
                        # Resize to half size
                        pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                        # Determine the PSP format
                        if pspFormat == 0:
                            # PNG4
                            # Export for PSP
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PSP", fileName, 1)
                            # Export for MUA2 PS2
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "MUA2 PS2", fileName, 2)
                        else:
                            # PNG8
                            # Export for PSP and MUA2 PS2
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PSP and MUA2 PS2", fileName, 2)
        else:
            # The image is not oversized
            # Determine the console
            if console == 1:
                # PC Only
                # Determine if the image needs transparency
                if transparency == 0:
                    # The image is transparent
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for PC and Steam
                        pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC and MUA1 Steam", fileName, 0)
                    else:
                        # Alchemy 5
                        # Export for PC
                        pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "MUA1 PC", fileName, 0)
                        # Export for Steam
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 Steam", fileName, 2, 0)
                else:
                    # The image is not transparent
                    # Flatten the image
                    exportLayer = pdb.gimp_image_flatten(exportImage)
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for PC
                        pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC", fileName, 2)
                        # Export for Steam
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 Steam", fileName, 0, 1)
                    else:
                        # Alchemy 5
                        # Export for PC
                        pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "MUA1 PC", fileName, 2)
                        # Export for Steam
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 Steam", fileName, 0, 0)
            else:
                # All consoles
                # Determine if the image needs transparency
                if transparency == 0:
                    # The image is transparent
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Determine the skin type
                        if skinType == 0:
                            # Primary skin
                            # Export for main consoles
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC, PS2, Xbox, Wii, MUA1 Steam, PS3, and 360", fileName, 0)
                        else:
                            # Secondary skin
                            # Export for main consoles (not PS2)
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC, Xbox, Wii, MUA1 Steam, PS3, and 360", fileName, 0)
                            # Resize to half size
                            pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                            # Export for PS2
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PS2", fileName, 0)
                        # Resize to half size
                        pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                        # Export for GameCube, PSP, and MUA2 PS2
                        pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "GameCube, PSP, and MUA2 PS2", fileName, 0)
                    else:
                        # Alchemy 5
                        # Export for PC
                        pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "Wii, MUA1 PC and 360", fileName, 0)
                        # Export for Steam
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 Steam and PS3", fileName, 2, 0)
                        # Determine the skin type
                        if skinType == 0:
                            # Primary skin
                            # Resize to half size
                            pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                        else:
                            # Secondary skin
                            # Resize to quarter size
                            pdb.python_fu_marvelmods_scaling_scaleQuarter(exportImage, exportLayer)
                        # Export for GameCube, PSP, and MUA2 PS2
                        pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PSP and MUA2 PS2", fileName, 0)
                else:
                    # The image is not transparent
                    # Flatten the image
                    exportLayer = pdb.gimp_image_flatten(exportImage)
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for Wii
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "Wii", fileName, 0, 0)
                        # Export for Steam and PS3
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 Steam and PS3", fileName, 0, 1)
                        # Determine if this is a primary or secondary skin
                        if skinType == 0:
                            # Primary
                            # Export for PC, PS2, Xbox, and MUA1 360
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC, PS2, Xbox, and MUA1 360", fileName, 2)
                        else:
                            # Secondary
                            # Export for PC, Xbox, and MUA1 360
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC, Xbox, and MUA1 360", fileName, 2)
                            # Resize to half size
                            pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                            # Export for PS2
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PS2", fileName, 2)
                        # Resize to half size
                        pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                        # Determine the PSP format
                        if pspFormat == 0:
                            # PNG4
                            # Export for PSP
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PSP", fileName, 1)
                            # Export for GameCube and MUA2 PS2
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "GameCube and MUA2 PS2", fileName, 2)
                        else:
                            # PNG8
                            # Export for GameCube, PSP, and MUA2 PS2
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "GameCube, PSP, and MUA2 PS2", fileName, 2)
                    else:
                        # Alchemy 5
                        # Export for PC
                        pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "MUA1 PC and 360", fileName, 2)
                        # Export for Steam
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "Wii, MUA1 Steam and PS3", fileName, 0, 0)
                        # Determine the skin type
                        if skinType == 0:
                            # Primary skin
                            # Resize to half size
                            pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                        else:
                            # Secondary skin
                            # Resize to quarter size
                            pdb.python_fu_marvelmods_scaling_scaleQuarter(exportImage, exportLayer)                            
                        # Determine the PSP format
                        if pspFormat == 0:
                            # PNG4
                            # Export for PSP
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PSP", fileName, 1)
                            # Export for MUA2 PS2
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "MUA2 PS2", fileName, 2)
                        else:
                            # PNG8
                            # Export for PSP and MUA2 PS2
                            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PSP and MUA2 PS2", fileName, 2)
        # Announce completion
        pdb.gimp_message("Export complete.")
    else:
        # Errors, cannot proceed
        # Display an error message
        pdb.gimp_message("The image was not exported.")


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_asset_skin",
    "Exports a skin texture in multiple formats. Also\nworks on 3D head textures and mannequin textures.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports a skin texture in multiple formats. Also works on 3D head textures and mannequin textures.",
    "BaconWizard17",
    "BaconWizard17",
    "March 2024",
    "Export Skin, Mannequin, or 3D Head (Primary Texture)",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask or channel", None),
        (PF_OPTION, "console", "Console:", 0, ["All","PC Only"]),
        (PF_OPTION, "skinType", "Skin Type:", 0, ["Primary Skin","Secondary Skin"]),
        (PF_OPTION, "charSize", "Character Size:", 0, ["Standard","Large"]),
        (PF_OPTION, "alchemyVersion", "Alchemy Version:", 0, ["Alchemy 2.5","Alchemy 5"]),
        (PF_OPTION, "transparency", "Requires Transparency:", 1, ["Yes","No"]),
        (PF_OPTION, "pspFormat", "PSP Texture Compression:", 1, ["PNG4","PNG8"])
    ],
    [],
    exportSkin,
    menu="<Image>/Marvel Mods/Export Textures/By Asset Type"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()