#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export power icons
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 01Feb2023: First published version.
#   v2.0: 12Dec2024: Full redesign for improved performance using an external module for common operations.

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
# Define the main operation
def exportIcons(image, layer, console, game):
    # Perform the initial operations
    (okayToExport, xcfPath) = MMBGP.initialOps(image, layer, checkSquare=True)
    # Verify that it's okay to export
    if okayToExport == True:
        # It's okay to export
        # Export a plain png copy as a preview
        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="Preview")
        # Pick the console
        if game == 0:
            # XML1
            # Determine if the image is oversized (only check width because it was confirmed to be square)
            if image.width > 128:
                # The image is oversized, so set the scaleFactor
                scaleFactor = 128 / float(image.width)
            else:
                # No scaling is needed
                scaleFactor = 1
            # Export the image
            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=scaleFactor, indexColors=256, subFolder="XML1 All")
        elif game == 1:
            # XML2
            # Determine if an icons2 file is needed
            if image.width > 128:
                icons2 = True
            else:
                icons2 = False
            # Decide what icons are needed
            if icons2 == True:
                # Export icons2
                # Pick the console
                if console == 1:
                    # PC Only
                    # Determine if the icons are high-res
                    if image.width > 256:
                        # 512x512 icons, export the PC as a dds
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", fileNameSuffix="2", subFolder="XML2 PC")
                    else:
                        # 256x256 icons, export as PNG8
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, fileNameSuffix="2", subFolder="XML2 PC")
                    # Get the scale factor for the icons1 file
                    scaleFactor = 128 / float(image.width)
                    # Export the image
                    MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, fileNameSuffix="1", subFolder="XML2 PC")
                else:
                    # All consoles
                    # Determine if PC needs high res icons
                    if image.width > 256:
                        # 512x512 icons, export the PC as a dds
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", fileNameSuffix="2", subFolder="XML2 PC")
                        # Get the scale factor for 256x256
                        scaleFactor = 256 / float(image.width)
                        # Export the console textures
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=scaleFactor, indexColors=256, fileNameSuffix="2", subFolder="XML2 Xbox")
                    else:
                        # 256x256 icons, export the PC with Xbox
                        # Export the image
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, fileNameSuffix="2", subFolder="XML2 PC and Xbox")
                    # Get the scale factor for 128x128
                    scaleFactor = 128 / float(image.width)
                    # Export the image
                    MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=scaleFactor, indexColors=256, fileNameSuffix="1", subFolder="XML2 All")
            else: 
                # Do not export icons2
                # Determine the console
                if console == 1:
                    # PC only
                    # Export the image
                    MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, fileNameSuffix="1", subFolder="XML2 PC")
                else:
                    # All consoles
                    # Export the image
                    MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, fileNameSuffix="1", subFolder="XML2 All")
        elif game == 2:
            # MUA1
            # Determine if the image is oversized
            if image.width > 256:
                scaleFactor = 256 / float(image.width)
            else:
                scaleFactor = 1
            # Determine the console
            if console == 0:
                # All
                # Export the image
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=scaleFactor, transparent=True, subFolder="MUA1 PC, Steam, PS3, and 360")
                # Get the scale factor for 128x128
                scaleFactor = 128 / float(image.width)
                # Export the last-gen textures
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=scaleFactor, transparent=True, subFolder="MUA1 Wii and Xbox")
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=scaleFactor, transparent=True, subFolder="MUA1 PS2 and PSP", alphaIndexed=True)
            else:
                # PC only
                # Export the image
                MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=scaleFactor, transparent=True, subFolder="MUA1 PC and Steam")   
        else:
            # MUA2
            # Determine if the image is oversized
            if image.width > 128:
                scaleFactor = 128 / float(image.width)
            else:
                scaleFactor = 1
            # Export the image
            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=scaleFactor, transparent=True, subFolder="MUA2 Wii")
            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=scaleFactor, transparent=True, subFolder="MUA2 PS2 and PSP", alphaIndexed=True)
        # Print the success message
        pdb.gimp_message("SUCCESS: exported " + xcfPath)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_asset_icons",
    "Exports a power icons texture in multiple formats.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports a power icons texture in multiple formats.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2024",
    "Export Power Icons",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask or channel", None),
        (PF_OPTION, "console", "Console:", 0, ["All", "PC Only"]),
        (PF_OPTION, "game", "Game:", 0, ["XML1", "XML2", "MUA1", "MUA2"])
    ],
    [],
    exportIcons,
    menu="<Image>/Marvel Mods/Export Textures/By Asset Type"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()