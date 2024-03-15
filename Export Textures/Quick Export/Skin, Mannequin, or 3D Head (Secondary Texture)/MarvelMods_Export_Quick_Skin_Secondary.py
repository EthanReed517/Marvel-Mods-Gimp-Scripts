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
#   v1.0: 01Mar2024: First published version.

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
# To be able to execute GIMP scripts
from gimpfu import*


# ######### #
# FUNCTIONS #
# ######### #
# Define the main operation
def exportSkinSecondary(image, layer):
    # Define the remaining properties
    primarySize = 0
    console = 0
    skinType = 0
    charSize = 0
    alchemyVersion = 0
    transparency = 1
    PSPFormat = 1
    # Call the main script
    pdb.python_fu_marvelmods_export_asset_skin_secondary(image, layer, primarySize, console, skinType, charSize, alchemyVersion, transparency, PSPFormat)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_quick_skin_secondary",
    "Exports a skin texture in multiple formats. Also\nworks on 3D head textures and mannequin textures.\nThis is an optimized version that runs without\noptions and with my preferred settings.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports a skin texture in multiple formats. Also works on 3D head textures and mannequin textures.",
    "BaconWizard17",
    "BaconWizard17",
    "March 2024",
    "Export Skin, Mannequin, or 3D Head (Secondary Texture)",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask, or channel", None)
    ],
    [],
    exportSkinSecondary,
    menu="<Image>/Marvel Mods/Export Textures/Quick Exporters"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()