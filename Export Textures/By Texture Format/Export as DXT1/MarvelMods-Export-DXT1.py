#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export an image in DXT1 format.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 30Jan2023: First published version.

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
# Import the OS module to be able to check file paths
import os
# Import the gimpfu module so that scripts can be executed
from gimpfu import*


# ######### #
# FUNCTIONS #
# ######### #
# Define the folder checking operation
def folderCheck(dirname, newFolder):
    # Append the paths
    outFolder = os.path.join(dirname, newFolder)
    # Check if the path exists
    outFolderExists = os.path.exists(outFolder)
    # If the path doesn't exist, create the new folder
    if outFolderExists == False:
        os.mkdir(outFolder)
    # Return the new path
    return outFolder
    
# Define the function for converting to DXT1
def convertDXT1(image, layer, isBGR, flattenChoice):
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Flatten the image if chosen
    if flattenChoice==1:
        layer = pdb.gimp_image_flatten(image)
    # RGB-BGR swap if needed
    if isBGR=="yes":
        pdb.plug_in_colors_channel_mixer(image, layer, FALSE, 0, 0, 1, 0, 1, 0, 1, 0, 0)
    # Display the changes
    pdb.gimp_displays_flush()
    # Get the active layer
    layer = pdb.gimp_image_get_active_layer(image)
    # return the new layer
    return layer

# Define the main operation
def exportDXT1(image, layer, exportRGB, exportBGR, flattenChoice):
    # Get the file path of the original image
    filePath = pdb.gimp_image_get_filename(image)
    # Save the file in its original format before proceeding
    pdb.gimp_file_save(image, layer, filePath, filePath)
    # Get the folder and file name from the file path
    dirname = os.path.dirname(filePath)
    fileName = os.path.basename(filePath)
    # Start an undo group so that the entire operation can be undone at once
    pdb.gimp_image_undo_group_start(image)
    # Get the name of the export folder, check if it exists, and create it if it doesn't
    if exportRGB==1:
        outFolderRGB = folderCheck(dirname, "DXT1 RGB")
        # Prep for export
        layer = convertDXT1(image, layer, "no", flattenChoice)
        # Get the new file name
        outFileName = fileName[0:-3] + "dds"
        # Get the full save file path
        outFilePathRGB = os.path.join(outFolderRGB, outFileName)
        # Export the image
        pdb.file_dds_save(image, layer, outFilePathRGB, outFilePathRGB, 1, 0, 4, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0)
    if exportBGR==1:
        outFolderBGR = folderCheck(dirname, "DXT1 RGB-BGR Swapped")
        # Prep for export
        layer = convertDXT1(image, layer, "yes", flattenChoice)
        # Get the new file name
        outFileName = fileName[0:-3] + "dds"
        # Get the full save file path
        outFilePathBGR = os.path.join(outFolderBGR, outFileName)
        # Export the image
        pdb.file_dds_save(image, layer, outFilePathBGR, outFilePathBGR, 1, 0, 4, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0)
    # End the undo group
    pdb.gimp_image_undo_group_end(image)

# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_dxt1",
    "Exports a texture to DXT1 format as a .dds.",
    "Exports a texture to DXT1 format as a .dds.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2023",
    "Export as DXT1",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, 'drawable', 'Layer, mask or channel', None),
        (PF_TOGGLE, "p2", "Export in RGB:", 1),
        (PF_TOGGLE, "p2", "Export RGB-BGR Swapped:", 1),
        (PF_TOGGLE, "p2", "Flatten Image:", 1)
    ],
    [],
    exportDXT1,
    menu='<Image>/Marvel Mods/Export Textures/By Texture Format'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()