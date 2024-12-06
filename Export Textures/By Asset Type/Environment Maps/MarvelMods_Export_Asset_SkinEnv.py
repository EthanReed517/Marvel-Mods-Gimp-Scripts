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
        # Check if the image dimensions are the same
        if currentWidth == currentHeight:
            # Dimensions are the same, can proceed
            # Check if the image is too big
            if currentWidth > 128:
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
                else:
                    # The layer exists
                    # Increase the count of good layers
                    goodLayers += 1
            # Check the number of layers that are named correctly
            if goodLayers == 6:
                # Layers with all 3 names are present
                # Allow the user to proceed
                canProceed = True
        else:
            # Dimensions are not the same
            # Give error message
            pdb.gimp_message("ERROR: Image dimensions are not equal. Equal image dimensions are needed for environment maps.")
    else:
        # Image dimensions are not powers of 2
        # Give error message
        pdb.gimp_message("ERROR: One or both image dimensions are not a power of 2. Alchemy only supports image dimensions that are powers of 2.\n\nPowers of 2: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, and so on.")
    # Return whether or not the script can proceed, as well as the width and height
    return canProceed, currentWidth

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
def exportEnvMaps(image, layer, folderName, subFolderName, fileName, format):
    # Define the list of layer names
    layerNames = ["Up", "Down", "Left", "Right", "Front", "Back"]
    # Define the list of export suffixes
    suffixes = ["UP", "DN", "LF", "RT", "FR", "BK"]
    # Go through the layers
    for layerName, suffix in zip(layerNames, suffixes):
        # Create a duplicate image that can be manipulated
        exportImage = pdb.gimp_image_duplicate(image)
        # Get the active layer of the new image
        exportLayer = pdb.gimp_image_get_active_layer(exportImage)
        # List the layers that need to be removed
        for layerRemoveName in layerNames:
            # Determine if the layer should be removed
            if not(layerRemoveName == layerName):
                # Layer should be removed
                # Get the layer by the name
                layerToRemove = pdb.gimp_image_get_layer_by_name(exportImage, layerRemoveName)
                # Remove the layer
                pdb.gimp_image_remove_layer(exportImage, layerToRemove)
        # Set up the file name
        outFileName = fileName + "_" + suffix
        # Determine the export method
        if format == "PNG4":
            # PNG4 format
            # Flatten the image
            exportLayer = pdb.gimp_image_flatten(exportImage)
            # Export the image
            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, subFolderName, outFileName, 1)
        elif format == "PNG8":
            # PNG8 format
            # Flatten the image
            exportLayer = pdb.gimp_image_flatten(exportImage)
            # Export the image
            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, subFolderName, outFileName, 2)
        elif format == "Plain PNG":
            # Plain PNG format
            # Get the active layer of the new image
            exportLayer = pdb.gimp_image_get_active_layer(exportImage)
            # Export the image
            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, subFolderName, outFileName, 0)
        elif format == "DXT1 RGB":
            # DXT1 RGB
            # Flatten the image
            exportLayer = pdb.gimp_image_flatten(exportImage)
            # Export the image
            pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, subFolderName, outFileName, 0, 0)
        else:
            # DXT1 BGR
            # Flatten the image
            exportLayer = pdb.gimp_image_flatten(exportImage)
            # Export the image
            pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, subFolderName, outFileName, 0, 1)

