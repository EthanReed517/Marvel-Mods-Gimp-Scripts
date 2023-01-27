#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export an image in PNG8 format.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 25Jan2023: First published version.

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


# ######## #
# FUNCTION #
# ######## #
# Define the function for converting to PNG8
def convertPNG8(image):
    # Start an undo group so that the entire operation can be undone at once
    pdb.gimp_image_undo_group_start(image)
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Flatten the Image
    layer = pdb.gimp_image_flatten(image)
    # Index the colors
    pdb.gimp_image_convert_indexed(image, CONVERT_DITHER_NONE, CONVERT_PALETTE_GENERATE, 256, FALSE, FALSE, "")
    # Display the changes
    pdb.gimp_displays_flush()
    # End the undo group
    pdb.gimp_image_undo_group_end(image)

# Define the main operation
def exportPNG8(image, layer):
    # Get the file path and file name
    filePath = pdb.gimp_image_get_filename(image)
    # Convert to PNG8
    convertPNG8(image)

# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_png8",
    "Exports a texture to PNG8 format.",
    "Exports a texture to PNG8 format.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2023",
    "Export as PNG8",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, 'drawable', 'Layer, mask or channel', None)
    ],
    [],
    exportPNG8,
    menu='<Image>/Marvel Mods/Export Textures/By Texture Format'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()