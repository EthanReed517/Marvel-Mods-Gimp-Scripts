#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a comic cover texture.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 17Dec2024: First published version.

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
# Define the operation for exporting the XML1 texture
def exportXML1Cov(xcfPath, image, console, alchemyVersion):
    # Determine if the correct console was picked
    if console == 0:
        # Determine if the correct Alchemy version was picked
        if alchemyVersion == 0:
            # Everything is correct
            # Get the active layer of the image
            layer = pdb.gimp_image_get_active_layer(image)
            # Export a plain png copy as a preview
            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="!Preview", fileNameSuffix=" (XML1)")
            # Scale the image accordingly
            pdb.gimp_image_scale(image, 1024, 1024)
            # Export for Xbox
            MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="XML1 Xbox")
            # Export for PS2
            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, scale_factor=0.5, subFolder="XML1 PS2")
            # Export for GameCube
            MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", scale_factor=0.5, subFolder="XML1 GC")

# Define the operation for exporting the XML2 texture
def exportXML2Cov(xcfPath, image, console, alchemyVersion):
    # Determine if the correct Alchemy version was picked
    if alchemyVersion == 0:
        # Get the active layer of the image
        layer = pdb.gimp_image_get_active_layer(image)
        # Crop the image accordingly
        pdb.gimp_image_resize(image, 1365, 1024, -228, 0)
        # Resize the layer to the image size
        pdb.gimp_layer_resize_to_image_size(layer)
        # Export a plain png copy as a preview
        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="!Preview", fileNameSuffix=" (XML2)")
        # Scale the image accordingly
        pdb.gimp_image_scale(image, 1024, 1024)
        # Determine which console was picked
        if console == 0:
            # All consoles
            # Export for PC and Xbox
            MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="XML2 PC and Xbox")
            # Export for PS2
            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, scale_factor=0.5, subFolder="XML2 PS2")
            # Export for GameCube
            MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", scale_factor=0.5, subFolder="XML2 GC")
        else:
            # PC only
            # Export for PC
            MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="XML2 PC")

# Define the operation for exporting the XML2 PSP texture
def exportXML2PSPCov(xcfPath, image, console, alchemyVersion):
    # Determine if the correct console was picked
    if console == 0:
        # Get the active layer of the image
        layer = pdb.gimp_image_get_active_layer(image)
        # Export a plain png copy as a preview
        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="!Preview", fileNameSuffix=" (XML2 PSP)")
        # Scale the image accordingly
        pdb.gimp_image_scale(image, 512, 512)
        # Determine which version of Alchemy was picked
        if alchemyVersion == 0:
            # Alchemy 2.5
            # Export for PSP
            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder="XML2 PSP")
        else:
            # Alchemy 5
            # Export for PSP
            MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", subFolder="XML2 PSP")

# Define the function for exporting the next-gen MUA1 texture
def exportMUA1NGCov(xcfPath, image, console, alchemyVersion):
    # Get the active layer of the image
    layer = pdb.gimp_image_get_active_layer(image)
    # Export a plain png copy as a preview
    MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="!Preview", fileNameSuffix=" (MUA1)")
    # Scale the image accordingly
    pdb.gimp_image_scale(image, 2048, 1024)
    # Determine which console was picked
    if console == 0:
        # All consoles
        # Determine which version of Alchemy was picked
        if alchemyVersion == 0:
            # Alchemy 2.5
            # Export for Next-Gen MUA1
            MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 Next-Gen")
        else:
            # Alchemy 5
            # Export for Next-Gen MUA1
            MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", subFolder="MUA1 Next-Gen")
    else:
        # PC only
        # Determine which version of Alchemy was picked
        if alchemyVersion == 0:
            # Alchemy 2.5
            # Export for Next-Gen MUA1
            MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 PC and Steam")
        else:
            # Alchemy 5
            # Export for Next-Gen MUA1
            MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", subFolder="MUA1 PC and Steam")

