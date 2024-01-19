#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to generate the black outline around a character for an XML1-style character select portrait.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 10Jan2024: First published version.
#   v1.1: 19Jan2024: Adjust parameters

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
def generateXML1CSPOutline(image, layer, currentWidth):
    # Determine values based on size
    blurRadius = currentWidth / 256
    growRadius = currentWidth / 64
    # Start an undo group so that the entire operation can be undone at once
    pdb.gimp_image_undo_group_start(image)
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Add the outline
    pdb.python_fu_gegl_dropshadow(image, layer, 0.0, 0.0, blurRadius, 1, growRadius, (0, 0, 0), 2.00)
    # Display the changes
    pdb.gimp_displays_flush()
    # End the undo group
    pdb.gimp_image_undo_group_end(image)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_utilities_generate_xml1_csp_outline",
    "Generates an outline for a conversation portrait.",
    "Generates an outline for a conversation portrait.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2024",
    "Generate XML1 Character Select Portrait Outline",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "layer", "Layer, mask or channel", None),
        (PF_INT, "currentWidth", "The current width of the image", 1)
    ],
    [],
    generateXML1CSPOutline,
    menu='<Image>/Marvel Mods/Utilities'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()