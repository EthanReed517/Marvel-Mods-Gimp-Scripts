#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a single skin preview in 3 different formats.
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
# Import the gimpfu module so that scripts can be executed
from gimpfu import*


# ######## #
# FUNCTION #
# ######## #
# Define the operation
def singleSkinPreviewExport (image, layer):
    # Get the current file name and path
    fileName = pdb.gimp_image_get_filename(image)
    # Change the path's extension to .png
    fileNameOutHalfSmall = fileName[:-4] + "_1HalfSmall.png"
    fileNameOutHalfLarge = fileName[:-4] + "_2HalfLarge.png"
    fileNameOutFull = fileName[:-4] + "_3Full.png"
    
    # Start an undo group so that the entire operation can be undone at once
    pdb.gimp_image_undo_group_start(image)
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Flatten the image
    layer = pdb.gimp_image_flatten(image)
    # Export the full preview
    pdb.file_png_save(image, layer, fileNameOutFull, fileNameOutFull, FALSE, 9, FALSE, FALSE, FALSE, FALSE, FALSE)
    # Crop the image for the half preview
    pdb.gimp_image_resize(image, 543, 1080, 0, 0)
    # Resize the layer to the image size
    pdb.gimp_layer_resize_to_image_size(layer)
    # Display the changes
    pdb.gimp_displays_flush()
    # Export the large half preview
    pdb.file_png_save(image, layer, fileNameOutHalfLarge, fileNameOutHalfLarge, FALSE, 9, FALSE, FALSE, FALSE, FALSE, FALSE)
    # Scale the image for the small half preview
    pdb.gimp_image_scale(image, 251, 500)
    # Resize the layer to the image size
    pdb.gimp_layer_resize_to_image_size(layer)
    # Display the changes
    pdb.gimp_displays_flush()
    # Export the small half preview
    pdb.file_png_save(image, layer, fileNameOutHalfSmall, fileNameOutHalfSmall, FALSE, 9, FALSE, FALSE, FALSE, FALSE, FALSE)
    # End the undo group
    pdb.gimp_image_undo_group_end(image)

# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_common_singleSkinPreviewExport",
    "Exports a single skin preview in the necessary sizes.",
    "Exports a single skin preview in the necessary sizes.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2022",
    "Export Single Skin Preview",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, 'drawable', 'Layer, mask or channel', None)
    ],
    [],
    singleSkinPreviewExport,
    menu='<Image>/Marvel Mods/Skin Previews/Skin Showcase'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()