# Define the main operation
def exportSkinEnv(image, layer, primarySize, console, alchemyVersion, pspFormat):
    # Save the file and get its path and name
    (folderName, fileName) = pdb.python_fu_marvelmods_basic_get_path_save(image, layer)
    # Check for errors
    (canProceed, currentWidth) = errorCheck(image, layer)
    # Determine if it's okay to proceed
    if canProceed == True:
        # No errors, can proceed
        # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
        pdb.gimp_selection_none(image)
        # Determine if the image is oversized
        oversized = sizeCheck(currentWidth)
        # Create a duplicate image that can be manipulated
        exportImage = pdb.gimp_image_duplicate(image)
        # Get the active layer of the new image
        exportLayer = pdb.gimp_image_get_active_layer(exportImage)
        # Begin the export
        # Determine if the image is oversized
        if oversized == True:
            # The image is oversized
            # Get the scale factor
            scaleFactor = currentWidth / 128
            # Reduce the image size
            pdb.python_fu_marvelmods_scaling_scaleAny(exportImage, exportLayer, scaleFactor)
        # Determine the console
        if console == 1:
            # PC Only
            # Determine the size of the primary texture
            if primarySize == 0:
                # 256x256 or less
                # Export for PC
                exportEnvMaps(exportImage, exportLayer, folderName, "PC", fileName, "PNG8")
                # Determine the version of Alchemy
                if alchemyVersion == 0:
                    # Alchemy 2.5
                    # Export for Steam
                    exportEnvMaps(exportImage, exportLayer, folderName, "Steam", fileName, "DXT1 BGR")
                else:
                    # Alchemy 5 (either)
                    # Export for Steam
                    exportEnvMaps(exportImage, exportLayer, folderName, "Steam", fileName, "DXT1 RGB")
            else:
                # over 256x256
                # Determine the version of Alchemy
                if alchemyVersion == 0:
                    # Alchemy 2.5
                    # Export for XML2 PC
                    exportEnvMaps(exportImage, exportLayer, folderName, "XML2 PC", fileName, "Plain PNG")
                    # Export for MUA1 PC and Steam
                    exportEnvMaps(exportImage, exportLayer, folderName, "MUA1 PC and Steam", fileName, "DXT1 BGR")
                else:
                    # Alchemy 5 (either)
                    # Export for MUA1 PC and Steam
                    exportEnvMaps(exportImage, exportLayer, folderName, "MUA1 PC and Steam", fileName, "DXT1 RGB")                
        else:
            # All consoles
            # Determine the width
            if currentWidth > 32:
                # Normal size
                # Determine the version of Alchemy
                if alchemyVersion == 0:
                    # Alchemy 2.5
                    # Determine the size of the primary texture
                    if primarySize == 0:
                        # 256x256 or less
                        # Export for PC and MUA1 360
                        exportEnvMaps(exportImage, exportLayer, folderName, "PC and MUA1 360", fileName, "PNG8")
                        # Export for Steam and PS3
                        exportEnvMaps(exportImage, exportLayer, folderName, "MUA1 Steam and PS3", fileName, "DXT1 BGR")
                        # Get the scale factor
                        scaleFactor = currentWidth / 32
                        # Reduce the image size
                        pdb.python_fu_marvelmods_scaling_scaleAny(exportImage, exportLayer, scaleFactor)
                        # Export for Xbox
                        exportEnvMaps(exportImage, exportLayer, folderName, "Xbox", fileName, "PNG8")
                        # Export for Wii
                        exportEnvMaps(exportImage, exportLayer, folderName, "Wii", fileName, "Plain PNG")
                    else:
                        # over 256x256
                        # Export for XML2 PC
                        exportEnvMaps(exportImage, exportLayer, folderName, "XML2 PC", fileName, "Plain PNG")
                        # Export for MUA1 PC, Steam, 360, and PS3
                        exportEnvMaps(exportImage, exportLayer, folderName, "MUA1 PC, Steam, 360, and PS3", fileName, "DXT1 BGR")
                        # Get the scale factor
                        scaleFactor = currentWidth / 32
                        # Reduce the image size
                        pdb.python_fu_marvelmods_scaling_scaleAny(exportImage, exportLayer, scaleFactor)
                        # Export for Xbox and Wii
                        exportEnvMaps(exportImage, exportLayer, folderName, "Xbox and Wii", fileName, "Plain PNG")
                    # Resize to half size
                    pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                    # Export for PS2
                    exportEnvMaps(exportImage, exportLayer, folderName, "PS2", fileName, "PNG8")
                    # Resize to half size
                    pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                    # Determine the PSP format
                    if pspFormat == 0:
                        # PSP is PNG4
                        # Export for PSP
                        exportEnvMaps(exportImage, exportLayer, folderName, "PSP", fileName, "PNG4")
                        # Export for GameCube and MUA2 PS2
                        exportEnvMaps(exportImage, exportLayer, folderName, "GameCube and MUA2 PS2", fileName, "PNG8")
                    else:
                        # PSP is PNG8
                        # Export for GameCube, PSP, and MUA2 PS2
                        exportEnvMaps(exportImage, exportLayer, folderName, "GameCube, PSP, and MUA2 PS2", fileName, "PNG8")
                else:
                    # Alchemy 5 (either)
                    # Determine the size of the primary texture
                    if primarySize == 0:
                        # 256x256 or smaller
                        # Export for PC and MUA1 360
                        exportEnvMaps(exportImage, exportLayer, folderName, "PC and MUA1 360", fileName, "PNG8")
                        # Export for Steam and PS3
                        exportEnvMaps(exportImage, exportLayer, folderName, "MUA1 Steam and PS3", fileName, "DXT1 RGB")
                    else:
                        # over 256x256
                        # Export for MUA1 PC, Steam, 360, and PS3
                        exportEnvMaps(exportImage, exportLayer, folderName, "MUA1 PC, Steam, 360, and PS3", fileName, "DXT1 RGB")                        
                    # Determine which alchemy 5 version was picked
                    if alchemyVersion == 1:
                        # Alchemy 5 in 3ds Max
                        # Get the scale factor
                        scaleFactor = currentWidth / 32
                        # Reduce the image size
                        pdb.python_fu_marvelmods_scaling_scaleAny(exportImage, exportLayer, scaleFactor)
                        # Export for Wii
                        exportEnvMaps(exportImage, exportLayer, folderName, "Wii", fileName, "DXT1 RGB")
                        # Resize to quarter size
                        pdb.python_fu_marvelmods_scaling_scaleQuarter(exportImage, exportLayer)
                        # Determine the PSP format
                        if pspFormat == 0:
                            # PSP is PNG4
                            # Export for PSP
                            exportEnvMaps(exportImage, exportLayer, folderName, "PSP", fileName, "PNG4")
                            # Export for GameCube and MUA2 PS2
                            exportEnvMaps(exportImage, exportLayer, folderName, "MUA2 PS2", fileName, "PNG8")
                        else:
                            # PSP is PNG8
                            # Export for GameCube, PSP, and MUA2 PS2
                            exportEnvMaps(exportImage, exportLayer, folderName, "PSP and MUA2 PS2", fileName, "PNG8")
            else:
                # Size is 32x32 or less
                # Determine the version of Alchemy
                if alchemyVersion == 0:
                    # Alchemy 2.5
                    # Determine the size of the primary texture
                    if primarySize == 0:
                        # 256x256 or less
                        # Export for Steam and PS3
                        exportEnvMaps(exportImage, exportLayer, folderName, "MUA1 Steam and PS3", fileName, "DXT1 BGR")
                        # Export for Xbox
                        exportEnvMaps(exportImage, exportLayer, folderName, "PC, Xbox, and MUA1 360", fileName, "PNG8")
                        # Export for Wii
                        exportEnvMaps(exportImage, exportLayer, folderName, "Wii", fileName, "DXT1 RGB")
                    else:
                        # over 256x256
                        # Export for MUA1 PC, Steam, 360, and PS3
                        exportEnvMaps(exportImage, exportLayer, folderName, "MUA1 PC, Steam, 360, and PS3", fileName, "DXT1 BGR")
                        # Export for Xbox and Wii
                        exportEnvMaps(exportImage, exportLayer, folderName, "Xbox, Wii, and XML2 PC", fileName, "DXT1 RGB")                        
                    # Resize to half size
                    pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                    # Export for PS2
                    exportEnvMaps(exportImage, exportLayer, folderName, "PS2", fileName, "PNG8")
                    # Resize to half size
                    pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                    # Determine the PSP format
                    if pspFormat == 0:
                        # PSP is PNG4
                        # Export for PSP
                        exportEnvMaps(exportImage, exportLayer, folderName, "PSP", fileName, "PNG4")
                        # Export for GameCube and MUA2 PS2
                        exportEnvMaps(exportImage, exportLayer, folderName, "GameCube and MUA2 PS2", fileName, "PNG8")
                    else:
                        # PSP is PNG8
                        # Export for GameCube, PSP, and MUA2 PS2
                        exportEnvMaps(exportImage, exportLayer, folderName, "GameCube, PSP, and MUA2 PS2", fileName, "PNG8")
                elif alchemyVersion == 1:
                    # Alchemy 5 in 3ds Max
                    # Determine the size of the primary texture
                    if primarySize == 0:
                        # 256x256 or less
                        # Export for PC
                        exportEnvMaps(exportImage, exportLayer, folderName, "PC and MUA1 360", fileName, "PNG8")
                        # Export for Wii
                        exportEnvMaps(exportImage, exportLayer, folderName, "Wii, MUA1 Steam and PS3", fileName, "DXT1 RGB")
                    else:
                        # over 256x256
                        # Export for Wii
                        exportEnvMaps(exportImage, exportLayer, folderName, "Wii, MUA1 PC, Steam, 360, and PS3", fileName, "DXT1 RGB")
                    # Resize to quarter size
                    pdb.python_fu_marvelmods_scaling_scaleQuarter(exportImage, exportLayer)
                    # Determine the PSP format
                    if pspFormat == 0:
                        # PSP is PNG4
                        # Export for PSP
                        exportEnvMaps(exportImage, exportLayer, folderName, "PSP", fileName, "PNG4")
                        # Export for GameCube and MUA2 PS2
                        exportEnvMaps(exportImage, exportLayer, folderName, "MUA2 PS2", fileName, "PNG8")
                    else:
                        # PSP is PNG8
                        # Export for GameCube, PSP, and MUA2 PS2
                        exportEnvMaps(exportImage, exportLayer, folderName, "PSP and MUA2 PS2", fileName, "PNG8")
                else:
                    # Alchemy 5 raven setup
                    # Determine the size of the primary texture
                    if primarySize == 0:
                        # 256x256 or less
                        # Export for PC
                        exportEnvMaps(exportImage, exportLayer, folderName, "PC and MUA1 360", fileName, "PNG8")
                        # Export for Wii
                        exportEnvMaps(exportImage, exportLayer, folderName, "MUA1 Steam and PS3", fileName, "DXT1 RGB")
                    else:
                        # over 256x256
                        # Export for Wii
                        exportEnvMaps(exportImage, exportLayer, folderName, "MUA1 PC, Steam, 360, and PS3", fileName, "DXT1 RGB")
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
    "python_fu_marvelmods_export_asset_skinEnv",
    "Exports a environment map textures in multiple formats.\nWorks with skins, 3D heads, and mannequins.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports a skin texture in multiple formats. Also works on 3D head textures and mannequin textures.",
    "BaconWizard17",
    "BaconWizard17",
    "September 2023",
    "Export Environment Maps",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask or channel", None),
        (PF_OPTION, "primarySize", "Primary Texture Size:", 0, ["256x256 or less","Over 256x256"]),
        (PF_OPTION, "console", "Console:", 0, ["All","PC Only"]),
        (PF_OPTION, "alchemyVersion", "Alchemy Version:", 0, ["Alchemy 2.5","Alchemy 5 (3ds Max)","Alchemy 5 (Raven Set Up Material)"]),
        (PF_OPTION, "pspFormat", "PSP Texture Compression:", 1, ["PNG4","PNG8"])
    ],
    [],
    exportSkinEnv,
    menu="<Image>/Marvel Mods/Export Textures/By Asset Type"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()
