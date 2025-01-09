#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a loading screen or concept art texture
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


# ######### #
# FUNCTIONS #
# ######### #
# Define the function for exporting a personal preview
def exportPersonalPreview(image, layer, xcfPath, desc, width, personalPreview):
    # Determine if the preview is needed
    if personalPreview == True:
        # A personal preview is needed
        # Create a duplicate of the image
        smallImage = pdb.gimp_image_duplicate(image)
        # Get the active layer of the image
        smallLayer = pdb.gimp_image_get_active_layer(smallImage)
        # Scale the image accordingly
        pdb.gimp_image_scale(smallImage, width, 282)
        # Start the new image
        newImage = pdb.gimp_image_new(502, 282, 0)
        # Create a new layer for this image
        newLayer = pdb.gimp_layer_new(newImage, 502, 282, 1, "New Layer", 100, 28)
        # Get the active layer of the image
        activeLayer = pdb.gimp_image_get_active_layer(newImage)
        # Apply the new layer to the active layer
        pdb.gimp_image_insert_layer(newImage, newLayer, activeLayer, 0)
        # Get the new active layer
        newLayer = pdb.gimp_image_get_active_layer(newImage)
        # Copy the asset layer and paste it in the new image
        pdb.gimp_edit_copy(smallLayer)
        floatingLayer = pdb.gimp_edit_paste(newLayer, False)
        # Determine the offsets
        xOffset, yOffset = floatingLayer.offsets
        xOffset = ((502 - width) / 2) - xOffset
        yOffset = 30 - yOffset
        pdb.gimp_layer_translate(floatingLayer, xOffset, yOffset)
        # Anchor the layer
        pdb.gimp_floating_sel_anchor(floatingLayer)
        # Get the new active layer
        newLayer = pdb.gimp_image_get_active_layer(newImage)
        # Set the foreground fill color
        pdb.gimp_context_set_foreground((255, 255, 255))
        # Set up the dicitonary of X positions
        xPosDict = {
            "XML1/XML2 (not PSP)": 14,
            "XML2 PSP/MUA1/MUA2": 6
        }
        # Create the text
        text_layer = pdb.gimp_text_fontname(newImage, newLayer, xPosDict[desc], 0, desc, 0, True, 31, 1, "Gunship")
        # Merge the layer
        pdb.gimp_floating_sel_anchor(text_layer)
        # Set up the suffixes
        suffixDict = {
            "XML1/XML2 (not PSP)": "4-3",
            "XML2 PSP/MUA1/MUA2": "16-9"
        }
        # Export the preview
        MMBGP.exportTextureMM(newImage, newLayer, xcfPath, ".png", transparent=True, subFolder="!Preview", fileNamePrefix="0Personal_", fileNameSuffix=" (" + suffixDict[desc] + ")")

# Define the function for exporting an XML2 PSP loading screen
def exportXML2PSPLoad(image, layer, xcfPath, alchemyVersion):
    # Create a duplicate image of the loading screen and get its active layer
    pspImage = pdb.gimp_image_duplicate(image)
    pspLayer = pdb.gimp_image_get_active_layer(pspImage)
    # Flatten the image
    pspLayer = pdb.gimp_image_flatten(pspImage)
    # Scale the image
    pdb.gimp_image_scale(pspImage, 480, 271)
    # Resize the layer to the image size
    pdb.gimp_layer_resize_to_image_size(pspLayer)
    # Create a plain black image
    blackImage = pdb.gimp_image_new(512, 512, 0)
    # Create a layer for the plain black image
    blackLayer = pdb.gimp_layer_new(blackImage, 512, 512, 0, "Background", 100, 28)
    # Get the current layer of the white image
    blackLayer2 = pdb.gimp_image_get_active_layer(blackImage)
    # Apply the layer to the image
    pdb.gimp_image_insert_layer(blackImage, blackLayer, blackLayer2, 0)
    # Set the background fill color
    pdb.gimp_context_set_background((0, 0, 0))
    # Fill the layer with the background color
    pdb.gimp_drawable_fill(blackLayer, 1)
    # Copy the PSP image's layer and paste it in the new image
    pdb.gimp_edit_copy(pspLayer)
    floatingLayer = pdb.gimp_edit_paste(blackLayer, False)
    # Determine the offsets
    xOffset, yOffset = floatingLayer.offsets
    xOffset = 0 - xOffset
    yOffset = 0 - yOffset
    pdb.gimp_layer_translate(floatingLayer, xOffset, yOffset)
    # Anchor the layer
    pdb.gimp_floating_sel_anchor(floatingLayer)
    # Determine the Alchemy version
    if alchemyVersion == 0:
        # Alchemy 2.5
        # Export for XML2 PSP
        MMBGP.exportTextureMM(blackImage, blackLayer, xcfPath, ".png", indexColors=256, subFolder="XML2 PSP")
    else:
        # Alchemy 5
        # Export for XML2 PSP
        MMBGP.exportTextureMM(blackImage, blackLayer, xcfPath, ".tga", subFolder="XML2 PSP")

