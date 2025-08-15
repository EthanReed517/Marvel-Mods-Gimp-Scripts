#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a character select portrait (CSP) and conversation portrait (HUD)
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 16Dec2024: First published version.

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
def errorCheck(image, layer, okayToExport, layerList):
    # Make sure it's already okay to export
    if okayToExport == True:
        # No errors were found so far
        # Check if the image is too small
        if image.width >= 64:
            # Image is not too small, can proceed
            # Initialize a variable to keep track of the number of correctly named layers
            goodLayers = 0
            # List the layers to check
            for layerName in layerList:
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
            if not(goodLayers == len(layerList)):
                # Layers with all names are not present
                # Don't allow the user to proceed
                okayToExport = False
        else:
            # Image is too small
            # Give error message
            pdb.gimp_message("ERROR: The image dimensions are too small. The image should be at least 64x64, or else it will not be clear.")
            # Update the status
            okayToExport = False
    # Return whether or not the script can proceed, as well as the width and height
    return okayToExport

# Define the function for exporting a standard portrait
def exportStandardPortrait(xcfPath, image, layer, console, alchemyVersion, template, prefix, **kwargs):
    # Determine if the suffix is needed
    if "_conversation" in xcfPath:
        suffix = ""
    else:
        suffix = "_conversation"
    # Determine the list of layers that need to be removed
    if template == "Combo":
        layersForRemoval = ["XML1 CSP Frame", "XML1 CSP Background", "XML2 CSP Background"]
    else:
        layersForRemoval = []
    # Determine the size
    if image.height == 64:
        # Console resolution
        # Determine the Alchemy version
        if alchemyVersion == 0:
            # Alchemy 2.5
            # Determine the console
            if console == 1:
                # PC only
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder="PC", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
                MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 Steam", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
            else:
                # All consoles
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder="Main", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
                MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="Wii", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
                MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 PS3 and Steam", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
        else:
            # Alchemy 5
            # Determine the console
            if console == 1:
                # PC Only
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", subFolder="MUA1 PC and Steam", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
            else:
                # All consoles
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", subFolder="All", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
    elif image.height == 128:
        # Standard resolution
        # Determine the Alchemy version
        if alchemyVersion == 0:
            # Alchemy 2.5
            # Determine the console
            if console == 1:
                # PC only
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder="PC", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
                MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 Steam", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
            else:
                # All consoles
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder="Main except PSP", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
                MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="Wii", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
                MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 PS3 and Steam", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, scale_factor=0.5, subFolder="PSP", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
        else:
            # Alchemy 5
            # Determine the console
            if console == 1:
                # PC Only
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", subFolder="MUA1 PC and Steam", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
            else:
                # All consoles
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", subFolder="Main", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", scale_factor=0.5, subFolder="PSP", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
    else:
        # HD resolution
        # Determine the scale factors
        lastGenScaleFactor = 128 / float(image.width)
        pspScaleFactor = lastGenScaleFactor / 2
        # Determine the Alchemy version
        if alchemyVersion == 0:
            # Alchemy 2.5
            # XML2 PC is the same regardless of console choice
            MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="XML2 PC", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
            # Determine the console
            if console == 1:
                # PC Only
                MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 PC and Steam", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
            else:
                # All consoles
                MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 PC and Next-Gen", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
                MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", scale_factor=lastGenScaleFactor, subFolder="Wii", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, scale_factor=lastGenScaleFactor, subFolder="GC, PS2, and Xbox", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, scale_factor=pspScaleFactor, subFolder="PSP", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
        else:
            # Alchemy 5
            # Determine the console
            if console == 1:
                # PC Only
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", subFolder="MUA1 PC and Steam", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
            else:
                # All consoles
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", subFolder="Main", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", scale_factor=lastGenScaleFactor, subFolder="Wii and MUA2 PS2", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", scale_factor=pspScaleFactor, subFolder="PSP", fileNamePrefix=prefix, fileNameSuffix=suffix, layersToRemove=layersForRemoval, portraitOutline=kwargs.get("outlineChoice", None))

