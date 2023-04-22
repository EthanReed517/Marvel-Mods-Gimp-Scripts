#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to create an template with grids to paste multiple skin previews. The template can have 1 to 8 rows and columns.
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
# Import the gimpfu module so that scripts can be executed
from gimpfu import*


# ######## #
# FUNCTION #
# ######## #
# Define the operation
def multiSkinPreviewAny (columns, rows):
    # Establish the dimensions of the image based on the number of rows and columns
    imageWidth = 543 * columns
    imageHeight = 1080 * rows
    # Create the image
    image = pdb.gimp_image_new(imageWidth, imageHeight, RGB)
    # Create the main layer
    layer = pdb.gimp_layer_new(image, imageWidth, imageHeight, RGBA_IMAGE, "Background", 100, LAYER_MODE_NORMAL)
    # Add the layer to the image
    pdb.gimp_image_add_layer(image, layer, 0)
    # Add guides at the top left and bottom right
    guide = pdb.gimp_image_add_vguide(image, 0) 
    guide = pdb.gimp_image_add_hguide(image, 0)
    guide = pdb.gimp_image_add_vguide(image, imageWidth) 
    guide = pdb.gimp_image_add_hguide(image, imageHeight)
    i = 0
    # Add 1 vertical guide for every column
    while i < columns:
        xcoord = i * 543
        guide = pdb.gimp_image_add_vguide(image, xcoord)
        i += 1
    # Re-initiate the counter
    i = 0
    # Add 1 horizontal guide for every row
    while i < rows:
        ycoord = i * 1080
        guide = pdb.gimp_image_add_hguide(image, ycoord)
        i += 1
    # Display the new image
    display = pdb.gimp_display_new(image)

# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP    
register(
	"python_fu_marvelmods_common_multiskinpreviewany",
	"Create template grid for skin preview images.",
	"Create template grid for skin preview images.",
	"BaconWizard17",
	"BaconWizard17",
	"January 2023",
	"Create Multi Skin Preview",
	"", 
	[
		(PF_SLIDER, "columns", "Number of Columns:", 2, (1, 8, 1)),
        (PF_SLIDER, "rows", "Number of Rows:", 2, (1, 8, 1))
	],
	[],
    multiSkinPreviewAny,
    menu="<Image>/Marvel Mods/Skin Previews/Skin Showcase",
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()