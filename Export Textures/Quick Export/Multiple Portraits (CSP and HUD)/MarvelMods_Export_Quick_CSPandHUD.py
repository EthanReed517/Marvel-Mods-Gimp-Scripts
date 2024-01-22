#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to give default values to the script that exports textures for a character select portrait (CSP) and conversation portrait (HUD)
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 21Jan2024: First published version.

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
def exportCSPandHUD(image, layer):
    # Define the remaining properties
    console = 0
    alchemyVersion = 0
    plainChoice = 0
    nextGenChoice = 1
    heroOutlineChoice = 1
    redVillainOutlineChoice = 0
    greenVillainOutlineChoice = 0
    xml1Choice = 0
    xml2Choice = 1
    # Call the main script
    pdb.python_fu_marvelmods_export_asset_cspandhud(image, layer, console, alchemyVersion, plainChoice, nextGenChoice, heroOutlineChoice, redVillainOutlineChoice, greenVillainOutlineChoice, xml1Choice, xml2Choice)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_quick_cspandhud",
    "Exports a character select portrait (CSP) texture\nand a conversation portrait (HUD) texture\nin multiple formats.\nThis is an optimized version that runs without\noptions and with my preferred settings.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports a character select portrait (CSP) texture\nand a conversation portrait (HUD) texture\nin multiple formats.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2024",
    "Export Multiple Portraits (CSP and HUD)",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask, or channel", None)
    ],
    [],
    exportCSPandHUD,
    menu="<Image>/Marvel Mods/Export Textures/Quick Exporters"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()