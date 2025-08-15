#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to add an outline to a portrait.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2025
#
#   History:
#   v1.0: 17Dec2024: First published version.
#   v2.0: 15Aug2025: Rewrite to fit my current code formatting.

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


# ######### #
# FUNCTIONS #
# ######### #
# This function generated a HUD outline.
def GenerateHudOutline(image, layer, color_choice):
    # Determine values based on size.
    blur_radius = image.width / 64
    grow_radius = image.width / 128
    # Figure out the color.
    if color_choice == 'HUDBlue':
        # Blue.
        # Assign the color.
        color = (0.454509803922, 0.787843137255, 0.961176470588)
    elif color_choice == 'HUDRed':
        # Red.
        # Assign the color.
        color = (0.745098039216, 0.180000000000, 0.172941176471)
    else:
        # Green.
        # Assign the color.
        color = (0.305882352941, 0.752941176471, 0.372549019608)
    # Add the outline.
    pdb.python_fu_gegl_dropshadow(image, layer, 0.0, 0.0, blur_radius, 1, grow_radius, color, 1.25)

# This function generates an XML1 CSP outline.
def GenerateXML1CSPOutline(image, layer):
    # Determine values based on size.
    blur_radius = image.width / 256
    grow_radius = image.width / 64
    # Add the outline.
    pdb.python_fu_gegl_dropshadow(image, layer, 0.0, 0.0, blur_radius, 1, grow_radius, (0, 0, 0), 2.00)

# This function gets the outline layer and picks the correct outline operation.
def GeneratePortraitOutline(image, outline_type):
    # Get the layer to add the outline to.
    outline_layer = pdb.gimp_image_get_layer_by_name(image, 'Character')
    # Determine if this is for a HUD.
    if 'HUD' in outline_type:
        # This is for a HUD.
        # Generate a HUD outline.
        GenerateHudOutline(image, outline_layer, outline_type)
    else:
        # This is for an XML1 CSP.
        # Generate the CSP outline.
        GenerateXML1CSPOutline(image, outline_layer)