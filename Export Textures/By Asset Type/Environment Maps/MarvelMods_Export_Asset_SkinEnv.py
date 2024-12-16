#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export environment maps to use with a skin, 3D head, or mannequin.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 25Jan2024: First published version.
#   v1.1: 06Dec2024: Last-gen DXT1 normal maps are replaced with plain PNG, since Alchemy 2.5 doesn't support DXT1 normal maps
#   v2.0: 12Dec2024: Full redesign for improved performance using an external module for common operations.

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


# ######### #
# FUNCTIONS #
# ######### #
# Define the function to check for image errors
def errorCheck(image, okayToExport):
    # Check if any errors were found before
    if okayToExport == True:
        # No errors were found before
        # Check if the image is too big
        if image.width > 128:
            # The image is too big
            # Warn the player
            pdb.gimp_message("WARNING: The image size is greater than 128x128. The maximum recommended size is 128x128. Larger images will be reduced in size.")
        # Initialize a variable to keep track of the number of correctly named layers
        goodLayers = 0
        # List the layers to check
        for layerName in ["Up", "Down", "Left", "Right", "Front", "Back"]:
            # Look for layers based on name
            testLayer = pdb.gimp_image_get_layer_by_name(image, layerName)
            # Check if the layer exists
            if testLayer == None:
                # The layer does not exist
                # Announce the error
                pdb.gimp_message("ERROR: There is no layer named \"" + layerName + "\".")
                # Update that it's not okay to export
                okayToExport = False
            else:
                # The layer exists
                # Increase the count of good layers
                goodLayers += 1
        # Check the number of layers that are named correctly
        if not(goodLayers == 6):
            # Layers with all 6 names are not present
            # Don't allow the user to proceed
            okayToExport = False
    # Return whether or not the script can proceed, as well as the width and height
    return okayToExport

# Define the size checking operation
def sizeCheck(currentWidth):
    # Check if the image is too big
    if currentWidth > 128:
        # The image is too big
        # Say so
        oversized = True
    else:
        # The image is not too big
        # Say so
        oversized = False
    # Return the result
    return oversized

# Define the operation for exporting the maps
def exportEnvMaps(image, layer, xcfPath, subFolderName, format, **kwargs):
    # Define the list of layer names
    layerNames = ["Up", "Down", "Left", "Right", "Front", "Back"]
    # Define the list of export suffixes
    suffixes = ["UP", "DN", "LF", "RT", "FR", "BK"]
    # Go through the layers
    for layerName, envSuffix in zip(layerNames, suffixes):
        # Create the list of layers that can be removed
        layersForRemoval = []
        for layerRemoveName in layerNames:
            if not(layerRemoveName == layerName):
                layersForRemoval.append(layerRemoveName)
        # Get the full suffix
        fullSuffix = "_" + envSuffix
        # Determine the export method
        if format == "PNG4":
            # PNG4 format
            # Export the image
            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=16, subFolder=subFolderName, scale_factor=kwargs.get("scaleFactor", 1), fileNameSuffix=fullSuffix, layersToRemove=layersForRemoval)
        elif format == "PNG8":
            # PNG8 format
            # Export the image
            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder=subFolderName, scale_factor=kwargs.get("scaleFactor", 1), fileNameSuffix=fullSuffix, layersToRemove=layersForRemoval)
        elif format == "Plain PNG":
            # Plain PNG format
            # Export the image
            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", subFolder=subFolderName, scale_factor=kwargs.get("scaleFactor", 1), fileNameSuffix=fullSuffix, layersToRemove=layersForRemoval)
        elif format == "DXT1 RGB":
            # DXT1 RGB
            # Export the image
            MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder=subFolderName, scale_factor=kwargs.get("scaleFactor", 1), fileNameSuffix=fullSuffix, layersToRemove=layersForRemoval)
        else:
            # DXT1 BGR
            # Export the image
            MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder=subFolderName, scale_factor=kwargs.get("scaleFactor", 1), fileNameSuffix=fullSuffix, layersToRemove=layersForRemoval)

