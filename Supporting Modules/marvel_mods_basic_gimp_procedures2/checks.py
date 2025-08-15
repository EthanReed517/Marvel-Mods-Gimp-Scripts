#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to perform various checks on an image
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2024
#
#   History:
#   v1.0: 12Dec2024: First published version.

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
# Define the log base 2 operation
def Log2(x):
    return (math.log10(x) / math.log10(2))
    
# Define the function to check if a number is a power of 2
def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

# Define the power of 2 checking operation
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
        # Print the warning
        pdb.gimp_message("ERROR: One or both image dimensions are not a power of 2. Alchemy only supports image dimensions that are powers of 2.\n\nPowers of 2: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, and so on.")
    # Return the value
    return po2Value

# Define the square checking operation
def squareCheck(image, layer):
    # Get the current dimensions of the image
    currentWidth = image.width
    currentHeight = image.height
    # Check if the dimensions are powers of 2
    if (currentWidth == currentHeight):
        # The dimensions are equal
        # return true
        squareValue = True
    else:
        # The dimensions are not square
        # return false
        squareValue = False
        # Print the warning
        pdb.gimp_message("ERROR: The dimensions of this image are not the same. This type of texture should be square.")
    # Return the value
    return squareValue

# Define the function for checking if a folder exists and creating it if needed
def folderCheck(xcfPath, subFolder):
    # Get the xcf's folder
    xcfFolderPath = os.path.dirname(xcfPath)
    # Get the path to the sub-folder
    subFolderPath = os.path.join(xcfFolderPath, subFolder)
    # If the path doesn't exist, create the new folder
    if os.path.exists(subFolderPath) == False:
        makedirs(subFolderPath)