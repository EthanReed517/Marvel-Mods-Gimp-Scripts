#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP to plugin crop a skin preview for the PC version of X-Men Legends II: Rise of Apocalypse.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 23Jan2023: First published version.

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
# To be able to execute GIMP scripts
from gimpfu import*


# ######## #
# FUNCTION #
# ######## #
# Define the operation
def previewSkin(image, layer):
    # Start an undo group so that the entire operation can be undone at once
    pdb.gimp_image_undo_group_start(image)
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Crop the image accordingly
    pdb.gimp_image_resize(image, 543, 1080, -222, 0)
    # Resize the layer to the image size
    pdb.gimp_layer_resize_to_image_size(layer)
    # Display the changes
    pdb.gimp_displays_flush()
    # End the undo group
    pdb.gimp_image_undo_group_end(image)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_preview_xml2_Skin",
    "Crops the preview window for XML2 skins.",
    "Crops the preview window for XML2 skins.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2023",
    "Crop Skin Preview",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask or channel", None)
    ],
    [],
    previewSkin,
    menu="<Image>/Marvel Mods/Skin Previews/Crop Screenshots - XML2"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()