#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a conversation portrait (HUD)
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 01Feb2023: First published version.
#   v1.1: 15Apr2023: Rewrote to accommodate for more portrait types and use the duplication function
#   v2.0: 15Jan2024: Full rewrite. Added more portrait types, changed basic operations to common procedures.
#   v2.1: 21Jan2024: Add support for Alchemy 5

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
        # Check if the image dimensions are the same
        if currentWidth == currentHeight:
            # Dimensions are the same, can proceed
            # Check if the image is too small
            if currentWidth >= 64:
                # Image is not too small, can proceed
                # Initialize a variable to keep track of the number of correctly named layers
                goodLayers = 0
                # List the layers to check
                for layerName in ["Frame", "Character", "Background"]:
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
                if goodLayers == 3:
                    # Layers with all 3 names are present
                    # Allow the user to proceed
                    canProceed = True
                canProceed = True
            else:
                # Image is too small
                # Give error message
                pdb.gimp_message("ERROR: The image dimensions are 32x32 or less. This size is not recommended because the image will not be clear.")
        else:
            # Dimensions are not the same
            # Give error message
            pdb.gimp_message("ERROR: Image dimensions are not equal. 3ds Max templates only support equal image dimensions for portraits.")
    else:
        # Image dimensions are not powers of 2
        # Give error message
        pdb.gimp_message("ERROR: One or both image dimensions are not a power of 2. Alchemy only supports image dimensions that are powers of 2.\n\nPowers of 2: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, and so on.")
    # Return whether or not the script can proceed, as well as the width and height
    return canProceed, currentWidth

# Define the standard exporting operation
def exportStandardHUD(image, console, folderName, fileName, currentWidth, outlineColor, namePrefix, alchemyVersion):
    # Create a duplicate image for the export
    exportImage = pdb.gimp_image_duplicate(image)
    # Determine if an outline is needed
    if not(outlineColor == "None"):
        # An outline is needed
        # Get the layer to add the outline to
        outlineLayer = pdb.gimp_image_get_layer_by_name(exportImage, "Character")
        # Generate an outline
        pdb.python_fu_marvelmods_utilities_generate_hud_outline(exportImage, outlineLayer, currentWidth, outlineColor)
    # Flatten the image
    exportLayer = pdb.gimp_image_flatten(exportImage)
    # Set up the file name
    outFileName = namePrefix + fileName
    # Do a test export
    #pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "Test", outFileName)
    # Filter remaining options based on the image size
    if currentWidth == 64:
        # Console resolution
        # Determine the alchemy version
        if alchemyVersion == 0:
            # Alchemy 2.5
            # Filter remaining export options based on console selection
            if console == 1:
                # PC Only
                # Export for PC
                pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC", outFileName, 2)
                # Export for Steam
                pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "Steam", outFileName, 0, 1)
            else:
                # All consoles
                # Export the cross-compatible version
                pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "Main", outFileName, 2)
                # Export the Wii version
                pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "Wii", outFileName, 0, 0)
                # Export the PS3 and Steam version
                pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "PS3 and Steam", outFileName, 0, 1)
        else:
            # Alchemy 5
            # Filter remaining export options based on console selection
            if console == 1:
                # PC Only
                # Export for PC and Steam
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "PC and Steam", outFileName)
            else:
                # All consoles
                # Export the cross-compatible version
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "All", outFileName)         
    elif currentWidth == 128:
        # Standard resolution
        # Determine the alchemy version
        if alchemyVersion == 0:
            # Alchemy 2.5
            # Filter remaining export options based on console selection
            if console == 1:
                # PC only
                # Export for PC
                pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC", outFileName, 2)
                # Export for Steam
                pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "Steam", outFileName, 0, 1)
            else:
                # All consoles
                # Export the cross-compatible version
                pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "Main", outFileName, 2)
                # Export the Wii version
                pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "Wii", outFileName, 0, 0)
                # Export the PS3 and Steam version
                pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "PS3 and Steam", outFileName, 0, 1)
                # Resize to half size
                pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                # Export the PSP version
                pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PSP", outFileName, 2)
        else:
            # Alchemy 5
            # Filter remaining export options based on console selection
            if console == 1:
                # PC Only
                # Export for PC and Steam
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "PC and Steam", outFileName)
            else:
                # All consoles
                # Export the cross-compatible version
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "Main", outFileName)   
                # Resize to half size
                pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                # Export the PSP version
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "PSP", outFileName)  
    else:
        # HD resolution and higher
        # Determine the alchemy version
        if alchemyVersion == 0:
            # Alchemy 2.5
            # Export for XML2 PC (same option regardless of console choice)
            pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "XML2 PC", outFileName, 0, 0)
            # Filter based on console selection
            if console == 1:
                # PC only
                # Export for MUA1 PC and Steam
                pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 PC and Steam", outFileName, 0, 1)
            else:
                # All consoles
                # Export for MUA1 PC and Next-Gen consoles
                pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "MUA1 PC and Next-Gen", outFileName, 0, 1)
                # Get the updated width
                reducedWidth = currentWidth / 128
                # Resize to 128x128
                pdb.python_fu_marvelmods_scaling_scaleAny(exportImage, exportLayer, reducedWidth)
                # Export the Wii and Xbox version
                pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "Wii and Xbox", outFileName, 0, 0)
                # Export the PS2 and GameCube version
                pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PS2 and GC", outFileName, 2)
                # Resize to half size
                pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                # Export the PSP version
                pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PSP", outFileName, 2)
        else:
            # Alchemy 5
            # Filter remaining export options based on console selection
            if console == 1:
                # PC Only
                # Export for PC and Steam
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "PC and Steam", outFileName)
            else:
                # All consoles
                # Export the cross-compatible version
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "Main", outFileName)  
                # Get the updated width
                reducedWidth = currentWidth / 128
                # Resize to 128x128
                pdb.python_fu_marvelmods_scaling_scaleAny(exportImage, exportLayer, reducedWidth) 
                # Export the Wii version
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "Wii", outFileName)  
                # Resize to half size
                pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                # Export the PSP version
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "PSP", outFileName)  

