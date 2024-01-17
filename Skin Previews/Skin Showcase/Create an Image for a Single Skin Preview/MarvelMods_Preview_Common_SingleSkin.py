#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to create an template with grids to paste a single skin preview and its associated assets. The template can include 1 to 4 slots to include additional assets.
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
def singleSkinPreview (previews):
    # Establish the dimensions of the image
    if previews<=2:
        imageHeight = 1080
    else:
        imageHeight = 2160
    if previews==1:
        imageWidth = 543
    else:
        imageWidth = 1086
    # Create the image
    image = pdb.gimp_image_new(imageWidth, imageHeight, RGB)
    # Create the main layer
    backgroundLayer = pdb.gimp_layer_new(image, imageWidth, imageHeight, RGBA_IMAGE, "Background", 100, LAYER_MODE_NORMAL)
    # Create the portrait layer
    portraitLayer = pdb.gimp_layer_new(image, imageWidth, imageHeight, RGBA_IMAGE, "Portraits", 100, LAYER_MODE_NORMAL)
    # Add the layers to the image
    pdb.gimp_image_add_layer(image, backgroundLayer, 0)
    pdb.gimp_image_add_layer(image, portraitLayer, 0)
    # Add guides in necessary positions
    # These guides are for all preview sizes
    guide = pdb.gimp_image_add_hguide(image, 100)
    guide = pdb.gimp_image_add_hguide(image, 250)
    guide = pdb.gimp_image_add_hguide(image, 1080)
    guide = pdb.gimp_image_add_vguide(image, 100)
    guide = pdb.gimp_image_add_vguide(image, 272)
    guide = pdb.gimp_image_add_vguide(image, 443)
    guide = pdb.gimp_image_add_vguide(image, 543)
    # For anything bigger, need more guides
    if previews>=2:
        guide = pdb.gimp_image_add_vguide(image, 643)
        guide = pdb.gimp_image_add_vguide(image, 815)
        guide = pdb.gimp_image_add_vguide(image, 986)
        guide = pdb.gimp_image_add_vguide(image, 1086)
    if previews>=3:
        guide = pdb.gimp_image_add_hguide(image, 1180)
        guide = pdb.gimp_image_add_hguide(image, 1430)
        guide = pdb.gimp_image_add_hguide(image, 2160)
    # Background layer should be active since we are pasting there
    pdb.gimp_image_set_active_layer(image, backgroundLayer)
    # Display the image
    display = pdb.gimp_display_new(image)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP    
register(
    "python_fu_marvelmods_preview_common_singleSkin",
    "Creates an image for a preview for 1 skin.",
    "Creates an image for a preview for 1 skin.",
	"BaconWizard17",
	"BaconWizard17",
	"January 2023",
	"Create Single Skin Preview",
	"", 
	[
        (PF_SLIDER, "previews", "Number of Previews Needed:", 2, (1, 4, 1))
	],
	[],
    singleSkinPreview,
    menu="<Image>/Marvel Mods/Skin Previews/Skin Showcase",
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()