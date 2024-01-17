#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a file to a png file in a new subfolder
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 17Jan2023: First published version.

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
def exportPNG(image, layer, folderName, newFolder, fileName, indexedChoice):
    # Create a duplicate image for the export
    exportImage = pdb.gimp_image_duplicate(image)
    # Get the active layer of the new image
    exportLayer = pdb.gimp_image_get_active_layer(exportImage)
    # Determine if it's necessary to index the colors
    if indexedChoice == 1:
        # Needs to be indexed to 16 colors
        # Index the colors
        exportLayer = pdb.python_fu_marvelmods_basic_indexcolors(exportImage, 16)
    elif indexedChoice == 2:
        # Needs to be indexed to 256 colors
        # Index the colors
        exportLayer = pdb.python_fu_marvelmods_basic_indexcolors(exportImage, 256)
    # Check if the export folder exists and create it if needed
    outFolder = pdb.python_fu_marvelmods_basic_folderCheck(folderName, newFolder)
    # Get the new file name
    outFileName = fileName + ".png"
    # Get the full save file path
    outFilePath = os.path.join(outFolder, outFileName)
    # Export the image
    pdb.file_png_save(exportImage, exportLayer, outFilePath, outFilePath, 0, 9, 0, 0, 0, 0, 0)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_basic_exportPNG",
    "Exports a .png file. Input the name of the folder of the xcf file, the name of the new subfolder where the file will be exported, and the file name without an extension.",
    "Exports a .png file. Input the name of the folder of the xcf file, the name of the new subfolder where the file will be exported, and the file name without an extension.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2024",
    "Export a .png File",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask, or channel", None),
        (PF_STRING, "folderName", "Directory of the xcf file", None),
        (PF_STRING, "newFolder", "New subfolder where the image will be saved", None),
        (PF_STRING, "fileName", "Filename without an extension", None),
        (PF_OPTION, "indexedChoice", "Index the colors?", 2, ["No", "Yes, with 16 colors", "Yes, with 256 colors"])
    ],
    [],
    exportPNG,
    menu='<Image>/Marvel Mods/Basic Procedures'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()