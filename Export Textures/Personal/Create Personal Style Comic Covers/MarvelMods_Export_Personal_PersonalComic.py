#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to create a comic cover from a character screenshot
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
# Define the main operation
def createPersonalComic(image, layer, xml1Choice, xml2Choice, mua1Choice, charSquat, bigLogo, smallLogo, directory, desc):
    # Set the character height
    charHeight = 1500
    # Create a duplicate image of the character
    charImage = pdb.gimp_image_duplicate(image)
    charLayer = pdb.gimp_image_get_active_layer(charImage)
    # Get the proper height and width
    newHeight = charHeight * charSquat
    newWidth = (charImage.width * (charHeight / float(charImage.height))) * charSquat
    # Scale the character image accordingly
    pdb.gimp_image_scale(charImage, newWidth, newHeight)
    # Open the template image
    tempImage = pdb.gimp_xcf_load(0, os.path.join(gimp.directory, "plug-ins", "MarvelModsTemplates", "BW17_Comic.xcf"), os.path.join(gimp.directory, "plug-ins", "MarvelModsTemplates", "BW17_Comic.xcf"))
    # Duplicate the template image
    templateImage = pdb.gimp_image_duplicate(tempImage)
    # Set up the list of icons to add
    iconList = [
        {"path": bigLogo, "xPos": 738, "yPos": 36},
        {"path": smallLogo, "xPos": 112, "yPos": 133}
    ]
    # Loop through the icons
    for icon in iconList:
        # Get the active layer of the template
        templateLayer = pdb.gimp_image_get_active_layer(templateImage)
        # Open the icon's image
        iconImage = pdb.gimp_xcf_load(0, icon["path"], icon["path"])
        # Get the active layer of the icon image
        iconLayer = pdb.gimp_image_get_active_layer(iconImage)
        # Copy the icon layer and paste it in the new image
        pdb.gimp_edit_copy(iconLayer)
        floatingLayer = pdb.gimp_edit_paste(templateLayer, False)
        # Determine the offsets
        xOffset, yOffset = floatingLayer.offsets
        xOffset = icon["xPos"] - xOffset
        yOffset = icon["yPos"] - yOffset
        pdb.gimp_layer_translate(floatingLayer, xOffset, yOffset)
        # Anchor the layer
        pdb.gimp_floating_sel_anchor(floatingLayer)
    # Get the active layer again
    templateLayer = pdb.gimp_image_get_active_layer(templateImage)
    # Create a new layer for the character
    templateCharLayer = pdb.gimp_layer_new(templateImage, templateImage.width, templateImage.height, 1, "Character", 100, 28)
    pdb.gimp_image_add_layer(templateImage, templateCharLayer, 0)
    # Copy the asset layer and paste it in the new image
    pdb.gimp_edit_copy(charLayer)
    floatingLayer = pdb.gimp_edit_paste(templateCharLayer, False)
    # Determine the offsets
    xOffset, yOffset = floatingLayer.offsets
    xOffset = (642 - (charImage.width / 2)) - xOffset
    yOffset = (1800 - charImage.height) - yOffset
    pdb.gimp_layer_translate(floatingLayer, xOffset, yOffset)
    # Anchor the layer
    pdb.gimp_floating_sel_anchor(floatingLayer)
    # Create the outline
    pdb.python_fu_gegl_dropshadow(templateImage, templateCharLayer, 0.0, 0.0, 20.0, 1, 10, (0, 0, 0), 0.75)
    # Get the active layer again
    templateLayer = pdb.gimp_image_get_active_layer(templateImage)
    # Display the image
    #display = pdb.gimp_display_new(templateImage)
    # Flush displays
    #pdb.gimp_displays_flush()
    # Set up the file path
    xcfPath = os.path.join(directory, "Comic Covers", desc, os.path.basename(directory).replace(" ", "_").lower() + "_cov.xcf")
    # Check if the folder exists
    if os.path.exists(os.path.dirname(xcfPath)) == False:
        makedirs(os.path.dirname(xcfPath))
    # Save the file as an xcf
    pdb.gimp_xcf_save(0, templateImage, templateLayer, xcfPath, xcfPath)
    pdb.gimp_image_set_filename(templateImage, xcfPath)
    # Export the image
    MMET.exportComic(templateImage, templateLayer, 0, 0, xml1Choice, xml2Choice, mua1Choice)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_utilities_personalcomic",
    "Creates comic covers from character screenshots.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Creates comic covers from character screenshots.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2025",
    "Create Personal-Style Comic Cover",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask or channel", None),
        (PF_TOGGLE, "xml1Choice", "Create an XML1 comic cover?", 0),
        (PF_TOGGLE, "xml2Choice", "Create an XML2 comic cover?", 1),
        (PF_TOGGLE, "mua1Choice", "Create an MUA1 comic cover?", 1),
        (PF_FLOAT, "charSquat", "Squat modifier:", 1.00),
        (PF_FILE, "bigLogo", "Big Logo:", os.path.join(gimp.directory, "plug-ins", "MarvelModsTemplates", "Logos", "Big", "X-Men.xcf")),
        (PF_FILE, "smallLogo", "Small Logo:", os.path.join(gimp.directory, "plug-ins", "MarvelModsTemplates", "Logos", "Small", "X-Men.xcf")),
        (PF_DIRNAME, "directory", "Character folder:", "C:\\Users\\ethan\\Desktop\\Marvel Mods\\BaconWizard17-Custom-Models\\Characters"),
        (PF_STRING, "desc", "Comic cover description:", "Description")
    ],
    [],
    createPersonalComic,
    menu="<Image>/Marvel Mods/Export Textures/Personal"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()