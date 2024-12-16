#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP to plugin crop a skin preview for the PC version of X-Men Legends II: Rise of Apocalypse.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 14Dec2024: First published version.

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
import Marvel_Mods_Export_Previews as MMEP
# External modules
import os.path


# ######## #
# FUNCTION #
# ######## #
# Define the main operation
def fullPreview(image, layer):
    MMEP.fullPreview(image, layer, "MUA")


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_preview_mua1_all",
    "Exports layers to create a skin preview.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports layers to create a skin preview.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2024",
    "Create All Previews",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask or channel", None)
    ],
    [],
    fullPreview,
    menu="<Image>/Marvel Mods/Skin Previews/Crop Screenshots - MUA1"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()