#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to reduce the size of an image by a factor of 2. 
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# (c) BaconWizard17 2022
#
#   History:
#   v1.0: 31Dec2022: First published version.

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
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
def scale_half (theImage, theLayer):
    # Start an undo group so that the entire operation can be undone at once
    pdb.gimp_image_undo_group_start(image)
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Get the current dimensions of the image
    currentWidth = theImage.width
    currentHeight = theImage.height
    # Get the new dimensions by dividing old dimensions by 2
    newWidth = currentWidth/2
    newHeight = currentHeight/2
    # scale the image accordingly
    pdb.gimp_image_scale(theImage, newWidth, newHeight)
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
    "python_fu_marvelmods_common_scale_half",
    "Scale image to half its original size.",
    "Scale image to half its original size.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2022",
    "Scale to Half Size",
    "*",
    [],
    [],
    scale_half,
    menu='<Image>/Marvel Mods/Image Scaling/'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()