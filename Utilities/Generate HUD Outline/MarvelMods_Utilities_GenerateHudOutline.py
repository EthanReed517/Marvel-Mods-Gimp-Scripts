#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to generate the glowing outline around characters for MUA1-style conversation portraits (HUDs) in one of 3 colors.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 10Jan2024: First published version.

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
def generateHudOutline(image, layer, currentWidth, colorChoice):
    # Determine values based on size
    blurRadius = currentWidth / 64
    growRadius = currentWidth / 128
    # Figure out the color
    if colorChoice == 0:
        # Blue
        # Assign the color
        color = (0.454509803922, 0.787843137255, 0.961176470588)
    elif colorChoice == 1:
        # Red
        # Assign the color
        color = (0.745098039216, 0.180000000000, 0.172941176471)
    else:
        # Green
        # Assign the color
        color = (0.305882352941, 0.752941176471, 0.372549019608)
    # Start an undo group so that the entire operation can be undone at once
    pdb.gimp_image_undo_group_start(image)
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Add the outline
    pdb.python_fu_gegl_dropshadow(image, layer, 0.0, 0.0, blurRadius, 1, growRadius, color, 1.25)
    # Display the changes
    pdb.gimp_displays_flush()
    # End the undo group
    pdb.gimp_image_undo_group_end(image)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_utilities_generate_hud_outline",
    "Generates an outline for a conversation portrait.",
    "Generates an outline for a conversation portrait.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2024",
    "Generate Conversation Portrait (HUD) Outline",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask, or channel", None),
        (PF_INT, "currentWidth", "The current width of the image", 1),
        (PF_OPTION, "p1", "Outline Color:", 0, ["Blue","Red","Green"])
    ],
    [],
    generateHudOutline,
    menu="<Image>/Marvel Mods/Utilities"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()