#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to check if the dimensions of an image are powers of 2.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 10Jan2023: First published version.

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
# To be able to perform log operations
import math


# ######### #
# FUNCTIONS #
# ######### #
# Define the log base 2 operation
def Log2(x):
    return (math.log10(x) / math.log10(2))
    
# Define the function to check if a number is a power of 2
def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

# Define the main operation
def po2Check(image, layer):
    # Get the current dimensions of the image
    currentWidth = image.width
    currentHeight = image.height
    # Check if the dimensions are powers of 2
    if (isPowerOfTwo(currentWidth) and isPowerOfTwo(currentHeight)):
        # Both dimensions are powers of 2
        # return true
        po2Value = True
    else:
        # One or neither dimension is a power of 2
        # return false
        po2Value = False
    # Return the value
    return po2Value


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_basic_p02check",
    "Checks is the dimensions of a texture are powers of 2. Returns True if both are and False if one or neither are.",
    "Checks is the dimensions of a texture are powers of 2. Returns True if both are and False if one or neither are.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2024",
    "Power of 2 Check",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask, or channel", None)
    ],
    [
        (PF_BOOL, "po2Value", "Power of 2 Status")
    ],
    po2Check,
    menu="<Image>/Marvel Mods/Basic Procedures"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()