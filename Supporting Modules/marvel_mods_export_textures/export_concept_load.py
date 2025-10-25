#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a loading screen or concept art texture
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2025
#
#   History:
#   v1.0: 17Dec2024: First published version.
#   v2.0: 11Sep2025: Reduced code, as all texture format conversion and resizing can now be done through ALchemy.

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


# ######### #
# FUNCTIONS #
# ######### #
# This function exports a personal preview.
def ExportPersonalPreview(image, layer, xcf_path, desc, width, personal_preview):
    # Determine if the preview is needed.
    if personal_preview == True:
        # A personal preview is needed.
        # Create a duplicate of the image.
        small_image = pdb.gimp_image_duplicate(image)
        # Get the active layer of the image.
        small_layer = pdb.gimp_image_get_active_layer(small_image)
        # Scale the image accordingly.
        pdb.gimp_image_scale(small_image, width, 282)
        # Start the new image.
        new_image = pdb.gimp_image_new(502, 282, 0)
        # Create a new layer for this image.
        new_layer = pdb.gimp_layer_new(new_image, 502, 282, 1, 'New Layer', 100, 28)
        # Get the active layer of the image.
        active_layer = pdb.gimp_image_get_active_layer(new_image)
        # Apply the new layer to the active layer.
        pdb.gimp_image_insert_layer(new_image, new_layer, active_layer, 0)
        # Get the new active layer.
        new_layer = pdb.gimp_image_get_active_layer(new_image)
        # Copy the asset layer and paste it in the new image.
        pdb.gimp_edit_copy(small_layer)
        floating_layer = pdb.gimp_edit_paste(new_layer, False)
        # Determine the offsets.
        x_offset, y_offset = floating_layer.offsets
        x_offset = ((502 - width) / 2) - x_offset
        y_offset = 30 - y_offset
        pdb.gimp_layer_translate(floating_layer, x_offset, y_offset)
        # Anchor the layer.
        pdb.gimp_floating_sel_anchor(floating_layer)
        # Get the new active layer.
        new_layer = pdb.gimp_image_get_active_layer(new_image)
        # Set the foreground fill color.
        pdb.gimp_context_set_foreground((255, 255, 255))
        # Set up the dicitonary of X positions.
        x_pos_dict = {
            'XML1/XML2 (not PSP)': 14,
            'XML2 PSP/MUA1/MUA2': 6
        }
        # Create the text.
        text_layer = pdb.gimp_text_fontname(new_image, new_layer, x_pos_dict[desc], 0, desc, 0, True, 31, 1, 'Gunship')
        # Merge the layer.
        pdb.gimp_floating_sel_anchor(text_layer)
        # Set up the suffixes.
        suffix_dict = {
            'XML1/XML2 (not PSP)': '4-3',
            'XML2 PSP/MUA1/MUA2': '16-9'
        }
        # Export the preview.
        mmbgp.ExportTextureMM(new_image, new_layer, xcf_path, '.png', transparent = True, file_name_prefix = '!Personal - ', file_name_suffix = ' (' + suffix_dict[desc] + ')')

# This function exports the XML2 PSP texture.
def ExportXML2PSPLoad(image, layer, xcf_path, alchemy_version):
    # Create a duplicate image of the loading screen and get its active layer.
    psp_image = pdb.gimp_image_duplicate(image)
    psp_layer = pdb.gimp_image_get_active_layer(psp_image)
    # Flatten the image.
    psp_layer = pdb.gimp_image_flatten(psp_image)
    # Scale the image.
    pdb.gimp_image_scale(psp_image, 480, 271)
    # Resize the layer to the image size.
    pdb.gimp_layer_resize_to_image_size(psp_layer)
    # Create a plain black image.
    black_image = pdb.gimp_image_new(512, 512, 0)
    # Create a layer for the plain black image.
    black_layer = pdb.gimp_layer_new(black_image, 512, 512, 0, "Background", 100, 28)
    # Get the current layer of the white image.
    black_layer2 = pdb.gimp_image_get_active_layer(black_image)
    # Apply the layer to the image.
    pdb.gimp_image_insert_layer(black_image, black_layer, black_layer2, 0)
    # Set the background fill color.
    pdb.gimp_context_set_background((0, 0, 0))
    # Fill the layer with the background color.
    pdb.gimp_drawable_fill(black_layer, 1)
    # Copy the PSP image's layer and paste it in the new image.
    pdb.gimp_edit_copy(psp_layer)
    floating_layer = pdb.gimp_edit_paste(black_layer, False)
    # Determine the offsets.
    x_offset, y_offset = floating_layer.offsets
    x_offset = 0 - x_offset
    y_offset = 0 - y_offset
    pdb.gimp_layer_translate(floating_layer, x_offset, y_offset)
    # Anchor the layer.
    pdb.gimp_floating_sel_anchor(floating_layer)
    # Determine the Alchemy version.
    if alchemy_version == 1:
        # Alchemy 5 texture replacement.
        # Export for XML2 PSP.
        mmbgp.ExportTextureMM(black_image, black_layer, xcf_path, '.tga', file_name_prefix = '16-9-P_')
    else:
        # 3ds Max.
        # Export for XML2 PSP.
        mmbgp.ExportTextureMM(black_image, black_layer, xcf_path, '.png', file_name_prefix = '16-9-P_')

