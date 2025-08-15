#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a conversation portrait (HUD)
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2025
#
#   History:
#   v1.0: 01Feb2023: First published version.
#   v1.1: 15Apr2023: Rewrote to accommodate for more portrait types and use the duplication function
#   v2.0: 15Jan2024: Full rewrite. Added more portrait types, changed basic operations to common procedures.
#   v2.1: 21Jan2024: Add support for Alchemy 5
#   v3.0: 16Dec2024: Full redesign for improved performance using an external module for common operations.
#   v4.0: 15Aug2025: Reduced options, as all texture format conversion and resizing can now be done through ALchemy.

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
# Internal modules
import marvel_mods_export_textures as mmet


# ######### #
# FUNCTIONS #
# ######### #
# This is the main operation.
def ExportHUD(image, layer, alchemy_version, plain_choice, next_gen_choice, hero_outline_choice, red_villain_outline_choice, green_villain_outline_choice):
    mmet.ExportPortraits(image, layer, alchemy_version, plain_choice, next_gen_choice, hero_outline_choice, red_villain_outline_choice, green_villain_outline_choice, 0, 0, 'HUD')


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    'python_fu_marvelmods_export_asset_hud',
    'Exports a conversation portrait (HUD) texture.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.',
    'Exports a conversation portrait (HUD) texture.',
    'BaconWizard17',
    'BaconWizard17',
    'August 2025',
    'Export Conversation Portrait (HUD)',
    '*',
    [
        (PF_IMAGE, 'image', 'Input image', None),
        (PF_DRAWABLE, 'layer', 'Layer, mask or channel', None),
        (PF_OPTION, 'alchemy_version', 'Alchemy Version:', 0, ['Alchemy 2.5', 'Alchemy 5', 'Alchemy 5 (Texture Replacement)']),
        (PF_TOGGLE, 'plain_choice', 'Export a plain portrait?', 0),
        (PF_TOGGLE, 'next_gen_choice', 'Export an MUA1 next-gen\nstyle portrait?', 1),
        (PF_TOGGLE, 'hero_outline_choice', 'Export a portrait with a\nhero outline?', 1),
        (PF_TOGGLE, 'red_villain_outline_choice', 'Export a portrait with a\nred villain outline?', 0),
        (PF_TOGGLE, 'green_villain_outline_choice', 'Export a portrait with a\ngreen villain outline?', 0)
    ],
    [],
    ExportHUD,
    menu='<Image>/Marvel Mods/Export Textures/By Asset Type'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()