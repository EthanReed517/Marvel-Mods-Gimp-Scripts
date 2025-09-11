#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a comic cover texture.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2025
#
#   History:
#   v1.0: 17Dec2024: First published version.
#   v2.0: 16Aug2025: Reduced code, as all texture format conversion and resizing can now be done through ALchemy.

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
        pdb.gimp_image_scale(small_image, width, 141)
        # Start the new image.
        new_image = pdb.gimp_image_new(251, 171, 0)
        # Create a new layer for this image.
        new_layer = pdb.gimp_layer_new(new_image, 251, 171, 1, 'New Layer', 100, 28)
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
        x_offset = ((251 - width) / 2) - x_offset
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
            'XML1': 73,
            'XML2': 63,
            'XML2 PSP': 16,
            'MUA1': 71
        }
        # Create the text.
        text_layer = pdb.gimp_text_fontname(new_image, new_layer, x_pos_dict[desc], 0, desc, 0, True, 31, 1, 'Gunship')
        # Merge the layer.
        pdb.gimp_floating_sel_anchor(text_layer)
        # Export the preview.
        mmbgp.ExportTextureMM(new_image, new_layer, xcf_path, '.png', transparent = True, file_name_prefix = '!Personal - ', file_name_suffix=' (' + desc + ')')

# This function exports the XML1 texture.
def ExportXML1Cov(xcf_path, image, alchemy_version, personal_preview):
    # Determine if the correct Alchemy version was picked.
    if alchemy_version == 0:
        # Everything is correct.
        # Get the active layer of the image.
        layer = pdb.gimp_image_get_active_layer(image)
        # Export a plain png copy as a preview.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = '!Preview - ', file_name_suffix = ' (XML1)')
        # Export a personal preview
        ExportPersonalPreview(image, layer, xcf_path, 'XML1', 188, personal_preview)
        # Scale the image accordingly
        pdb.gimp_image_scale(image, 1024, 1024)
        # Export the texture.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = 'XML1_')

# This function exports the XML2 texture.
def ExportXML2Cov(xcf_path, image, alchemy_version, personal_preview):
    # Determine if the correct Alchemy version was picked.
    if alchemyVersion == 0:
        # The correct alchemy version was picked.
        # Get the active layer of the image.
        layer = pdb.gimp_image_get_active_layer(image)
        # Crop the image accordingly.
        pdb.gimp_image_resize(image, 1365, 1024, -228, 0)
        # Resize the layer to the image size.
        pdb.gimp_layer_resize_to_image_size(layer)
        # Export a plain png copy as a preview.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = '!Preview - ', file_name_suffix = ' (XML2)')
        # Export a personal preview.
        ExportPersonalPreview(image, layer, xcf_path, 'XML2', 188, personal_preview)
        # Scale the image accordingly.
        pdb.gimp_image_scale(image, 1024, 1024)
        # Export the texture.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = 'XML2_')

# This function exports the XML2 PSP texture.
def ExportXML2PSPCov(xcf_path, image, alchemy_version, personal_preview):
    # Scale the image accordingly.
    pdb.gimp_image_scale(image, 910, 512)
    # Get the active layer of the image.
    layer = pdb.gimp_image_get_active_layer(image)
    # Export a plain png copy as a preview.
    mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = '!Preview - ', file_name_suffix = ' (XML2 PSP)')
    # Export a personal preview.
    ExportPersonalPreview(image, layer, xcf_path, 'XML2 PSP', 251, personal_preview)
    # Scale the image accordingly.
    pdb.gimp_image_scale(image, 512, 512)
    # Determine which version of Alchemy was picked.
    if alchemyVersion == 2:
        # Alchemy 5 texture replacement.
        # Export for PSP.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.tga', file_name_prefix = 'XML2_PSP_')
    else:
        # 3ds Max.
        # Export for PSP.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = 'XML2_PSP_')

# This function exports the MUA1 next-gen texture.
def ExportMUA1NGCov(xcf_path, image, alchemy_version, personal_preview):
    # Get the active layer of the image
    layer = pdb.gimp_image_get_active_layer(image)
    # Export a plain png copy as a preview.
    mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = '!Preview - ', file_name_suffix = ' (MUA1)')
    # Export a personal preview.
    ExportPersonalPreview(image, layer, xcf_path, 'MUA1', 251, personal_preview)
    # Scale the image accordingly
    pdb.gimp_image_scale(image, 2048, 1024)
    # Determine which version of Alchemy was picked.
    if alchemyVersion == 2:
        # Alchemy 5 texture replacement.
        # Export the texture.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.tga', file_name_prefix = 'MUA1_NG_')
    else:
        # 3ds Max.
        # Export the texture.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = 'MUA1_NG_')

