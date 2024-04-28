#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a character select portrait (CSP)
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 01Feb2023: First published version.
#   v1.1: 21Apr2023: Updated folder names
#   v2.0: 19Jan2024: Full rewrite. Now uses common procedures, generates the CSP outline in process, and can do both portraits at the same time.    

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
            # Check if the image is too small
            if currentWidth >= 64:
                # Image is not too small, can proceed
                # Initialize a variable to keep track of the number of correctly named layers
                goodLayers = 0
                # List the layers to check
                for layerName in ["Frame", "Character", "XML1 Background", "XML2 Background"]:
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

# Define the XML1 exporting operation
def exportXML1CSP(image, console, folderName, fileName, currentWidth):
    # Create a duplicate image for the export
    exportImage = pdb.gimp_image_duplicate(image)
    # Get the layer to remove
    layerToRemove = pdb.gimp_image_get_layer_by_name(exportImage, "XML2 Background")
    # Remove the layer
    pdb.gimp_image_remove_layer(exportImage, layerToRemove)
    # Get the layer to add the outline to
    outlineLayer = pdb.gimp_image_get_layer_by_name(exportImage, "Character")
    # Generate an outline
    pdb.python_fu_marvelmods_utilities_generate_xml1_csp_outline(exportImage, outlineLayer, currentWidth)
    # Flatten the image
    exportLayer = pdb.gimp_image_flatten(exportImage)
    # Set up the file name
    outFileName = "x1c_" + fileName
    # Filter remaining options based on the console
    if console == 1:
        # PC Only
        # Do nothing
        pdb.gimp_message("No XML1 portrait is exported when \"PC Only\" is selected")
    else:
        # Consoles
        if currentWidth <= 128:
            # Console resolution or standard resolution
            # Export the cross-compatible version
            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "All", outFileName, 2)
        else:
            # HD resolution and higher
            # Get the updated width
            reducedWidth = currentWidth / 128
            # Resize to 128x128
            pdb.python_fu_marvelmods_scaling_scaleAny(exportImage, exportLayer, reducedWidth)
            # Export the cross-compatible version
            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "All", outFileName, 2)

# Define the XML2 exporting operation
def exportXML2CSP(image, console, folderName, fileName, currentWidth):
    # Create a duplicate image for the export
    exportImage = pdb.gimp_image_duplicate(image)
    # List the layers that need to be removed
    for layerName in ["Frame", "XML1 Background"]:
        # Get the layer by the name
        layerToRemove = pdb.gimp_image_get_layer_by_name(exportImage, layerName)
        # Remove the layer
        pdb.gimp_image_remove_layer(exportImage, layerToRemove)
    # Flatten the image
    exportLayer = pdb.gimp_image_flatten(exportImage)
    # Set up the file name
    outFileName = "x2c_" + fileName
    # Filter remaining options based on the image size
    if currentWidth == 64:
       # Console resolution
        # Filter remaining export options based on console selection
        if console == 1:
            # PC Only
            # Export for PC
            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC", outFileName, 2)
        else:
            # All consoles
            # Export the cross-compatible version
            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "All", outFileName, 2)
    elif currentWidth == 128:
        # standard resolution
        # Filter remaining export options based on console selection
        if console == 1:
            # PC Only
            # Export for PC
            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PC", outFileName, 2)
        else:
            # All consoles
            # Export the cross-compatible version
            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "All except PSP", outFileName, 2)
            # Resize to 64x64
            pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
            # Export the PSP version
            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PSP", outFileName, 2)
    else:
        # HD resolution and higher
        # Filter based on console selection
        if console == 1:
            # PC only
            # Export for PC
            pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "PC", outFileName, 0, 0)
        else:
            # All consoles
            # Export for PC
            pdb.python_fu_marvelmods_basic_exportDDS(exportImage, exportLayer, folderName, "PC", outFileName, 0, 0)
            # Get the updated width
            reducedWidth = currentWidth / 128
            # Resize to 128x128
            pdb.python_fu_marvelmods_scaling_scaleAny(exportImage, exportLayer, reducedWidth)
            # Export the console version
            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "GC, PS2, and Xbox", outFileName, 2)
            # Resize to 64x64
            pdb.python_fu_marvelmods_scaling_scaleHalf(exportImage, exportLayer)
            # Export the PSP version
            pdb.python_fu_marvelmods_basic_exportPNG(exportImage, exportLayer, folderName, "PSP", outFileName, 2)

# Define the main operation
def exportCSP(image, layer, console, xml1Choice, xml2Choice):
    # Save the file and get its path and name
    (folderName, fileName) = pdb.python_fu_marvelmods_basic_get_path_save(image, layer) 
    # Check for errors
    (canProceed, currentWidth) = errorCheck(image, layer)
    # Determine if it's okay to proceed
    if canProceed == True:
        # No errors, can proceed
        # Determine if no portrait was exported
        if (xml1Choice == 0) and (xml2Choice == 0):
            # No portrait was exported
            # Display an error message
            pdb.gimp_message("Nothing was exported. Choose at least one export type.")
        else:
            # Something was picked
            # Determine if an XML1 portrait should be exported
            if xml1Choice == 1:
                # XML1 portrait needed
                # Export for XML1
                exportXML1CSP(image, console, folderName, fileName, currentWidth)
            # Determine if an XML2 portrait should be exported
            if xml2Choice == 1:
                # XML2 portrait needed
                # Export for XML2
                exportXML2CSP(image, console, folderName, fileName, currentWidth)
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
    "python_fu_marvelmods_export_asset_csp",
    "Exports a character select portrait (CSP) texture\nin multiple formats.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports a character select portrait (CSP) texture in multiple formats.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2024",
    "Export Character Select Portrait (CSP)",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask or channel", None),
        (PF_OPTION, "console", "Console:", 0, ["All","PC Only"]),
        (PF_TOGGLE, "xml1Choice", "Export a CSP for XML1?", 0),
        (PF_TOGGLE, "xml2Choice", "Export a CSP for XML2?", 1)
    ],
    [],
    exportCSP,
    menu="<Image>/Marvel Mods/Export Textures/By Asset Type"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()