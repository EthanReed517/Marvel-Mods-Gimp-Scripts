#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a file to a dds file in a new subfolder
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
# Define the function for RGB-BGR swapping
def RGB_BGR(image, layer):
    # Perform the swap
    pdb.plug_in_colors_channel_mixer(image, layer, FALSE, 0, 0, 1, 0, 1, 0, 1, 0, 0)

# Define the main operation
def exportDDS(image, layer, folderName, newFolder, fileName, compressionChoice, rgbChoice):
    # Create a duplicate image for the export
    exportImage = pdb.gimp_image_duplicate(image)
    # Get the active layer of the new image
    exportLayer = pdb.gimp_image_get_active_layer(exportImage)
    # Determine if it's necessary to RGB-BGR swap
    if rgbChoice == 1:
        # RGB-BGR swap is needed
        # Do the swap
        RGB_BGR(exportImage, exportLayer)
    # Determine the compression value
    if compressionChoice == 0:
        # DXT1
        # Set the compression value
        compression = 1
    elif compressionChoice == 1:
        # DXT3
        # Set the compression value
        compression = 2
    else:
        # DXT5
        # Set the compression value
        compression = 3
    # Check if the export folder exists and create it if needed
    outFolder = pdb.python_fu_marvelmods_basic_folderCheck(folderName, newFolder)
    # Get the new file name
    outFileName = fileName + ".dds"
    # Get the full save file path
    outFilePath = os.path.join(outFolder, outFileName)
    # Export the image
    pdb.file_dds_save(exportImage, exportLayer, outFilePath, outFilePath, compression, 0, 4, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_basic_exportDDS",
    "Exports a .dds file. Input the name of the folder of the xcf file, the name of the new subfolder where the file will be exported, the file name without an extension, and the compression format.",
    "Exports a .dds file. Input the name of the folder of the xcf file, the name of the new subfolder where the file will be exported, the file name without an extension, and the compression format.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2024",
    "Export a .dds File",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask, or channel", None),
        (PF_STRING, "folderName", "Directory of the xcf file", None),
        (PF_STRING, "newFolder", "New subfolder where the image will be saved", None),
        (PF_STRING, "fileName", "Filename without an extension", None),
        (PF_OPTION, "compressionChoice", "Compression:", 0, ["DXT1","DXT3","DXT5"]),
        (PF_TOGGLE, "rgbChoice", "RGB-BGR Swap?", 0)
    ],
    [],
    exportDDS,
    menu='<Image>/Marvel Mods/Basic Procedures'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()