# Define the function for exporting the 16:9 loading screen
def export16_9Loading(image, layer, console, alchemyVersion, xcfPath, type, personalPreview):
    # Export a plain png copy as a preview
    MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="!Preview", fileNameSuffix=" (16-9)")
    # Export the personal preview
    exportPersonalPreview(image, layer, xcfPath, "XML2 PSP/MUA1/MUA2", 502, personalPreview)
    # Create a duplicate for the next-gen image
    nextGenImage = pdb.gimp_image_duplicate(image)
    nextGenLayer = pdb.gimp_image_get_active_layer(nextGenImage)
    # Scale the next-gen image
    pdb.gimp_image_scale(nextGenImage, nextGenImage.height * 2, nextGenImage.height)
    # Determine the alchemy version 
    if alchemyVersion == 0:
        # Alchemy 2.5
        # Determine the console
        if console == 0:
            # All consoles
            # Determine the size
            if image.height == 2048:
                # This is the largest size 
                # Export for PC and Steam
                MMBGP.exportTextureMM(nextGenImage, nextGenLayer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 PC and Steam")
                # Export for 360 and PS3
                MMBGP.exportTextureMM(nextGenImage, nextGenLayer, xcfPath, ".dds", scale_factor=0.5, RGB_BGR=True, subFolder="MUA1 PS3 and 360")
            else:
                # This is medium or small size
                # Export for MUA1 next-gen
                MMBGP.exportTextureMM(nextGenImage, nextGenLayer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 Next-Gen")
        else:
            # This is for PC only
            # Export for MUA1 PC and Steam
            MMBGP.exportTextureMM(nextGenImage, nextGenLayer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 PC and Steam")
    else:
        # This is for Alchemy 5
        # Determine the console
        if console == 0:
            # All consoles
            # Determine the size
            if image.height == 2048:
                # This is the largest size
                # Export for PC and Steam
                MMBGP.exportTextureMM(nextGenImage, nextGenLayer, xcfPath, ".tga", subFolder="MUA1 PC and Steam")
                # Export for PS3 and 360
                MMBGP.exportTextureMM(nextGenImage, nextGenLayer, xcfPath, ".tga", scale_factor=0.5, subFolder="MUA1 PS3 and 360")
            else:
                # This is medium or small size
                # Export for MUA1 next-gen
                MMBGP.exportTextureMM(nextGenImage, nextGenLayer, xcfPath, ".tga", subFolder="MUA1 Next-Gen")
        else:
            # This is for PC only
            # Export for MUA1 PC and Steam
            MMBGP.exportTextureMM(nextGenImage, nextGenLayer, xcfPath, ".tga", subFolder="MUA1 PC and Steam")
    # Create a duplicate for the last-gen image
    lastGenImage = pdb.gimp_image_duplicate(image)
    lastGenLayer = pdb.gimp_image_get_active_layer(lastGenImage)
    # Determine the console
    if ((console == 0) and (type == "loading")):
        # All consoles
        # Export for XML2 PSP
        exportXML2PSPLoad(image, layer, xcfPath, alchemyVersion)
    # Scale the last-gen image
    pdb.gimp_image_scale(lastGenImage, lastGenImage.height, lastGenImage.height)
    # Determine the alchemy version 
    if alchemyVersion == 0:
        # Alchemy 2.5
        # Determine the console
        if console == 0:
            # All consoles
            # Determine the type
            if type == "concept":
                # This is a piece of concept art
                # Export for PS2 and PSP
                MMBGP.exportTextureMM(lastGenImage, lastGenLayer, xcfPath, ".png", indexColors=256, scale_factor=(512/float(image.height)), subFolder="XML2 and MUA1 PSP, MUA1 PS2")
            else:
                # This is a loading screen
                # Export for PS2 and PSP
                MMBGP.exportTextureMM(lastGenImage, lastGenLayer, xcfPath, ".png", indexColors=256, scale_factor=(512/float(image.height)), subFolder="MUA1 and MUA2 PS2 and PSP")
            # Determine the size
            if image.height == 512:
                # This is the smallest size
                # Determine the type
                if type == "loading":
                    # THis is a loading screen
                    # Export for Xbox and Wii
                    MMBGP.exportTextureMM(lastGenImage, lastGenLayer, xcfPath, ".dds", subFolder="MUA1 Wii and Xbox, MUA2 Wii")
                else:
                    # This is a piece of concept art
                    # Export for Xbox and Wii
                    MMBGP.exportTextureMM(lastGenImage, lastGenLayer, xcfPath, ".dds", subFolder="MUA1 Wii and Xbox")
            else:
                # This is a larger size
                # Determine the type
                if type == "loading":
                    # THis is a loading screen
                    # Export for Xbox and Wii
                    MMBGP.exportTextureMM(lastGenImage, lastGenLayer, xcfPath, ".dds", scale_factor=(1024/float(image.height)), subFolder="MUA1 Wii and Xbox, MUA2 Wii")
                else:
                    # This is a piece of concept art
                    # Export for Xbox and Wii
                    # Export for Xbox and Wii
                    MMBGP.exportTextureMM(lastGenImage, lastGenLayer, xcfPath, ".dds", scale_factor=(1024/float(image.height)), subFolder="MUA1 Wii and Xbox")
    else:
        # Alchemy 5
        # Determine the console
        if console == 0:
            # All consoles
            # Determine the type
            if type == "concept":
                # This is a piece of concept art
                # Export for PS2 and PSP
                MMBGP.exportTextureMM(lastGenImage, lastGenLayer, xcfPath, ".tga", scale_factor=(512/float(image.height)), subFolder="XML2 and MUA1 PSP")
            else:
                # This is a loading screen
                # Export for PS2 and PSP
                MMBGP.exportTextureMM(lastGenImage, lastGenLayer, xcfPath, ".tga", scale_factor=(512/float(image.height)), subFolder="MUA1 PSP, MUA2 PSP and PS2")
            # Determine the size
            if image.height == 512:
                # This is the smallest size
                # Determine the type
                if type == "loading":
                    # This is a loading screen
                    # Export for Wii
                    MMBGP.exportTextureMM(lastGenImage, lastGenLayer, xcfPath, ".tga", subFolder="MUA1 Wii and MUA2 Wii")
                else:
                    # This is a piece of concept art
                    # Export for Wii
                    MMBGP.exportTextureMM(lastGenImage, lastGenLayer, xcfPath, ".tga", subFolder="MUA1 Wii")
            else:
                # This is a larger size
                # Determine the type
                if type == "loading":
                    # This is a loading screen
                    # Export for Wii
                    MMBGP.exportTextureMM(lastGenImage, lastGenLayer, xcfPath, ".tga", scale_factor=(1024/float(image.height)), subFolder="MUA1 Wii and MUA2 Wii")
                else:
                    # This is a piece of concept art
                    # Export for Wii
                    MMBGP.exportTextureMM(lastGenImage, lastGenLayer, xcfPath, ".tga", scale_factor=(1024/float(image.height)), subFolder="MUA1 Wii")

# Define the function for cropping the 16:9 screen to 4:3 and exporting
def crop16_9to4_3AndExport(image, layer, console, alchemyVersion, xcfPath, guidePosition, personalPreview):
    # Create a duplicate for the export image
    exportImage = pdb.gimp_image_duplicate(image)
    exportLayer = pdb.gimp_image_get_active_layer(exportImage)
    # Create the dictionary of appropriate widths
    widthsDict = {"512": 683, "1024": 1365, "2048": 2731}
    # Crop the image accordingly
    pdb.gimp_image_resize(exportImage, widthsDict[str(image.height)], image.height, (guidePosition * -1), 0)
    # Resize the layer to the image size
    pdb.gimp_layer_resize_to_image_size(exportLayer)
    # Export the image
    export4_3Loading(exportImage, exportLayer, console, alchemyVersion, xcfPath, personalPreview)

# Define the function for exporting a 4:3 loading screen
def export4_3Loading(image, layer, console, alchemyVersion, xcfPath, personalPreview):
    # Export a plain png copy as a preview
    MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="!Preview", fileNameSuffix=" (4-3)")
    # Export the personal preview
    exportPersonalPreview(image, layer, xcfPath, "XML1/XML2 (not PSP)", 376, personalPreview)
    # Create a duplicate for the export image
    exportImage = pdb.gimp_image_duplicate(image)
    exportLayer = pdb.gimp_image_get_active_layer(exportImage)
    # Scale the export image
    pdb.gimp_image_scale(exportImage, exportImage.height, exportImage.height)
    # Determine the alchemy version 
    if alchemyVersion == 0:
        # Alchemy 2.5
        # Determine the console
        if console == 0:
            # All consoles
            # Determine the size
            if image.height == 2048:
                # This is the largest size
                # Export for XML2 PC
                MMBGP.exportTextureMM(exportImage, exportLayer, xcfPath, ".dds", subFolder="XML2 PC")
                # Export for Xbox
                MMBGP.exportTextureMM(exportImage, exportLayer, xcfPath, ".dds", scale_factor=0.5, subFolder="XML1 and XML2 Xbox")
            else:
                # Export for PC and Xbox
                MMBGP.exportTextureMM(exportImage, exportLayer, xcfPath, ".dds", subFolder="XML1 Xbox, XML2 PC and Xbox")
            # Export for PS2
            MMBGP.exportTextureMM(exportImage, exportLayer, xcfPath, ".png", indexColors=256, scale_factor=(512/float(image.height)), subFolder="XML1 and XML2 PS2")
            # Export for GameCube
            MMBGP.exportTextureMM(exportImage, exportLayer, xcfPath, ".dds", scale_factor=(512/float(image.height)), subFolder="XML1 and XML2 GameCube")
        else:
            # PC only
            # Export for XML2 PC
            MMBGP.exportTextureMM(exportImage, exportLayer, xcfPath, ".dds", subFolder="XML2 PC")

# Define the main operation
def exportConceptLoading(image, layer, console, alchemyVersion, type, **kwargs):
    # Determine if personal previews are needed
    personalPreview = kwargs.get("personalPreview", False)
    # Perform the initial operations
    (okayToExport, xcfPath, aspectRatio, guidePosition) = MMBGP.initialOpsLoading(image, layer)
    # Determine if it's okay to export
    if okayToExport == True:
        # It's okay to export
        # Determine the aspect ratio
        if aspectRatio == "16:9":
            # This is a 16:9 loading screen
            # Export the loading screen
            export16_9Loading(image, layer, console, alchemyVersion, xcfPath, type, personalPreview)
            # Determine if a 4:3 loading screen is needed
            if guidePosition is not None:
                # There is a guide
                # Export a 4:3 loading screen
                crop16_9to4_3AndExport(image, layer, console, alchemyVersion, xcfPath, guidePosition, personalPreview)
        else:
            # This is a 4:3 loading screen
            # Export the loading screen
            export4_3Loading(image, layer, console, alchemyVersion, xcfPath, personalPreview)
        # Print the success message
        pdb.gimp_message("SUCCESS: exported " + xcfPath)