# Define the next-gen exporting operation
def exportNGHUD(image, console, folderName, fileName, currentWidth, alchemyVersion):
    # Create a duplicate image for the export
    exportImage = pdb.gimp_image_duplicate(image)
    # List the layers that need to be removed
    for layerName in ["Frame", "Background"]:
        # Get the layer by the name
        layerToRemove = pdb.gimp_image_get_layer_by_name(exportImage, layerName)
        # Remove the layer
        pdb.gimp_image_remove_layer(exportImage, layerToRemove)
    # Get the active layer of the new image
    exportLayer = pdb.gimp_image_get_active_layer(exportImage)
    # Set up the file name
    outFileName = "ng_" + fileName
    # Filter remaining options based on the image size
    if currentWidth == 64:
        # Console resolution
        # Determine the alchemy version
        if alchemyVersion == 0:
            # Alchemy 2.5
            # Filter remaining export options based on console selection
            if console == 1:
                # PC Only
                # Export for PC
                pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC and Steam", outFileName, 0)
            else:
                # All consoles
                # Export the cross-compatible version
                pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "All", outFileName, 0)
        else:
            # Alchemy 5
            # Filter remaining export options based on console selection
            if console == 1:
                # PC Only
                # Export for PC and Steam
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "PC and Steam", outFileName)
            else:
                # All consoles
                # Export the cross-compatible version
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "All", outFileName)
    elif currentWidth == 128:
        # Standard resolution
        # Determine the alchemy version
        if alchemyVersion == 0:
            # Alchemy 2.5
            # Filter remaining export options based on console selection
            if console == 1:
                # PC only
                # Export for PC
                pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC and Steam", outFileName, 0)
            else:
                # All consoles
                # Export the cross-compatible version
                pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "All", outFileName, 0)
                # Resize to half size
                pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                # Export the PSP version
                pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PSP", outFileName, 0)
        else:
            # Alchemy 5
            # Filter remaining export options based on console selection
            if console == 1:
                # PC Only
                # Export for PC and Steam
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "PC and Steam", outFileName)
            else:
                # All consoles
                # Export the cross-compatible version
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "Main", outFileName)   
                # Resize to half size
                pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                # Export the PSP version
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "PSP", outFileName)  
    else:
        # HD resolution and higher
        # Determine the alchemy version
        if alchemyVersion == 0:
            # Alchemy 2.5
            # Filter based on console selection
            if console == 1:
                # PC only
                # Export for PC and Steam
                pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC and Steam", outFileName, 0)
            else:
                # All consoles
                # Export for PC and Next-Gen consoles
                pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC and Next-Gen", outFileName, 0)
                # Get the updated width
                reducedWidth = currentWidth / 128
                # Resize to 128x128
                pdb.python_fu_marvelmods_scaling_scaleAny(exportImage, exportLayer, reducedWidth)
                # Export the Wii and Xbox version
                pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "Last-Gen", outFileName, 0)
                # Resize to half size
                pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                # Export the PSP version
                pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PSP", outFileName, 0)
        else:
            # Alchemy 5
            # Filter remaining export options based on console selection
            if console == 1:
                # PC Only
                # Export for PC and Steam
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "PC and Steam", outFileName)
            else:
                # All consoles
                # Export the cross-compatible version
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "Main", outFileName)  
                # Get the updated width
                reducedWidth = currentWidth / 128
                # Resize to 128x128
                pdb.python_fu_marvelmods_scaling_scaleAny(exportImage, exportLayer, reducedWidth) 
                # Export the Wii version
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "Wii", outFileName)  
                # Resize to half size
                pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
                # Export the PSP version
                pdb.python_fu_marvelmods_basic_exportTGA(exportImage, exportLayer, folderName, "PSP", outFileName)  