# Define the main operation
def exportSkinEnv(image, layer, primarySize, console, alchemyVersion, pspFormat):
    # Perform the initial operations
    (okayToExport, xcfPath) = MMBGP.initialOps(image, layer, checkSquare=True)
    okayToExport = errorCheck(image, okayToExport)
    # Determine if it's okay to proceed
    if okayToExport == True:
        # No errors, can proceed
        # Determine if the image is oversized
        oversized = sizeCheck(image.width)
        # Determine if the image is oversized
        if oversized == True:
            # The image is oversized
            # Get the scale factor
            scaleFactor = 128 / float(image.width)
        else:
            # The image is not oversized
            # No scale factor is needed
            scaleFactor = 1
        # Determine the console
        if console == 1:
            # PC Only
            # Determine the size of the primary texture
            if primarySize == 0:
                # 256x256 or less
                # Export for PC
                exportEnvMaps(image, layer, xcfPath, "PC", "PNG8")
                # Determine the version of Alchemy
                if alchemyVersion == 0:
                    # Alchemy 2.5
                    # Export for Steam
                    exportEnvMaps(image, layer, xcfPath, "Steam", "DXT1 RGB")
                else:
                    # Alchemy 5 (either)
                    # Export for Steam
                    exportEnvMaps(image, layer, xcfPath, "Steam", "DXT1 RGB")
            else:
                # over 256x256
                # Determine the version of Alchemy
                if alchemyVersion == 0:
                    # Alchemy 2.5
                    # Export for XML2 PC
                    exportEnvMaps(image, layer, xcfPath, "XML2 PC", "Plain PNG")
                    # Export for MUA1 PC and Steam
                    exportEnvMaps(image, layer, xcfPath, "MUA1 PC and Steam", "DXT1 RGB")
                else:
                    # Alchemy 5 (either)
                    # Export for MUA1 PC and Steam
                    exportEnvMaps(image, layer, xcfPath, "MUA1 PC and Steam", "DXT1 RGB")                
        else:
            # All consoles
            # Determine the width
            if image.width > 32:
                # Normal size
                # Determine the version of Alchemy
                if alchemyVersion == 0:
                    # Alchemy 2.5
                    # Determine the size of the primary texture
                    if primarySize == 0:
                        # 256x256 or less
                        # Export for PC and MUA1 360
                        exportEnvMaps(image, layer, xcfPath, "PC and MUA1 360", "PNG8")
                        # Export for Steam and PS3
                        exportEnvMaps(image, layer, xcfPath, "MUA1 Steam and PS3", "DXT1 RGB")
                        # Get the scale factor
                        scaleFactor = 32 / float(image.width)
                        # Export for Xbox
                        exportEnvMaps(image, layer, xcfPath, "Xbox", "PNG8", scale_factor=scaleFactor)
                        # Export for Wii
                        exportEnvMaps(image, layer, xcfPath, "Wii", "Plain PNG", scale_factor=scaleFactor)
                    else:
                        # over 256x256
                        # Export for XML2 PC
                        exportEnvMaps(image, layer, xcfPath, "XML2 PC", "Plain PNG")
                        # Export for MUA1 PC, Steam, 360, and PS3
                        exportEnvMaps(image, layer, xcfPath, "MUA1 PC, Steam, 360, and PS3", "DXT1 RGB")
                        # Get the scale factor
                        scaleFactor = image.width / 32
                        # Export for Xbox and Wii
                        exportEnvMaps(image, layer, xcfPath, "Xbox and Wii", "Plain PNG", scale_factor=scaleFactor)
                    # Resize to half size
                    scaleFactor = scaleFactor * 0.5
                    # Export for PS2
                    exportEnvMaps(image, layer, xcfPath, "PS2", "PNG8", scale_factor=scaleFactor)
                    # Resize to half size
                    scaleFactor = scaleFactor * 0.5
                    # Determine the PSP format
                    if pspFormat == 0:
                        # PSP is PNG4
                        # Export for PSP
                        exportEnvMaps(image, layer, xcfPath, "PSP", "PNG4", scale_factor=scaleFactor)
                        # Export for GameCube and MUA2 PS2
                        exportEnvMaps(image, layer, xcfPath, "GameCube and MUA2 PS2", "PNG8", scale_factor=scaleFactor)
                    else:
                        # PSP is PNG8
                        # Export for GameCube, PSP, and MUA2 PS2
                        exportEnvMaps(image, layer, xcfPath, "GameCube, PSP, and MUA2 PS2", "PNG8", scale_factor=scaleFactor)
                else:
                    # Alchemy 5
                    # Determine the size of the primary texture
                    if primarySize == 0:
                        # 256x256 or smaller
                        # Export for PC and MUA1 360
                        exportEnvMaps(image, layer, xcfPath, "PC and MUA1 360", "PNG8")
                        # Export for Steam and PS3
                        exportEnvMaps(image, layer, xcfPath, "MUA1 Steam and PS3", "DXT1 RGB")
                    else:
                        # over 256x256
                        # Export for MUA1 PC, Steam, 360, and PS3
                        exportEnvMaps(image, layer, xcfPath, "MUA1 PC, Steam, 360, and PS3", "DXT1 RGB")
                    # Get the scale factor
                    scaleFactor = 32 / float(image.width)
                    # Export for Wii
                    exportEnvMaps(image, layer, xcfPath, "Wii", "DXT1 RGB", scale_factor=scaleFactor)
                    # Resize to quarter size
                    scaleFactor = scaleFactor * 0.25
                    # Determine the PSP format
                    if pspFormat == 0:
                        # PSP is PNG4
                        # Export for PSP
                        exportEnvMaps(image, layer, xcfPath, "PSP", "PNG4", scale_factor=scaleFactor)
                        # Export for GameCube and MUA2 PS2
                        exportEnvMaps(image, layer, xcfPath, "MUA2 PS2", "PNG8", scale_factor=scaleFactor)
                    else:
                        # PSP is PNG8
                        # Export for GameCube, PSP, and MUA2 PS2
                        exportEnvMaps(image, layer, xcfPath, "PSP and MUA2 PS2", "PNG8", scale_factor=scaleFactor)
            else:
                # Size is 32x32 or less
                # Determine the version of Alchemy
                if alchemyVersion == 0:
                    # Alchemy 2.5
                    # Determine the size of the primary texture
                    if primarySize == 0:
                        # 256x256 or less
                        # Export for Steam and PS3
                        exportEnvMaps(image, layer, xcfPath, "MUA1 Steam and PS3", "DXT1 RGB")
                        # Export for Xbox
                        exportEnvMaps(image, layer, xcfPath, "PC, Xbox, and MUA1 360", "PNG8")
                        # Export for Wii
                        exportEnvMaps(image, layer, xcfPath, "Wii", "DXT1 RGB")
                    else:
                        # over 256x256
                        # Export for MUA1 PC, Steam, 360, and PS3
                        exportEnvMaps(image, layer, xcfPath, "MUA1 PC, Steam, 360, and PS3", "DXT1 RGB")
                        # Export for Xbox and Wii
                        exportEnvMaps(image, layer, xcfPath, "Xbox, Wii, and XML2 PC", "Plain PNG")                        
                    # Resize to half size
                    scaleFactor = float(image.width) * 0.5
                    # Export for PS2
                    exportEnvMaps(image, layer, xcfPath, "PS2", "PNG8", scale_factor=scaleFactor)
                    # Resize to half size
                    scaleFactor = scaleFactor * 0.5
                    # Determine the PSP format
                    if pspFormat == 0:
                        # PSP is PNG4
                        # Export for PSP
                        exportEnvMaps(image, layer, xcfPath, "PSP", "PNG4", scale_factor=scaleFactor)
                        # Export for GameCube and MUA2 PS2
                        exportEnvMaps(image, layer, xcfPath, "GameCube and MUA2 PS2", "PNG8", scale_factor=scaleFactor)
                    else:
                        # PSP is PNG8
                        # Export for GameCube, PSP, and MUA2 PS2
                        exportEnvMaps(image, layer, xcfPath, "GameCube, PSP, and MUA2 PS2", "PNG8", scale_factor=scaleFactor)
                elif alchemyVersion == 1:
                    # Alchemy 5
                    # Determine the size of the primary texture
                    if primarySize == 0:
                        # 256x256 or less
                        # Export for PC
                        exportEnvMaps(image, layer, xcfPath, "PC and MUA1 360", "PNG8")
                        # Export for Next-Gen
                        exportEnvMaps(image, layer, xcfPath, "MUA1 Steam and PS3", "DXT1 RGB")
                        # Export for Wii
                        exportEnvMaps(image, layer, xcfPath, "Wii", "DXT1 RGB")
                    else:
                        # over 256x256
                        # Export for PC
                        exportEnvMaps(image, layer, xcfPath, "MUA1 PC, Steam, 360, and PS3", "DXT1 RGB")
                        # Export for Wii
                        exportEnvMaps(image, layer, xcfPath, "Wii", "DXT1 RGB")
                    # Resize to quarter size
                    scaleFactor = float(image.width) * 0.25
                    # Determine the PSP format
                    if pspFormat == 0:
                        # PSP is PNG4
                        # Export for PSP
                        exportEnvMaps(image, layer, xcfPath, "PSP", "PNG4", scale_factor=scaleFactor)
                        # Export for GameCube and MUA2 PS2
                        exportEnvMaps(image, layer, xcfPath, "MUA2 PS2", "PNG8", scale_factor=scaleFactor)
                    else:
                        # PSP is PNG8
                        # Export for GameCube, PSP, and MUA2 PS2
                        exportEnvMaps(image, layer, xcfPath, "PSP and MUA2 PS2", "PNG8", scale_factor=scaleFactor)
        # Print the success message
        pdb.gimp_message("SUCCESS: exported " + xcfPath)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_asset_skinEnv",
    "Exports a environment map textures in multiple formats.\nWorks with skins, 3D heads, and mannequins.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports a skin texture in multiple formats. Also works on 3D head textures and mannequin textures.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2024",
    "Export Environment Maps",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask or channel", None),
        (PF_OPTION, "primarySize", "Primary Texture Size:", 0, ["256x256 or less", "Over 256x256"]),
        (PF_OPTION, "console", "Console:", 0, ["All", "PC Only"]),
        (PF_OPTION, "alchemyVersion", "3ds Max Version:", 0, ["3ds Max 5 (Alchemy 2.5)", "3ds Max 10 or 12 (Alchemy 5)"]),
        (PF_OPTION, "pspFormat", "PSP Texture Compression:", 1, ["PNG4", "PNG8"])
    ],
    [],
    exportSkinEnv,
    menu="<Image>/Marvel Mods/Export Textures/By Asset Type"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()
