#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export 3D asset's advanced textures.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2025.
#
#   History:
#   v1.0: 12Dec2024: First published version.
#   v2.0: 15Aug2025: Reduced code, as all texture format conversion and resizing can now be done through ALchemy.

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
# GIMP module
from gimpfu import *
# Internal modules
import marvel_mods_basic_gimp_procedures as mmbgp
# External modules
from datetime import datetime
import os.path


# ######### #
# FUNCTIONS #
# ######### #
# This function creates a white image that's used to make a channel all white when composing.
def CreateWhiteImage(export_image):
    # Create an image that will be made plain white.
    white_image = pdb.gimp_image_new(export_image.width, export_image.height, 0)
    # Create a layer for the plain white image.
    white_layer = pdb.gimp_layer_new(white_image, export_image.width, export_image.height, 0, 'Background', 100, 28)
    # Get the current layer of the white image.
    white_image_active_layer = pdb.gimp_image_get_active_layer(white_image)
    # Apply the layer to the image.
    pdb.gimp_image_insert_layer(white_image, white_layer, white_image_active_layer, 0)
    # Set the background fill color to white.
    pdb.gimp_context_set_background((255, 255, 255))
    # Fill the layer with the background color.
    pdb.gimp_drawable_fill(white_layer, 1)
    # Return the white image.
    return white_image

# This function is used to export the two types of Normal maps.
def ExportNorm(image, layer, xcf_path, normal_color, suffix):
    # Export the green normal map.
    mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', transparent = True, file_name_suffix = suffix + '_g')
    # Create a duplicate image for the other map and get its active layer.
    export_image = pdb.gimp_image_duplicate(image)
    export_layer = pdb.gimp_image_get_active_layer(export_image)
    # Decompose the image's channels to separate images.
    red_image, green_image, blue_image, alpha_image = pdb.plug_in_decompose(export_image, export_layer, 'RGBA', 0)
    # Create a plain white image to fill a channel all white.
    white_image = CreateWhiteImage(export_image)
    # Determine what the normal map color should be.
    if normal_color == 0:
        # The normal map should be yellow.
        # Compose the image: green channel in red channel, alpha channel in green channel, red channel (all black) in blue channel, white image in alpha channel.
        export_image = pdb.plug_in_compose(green_image, export_layer, alpha_image, red_image, white_image, 'RGBA')
    else:
        # The normal map should be blue.
        # Compose the image: green channel in red channel, alpha channel in green channel, white image in blue channel, white image in alpha channel.
        export_image = pdb.plug_in_compose(green_image, export_layer, alpha_image, white_image, white_image, 'RGBA')
    # Get the active layer of the new image.
    export_layer = pdb.gimp_image_get_active_layer(export_image)
    # Export the new image.
    mmbgp.ExportTextureMM(export_image, export_layer, xcf_path, '.png', file_name_suffix = suffix + '_b')

# Define the main operation
def Export3DAdv(image, layer, texture_type, normal_color, **kwargs):
    # Perform the initial operations.
    (okay_to_export, xcf_path) = mmbgp.InitialOps(image, layer)
    # Create a dictionary for the suffixes by texture type.
    suffix_dict = {'0': '_n', '1': '_s', '2': '_g', '3': '_m'}
    # Get the file name.
    file_name = os.path.splitext(os.path.basename(xcf_path))[0]
    # Get the suffix by the texture type.
    suffix = suffix_dict[str(texture_type)]
    # Determine if the file name ends with the suffix.
    if file_name.endswith(suffix):
        # The file name ends with the suffix.
        # No additional suffix is needed.
        suffix = ''
    # Determine if it's okay to proceed.
    if okay_to_export == True:
        # No errors, can proceed.
        # Determine the texture type.
        if texture_type == 0:
            # This is a normal map.
            # Export the normal map.
            ExportNorm(image, layer, xcf_path, normal_color, suffix)
        else:
            # All other texture types.
            # Export the texture.
            mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_suffix = suffix)
        # Print the success message.
        pdb.gimp_message('SUCCESS: exported ' + xcf_path + ' at ' + str(datetime.now().strftime('%H:%M:%S')))