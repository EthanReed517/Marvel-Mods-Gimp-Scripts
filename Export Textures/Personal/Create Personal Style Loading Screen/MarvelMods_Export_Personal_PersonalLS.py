#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to create a loading screen from a character screenshot
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 02Jan2025: First published version.   

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
import Marvel_Mods_Export_Textures as MMET
# External modules
from os import makedirs
import os.path


# ######### #
# FUNCTIONS #
# ######### #
# Define the function for splitting the character name
def splitCharName(charName):
    # Split by spaces
    charNameSplit = charName.split(" ")
    # Start a list that will contain the resulting names
    charNameList = []
    # Start a counter to track the index
    index = 0
    # Start a list of indices that have been used
    indicesUsed = []
    # Loop through the words
    for word in charNameSplit:
        # Determine if this index has been used
        if index in indicesUsed:
            # This word has already been used
            # Pass
            pass
        else:
            # This word has not been used
            # Check if this is the last word
            if index == (len(charNameSplit) - 1):
                # This is the last word
                # Add it to the list
                charNameList.append(word)
                # Add the index to the list
                indicesUsed.append(index)
            else:
                # This is not the last word
                # Determine the length of this word and the next one
                if len(word + " " + charNameSplit[index + 1]) < 12:
                    # The length is less than 12, so the words can be combined
                    # Append to the list
                    charNameList.append(word + " " + charNameSplit[index + 1])
                    # Add the indices to the list
                    indicesUsed.append(index)
                    indicesUsed.append(index + 1)
                else:
                    # Add just one word to the list
                    charNameList.append(word)
                    # Add the index to the list
                    indicesUsed.append(index)
        # Increment the counter
        index += 1
    # Return the list of words
    return charNameList