# Define the main operation
def exportHUD(image, layer, console, plainChoice, nextGenChoice, heroOutlineChoice, redVillainOutlineChoice, greenVillainOutlineChoice, alchemyVersion):
    # Save the file and get its path and name
    (folderName, fileName) = pdb.python_fu_marvelmods_basic_get_path_save(image, layer)
    # Check for errors
    (canProceed, currentWidth) = errorCheck(image, layer)
    # Determine if it's okay to proceed
    if canProceed == True:
        # No errors, can proceed
        # Determine if a plain portrait needs to be exported
        if plainChoice == 1:
            # A plain portrait is needed
            # Export a plain portrait
            exportStandardHUD(image, console, folderName, fileName, currentWidth, "None", "", alchemyVersion)
        # Determine if a portrait with a hero outline needs to be exported
        if heroOutlineChoice == 1:
            # A portrait with a hero outline is needed
            # Export a portrait with a hero outline
            exportStandardHUD(image, console, folderName, fileName, currentWidth, 0, "b_", alchemyVersion)
        # Determine if a portrait with a red villain outline needs to be exported
        if redVillainOutlineChoice == 1:
            # A portrait with a red villain outline is needed
            # Export a portrait with a hero outline
            exportStandardHUD(image, console, folderName, fileName, currentWidth, 1, "r_", alchemyVersion)
        # Determine if a portrait with a green villain outline needs to be exported
        if greenVillainOutlineChoice == 1:
            # A portrait with a green villain outline is needed
            # Export a portrait with a green outline
            exportStandardHUD(image, console, folderName, fileName, currentWidth, 2, "g_", alchemyVersion)
        # Determine if a next-gen-style portrait needs to be exported
        if nextGenChoice == 1:
            # A next-gen-style portrait is needed
            # Export a next-gen-style portrait
            exportNGHUD(image, console, folderName, fileName, currentWidth, alchemyVersion)
    else:
        # Errors, cannot proceed
        # Display an error message
        pdb.gimp_message("The image was not exported.")


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_asset_hud",
    "Exports a conversation portrait (HUD) texture in\nmultiple formats.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports a conversation portrait (HUD) texture in multiple formats.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2024",
    "Export Conversation Portrait (HUD)",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask or channel", None),
        (PF_OPTION, "console", "Console:", 0, ["All","PC Only"]),
        (PF_TOGGLE, "plainChoice", "Export a plain portrait?", 0),
        (PF_TOGGLE, "nextGenChoice", "Export an MUA1 next-gen\nstyle portrait?", 1),
        (PF_TOGGLE, "heroOutlineChoice", "Export a portrait with a\nhero outline?", 1),
        (PF_TOGGLE, "redVillainOutlineChoice", "Export a portrait with a\nred villain outline?", 0),
        (PF_TOGGLE, "greenVillainOutlineChoice", "Export a portrait with a\ngreen villain outline?", 0),
        (PF_OPTION, "alchemyVersion", "Alchemy Version:", 0, ["Alchemy 2.5","Alchemy 5"])
    ],
    [],
    exportHUD,
    menu="<Image>/Marvel Mods/Export Textures/By Asset Type"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()