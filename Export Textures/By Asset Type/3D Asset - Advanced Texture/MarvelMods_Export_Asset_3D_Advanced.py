#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export 3D asset's advanced textures.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2025
#
#   History:
#   v1.0: 25Jan2024: First published version.
#   v1.1: 01Mar2024: Streamline to focus only on primary textures
#   v2.0: 12Dec2024: Full redesign for improved performance using an external module for common operations.
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
def Export3DAdv(image, layer, texture_type, normal_color):
    mmet.Export3DAdv(image, layer, texture_type, normal_color)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP.
register(
    'python_fu_marvelmods_export_asset_3d_advanced',
    'Exports a 3D asset\'s advanced textures. Works with\nskins, mannequins, boltons, and other models.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.',
    'Exports a 3D asset\'s advanced texture. Works with skins, mannequins, boltons, and other models.',
    'BaconWizard17',
    'BaconWizard17',
    'August 2025',
    'Export 3D Asset - Advanced Texture',
    '*',
    [
        (PF_IMAGE, 'image', 'Input image', None),
        (PF_DRAWABLE, 'layer', 'Layer, mask or channel', None),
        (PF_OPTION, 'texture_type', 'Advanced Texture Type:', 0, ['Normal Map', 'Specular Map', 'Gloss/Emissive Map', 'Environment Mask']),
        (PF_OPTION, 'normal_color', 'Steam/360 Normal Map Color:', 1, ['Yellow', 'Blue'])
    ],
    [],
    Export3DAdv,
    menu='<Image>/Marvel Mods/Export Textures/By Asset Type'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()