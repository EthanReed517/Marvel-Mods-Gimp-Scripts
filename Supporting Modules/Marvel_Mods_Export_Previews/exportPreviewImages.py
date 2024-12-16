#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP to plugin crop a skin preview for the PC version of X-Men Legends II: Rise of Apocalypse.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 14Dec2024: First published version.

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
# External modules
import os.path


# ######## #
# FUNCTION #
# ######## #
# Define the function for creating a new image
def createNewImage(width, height):
    # Start the new image
    newImage = pdb.gimp_image_new(width, height, 0)
    # Create a new layer for this image
    newLayer = pdb.gimp_layer_new(newImage, width, height, 1, "New Layer", 100, 28)
    # Get the active layer of the image
    activeLayer = pdb.gimp_image_get_active_layer(newImage)
    # Apply the new layer to the active layer
    pdb.gimp_image_insert_layer(newImage, newLayer, activeLayer, 0)
    # Get the new active layer
    newLayer = pdb.gimp_image_get_active_layer(newImage)
    # Return the new image and layer
    return newImage, newLayer

# Define the function for getting the file name
def getAssetFileName(xcfPath, assetType, skinNum, descriptor):
    # Get the folder
    folder = os.path.dirname(xcfPath)
    # Determine if any descriptor is needed for a suffix
    if not(descriptor == "None"):
        suffix = " - " + descriptor
    else:
        suffix = ""
    # Set up the dictionary of file names based on asset type
    fileNameDict = {
        "Skin": skinNum + " (Skin" + suffix + ")",
        "HUD": "hud_head_" + skinNum + " (" + suffix + ")",
        "Head": skinNum + " (3D Head" + suffix + ")",
        "CSP": skinNum + " (Character Select Portrait" + suffix + ")",
        "Mann": skinNum + " (Mannequin" + suffix + ")"
    }
    # Get the out file path using the asset type
    outFilePath = os.path.join(folder, fileNameDict[assetType] + ".png")
    # Fix the Start of the suffix for HUDs
    if "( - " in outFilePath:
        outFilePath = outFilePath.replace("( - ", "(")
    # Fix the ending for huds without suffixes
    if " ()" in outFilePath:
        outFilePath = outFilePath.replace(" ()", "")
    # Return the file path
    return outFilePath

# Define the function for cropping the preview
def cropPreview(image, layer, assetType, game):
    # Start a variable that assumes that the crop was successful
    cropSuccessful = True
    # Set up the dictionary for the processing dimensions
    if game == "XML":
        # XML2
        dimsDict = {
            "Skin": {"width": 543, "height": 1080, "xOffset": -222, "yOffset": 0},
            "HUD": {"width": 152, "height": 152, "xOffset": -280, "yOffset": -496, "circle": True},
            "Head": {"width": 201, "height": 201, "xOffset": -116, "yOffset": -747},
            "CSP": {"width": 163, "height": 163, "xOffset": -360, "yOffset": -320}
        }
    else:
        # MUA1
        dimsDict = {
            "Skin": {"width": 395, "height": 785, "xOffset": -339, "yOffset": -196, "scale": True},
            "HUD": {"width": 169, "height": 169, "xOffset": -90, "yOffset": -850, "circle": True},
            "Mann": {"width": 493, "height": 981, "xOffset": -713, "yOffset": 0, "scale": True}
        }
    # Execute the operation
    try:
        # Crop the image accordingly
        pdb.gimp_image_resize(image, dimsDict[assetType]["width"], dimsDict[assetType]["height"], dimsDict[assetType]["xOffset"], dimsDict[assetType]["yOffset"])
        # Resize the layer to the image size
        pdb.gimp_layer_resize_to_image_size(layer)
        # Determine if it's necessary to crop it to a circle
        if dimsDict[assetType].get("circle", False) == True:
            # This needs to be a circle
            # Add an alpha channel just in case the layer doesn't currently have one
            pdb.gimp_layer_add_alpha(layer)
            # Create a circular (elliptical) selection for the portrait
            pdb.gimp_image_select_ellipse(image, CHANNEL_OP_ADD, 0, 0, dimsDict[assetType]["width"], dimsDict[assetType]["height"])
            # Invert the selection (because the stuff outside the circle needs to be deleted)
            pdb.gimp_selection_invert(image)
            # Delete what's selected
            pdb.gimp_drawable_edit_clear(layer)
            # Clear the selection
            pdb.gimp_selection_none(image)
        # Determine if it's necessary to scale the image
        if dimsDict[assetType].get("scale", False) == True:
            # This needs to be scaled (MUA1 skin or mannequin)
            # Scale the image accordingly
            pdb.gimp_image_scale(image, 543, 1080)
            # Resize the layer to the image size
            pdb.gimp_layer_resize_to_image_size(layer)
    except KeyError:
        # Create an error
        pdb.gimp_message("ERROR: A layer with an unrecognized asset type (" + assetType + ") was found. This layer was not exported.")
        # Update to indicate that the crop was not successful
        cropSuccessful = False
    # Return the crop status
    return cropSuccessful

