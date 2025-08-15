#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to add an outline to a portrait.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2024
#
#   History:
#   v1.0: 17Dec2024: First published version.

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
# Define the function for HUD outlines
def generateHudOutline(image, layer, colorChoice):
    # Determine values based on size
    blurRadius = image.width / 64
    growRadius = image.width / 128
    # Figure out the color
    if colorChoice == "HUDBlue":
        # Blue
        # Assign the color
        color = (0.454509803922, 0.787843137255, 0.961176470588)
    elif colorChoice == "HUDRed":
        # Red
        # Assign the color
        color = (0.745098039216, 0.180000000000, 0.172941176471)
    else:
        # Green
        # Assign the color
        color = (0.305882352941, 0.752941176471, 0.372549019608)
    # Add the outline
    pdb.python_fu_gegl_dropshadow(image, layer, 0.0, 0.0, blurRadius, 1, growRadius, color, 1.25)

# Define the function for XML1 CSP outlines
def generateXML1CSPOutline(image, layer):
    # Determine values based on size
    blurRadius = image.width / 256
    growRadius = image.width / 64
    # Add the outline
    pdb.python_fu_gegl_dropshadow(image, layer, 0.0, 0.0, blurRadius, 1, growRadius, (0, 0, 0), 2.00)

# Define the main function
def generatePortraitOutline(image, outlineType):
    # Get the layer to add the outline to
    outlineLayer = pdb.gimp_image_get_layer_by_name(image, "Character")
    # Determine if this is for a HUD
    if "HUD" in outlineType:
        # This is for a HUD
        generateHudOutline(image, outlineLayer, outlineType)
    else:
        # This is for an XML1 CSP
        generateXML1CSPOutline(image, outlineLayer)