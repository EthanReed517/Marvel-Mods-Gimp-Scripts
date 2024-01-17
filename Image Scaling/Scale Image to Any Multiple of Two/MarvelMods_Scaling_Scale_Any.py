#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to reduce the size of an image by a particular scale factor (multiple of 2) from 2 to 16. 
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 23Jan2023: First published version.
#   v1.1: 17Jan2024: minor updates for compatibility.

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
def scaleAny(image, layer, scale_factor):
    # Start an undo group so that the entire operation can be undone at once
    pdb.gimp_image_undo_group_start(image)
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Get the current dimensions of the image
    currentWidth = image.width
    currentHeight = image.height
    # Get the new dimensions by dividing old dimensions by the scale factor
    newWidth = currentWidth/scale_factor
    newHeight = currentHeight/scale_factor
    # scale the image accordingly
    pdb.gimp_image_scale(image, newWidth, newHeight)
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
    "python_fu_marvelmods_scaling_scaleAny",
    "Scale image to any smaller multiple of 2.",
    "Scale image to any smaller multiple of 2.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2024",
    "Scale to Any Size",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "Layer", "Layer, mask or channel", None),
        (PF_SLIDER, "scale_factor", "Divide size by:", 8, (2, 16, 2))
    ],
    [],
    scaleAny,
    menu="<Image>/Marvel Mods/Image Scaling"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()