# Define the function for exporting the last-gen MUA1 texture
def exportMUA1LGCov(xcfPath, image, console, alchemyVersion):
    # Determine which console was picked
    if console == 0:
        # All consoles
        # Get the active layer of the image
        layer = pdb.gimp_image_get_active_layer(image)
        # Scale the image accordingly
        pdb.gimp_image_scale(image, 1024, 1024)
        # Determine which version of ALchemy was picked
        if alchemyVersion == 0:
            # Alchemy 2.5
            # Export for Xbox and Wii
            MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="MUA1 Wii and Xbox")
            # Export for PS2 and PSP
            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, scale_factor=0.5, subFolder="MUA1 PS2 and PSP")
        else:
            # Alchemy 5
            # Export for Wii
            MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", subFolder="MUA1 Wii")
            # Export for PSP
            MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", scale_factor=0.5, subFolder="MUA1 PSP")

# Define the main operation
def exportComic(image, layer, console, alchemyVersion, xml1Choice, xml2Choice, mua1Choice):
    # Perform initial operations on the comic cover
    xcfPath = MMBGP.initialOpsComic(image, layer)
    # Create the list of consoles
    gameList = []
    if xml1Choice == 1:
        gameList.append("XML1")
    if xml2Choice == 1:
        gameList.append("XML2")
        gameList.append("XML2_PSP")
    if mua1Choice == 1:
        gameList.append("MUA1_LG")
        gameList.append("MUA1_NG")
    # Set up the dictionary of game-specific information
    gameInfoDict = {
        "XML1": {"width": 573, "height": 885, "xOffset": 397, "yOffset": 72, "exportFunction": exportXML1Cov, "templateFileName": "XML1_Comic.xcf"},
        "XML2": {"width": 562, "height": 863, "xOffset": 613, "yOffset": 51, "exportFunction": exportXML2Cov, "templateFileName": "XML2_Comic.xcf"},
        "XML2_PSP": {"width": 562, "height": 863, "xOffset": 613, "yOffset": 51, "exportFunction": exportXML2PSPCov, "templateFileName": "XML2_Comic.xcf"},
        "MUA1_LG": {"width": 544, "height": 838, "xOffset": 814, "yOffset": 94, "exportFunction": exportMUA1LGCov, "templateFileName": "MUA1_Comic.xcf"},
        "MUA1_NG": {"width": 544, "height": 838, "xOffset": 814, "yOffset": 94, "exportFunction": exportMUA1NGCov, "templateFileName": "MUA1_Comic.xcf"}
    }
    # Loop through the list of consoles
    for game in gameList:
        # Create a duplicate image of the cover
        coverImage = pdb.gimp_image_duplicate(image)
        coverLayer = pdb.gimp_image_merge_visible_layers(coverImage, 1)
        # Scale the image accordingly for the game
        pdb.gimp_image_scale(coverImage, gameInfoDict[game]["width"], gameInfoDict[game]["height"])
        # Open the game-specific image and get its active layer
        gameImage = pdb.gimp_xcf_load(0, os.path.join(gimp.directory, "plug-ins", "MarvelModsTemplates", gameInfoDict[game]["templateFileName"]), os.path.join("MarvelModsTemplates", gameInfoDict[game]["templateFileName"]))
        gameLayer = pdb.gimp_image_get_active_layer(gameImage)
        # Copy the asset layer and paste it in the new image
        pdb.gimp_edit_copy(coverLayer)
        floatingLayer = pdb.gimp_edit_paste(gameLayer, False)
        # Determine the offsets
        xOffset, yOffset = floatingLayer.offsets
        xOffset = gameInfoDict[game]["xOffset"] - xOffset
        yOffset = gameInfoDict[game]["yOffset"] - yOffset
        pdb.gimp_layer_translate(floatingLayer, xOffset, yOffset)
        # Anchor the layer
        pdb.gimp_floating_sel_anchor(floatingLayer)
        # Export the image
        gameInfoDict[game]["exportFunction"](xcfPath, gameImage, console, alchemyVersion)
    # Print the success message
    pdb.gimp_message("SUCCESS: exported " + xcfPath)