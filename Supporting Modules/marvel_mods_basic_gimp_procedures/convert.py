#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to perform common conversions on textures
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2025
#
#   History:
#   v1.0: 12Dec2024: First published version.
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
# This function is used to RGB-BGR swap an image.
def RGB_BGR(image, layer):
    # Perform the swap.
    pdb.plug_in_colors_channel_mixer(image, layer, FALSE, 0, 0, 1, 0, 1, 0, 1, 0, 0)
    # Display the changes.
    pdb.gimp_displays_flush()

# This function is used to index the colors for an image.
def IndexColors(image, colors):
    # Index the colors.
    pdb.gimp_image_convert_indexed(image, CONVERT_DITHER_NONE, CONVERT_PALETTE_GENERATE, colors, FALSE, FALSE, "")
    # Display the changes.
    pdb.gimp_displays_flush()
    # Get the active layer.
    layer = pdb.gimp_image_get_active_layer(image)
    # return the new layer.
    return layer