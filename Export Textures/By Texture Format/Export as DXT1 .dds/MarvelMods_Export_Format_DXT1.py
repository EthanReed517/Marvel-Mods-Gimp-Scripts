#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export an image in DXT1 format.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 30Jan2023: First published version.
#   v2.0: 22Jan2024: Full rewrite to include error checking, Alchemy 5, and basic procedures.

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
    return canProceed

# Define the main operation
def exportDXT1(image, layer, alchemyVersion, exportRGB, exportBGR):
    # Save the file and get its path and name
    (folderName, fileName) = pdb.python_fu_marvelmods_basic_get_path_save(image, layer)
    # Check for errors
    canProceed = errorCheck(image, layer)
    # Determine if it's okay to proceed
    if canProceed == True:
        # No errors, can proceed
        # Create a duplicate image for the export
        exportImage = pdb.gimp_image_duplicate(image)
        # Get the active layer of the new image
        exportLayer = pdb.gimp_image_get_active_layer(exportImage)
        # Flatten the image
        exportLayer = pdb.gimp_image_flatten(exportImage)
        # Determine if an RGB version needs to be exported
        if exportRGB == 1:
            # RGB version needs to be exported
            # Export the RGB version
            pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "DXT1 RGB", fileName, 0, 0)
        # Determine if a BGR version needs to be exported
        if exportBGR == 1:
            # BGR version needs to be exported
            # Check the Alchemy version
            if alchemyVersion == 0:
                # Alchemy 2.5
                # Export the BGR version
                pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "DXT1 BGR", fileName, 0, 1)
            else:
                # Alchemy 5
                # Display the warning.
                pdb.gimp_message("WARNING: It is not necessary to RGB-BGR swap colors with Alchemy 5. No RGB-BGR-swapped texture was exported.")
        # Announce completion
        pdb.gimp_message(folderName + "\\" + fileName + ".xcf was successfully exported.")
    else:
        # Errors, cannot proceed
        # Display an error message
        pdb.gimp_message(folderName + "\\" + fileName + ".xcf could not be exported.")


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_format_dxt1",
    "Exports a texture to DXT1 format as a .dds.",
    "Exports a texture to DXT1 format as a .dds.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2024",
    "Export as DXT1 .dds",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "drawable", "Layer, mask or channel", None),
        (PF_OPTION, "alchemyVersion", "Alchemy Version:", 0, ["Alchemy 2.5","Alchemy 5"]),
        (PF_TOGGLE, "exportRGB", "Export in RGB?", 1),
        (PF_TOGGLE, "exportBGR", "Export RGB-BGR Swapped?", 1)
    ],
    [],
    exportDXT1,
    menu="<Image>/Marvel Mods/Export Textures/By Texture Format"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()