#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP to plugin create a skin preview collection from a .xml file.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 30Dec2024: First published version.

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
from os import listdir, makedirs
import xml.etree.ElementTree as ET


# ######### #
# FUNCTIONS #
# ######### #
# Define the function for opening an xml file and getting the tree and root
def openGetTreeAndRoot(file):
    # Parse the file to get the tree
    try:
        tree = ET.parse(file)
    except:
        pdb.gimp_message("Failed to open " + file + " due to a formatting error.")
        tree = ET.parse(file)
    # Get the root from the tree
    root = tree.getroot()
    # Return the root for further operations
    return root

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

# Define the main operation
def xmlPreview(character):
    # Set the screenshot path
    screenshotOutPath = "C:\\Users\\ethan\\Pictures\\Skin Pack Screenshots"
    # Open the xml file and get its root
    packsRoot = openGetTreeAndRoot(character)
    # Loop through the packs
    for packElem in packsRoot.findall("pack"):
        # Get the number of rows and columns of the pack
        columnCount = int(packElem.get("columns"))
        rowCount = int(packElem.get("rows"))
        # Create the image for the combined preview
        combinedImage, combinedLayer = createNewImage(543 * columnCount, 1080 * rowCount)
        # Set the foreground fill color
        pdb.gimp_context_set_foreground((255, 255, 255))
        # Set the background fill color
        pdb.gimp_context_set_background((0, 0, 0))
        # Fill the layer with the background color
        pdb.gimp_drawable_fill(combinedLayer, 1)
        # Loop through the screenshots
        for screenshotElem in packElem.findall("screenshot"):
            # Get the active layer of the image
            combinedLayer = pdb.gimp_image_get_active_layer(combinedImage)
            # Determine if there is a path
            if screenshotElem.get("path") is not None:
                # There is a path
                # Open the screenshot
                screenshotImage = pdb.file_png_load(screenshotElem.get("path"), screenshotElem.get("path"))
                # Get the active layer of the image
                screenshotLayer = pdb.gimp_image_get_active_layer(screenshotImage)
                # Copy the asset layer and paste it in the new image
                pdb.gimp_edit_copy(screenshotLayer)
                floatingLayer = pdb.gimp_edit_paste(combinedLayer, False)
                # Get the position of the image
                if screenshotElem.get("pos") is None:
                    position = "0"
                else:
                    position = screenshotElem.get("pos")
                # Determine the goal positions
                xGoalsDict = {
                    "0": 0,
                    "1": (100 - (screenshotImage.width / 2)),
                    "2": (272 - (screenshotImage.width / 2)),
                    "3": (443 - (screenshotImage.width / 2)),
                    "4": (100 - (screenshotImage.width / 2)),
                    "5": (443 - (screenshotImage.width / 2))
                }
                yGoalsDict = {
                    "0": 0,
                    "1": (100 - (screenshotImage.height / 2)),
                    "2": (100 - (screenshotImage.height / 2)),
                    "3": (100 - (screenshotImage.height / 2)),
                    "4": (250 - (screenshotImage.height / 2)),
                    "5": (250 - (screenshotImage.height / 2))
                }
                # Determine the offsets
                xOffset, yOffset = floatingLayer.offsets
                xGoal = (543 * (int(screenshotElem.get("column")) - 1)) + xGoalsDict[position]
                yGoal = (1080 * (int(screenshotElem.get("row")) - 1)) + yGoalsDict[position]
                xOffset = xGoal - xOffset
                yOffset = yGoal - yOffset
                pdb.gimp_layer_translate(floatingLayer, xOffset, yOffset)
                # Anchor the layer
                pdb.gimp_floating_sel_anchor(floatingLayer)
                combinedLayer = pdb.gimp_image_get_active_layer(combinedImage)
            # Determine if the layer needs text
            if screenshotElem.get("desc") is not None:
                # Text is needed
                # Determine where the screenshots were taken
                if packElem.get("source") == "XML2":
                    # Set the foreground fill color
                    pdb.gimp_context_set_foreground((255, 255, 255))
                    # Get the X and Y positions
                    xPos = (543 * (int(screenshotElem.get("column")) - 1)) + 112
                    yPos = (1080 * (int(screenshotElem.get("row")) - 1)) + 998
                else:
                    # The screenshots were taken in MUA1
                    # Set the foreground fill color
                    if screenshotElem.get("path") is None:
                        pdb.gimp_context_set_foreground((255, 255, 255))
                    else:
                        pdb.gimp_context_set_foreground((0, 0, 0))
                    # Get the X and Y positions
                    xPos = (543 * (int(screenshotElem.get("column")) - 1)) + 22
                    yPos = (1080 * (int(screenshotElem.get("row")) - 1)) + 1004
                # Create the text
                text_layer = pdb.gimp_text_fontname(combinedImage, combinedLayer, xPos, yPos, screenshotElem.get("desc"), 0, True, 28, 0, "Gunship Condensed, Condensed")
                # Merge the layer
                pdb.gimp_floating_sel_anchor(text_layer)
        # Export the combined image
        outFilePath = os.path.join(screenshotOutPath, packElem.get("subFolder"), packElem.get("name") + ".png")
        if not(os.path.exists(os.path.dirname(outFilePath))):
            makedirs(os.path.dirname(outFilePath))
        pdb.file_png_save(combinedImage, combinedLayer, outFilePath, outFilePath, 0, 9, 0, 0, 0, 0, 0)
    # Print the success message
    pdb.gimp_message("SUCCESS: exported all previews for " + os.path.basename(character))


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_preview_common_xml",
    "Uses a .xml file to create multi-skin previews.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Uses a .xml file to create multi-skin previews.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2024",
    "Create Multi-Skin Previews from .xml",
    "",
    [
        (PF_FILENAME, "character", "Character XML File:", 0)
    ],
    [],
    xmlPreview,
    menu="<Image>/Marvel Mods/Skin Previews/Skin Showcase"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()