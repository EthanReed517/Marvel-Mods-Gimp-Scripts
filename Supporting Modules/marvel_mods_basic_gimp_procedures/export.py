#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export different texture types
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2025
#
#   History:
#   v1.0: 12Dec2024: First published version.
#   v2.0: 15Aug2025: Rewrite to fit my current code formatting.

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
from os import remove, rename
import os.path
import subprocess


# ######### #
# FUNCTIONS #
# ######### #
# This function is used to resize an image.
def ResizeImage(image, layer, scale_factor):
    # Get the current image dimensions
    current_width = float(image.width)
    current_height = float(image.height)
    # Get the new sizes
    new_width = scale_factor * current_width
    new_height = scale_factor * current_height
    # scale the image accordingly
    pdb.gimp_image_scale(image, new_width, new_height)
    # Resize the layer to the image size
    pdb.gimp_layer_resize_to_image_size(layer)

# This function converts to PNG8 Alpha after the image is exported.
def PNG8Alpha(out_file_path, colors):
    # Index the result file
    subprocess.call('pngquant --force --verbose ' + str(colors) + ' "' + out_file_path + '"')
    # Delete the original file.
    remove(out_file_path)
    # Set up the path to the new file that pngquant created.
    new_path = os.path.splitext(out_file_path)[0] + '-fs8.png'
    # Rename the new file to the old file's name.
    rename(new_path, out_file_path)

# This function exports any image.
def ExportTextureMM(image, layer, xcf_path, extension, **kwargs):
    # Create a duplicate image for export and get its active layer.
    export_image = pdb.gimp_image_duplicate(image)
    export_layer = pdb.gimp_image_get_active_layer(export_image)
    # Loop through the layers that need to be removed (by default, none need to be).
    for layer in kwargs.get('layers_to_remove', []):
        # Get the layer by the name and remove it.
        layer_to_remove = pdb.gimp_image_get_layer_by_name(export_image, layer)
        pdb.gimp_image_remove_layer(export_image, layer_to_remove)
    # Determine if an outline is needed.
    if kwargs.get('portrait_outline', None) is not None:
        # An outline is needed.
        # Generate an outline.
        mmbgp.GeneratePortraitOutline(export_image, kwargs['portrait_outline'])
    # Determine if the image uses transparency.
    if kwargs.get('transparent', False) == True:
        # Transparency is needed.
        # Merge the layers.
        export_layer = pdb.gimp_image_merge_visible_layers(export_image, 1)
    else:
        # Transparency is not needed.
        # Flatten the image.
        export_layer = pdb.gimp_image_flatten(export_image)
    # Determine if the image needs to be scaled
    if not(kwargs.get('scale_factor', 1) == 1):
        # Scaling is needed.
        # Scale the image.
        ResizeImage(export_image, export_layer, kwargs['scale_factor'])
    # Determine if RGB-BGR swapping is needed.
    if kwargs.get('rgb_bgr', False) == True:
        # RGB-BGR swapping is needed.
        # Perform the swap.
        mmbgp.RGB_BGR(export_image, export_layer)
    # Determine if indexing is needed.
    if kwargs.get('index_colors', 0) > 0:
        # The image needs to be indexed.
        # Index the colors.
        export_layer = mmbgp.IndexColors(export_image, kwargs['index_colors'])
    # Get the out file path.
    xcf_folder = os.path.dirname(xcf_path)
    file_name = os.path.splitext(os.path.basename(xcf_path))[0]
    # Determine if a sub-folder is needed for the export.
    if not(kwargs.get('sub_folder', '') == ''):
        # A sub-folder is needed.
        # Check for the subfolder and create it if needed.
        mmbgp.FolderCheck(xcf_path, kwargs['sub_folder'])
    # Set up the output path.
    out_file_path = os.path.join(xcf_folder, kwargs.get('sub_folder', ''), kwargs.get('file_name_prefix', '') + file_name + kwargs.get('file_name_suffix', '') + extension)
    # Export based on the file extension.
    if extension == '.png':
        # This needs to be a .png file.
        # Export as a .png file.
        pdb.file_png_save(export_image, export_layer, out_file_path, out_file_path, 0, 9, 0, 0, 0, 0, 0)
    elif extension == '.dds':
        # This needs to be a .dds file.
        # Set up a dictionary for compression types.
        compression_type_dict = {
            'DXT1': 1,
            'DXT3': 2,
            'DXT5': 3
        }
        # Export the file.
        pdb.file_dds_save(export_image, export_layer, out_file_path, out_file_path, compression_type_dict[kwargs.get('dds_compression', 'DXT1')], 0, 4, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0)
    elif extension == '.tga':
        # This needs to be a .tga file.
        # Export the file.
        pdb.file_tga_save(export_image, export_layer, out_file_path, out_file_path, 1, 0)
    # Determine if the image needs to be PNG8 alpha.
    if kwargs.get('alpha_index_colors', 0) > 0:
        # This needs to be alpha indexed.
        # Perform alpha indexing.
        png8Alpha(out_file_path, kwargs.get('alpha_index_colors', 256))