#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to save a file and collect its file path information.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 17Jan2024: First published version.

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
# To be able to check file paths
import os
# So that scripts can be executed
from gimpfu import*


# ######### #
# FUNCTIONS #
# ######### #
# Define the main operation
def getPathSave(image, layer):
    # Get the file path of the original image
    filePath = pdb.gimp_image_get_filename(image)  
    # Save the file in its original format before proceeding
    pdb.gimp_file_save(image, layer, filePath, filePath)
    # Get the folder and file name from the file path
    folderName = os.path.dirname(filePath)  
    fileName = os.path.splitext(os.path.basename(filePath))[0]
    # Return the collected information
    return folderName, fileName


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_basic_get_path_save",
    "Saves the file and collects file path information. Returns the folder that the file is in, as well as its name (without the extension).",
    "Saves the file and collects file path information. Returns the folder that the file is in, as well as its name (without the extension).",
    "BaconWizard17",
    "BaconWizard17",
    "January 2024",
    "Get File Path and Save",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask, or channel", None)
    ],
    [
        (PF_STRING, "folderName", "The folder that the file is in"),
        (PF_STRING, "fileName", "The file name")
    ],
    getPathSave,
    menu='<Image>/Marvel Mods/Basic Procedures'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()