#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export advanced textures for next-gen skins and mannequins.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 25Jan2024: First published version.
#   v1.1: 01Mar2024: Streamline to focus only on primary textures
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
import Marvel_Mods_Export_Textures as MMET


# ######### #
# FUNCTIONS #
# ######### #
# Define the main operation
def exportSkinAdv(image, layer, textureType, console, alchemyVersion, normalColor):
    MMET.exportSkinAdv(image, layer, textureType, console, alchemyVersion, normalColor, True)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_asset_skinadv",
    "Exports advanced material textures for next-gen skins and mannequins in multiple formats.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports advanced material textures for next-gen skins and mannequins in multiple formats.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2024",
    "Export Advanced Textures for Next-Gen (Primary Texture)",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask or channel", None),
        (PF_OPTION, "textureType", "Advanced Texture Type:", 0, ["Normal Map", "Specular Map", "Gloss/Emissive Map", "Environment Mask"]),
        (PF_OPTION, "console", "Console:", 0, ["All", "PC Only"]),
        (PF_OPTION, "alchemyVersion", "Alchemy Version:", 1, ["Alchemy 2.5", "Alchemy 5"]),
        (PF_OPTION, "normalColor", "Steam/360 Normal Map Color:", 0, ["Yellow", "Blue"])
    ],
    [],
    exportSkinAdv,
    menu="<Image>/Marvel Mods/Export Textures/By Asset Type"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()