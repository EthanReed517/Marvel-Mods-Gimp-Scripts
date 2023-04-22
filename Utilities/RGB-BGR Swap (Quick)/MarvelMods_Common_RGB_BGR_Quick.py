#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to switch the red and blue channels of an image.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 26Jan2023: First published version.
#   v1.1: 22Apr2023: Correct an error with the inputs

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
def rgb_bgr_quick (image, layer):
    # Define the additional options
    flattenChoice = 0
    # Start an undo group so that the entire operation can be undone at once
    pdb.gimp_image_undo_group_start(image)
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Flatten the image if this option is selected
    if flattenChoice == 0:
        layer = pdb.gimp_image_flatten(image)
    # Perform the swap
    pdb.plug_in_colors_channel_mixer(image, layer, FALSE, 0, 0, 1, 0, 1, 0, 1, 0, 0)
    # Display the changes
    pdb.gimp_displays_flush()
    # End the undo group
    pdb.gimp_image_undo_group_end(image)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_common_rgb_bgr_quick",
    "Switches the red and blue channels of an image.\nRuns without a dialog and flattens automatically.",
    "Switches the red and blue channels of an image.\nRuns without a dialog and flattens automatically.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2023",
    "RGB-BGR Swap (Quick)",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, 'drawable', 'Layer, mask or channel', None)
    ],
    [],
    rgb_bgr_quick,
    menu='<Image>/Marvel Mods/Utilities'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()