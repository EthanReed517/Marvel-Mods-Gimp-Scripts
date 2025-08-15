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
#   v1.0: 12Dec2024: First published version.

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
# GIMP module
from gimpfu import *
# Marvel Mods Operations
import Marvel_Mods_Basic_Gimp_Procedures as MMBGP
# External modules
import os.path


# ######### #
# FUNCTIONS #
# ######### #
# Define the size checking operation
def sizeCheckAdv(currentWidth, currentHeight):
    # compare the criteria to the current texture size
    if (currentWidth > 256) or (currentHeight > 256):
        oversized = True
    else:
        oversized = False
    return oversized

# Define the function for exporting the two types of normal maps.
def exportNorm(image, layer, xcfPath, greenFolderName, yellowFolderNameList, BGR, normalColor, suffix):
    # Export the green normal map
    MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=BGR, transparent=True, subFolder=greenFolderName, fileNameSuffix=suffix, ddsCompression="DXT5")
    # Create a duplicate image for the other map and get its active layer
    exportImage = pdb.gimp_image_duplicate(image)
    exportLayer = pdb.gimp_image_get_active_layer(exportImage)
    # Decompose the image
    redImage, greenImage, blueImage, alphaImage = pdb.plug_in_decompose(exportImage, exportLayer, "RGBA", 0)
    # Create a plain white image
    whiteImage = pdb.gimp_image_new(exportImage.width, exportImage.height, 0)
    # Create a layer for the plain white image
    whiteLayer = pdb.gimp_layer_new(whiteImage, exportImage.width, exportImage.height, 0, "Background", 100, 28)
    # Get the current layer of the white image
    whiteLayer2 = pdb.gimp_image_get_active_layer(whiteImage)
    # Apply the layer to the image
    pdb.gimp_image_insert_layer(whiteImage, whiteLayer, whiteLayer2, 0)
    # Set the background fill color
    pdb.gimp_context_set_background((255, 255, 255))
    # Fill the layer with the background color
    pdb.gimp_drawable_fill(whiteLayer, 1)
    # Determine what the normal map color should be
    if normalColor == 0:
        # Yellow normal map
        # Compose the image
        exportImage = pdb.plug_in_compose(greenImage, exportLayer, alphaImage, redImage, whiteImage, "RGBA")
    else:
        # Blue normal map
        # Compose the image
        exportImage = pdb.plug_in_compose(greenImage, exportLayer, alphaImage, whiteImage, whiteImage, "RGBA")
    # Get the active layer of the new image
    exportLayer = pdb.gimp_image_get_active_layer(exportImage)
    # Export the first yellow folder (there will always be at least one, and the first will always be the DXT1 folder)
    MMBGP.exportTextureMM(exportImage, exportLayer, xcfPath, ".dds", RGB_BGR=BGR, subFolder=yellowFolderNameList[0], fileNameSuffix=suffix)
    if len(yellowFolderNameList) == 2:
        # There are two yellow folders
        # The second yellow folder will always be PNG8
        MMBGP.exportTextureMM(exportImage, exportLayer, xcfPath, ".png", indexColors=256, subFolder="MUA1 PC", fileNameSuffix=yellowFolderNameList[1])

# Define the main operation
def exportSkinAdv(image, layer, textureType, console, alchemyVersion, normalColor, primary, **kwargs):
    # Perform the initial operations
    (okayToExport, xcfPath) = MMBGP.initialOps(image, layer)
    # Create a dictionary for the texture types and their suffixes and then match the suffix
    suffixDict = {"0": "_n", "1": "_s", "2": "_g", "3": "_m"}
    suffix = suffixDict[str(textureType)]
    # Check if the suffix is in use
    fileName = os.path.splitext(os.path.basename(xcfPath))[0]
    if fileName.endswith(suffix):
        suffix = ""
    # Determine if it's okay to proceed
    if okayToExport == True:
        # No errors, can proceed
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
                    exportNorm(image, layer, xcfPath, "MUA1 PC", ["MUA1 Steam"], True, normalColor, suffix)
                else:
                    # Alchemy 5
                    # Export for MUA1 PC and Steam
                    exportNorm(image, layer, xcfPath, "MUA1 PC", ["MUA1 Steam"], False, normalColor, suffix)
            else:
                # All consoles
                # Determine if the image is oversized
                if primary == True:
                    oversized = sizeCheckAdv(image.width, image.height)
                else:
                    oversized = kwargs.get("primary_size", False)
                # Determine if the image is oversized
                if oversized == True:
                    # The image is oversized
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for next-gen MUA1
                        exportNorm(image, layer, xcfPath, "MUA1 PC and PS3", ["MUA1 Steam and 360"], True, normalColor, Suffix)
                    else:
                        # Alchemy 5
                        # Export for next-gen MUA1
                        exportNorm(image, layer, xcfPath, "MUA1 PC and PS3", ["MUA1 Steam and 360"], False, normalColor, suffix)
                else:
                    # The image is not oversized
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for next-gen MUA1
                        exportNorm(image, layer, xcfPath, "MUA1 PC and PS3", ["MUA1 Steam", "MUA1 360"], True, normalColor, suffix)
                    else:
                        # Alchemy 5
                        # Export for next-gen MUA1
                        exportNorm(image, layer, xcfPath, "MUA1 PC and PS3", ["MUA1 Steam", "MUA1 360"], False, normalColor, suffix)
        else:
            # All others
            # Determine if the image is oversized
            if primary == True:
                oversized = sizeCheckAdv(image.width, image.height)
            else:
                oversized = kwargs.get("primary_size", False)
            # Determine if the image is oversized
            if oversized == True:
                # The image is still oversized for the main consoles
                # Determine the console
                if console == 1:
                    # PC Only
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for MUA1 PC and Steam
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 PC and Steam", fileNameSuffix=suffix)
                    else:
                        # Alchemy 5
                        # Export for MUA1 PC and Steam
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="MUA1 PC and Steam", fileNameSuffix=suffix)
                else:
                    # All consoles
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for next-gen MUA1
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 PC, Steam, PS3, and 360", fileNameSuffix=suffix)
                    else:
                        # Alchemy 5
                        # Export for next-gen MUA1
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="MUA1 PC, Steam, PS3, and 360", fileNameSuffix=suffix)
            else:
                # The image is not oversized
                # Determine the console
                if console == 1:
                    # PC Only
                    # Export for PC
                    MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder="MUA1 PC", fileNameSuffix=suffix)
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for Steam
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 Steam", fileNameSuffix=suffix)
                    else:
                        # Alchemy 5
                        # Export for Steam
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="MUA1 Steam", fileNameSuffix=suffix)
                else:
                    # All consoles
                    # Export for PC and 360
                    MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder="MUA1 PC and 360", fileNameSuffix=suffix)
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for Steam
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 Steam and PS3", fileNameSuffix=suffix)
                    else:
                        # Alchemy 5
                        # Export for Steam
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="MUA1 Steam and PS3", fileNameSuffix=suffix)
        # Print the success message
        pdb.gimp_message("SUCCESS: exported " + xcfPath)