# Define the function for exporting a NG portrait
def exportNGPortrait(xcfPath, image, layer, console, alchemyVersion, template):
    # Determine if the suffix is needed
    if "_conversation" in xcfPath:
        suffix = ""
    else:
        suffix = "_conversation"
    # Determine the list of layers that need to be removed
    if template == "Combo":
        layersForRemoval = ["XML1 CSP Frame", "HUD Frame", "HUD Background", "XML1 CSP Background", "XML2 CSP Background"]
    else:
        layersForRemoval = ["Frame", "Background"]
    # Determine the size
    if image.height == 64:
        # Console resolution
        # Determine the Alchemy version
        if alchemyVersion == 0:
            # Alchemy 2.5
            # Determine the console
            if console == 1:
                # PC only
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="PC and MUA1 Steam", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval)
            else:
                # All consoles
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="All except GC, PS2, and PSP", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval)
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="GC, PS2, and PSP", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval, alphaIndexed=True)
        else:
            # Alchemy 5
            # Determine the console
            if console == 1:
                # PC only
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", transparent=True, subFolder="MUA1 PC and Steam", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval)
            else:
                # All consoles
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", transparent=True, subFolder="All", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval)
    elif image.height == 128:
        # Standard resolution
        # Determine the Alchemy version
        if alchemyVersion == 0:
            # Alchemy 2.5
            # Determine the console
            if console == 1:
                # PC only
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="PC and MUA1 Steam", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval)
            else:
                # All consoles
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="All except GC, PS2, and PSP", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval)
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="GC and PS2", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval, alphaIndexed=True)
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=0.5, subFolder="PSP", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval, alphaIndexed=True)
        else:
            # Alchemy 5
            # Determine the console
            if console == 1:
                # PC only
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", transparent=True, subFolder="MUA1 PC and Steam", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval)
            else:
                # All consoles
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", transparent=True, subFolder="All except PSP", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval)
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", transparent=True, scale_factor=0.5, subFolder="PSP", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval)
    else:
        # HD resolution
        # Determine the scale factors
        lastGenScaleFactor = 128 / float(image.width)
        pspScaleFactor = lastGenScaleFactor / 2
        # Determine the Alchemy version
        if alchemyVersion == 0:
            # Alchemy 2.5
            # Determine the console
            if console == 1:
                # PC Only
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="PC and MUA1 Steam", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval)
            else:
                # All consoles
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="PC and MUA1 Next-Gen", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval)
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=lastGenScaleFactor, subFolder="Wii and Xbox", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval)
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=lastGenScaleFactor, subFolder="GC and PS2", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval, alphaIndexed=True)
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=pspScaleFactor, subFolder="PSP", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval, alphaIndexed=True)
        else:
            # Alchemy 5
            # Determine the console
            if console == 1:
                # PC only
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="MUA1 PC and Steam", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval)
            else:
                # All consoles
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", transparent=True, subFolder="MUA1 PC and Next-Gen", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval)
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", transparent=True, scale_factor=lastGenScaleFactor, subFolder="PS2 and Wii", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval)
                MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", transparent=True, scale_factor=pspScaleFactor, subFolder="PSP", fileNamePrefix="ng_", fileNameSuffix=suffix, layersToRemove=layersForRemoval)

# Define the function for exporting an XML1 CSP
def exportXML1CSP(xcfPath, image, layer, console, alchemyVersion, template):
    # Determine the list of layers that need to be removed
    if template == "Combo":
        layersForRemoval = ["HUD Frame", "HUD Background", "XML2 CSP Background"]
    else:
        layersForRemoval = ["XML2 Background"]
    # Determine if the Alchemy version is correct
    if alchemyVersion == 0:
        # Alchemy 2.5
        # Determine if the console is correct
        if console == 0:
            # All consoles
            # Determine the size
            if image.width > 128:
                # Oversized
                # Determine the scaleFactor
                scaleFactor = 128 / float(image.width)
            else:
                # Not oversized
                # No scaleFactor is needed
                scaleFactor = 1
            # Export the portrait
            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, scale_factor=scaleFactor, subFolder="All", fileNamePrefix="x1c_", layersToRemove=layersForRemoval, portraitOutline="XML1CSP")

