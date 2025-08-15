#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to perform various checks on an image.
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
# External modules
import math
from os import makedirs
import os.path


# ######### #
# FUNCTIONS #
# ######### #
# This function is used to calculate the log base 2 of a number.
def Log2(x):
    return (math.log10(x) / math.log10(2))
    
# This function checks if a number is a power of 2.
def IsPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

# This function checks image dimensions to see if they're powers of 2.
def Po2Check(image, layer):
    # Get the current dimensions of the image.
    current_width = image.width
    current_height = image.height
    # Check if the dimensions are powers of 2.
    if (IsPowerOfTwo(current_width) and IsPowerOfTwo(current_height)):
        # Both dimensions are powers of 2.
        # Update the value to indicate that the dimensions are powers of 2.
        po2_value = True
    else:
        # One or neither dimension is a power of 2.
        # Update the value to indicate that the dimensions are not powers of 2.
        po2_value = False
        # Print the error for the user.
        pdb.gimp_message('ERROR: One or both image dimensions are not a power of 2. Alchemy only supports image dimensions that are powers of 2.\n\nPowers of 2: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, and so on.')
    # Return the value
    return po2_value

# This function checks if an image is square.
def SquareCheck(image, layer):
    # Get the current dimensions of the image.
    current_width = image.width
    current_height = image.height
    # Check if the dimensions are equal.
    if (current_width == current_height):
        # The dimensions are equal, so the image is a square.
        # Update the value to indicate that the image is square.
        square_value = True
    else:
        # The dimensions are not equal, so the image is not square.
        # Update the value to indicate that the image is not square.
        square_value = False
        # Print the error for the user.
        pdb.gimp_message('ERROR: The dimensions of this image are not the same. This type of texture should be square.')
    # Return the value
    return square_value

# This function checks if a folder exists and creates it if needed.
def FolderCheck(xcf_path, sub_folder):
    # Get the xcf's folder.
    xcf_folder_path = os.path.dirname(xcf_path)
    # Get the path to the sub-folder
    sub_folder_path = os.path.join(xcf_folder_path, sub_folder)
    # If the path doesn't exist, create the new folder
    if os.path.exists(sub_folder_path) == False:
        makedirs(sub_folder_path)