# Define the main operation
def createPersonalLS(image, layer, hero4_3choice, vill4_3choice, hero16_9choice, vill16_9choice, charName, charSquat, directory, desc):
    # Create a duplicate image of the character
    charImage = pdb.gimp_image_duplicate(image)
    charLayer = pdb.gimp_image_get_active_layer(charImage)
    # Get the proper height and width
    newHeight = 800 * charSquat
    newWidth = (charImage.width * (800 / float(charImage.height))) * charSquat
    # Scale the character image accordingly
    pdb.gimp_image_scale(charImage, newWidth, newHeight)
    # Split the character name into a list
    charNameList = splitCharName(charName)
    # Set up the list for processing
    screenList = [
        {"variable": hero4_3choice, "templateFileName": "BW17_Load_Hero.xcf", "color": (0, 131, 221), "fontHeight": 75, "fontHeightOutline": 80, "charCenter": 986, "crop": True, "folder": "XML"},
        {"variable": vill4_3choice, "templateFileName": "BW17_Load_Villain.xcf", "color": (156, 6, 0), "fontHeight": 75, "fontHeightOutline": 80, "charCenter": 986, "crop": True, "folder": "XML", "prefix": "v_"},
        {"variable": hero16_9choice, "templateFileName": "BW17_Load_Hero.xcf", "color": (0, 131, 221), "fontHeight": 94, "fontHeightOutline": 100, "charCenter": 1212, "crop": False, "folder": "MUA"},
        {"variable": vill16_9choice, "templateFileName": "BW17_Load_Villain.xcf", "color": (156, 6, 0), "fontHeight": 94, "fontHeightOutline": 100, "charCenter": 1212, "crop": False, "folder": "MUA", "prefix": "v_"}
    ]
    # Loop through the list of possible loading screens to create
    for screen in screenList:
        # Determine if the variable is true
        if screen["variable"] == True:
            # This should be processed
            # Open the template image
            tempImage = pdb.gimp_xcf_load(0, os.path.join(gimp.directory, "plug-ins", "MarvelModsTemplates", screen["templateFileName"]), os.path.join(gimp.directory, "plug-ins", "MarvelModsTemplates", screen["templateFileName"]))
            # Duplicate the template image and get its active layer
            templateImage = pdb.gimp_image_duplicate(tempImage)
            templateLayer = pdb.gimp_image_get_active_layer(templateImage)
            # Crop the image accordingly
            if screen["crop"] == True:
                pdb.gimp_image_resize(templateImage, 1365, 1024, -226, 0)
                # Resize the layer to the image size
                pdb.gimp_layer_resize_to_image_size(templateLayer)
            # Copy the asset layer and paste it in the new image
            pdb.gimp_edit_copy(charLayer)
            floatingLayer = pdb.gimp_edit_paste(templateLayer, False)
            # Determine the offsets
            xOffset, yOffset = floatingLayer.offsets
            xOffset = (screen["charCenter"] - (charImage.width / 2)) - xOffset
            yOffset = (913 - charImage.height) - yOffset
            pdb.gimp_layer_translate(floatingLayer, xOffset, yOffset)
            # Anchor the layer
            pdb.gimp_floating_sel_anchor(floatingLayer)
            # Get the active layer again
            templateLayer = pdb.gimp_image_get_active_layer(templateImage)
            # Set the color for the text
            pdb.gimp_context_set_foreground(screen["color"])
            # Start a counter for the words
            wordCount = 0
            # Loop through the words
            for word in charNameList:
                # Set the color for the outline text
                pdb.gimp_context_set_foreground(screen["color"])
                # Create the outline text
                text_layer = pdb.gimp_text_fontname(templateImage, templateLayer, 100, (100 + (wordCount * screen["fontHeight"])), word, 0, True, screen["fontHeightOutline"], 1, "Gunship Outline")
                # Merge the layer
                pdb.gimp_floating_sel_anchor(text_layer)
                # Get the active layer again
                templateLayer = pdb.gimp_image_get_active_layer(templateImage)
                # Set the color for the white text
                pdb.gimp_context_set_foreground((255, 255, 255))
                # Create the white text
                text_layer = pdb.gimp_text_fontname(templateImage, templateLayer, 100, (100 + (wordCount * screen["fontHeight"])), word, 0, True, screen["fontHeight"], 1, "Gunship")
                # Merge the layer
                pdb.gimp_floating_sel_anchor(text_layer)
                # Get the active layer again
                templateLayer = pdb.gimp_image_get_active_layer(templateImage)
                # Increment the word count
                wordCount += 1
            # Display the image
            #display = pdb.gimp_display_new(templateImage)
            # Flush displays
            #pdb.gimp_displays_flush()
            # Set up the file path
            xcfPath = os.path.join(directory, "Loading Screens (" + screen["folder"] + ")", desc, screen.get("prefix", "") + "12301.xcf")
            # Check if the folder exists
            if os.path.exists(os.path.dirname(xcfPath)) == False:
                makedirs(os.path.dirname(xcfPath))
            # Save the file as an xcf
            pdb.gimp_xcf_save(0, templateImage, templateLayer, xcfPath, xcfPath)
            pdb.gimp_image_set_filename(templateImage, xcfPath)
            # Export the image
            MMET.exportConceptLoading(templateImage, templateLayer, 0, 0, "loading")


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_utilities_personalls",
    "Creates loading screens from character screenshots.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Creates loading screens from character screenshots.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2025",
    "Create Personal-Style Loading Screen",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask or channel", None),
        (PF_TOGGLE, "hero4_3choice", "Create a 4:3 hero loading screen?", 1),
        (PF_TOGGLE, "vill4_3choice", "Create a 4:3 villain loading screen?", 0),
        (PF_TOGGLE, "hero16_9choice", "Create a 16:9 hero loading screen?", 1),
        (PF_TOGGLE, "vill16_9choice", "Create a 16:9 villain loading screen?", 0),
        (PF_STRING, "charName", "Character name:", "Character Name"),
        (PF_FLOAT, "charSquat", "Squat modifier:", 1.00),
        (PF_DIRNAME, "directory", "Character folder:", "C:\\Users\\ethan\\Desktop\\Marvel Mods\\BaconWizard17-Custom-Models\\Characters"),
        (PF_STRING, "desc", "Loading screen description:", "Description")
    ],
    [],
    createPersonalLS,
    menu="<Image>/Marvel Mods/Export Textures/Personal"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()