#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a skin, 3D head, or mannequin texture.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 30Jan2023: First published version.
#   v1.1: 30Aug2023: Add support for transparency, add support for next-gen MUA1 (Steam, PS3, and Xbox 360), and add support for MUA2 PS2. Improve efficiency
#   v1.2: 06Sep2023: Now checks if image dimensions are a power of 2 and gives an error if not.
#   v2.0: 10Jan2024: Simplified to call the main script but with pre-selected parameters
#   v2.1: 01Mar2024: Focused purely on primary textures to simplify the code
#   v3.0: 20Dec2024: Updated to use an external module to increase speed

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
def exportSkin(image, layer):
    # Define the remaining properties
    console = 0
    skinType = 0
    charSize = 0
    alchemyVersion = 0
    transparency = 1
    pspFormat = 1
    # Call the main script
    MMET.exportSkin(image, layer, console, skinType, charSize, alchemyVersion, transparency, pspFormat, True)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_quick_skin",
    "Exports a skin texture in multiple formats. Also\nworks on 3D head textures and mannequin textures.\nThis is an optimized version that runs without\noptions and with my preferred settings.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports a skin texture in multiple formats. Also works on 3D head textures and mannequin textures.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2024",
    "Export Skin, Mannequin, or 3D Head (Primary Texture)",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask, or channel", None)
    ],
    [],
    exportSkin,
    menu="<Image>/Marvel Mods/Export Textures/Quick Exporters"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()