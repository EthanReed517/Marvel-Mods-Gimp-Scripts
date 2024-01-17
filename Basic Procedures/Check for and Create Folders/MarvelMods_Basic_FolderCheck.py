#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to check if a folder exists and create it if not.
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
# To be able to check file paths
import os
# To be able to execute GIMP scripts
from gimpfu import*


# ######### #
# FUNCTIONS #
# ######### #
# Define the main operation
def folderCheck(folderName, newFolder):
    # Append the paths
    outFolder = os.path.join(folderName, newFolder)
    # Check if the path exists
    outFolderExists = os.path.exists(outFolder)
    # If the path doesn't exist, create the new folder
    if outFolderExists == False:
        os.mkdir(outFolder)
    # Return the new path
    return outFolder


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_basic_folderCheck",
    "Checks is a folder exists and creates it if not. Input the directory where the image is, as well as the destination folder. Returns the combined file path.",
    "Checks is a folder exists and creates it if not. Input the directory where the image is, as well as the destination folder. Returns the combined file path.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2024",
    "Folder Check",
    "*",
    [
        (PF_STRING, "folderName", "Directory of the xcf file", None),
        (PF_STRING, "newFolder", "New subfolder where the image will be saved", None)
    ],
    [
        (PF_STRING, "outFolder", "Full folder path")
    ],
    folderCheck,
    menu="<Image>/Marvel Mods/Basic Procedures"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()