#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to give default values to the script that exports textures for a character select portrait (CSP) and conversation portrait (HUD)
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2025
#
#   History:
#   v1.0: 21Jan2024: First published version.
#   v2.0: 20Dec2024: Updated to use an external module to increase speed
#   v3.0: 15Aug2025: Reduced options, as all texture format conversion and resizing can now be done through ALchemy.

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
def ExportCSPandHUD(image, layer):
    mmet.ExportPortraits(image, layer, 0, 0, 1, 1, 0, 0, 1, 1, 'Combo')


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    'python_fu_marvelmods_export_quick_cspandhud',
    'Exports a character select portrait (CSP) texture\nand a conversation portrait (HUD) texture\nin multiple formats.\nThis is an optimized version that runs without\noptions and with my preferred settings.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.',
    'Exports a character select portrait (CSP) texture\nand a conversation portrait (HUD) texture\nin multiple formats.',
    'BaconWizard17',
    'BaconWizard17',
    'August 2025',
    'Export Multiple Portraits (CSP and HUD)',
    '*',
    [
        (PF_IMAGE, 'image', 'Input image', None),
        (PF_DRAWABLE, 'layer', 'Layer, mask or channel', None)
    ],
    [],
    ExportCSPandHUD,
    menu='<Image>/Marvel Mods/Export Textures/Quick Exporters'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()