# Define the main operation
def fullPreview(image, layer, game):
    # Verify that the image is 1920x1080
    if not((image.width == 1920) and (image.height == 1080)):
        # Warn the user
        pdb.gimp_message("ERROR: The image is not 1920 x 1080. This size is required for the locations to be correct. Nothing will be exported.")
    else:
        # It's okay to proceed
        # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
        pdb.gimp_selection_none(image)
        # Get the file path of the image
        xcfPath = pdb.gimp_image_get_filename(image)
        # Save the file as an xcf
        pdb.gimp_file_save(image, layer, xcfPath, xcfPath)
        # Start counters to keep track of the number of rows and columns in the final image
        rowCount = 1
        columnCount = 1
        # Start a list to track the images that need to be added to the final preview
        imageList = []
        # Start a counter to keep track of the current image for naming purposes
        counter = 1
        # Loop through the layers in the current image
        for assetLayer in image.layers:
            # Get the layer's name
            layerName = pdb.gimp_item_get_name(assetLayer)
            # Split the name to get the information
            layerNameSplit = layerName.split(",")
            assetType = layerNameSplit[0]
            skinNum = layerNameSplit[1]
            row = int(layerNameSplit[2])
            column = int(layerNameSplit[3])
            position = int(layerNameSplit[4])
            descriptor = layerNameSplit[5]
            # Start a new image for this asset
            assetImage, newLayer = createNewImage(image.width, image.height)
            # Copy the asset layer and paste it in the new image
            pdb.gimp_edit_copy(assetLayer)
            floatingLayer = pdb.gimp_edit_paste(newLayer, False)
            pdb.gimp_floating_sel_anchor(floatingLayer)
            # Get the active layer of the new image
            activeLayer = pdb.gimp_image_get_active_layer(assetImage)
            # Get the name of the file
            outFilePath = getAssetFileName(xcfPath, assetType, skinNum, descriptor)
            # Crop the image accordingly
            cropSuccessful = cropPreview(assetImage, activeLayer, layerNameSplit[0], game)
            # Verify that the crop was achieved successfully
            if cropSuccessful == True:
                # Export the new image
                pdb.file_png_save(assetImage, activeLayer, outFilePath, outFilePath, 0, 9, 0, 0, 0, 0, 0)
                # Check if the number of rows or columns needs to be updated
                if int(layerNameSplit[2]) > rowCount:
                    rowCount = int(layerNameSplit[2])
                if int(layerNameSplit[3]) > columnCount:
                    columnCount = int(layerNameSplit[3])
                # Set the image name for disambiguation purposes
                pdb.gimp_image_set_filename(assetImage, "image" + str(counter))
                counter += 1
                # Add the image to the preview list
                imageList.append({"image": assetImage, "row": int(layerNameSplit[2]), "column": int(layerNameSplit[3]), "position": int(layerNameSplit[4])})
        # Create the image for the combined preview
        combinedImage, combinedLayer = createNewImage(543 * columnCount, 1080 * rowCount)
        # Loop through the images to add to the combined preview
        for assetImageDict in imageList:
            # Get the active layer of the image
            exportImageLayer = pdb.gimp_image_get_active_layer(assetImageDict["image"])
            # Copy the asset layer and paste it in the new image
            pdb.gimp_edit_copy(exportImageLayer)
            floatingLayer = pdb.gimp_edit_paste(combinedLayer, False)
            # Determine the goal positions
            xGoalsDict = {
                "0": 0,
                "1": (100 - (assetImageDict["image"].width / 2)),
                "2": (272 - (assetImageDict["image"].width / 2)),
                "3": (443 - (assetImageDict["image"].width / 2)),
                "4": (100 - (assetImageDict["image"].width / 2)),
                "5": (443 - (assetImageDict["image"].width / 2))
            }
            yGoalsDict = {
                "0": 0,
                "1": (100 - (assetImageDict["image"].height / 2)),
                "2": (100 - (assetImageDict["image"].height / 2)),
                "3": (100 - (assetImageDict["image"].height / 2)),
                "4": (250 - (assetImageDict["image"].height / 2)),
                "5": (250 - (assetImageDict["image"].height / 2))
            }
            # Determine the offsets
            xOffset, yOffset = floatingLayer.offsets
            xGoal = (543 * (assetImageDict["column"] - 1)) + xGoalsDict[str(assetImageDict["position"])]
            yGoal = (1080 * (assetImageDict["row"] - 1)) + yGoalsDict[str(assetImageDict["position"])]
            xOffset = xGoal - xOffset
            yOffset = yGoal - yOffset
            pdb.gimp_layer_translate(floatingLayer, xOffset, yOffset)
            # Anchor the layer
            pdb.gimp_floating_sel_anchor(floatingLayer)
            combinedLayer = pdb.gimp_image_get_active_layer(combinedImage)
        # Export the combined image
        outFilePath = os.path.join(os.path.dirname(xcfPath), "Full_3Full.png")
        pdb.file_png_save(combinedImage, combinedLayer, outFilePath, outFilePath, 0, 9, 0, 0, 0, 0, 0)
        # Crop the image accordingly
        pdb.gimp_image_resize(combinedImage, 543, 1080, 0, 0)
        # Resize the layer to the image size
        pdb.gimp_layer_resize_to_image_size(combinedLayer)
        # Export the combined image
        outFilePath = os.path.join(os.path.dirname(xcfPath), "Full_2HalfLarge.png")
        pdb.file_png_save(combinedImage, combinedLayer, outFilePath, outFilePath, 0, 9, 0, 0, 0, 0, 0)
        # Scale the image accordingly
        pdb.gimp_image_scale(combinedImage, 251, 500)
        # Resize the layer to the image size
        pdb.gimp_layer_resize_to_image_size(combinedLayer)
        # Export the combined image
        outFilePath = os.path.join(os.path.dirname(xcfPath), "Full_1HalfSmall.png")
        pdb.file_png_save(combinedImage, combinedLayer, outFilePath, outFilePath, 0, 9, 0, 0, 0, 0, 0)
        # Print the success message
        pdb.gimp_message("SUCCESS: exported " + xcfPath)