# This function exports the last-gen MUA1 texture.
def ExportMUA1LGCov(xcf_path, image, alchemy_version, personal_preview):
    # Get the active layer of the image.
    layer = pdb.gimp_image_get_active_layer(image)
    # Scale the image accordingly.
    pdb.gimp_image_scale(image, 1024, 1024)
    # Determine which version of ALchemy was picked.
    if alchemyVersion == 2:
        # Alchemy 5 texture replacement.
        # Export the texture.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.tga', file_name_prefix = 'MUA1_LG_')
    else:
        # 3ds Max.
        # Export the texture.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = 'MUA1_LG_')

# Define the main operation
def ExportComic(image, layer, alchemy_version, xml1_choice, xml2_choice, mua1_choice, **kwargs):
    # Determine if personal previews are needed.
    personal_preview = kwargs.get('personal_preview', False)
    # Perform initial operations on the comic cover.
    xcf_path = mmbgp.InitialOpsComic(image, layer)
    # Create the list of consoles.
    game_list = []
    if xml1_choice == 1:
        game_list.append('XML1')
    if xml2_choice == 1:
        game_list.append('XML2')
        game_list.append('XML2_PSP')
    if mua1_choice == 1:
        game_list.append('MUA1_LG')
        game_list.append('MUA1_NG')
    # Set up the dictionary of game-specific information.
    game_info_dict = {
        'XML1': {'width': 573, 'height': 885, 'x_offset': 397, 'y_offset': 72, 'export_function': ExportXML1Cov, 'template_file_name': 'XML1_Comic.xcf'},
        'XML2': {'width': 562, 'height': 863, 'x_offset': 613, 'y_offset': 51, 'export_function': ExportXML2Cov, 'template_file_name': 'XML2_Comic.xcf'},
        'XML2_PSP': {'width': 562, 'height': 863, 'x_offset': 613, 'y_offset': 51, 'export_function': ExportXML2PSPCov, 'template_file_name': 'XML2_Comic.xcf'},
        'MUA1_LG': {'width': 544, 'height': 838, 'x_offset': 814, 'y_offset': 94, 'export_function': ExportMUA1LGCov, 'template_file_name': 'MUA1_Comic.xcf'},
        'MUA1_NG': {'width': 544, 'height': 838, 'x_offset': 814, 'y_offset': 94, 'export_function': ExportMUA1NGCov, 'template_file_name': 'MUA1_Comic.xcf'}
    }
    # Loop through the list of consoles.
    for game in game_list:
        # Create a duplicate image of the cover.
        cover_image = pdb.gimp_image_duplicate(image)
        cover_layer = pdb.gimp_image_merge_visible_layers(cover_image, 1)
        # Scale the image accordingly for the game.
        pdb.gimp_image_scale(cover_image, game_info_dict[game]['width'], game_info_dict[game]['height'])
        # Open the game-specific image and get its active layer.
        game_image = pdb.gimp_xcf_load(0, os.path.join(gimp.directory, 'plug-ins', 'MarvelModsTemplates', game_info_dict[game]['template_file_name']), os.path.join('MarvelModsTemplates', gameInfoDict[game]['template_file_name']))
        game_layer = pdb.gimp_image_get_active_layer(game_image)
        # Copy the asset layer and paste it in the new image.
        pdb.gimp_edit_copy(cover_layer)
        floating_layer = pdb.gimp_edit_paste(game_layer, False)
        # Determine the offsets.
        x_offset, y_offset = floating_layer.offsets
        x_offset = game_info_dict[game]['x_offset'] - x_offset
        y_offset = game_info_dict[game]['y_offset'] - y_offset
        pdb.gimp_layer_translate(floating_layer, x_offset, y_offset)
        # Anchor the layer
        pdb.gimp_floating_sel_anchor(floating_layer)
        # Export the image
        game_info_dict[game]['export_function'](xcf_path, game_image, alchemy_version, personal_preview)
    # Print the success message.
    pdb.gimp_message('SUCCESS: exported ' + xcf_path + ' at ' + str(datetime.now().strftime('%H:%M:%S')))