# Define the function for exporting an XML2 CSP
def exportXML2CSP(xcfPath, image, layer, console, alchemyVersion, template):
    # Determine the list of layers that need to be removed
    if template == "Combo":
        layersForRemoval = ["XML1 CSP Frame", "HUD Frame", "HUD Background", "XML1 CSP Background"]
    else:
        layersForRemoval = ["Frame", "XML1 Background"]
    # Determine the alchemy version
    if alchemyVersion == 0:
        # Alchemy 2.5
        # Determine the size
        if image.width == 64:
            # Console resolution
            # Determine the console
            if console == 1:
                # PC only
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder="PC", fileNamePrefix="x2c_", layersToRemove=layersForRemoval)
            else:
                # All consoles
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder="All", fileNamePrefix="x2c_", layersToRemove=layersForRemoval)
        elif image.width == 128:
            # Standard resolution
            # Determine the console
            if console == 1:
                # PC only
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder="PC", fileNamePrefix="x2c_", layersToRemove=layersForRemoval)
            else:
                # All consoles
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder="All except PSP", fileNamePrefix="x2c_", layersToRemove=layersForRemoval)
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=0.5, indexColors=256, subFolder="PSP", fileNamePrefix="x2c_", layersToRemove=layersForRemoval)
        else:
            # HD resolution
            # Determine the console
            if console == 1:
                MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="PC", fileNamePrefix="x2c_", layersToRemove=layersForRemoval)
            else:
                # All consoles
                # Determine the scale factors
                lastGenScaleFactor = 128 / float(image.width)
                pspScaleFactor = lastGenScaleFactor / 2
                # Export the images
                MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="PC", fileNamePrefix="x2c_", layersToRemove=layersForRemoval)
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=lastGenScaleFactor, indexColors=256, subFolder="GC, PS2, and Xbox", fileNamePrefix="x2c_", layersToRemove=layersForRemoval)
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=pspScaleFactor, indexColors=256, subFolder="PSP", fileNamePrefix="x2c_", layersToRemove=layersForRemoval)
    else:
        # Alchemy 5
        # Determine the scaleFactor
        scaleFactor = 64 / float(image.width)
        # Export for PSP
        MMBGP.exportTextureMM(image, layer, xcfPath, ".tga", scale_factor=scaleFactor, subFolder="PSP", fileNamePrefix="x2c_", layersToRemove=layersForRemoval)

# Define the main operation
def exportPortraits(image, layer, console, alchemyVersion, plainChoice, nextGenChoice, heroOutlineChoice, redVillainOutlineChoice, greenVillainOutlineChoice, xml1Choice, xml2Choice, template):
    # Get the list of layers based on the template
    templateLayerListDict = {
        "Combo": ["XML1 CSP Frame", "HUD Frame", "Character", "HUD Background", "XML1 CSP Background", "XML2 CSP Background"],
        "CSP": ["Frame", "Character", "XML1 Background", "XML2 Background"],
        "HUD": ["Frame", "Character", "Background"]
    }
    layerList = templateLayerListDict[template]
    # Perform the initial operations
    (okayToExport, xcfPath) = MMBGP.initialOps(image, layer, checkSquare=True)
    okayToExport = errorCheck(image, layer, okayToExport, layerList)
    # Determine if it's okay to proceed
    if okayToExport == True:
        # There are no issues with the image
        # Go through the different exports
        if plainChoice == 1:
            exportStandardPortrait(xcfPath, image, layer, console, alchemyVersion, template, "")
        if heroOutlineChoice == 1:
            exportStandardPortrait(xcfPath, image, layer, console, alchemyVersion, template, "b_", outlineChoice="HUDBlue")
        if greenVillainOutlineChoice == 1:
            exportStandardPortrait(xcfPath, image, layer, console, alchemyVersion, template, "g_", outlineChoice="HUDGreen")
        if redVillainOutlineChoice == 1:
            exportStandardPortrait(xcfPath, image, layer, console, alchemyVersion, template, "r_", outlineChoice="HUDRed")
        if nextGenChoice == 1:
            exportNGPortrait(xcfPath, image, layer, console, alchemyVersion, template)
        if xml1Choice == 1:
            exportXML1CSP(xcfPath, image, layer, console, alchemyVersion, template)
        if xml2Choice == 1:
            exportXML2CSP(xcfPath, image, layer, console, alchemyVersion, template)
        # Print the success message
        pdb.gimp_message("SUCCESS: exported " + xcfPath)