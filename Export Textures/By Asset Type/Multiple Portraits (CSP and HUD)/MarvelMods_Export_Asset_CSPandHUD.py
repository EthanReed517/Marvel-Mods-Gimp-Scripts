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
#   v1.0: 21Jan2024: First published version.   
#   v2.0: 16Dec2024: Full redesign for improved performance using an external module for common operations.

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
def exportCSPandHUD(image, layer, console, alchemyVersion, plainChoice, nextGenChoice, heroOutlineChoice, redVillainOutlineChoice, greenVillainOutlineChoice, xml1Choice, xml2Choice):
    MMET.exportPortraits(image, layer, console, alchemyVersion, plainChoice, nextGenChoice, heroOutlineChoice, redVillainOutlineChoice, greenVillainOutlineChoice, xml1Choice, xml2Choice, "Combo")


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_asset_cspandhud",
    "Exports a character select portrait (CSP) texture\nand a conversation portrait (HUD) texture\nin multiple formats.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.",
    "Exports a character select portrait (CSP) texture\nand a conversation portrait (HUD) texture\nin multiple formats.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2024",
    "Export Multiple Portraits (CSP and HUD)",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask or channel", None),
        (PF_OPTION, "console", "Console:", 0, ["All","PC Only"]),
        (PF_OPTION, "alchemyVersion", "Alchemy Version:", 0, ["Alchemy 2.5","Alchemy 5"]),
        (PF_TOGGLE, "plainChoice", "Export a plain HUD?", 0),
        (PF_TOGGLE, "nextGenChoice", "Export an MUA1 next-gen\nstyle HUD?", 1),
        (PF_TOGGLE, "heroOutlineChoice", "Export a HUD with a\nhero outline?", 1),
        (PF_TOGGLE, "redVillainOutlineChoice", "Export a HUD with a\nred villain outline?", 0),
        (PF_TOGGLE, "greenVillainOutlineChoice", "Export a HUD with a\ngreen villain outline?", 0),
        (PF_TOGGLE, "xml1Choice", "Export a CSP for XML1?", 0),
        (PF_TOGGLE, "xml2Choice", "Export a CSP for XML2?", 1)
    ],
    [],
    exportCSPandHUD,
    menu="<Image>/Marvel Mods/Export Textures/By Asset Type"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()