#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export advanced textures for next-gen skins and mannequins.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 01Mar2024: First published version.

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

# Define the main operation
def exportSkinAdv(image, layer, primarySize, textureType, console, alchemyVersion):
    # Save the file and get its path and name
    (folderName, fileName) = pdb.python_fu_marvelmods_basic_get_path_save(image, layer)
    # List the texture types and suffix
    for type, suffix in zip([0, 1, 2, 3], ["_n", "_s", "_g", "_m"]):
        # determine if the type matches
        if type == textureType:
            # The type matches
            # Determine if a suffix is needed
            if not(fileName[-2:] == suffix):
                # Suffix is needed
                # Set the suffix
                fileName = fileName + suffix
    # Check for errors
    (canProceed, currentWidth, currentHeight) = errorCheck(image, layer)
    # Determine if it's okay to proceed
    if canProceed == True:
        # No errors, can proceed
        # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
        pdb.gimp_selection_none(image)
        # Create a duplicate image that can be manipulated
        exportImage = pdb.gimp_image_duplicate(image)
        # Get the active layer of the new image
        exportLayer = pdb.gimp_image_get_active_layer(exportImage)
        # Determine the texture type
        if textureType == 0:
            # Normal map
            # Determine the console
            if console == 1:
                # PC Only
                # Determine the Alchemy version
                if alchemyVersion == 0:
                    # Alchemy 2.5
                    # Export for MUA1 PC and Steam
                    pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 PC and Steam", fileName, 2, 1)
                else:
                    # Alchemy 5
                    # Export for MUA1 PC and Steam
                    pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 PC and Steam", fileName, 2, 0)
            else:
                # All consoles
                # Determine the Alchemy version
                if alchemyVersion == 0:
                    # Alchemy 2.5
                    # Export for next-gen MUA1
                    pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 PC, Steam, PS3, and 360", fileName, 2, 1)
                else:
                    # Alchemy 5
                    # Export for next-gen MUA1
                    pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 PC, Steam, PS3, and 360", fileName, 2, 0)
        else:
            # All others
            # Flatten the image
            exportLayer = pdb.gimp_image_flatten(exportImage)
            # Determine if the image is oversized
            if primarySize == 1:
                # The image is still oversized for the main consoles
                # Determine the console
                if console == 1:
                    # PC Only
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for MUA1 PC and Steam
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 PC and Steam", fileName, 0, 1)
                    else:
                        # Alchemy 5
                        # Export for MUA1 PC and Steam
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 PC and Steam", fileName, 0, 0)
                else:
                    # All consoles
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for next-gen MUA1
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 PC, Steam, PS3, and 360", fileName, 0, 1)
                    else:
                        # Alchemy 5
                        # Export for next-gen MUA1
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 PC, Steam, PS3, and 360", fileName, 0, 0)
            else:
                # The image is not oversized
                # Determine the console
                if console == 1:
                    # PC Only
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for PC
                        pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "MUA1 PC", fileName, 2)
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
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for PC, PS2, Xbox, and MUA1 360
                        pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "MUA1 PC and 360", fileName, 2)
                        # Export for Steam and PS3
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 Steam and PS3", fileName, 0, 1)
                    else:
                        # Alchemy 5
                        # Export for PC
                        pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "MUA1 PC and 360", fileName, 2)
                        # Export for Steam
                        pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 Steam and PS3", fileName, 0, 0)
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
    "python_fu_marvelmods_export_asset_skinadvsecondary",
    "Exports advanced material textures for next-gen skins and mannequins in multiple formats.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports advanced material textures for next-gen skins and mannequins in multiple formats.",
    "BaconWizard17",
    "BaconWizard17",
    "March 2024",
    "Export Advanced Textures for Next-Gen (Secondary Texture)",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask or channel", None),
        (PF_OPTION, "primarySize", "Primary Texture Size:", 0, ["256x256 or less","Over 256x256"]),
        (PF_OPTION, "textureType", "Advanced Texture Type:", 0, ["Normal Map","Specular Map","Gloss/Emissive Map","Environment Mask"]),
        (PF_OPTION, "console", "Console:", 0, ["All","PC Only"]),
        (PF_OPTION, "alchemyVersion", "Alchemy Version:", 1, ["Alchemy 2.5","Alchemy 5"])
    ],
    [],
    exportSkinAdv,
    menu="<Image>/Marvel Mods/Export Textures/By Asset Type"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()