# This function exports a 16:9 loading screen.
def Export16_9Loading(image, layer, alchemy_version, xcf_path, type, personal_preview):
    # Export a plain png copy as a preview.
    mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = '!Preview - ', file_name_suffix = ' (16-9)')
    # Export the personal preview.
    ExportPersonalPreview(image, layer, xcf_path, 'XML2 PSP/MUA1/MUA2', 502, personal_preview)
    # Create a duplicate for the next-gen texture.
    next_gen_image = pdb.gimp_image_duplicate(image)
    next_gen_layer = pdb.gimp_image_get_active_layer(next_gen_image)
    # Create a duplicate for the last-gen texture.
    last_gen_image = pdb.gimp_image_duplicate(image)
    last_gen_layer = pdb.gimp_image_get_active_layer(last_gen_image)
    # Scale the textures.
    pdb.gimp_image_scale(next_gen_image, next_gen_image.height * 2, next_gen_image.height)
    pdb.gimp_image_scale(last_gen_image, last_gen_image.height, last_gen_image.height)
    # Determine the alchemy version.
    if alchemy_version == 1:
        # Alchemy 5 texture replacement.
        # Export the textures.
        mmbgp.ExportTextureMM(next_gen_image, next_gen_layer, xcf_path, '.tga', file_name_prefix = '16-9-N_')
        mmbgp.ExportTextureMM(last_gen_image, last_gen_layer, xcf_path, '.tga', file_name_prefix = '16-9-L_')
        # Determine the type.
        if type == 'loading':
            # This is loading screen.
            # Export the XML2 PSP texture.
            ExportXML2PSPLoad(image, layer, xcf_path, alchemy_version)
    else:
        # 3ds Max.
        # Export the texture.
        # Export the textures.
        mmbgp.ExportTextureMM(next_gen_image, next_gen_layer, xcf_path, '.png', file_name_prefix = '16-9-N_')
        mmbgp.ExportTextureMM(last_gen_image, last_gen_layer, xcf_path, '.png', file_name_prefix = '16-9-L_')
        # Determine the type.
        if type == 'loading':
            # This is loading screen.
            # Export the XML2 PSP texture.
            ExportXML2PSPLoad(image, layer, xcf_path, alchemy_version)

#This function exports a 4:3 loading screen.
def Export4_3Loading(image, layer, alchemy_version, xcf_path, personal_preview):
    # Export a plain png copy as a preview.
    mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = '!Preview - ', file_name_suffix = ' (4-3)')
    # Export the personal preview
    ExportPersonalPreview(image, layer, xcf_path, 'XML1/XML2 (not PSP)', 376, personal_preview)
    # Create a duplicate for the export image
    export_image = pdb.gimp_image_duplicate(image)
    export_layer = pdb.gimp_image_get_active_layer(export_image)
    # Scale the export image
    pdb.gimp_image_scale(export_image, export_image.height, export_image.height)
    # Determine the alchemy version.
    if alchemy_version == 0:
        # 3ds Max 5.
        # Export the texture.
        mmbgp.ExportTextureMM(export_image, export_layer, xcf_path, '.png', file_name_prefix = '4-3_')

# This function crops the 16:9 screen to 4:3 and exports it.
def Crop16_9to4_3AndExport(image, layer, alchemy_version, xcf_path, guide_position, personal_preview):
    # Create a duplicate for the export image.
    export_image = pdb.gimp_image_duplicate(image)
    export_layer = pdb.gimp_image_get_active_layer(export_image)
    # Create the dictionary of appropriate widths.
    widths_dict = {'512': 683, '1024': 1365, '2048': 2731}
    # Crop the image accordingly.
    pdb.gimp_image_resize(export_image, widths_dict[str(image.height)], image.height, (guide_position * -1), 0)
    # Resize the layer to the image size.
    pdb.gimp_layer_resize_to_image_size(export_layer)
    # Export the image.
    Export4_3Loading(export_image, export_layer, alchemy_version, xcf_path, personal_preview)

# This is the main operation.
def ExportConceptLoading(image, layer, alchemy_version, type, **kwargs):
    # Determine if personal previews are needed.
    personal_preview = kwargs.get('personal_preview', False)
    # Perform the initial operations.
    (okay_to_export, xcf_path, aspect_ratio, guide_position) = mmbgp.InitialOpsLoading(image, layer)
    # Determine if it's okay to export.
    if okay_to_export == True:
        # It's okay to export.
        # Determine the aspect ratio.
        if aspect_ratio == '16:9':
            # This is a 16:9 loading screen.
            # Export the loading screen.
            Export16_9Loading(image, layer, alchemy_version, xcf_path, type, personal_preview)
            # Determine if a 4:3 loading screen is needed.
            if guide_position is not None:
                # There is a guide.
                # Export a 4:3 loading screen.
                Crop16_9to4_3AndExport(image, layer, alchemy_version, xcf_path, guide_position, personal_preview)
        else:
            # This is a 4:3 loading screen.
            # Export the loading screen.
            Export4_3Loading(image, layer, alchemy_version, xcf_path, personal_preview)
        # Print the success message.
        pdb.gimp_message('SUCCESS: exported ' + xcf_path + ' at ' + str(datetime.now().strftime('%H:%M:%S')))