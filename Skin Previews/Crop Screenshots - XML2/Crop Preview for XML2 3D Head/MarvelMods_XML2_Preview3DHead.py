#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to crop a 3D Head preview for the PC version of X-Men Legends II: Rise of Apocalypse.
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
def preview3dHead (image, layer):
    # Start an undo group so that the entire operation can be undone at once
    pdb.gimp_image_undo_group_start(image)
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Crop the image accordingly
    pdb.gimp_image_resize(image, 141, 141, -146, -777)
    # Resize the layer to the image size
    pdb.gimp_layer_resize_to_image_size(layer)
    # Add an alpha channel just in case the layer doesn't currently have one
    pdb.gimp_layer_add_alpha(layer)
    # Create a circular (elliptical) selection for the portrait
    pdb.gimp_image_select_ellipse(image, CHANNEL_OP_ADD, 0, 0, 141, 141)
    # Invert the selection (because the stuff outside the circle needs to be deleted)
    pdb.gimp_selection_invert(image)
    # Delete what's selected
    pdb.gimp_drawable_edit_clear(layer)
    # Clear the selection
    pdb.gimp_selection_none(image)
    # Display the changes
    pdb.gimp_displays_flush()
    # End the undo group
    pdb.gimp_image_undo_group_end(image)

# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_xml2_preview3DHead",
    "Crops the preview window for XML2 3D heads.",
    "Crops the preview window for XML2 3D heads.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2023",
    "Crop 3D Head Preview",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, 'drawable', 'Layer, mask or channel', None)
    ],
    [],
    preview3dHead,
    menu='<Image>/Marvel Mods/Skin Previews/Crop Screenshots - XML2'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()