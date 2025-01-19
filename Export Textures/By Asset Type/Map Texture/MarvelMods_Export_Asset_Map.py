#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a map textures
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 18Jan2025: First published version.

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
def exportMap(image, layer, console, alchemyVersion, transparency, nextGenSize):
    # Perform the initial operations
    (okayToExport, xcfPath) = MMBGP.initialOps(image, layer)
    # Determine if it's okay to proceed
    if okayToExport == True:
        # No errors, can proceed
        # Determine the console
        if console == 0:
            # All consoles
            # Determine the Alchemy version
            if alchemyVersion == 0:
                # Alchemy 2.5
                #  Determine the transparency
                if transparency == 0:
                    # Transparent
                    # Determine the next-gen size
                    if nextGenSize == 0:
                        # Double size
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="MUA1 PC, Steam, PS3, and 360")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=0.5, subFolder="Wii, Xbox, and XML2 PC")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=0.25, subFolder="GameCube", alphaIndexed=True)
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=0.25, subFolder="PS2", alphaIndexed=True)
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=0.25, subFolder="PSP", alphaIndexed=True, alphaIndexColors=16)
                    else:
                        # Same Size
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="MUA1 PC, Steam, PS3, and 360")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="Wii, Xbox, and XML2 PC")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=0.5, subFolder="GameCube", alphaIndexed=True)
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=0.5, subFolder="PS2", alphaIndexed=True)
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=0.5, subFolder="PSP", alphaIndexed=True, alphaIndexColors=16)
                else:
                    # Not transparent
                    # Determine the next-gen size
                    if nextGenSize == 0:
                        # Double size
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 PC, Steam, PS3, and 360")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", scale_factor=0.5, subFolder="Wii, Xbox, and XML2 PC")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", scale_factor=0.25, subFolder="GameCube")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, scale_factor=0.25, subFolder="PS2")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=16, scale_factor=0.25, subFolder="PSP")
                    else:
                        # Same size
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 PC, Steam, PS3, and 360")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="Wii, Xbox, and XML2 PC")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", scale_factor=0.5, subFolder="GameCube")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, scale_factor=0.5, subFolder="PS2")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=16, scale_factor=0.5, subFolder="PSP")
            else:
                # Alchemy 5
                # Determine the transparency
                if transparency == 0:
                    # Transparent
                    # Determine the next-gen size
                    if nextGenSize == 0:
                        # Double size
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", transparent=True, subFolder="MUA1 PC, Steam, PS3, and 360", ddsCompression="DXT5")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=0.5, subFolder="Wii")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=0.25, subFolder="MUA2 PS2", alphaIndexed=True)
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=0.25, subFolder="PSP", alphaIndexed=True, alphaIndexColors=16)
                    else:
                        # Same size
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", transparent=True, subFolder="MUA1 PC, Steam, PS3, and 360", ddsCompression="DXT5")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="Wii")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=0.5, subFolder="MUA2 PS2", alphaIndexed=True)
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=0.5, subFolder="PSP", alphaIndexed=True, alphaIndexColors=16)
                        
                else:
                    # Not transparent
                    # Determine the next-gen size
                    if nextGenSize == 0:
                        # Double size
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="MUA1 PC, Steam, PS3, and 360")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", scale_factor=0.5, subFolder="Wii")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, scale_factor=0.25, subFolder="MUA2 PS2")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=16, scale_factor=0.25, subFolder="PSP")
                    else:
                        # Same size
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="MUA1 PC, Steam, PS3, and 360")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="Wii")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, scale_factor=0.5, subFolder="MUA2 PS2")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=16, scale_factor=0.5, subFolder="PSP")
        else:
            # PC Only
            # Determine the Alchemy version
            if alchemyVersion == 0:
                # Alchemy 2.5
                # Determine the transparency
                if transparency == 0:
                    # Transparent
                    # Determine the next-gen size
                    if nextGenSize == 0:
                        # Double size
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="MUA1 PC and Steam")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=0.5, subFolder="XML2 PC")
                    else:
                        # Same size
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="MUA1 PC and Steam")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="XML2 PC")
                else:
                    # Not transparent
                    # Determine the next-gen size
                    if nextGenSize == 0:
                        # Double size
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 PC and Steam")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", scale_factor=0.5, subFolder="XML2 PC")
                    else:
                        # Same size
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 PC and Steam")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="XML2 PC")
            else:
                # Alchemy 5
                # Determine the transparency
                if transparency == 0:
                    # Transparent
                    MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", transparent=True, subFolder="MUA1 PC and Steam", ddsCompression="DXT5")
                else:
                    # Not transparent
                    MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="MUA1 PC and Steam")
        # Print the success message
        pdb.gimp_message("SUCCESS: exported " + xcfPath)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_asset_map",
    "Exports a map texture in multiple formats.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports a map texture in multiple formats.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2025",
    "Export Map Texture",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask or channel", None),
        (PF_OPTION, "console", "Console:", 0, ["All", "PC Only"]),
        (PF_OPTION, "alchemyVersion", "Alchemy Version:", 0, ["Alchemy 2.5", "Alchemy 5"]),
        (PF_OPTION, "transparency", "Requires Transparency:", 1, ["Yes", "No"]),
        (PF_OPTION, "nextGenSize", "Next-Gen Size:", 1, ["Double", "Same as Wii, Xbox, and XML2 PC"])
    ],
    [],
    exportMap,
    menu="<Image>/Marvel Mods/Export Textures/By Asset Type"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()