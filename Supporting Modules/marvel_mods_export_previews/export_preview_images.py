#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP to plugin crop a skin preview for the PC version of X-Men Legends II: Rise of Apocalypse.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2025
#
#   History:
#   v1.0: 14Dec2024: First published version.
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
# External modules
from datetime import datetime
import os.path


# ######## #
# FUNCTION #
# ######## #
# This function creates a new image.
def CreateNewImage(width, height):
    # Start the new image.
    new_image = pdb.gimp_image_new(width, height, 0)
    # Create a new layer for this image.
    new_layer = pdb.gimp_layer_new(new_image, width, height, 1, 'New Layer', 100, 28)
    # Get the active layer of the image.
    active_layer = pdb.gimp_image_get_active_layer(new_image)
    # Apply the new layer to the active layer.
    pdb.gimp_image_insert_layer(new_image, new_layer, active_layer, 0)
    # Get the new active layer.
    new_layer = pdb.gimp_image_get_active_layer(new_image)
    # Return the new image and layer.
    return new_image, new_layer

# This function gets the asset file name.
def GetAssetFileName(xcf_path, asset_type, skin_num, descriptor):
    # Get the folder.
    folder = os.path.dirname(xcf_path)
    # Determine if any descriptor is needed for a suffix.
    if not(descriptor == 'None'):
        suffix = ' - ' + descriptor
    else:
        suffix = ''
    # Set up the dictionary of file names based on asset type.
    file_name_dict = {
        'Skin': skin_num + ' (Skin' + suffix + ')',
        'HUD': 'hud_head_' + skin_num + ' (' + suffix + ')',
        'Head': skin_num + ' (3D Head' + suffix + ')',
        'CSP': skin_num + ' (Character Select Portrait' + suffix + ')',
        'Mann': skin_num + ' (Mannequin' + suffix + ')'
    }
    # Get the out file path using the asset type.
    out_file_path = os.path.join(folder, file_name_dict[asset_type] + '.png')
    # Fix the Start of the suffix for HUDs.
    if '( - ' in out_file_path:
        out_file_path = out_file_path.replace('( - ', '(')
    # Fix the ending for huds without suffixes.
    if ' ()' in out_file_path:
        out_file_path = out_file_path.replace(' ()', '')
    # Return the file path.
    return out_file_path

# This function crops the preview.
def CropPreview(image, layer, asset_type, game):
    # Start a variable that assumes that the crop was successful.
    crop_successful = True
    # Set up the dictionary for the processing dimensions.
    if game == 'XML':
        # XML2.
        dims_dict = {
            'Skin': {'width': 543, 'height': 1080, 'x_offset': -222, 'y_offset': 0},
            'HUD': {'width': 152, 'height': 152, 'x_offset': -280, 'y_offset': -496, 'circle': True},
            'Head': {'width': 201, 'height': 201, 'x_offset': -116, 'y_offset': -747},
            'CSP': {'width': 163, 'height': 163, 'x_offset': -360, 'y_offset': -320}
        }
    else:
        # MUA1.
        dims_dict = {
            'Skin': {'width': 395, 'height': 785, 'x_offset': -339, 'y_offset': -196, 'scale': True},
            'HUD': {'width': 169, 'height': 169, 'x_offset': -90, 'y_offset': -850, 'circle': True},
            'Mann': {'width': 493, 'height': 981, 'x_offset': -713, 'y_offset': 0, 'scale': True}
        }
    # Execute the operation.
    try:
        # Crop the image accordingly.
        pdb.gimp_image_resize(image, dims_dict[asset_type]['width'], dims_dict[asset_type]['height'], dims_dict[asset_type]['x_offset'], dims_dict[asset_type]['y_offset'])
        # Resize the layer to the image size.
        pdb.gimp_layer_resize_to_image_size(layer)
        # Determine if it's necessary to crop it to a circle.
        if dims_dict[asset_type].get('circle', False) == True:
            # This needs to be a circle.
            # Add an alpha channel just in case the layer doesn't currently have one.
            pdb.gimp_layer_add_alpha(layer)
            # Create a circular (elliptical) selection for the portrait.
            pdb.gimp_image_select_ellipse(image, CHANNEL_OP_ADD, 0, 0, dims_dict[asset_type]['width'], dims_dict[asset_type]['height'])
            # Invert the selection (because the stuff outside the circle needs to be deleted).
            pdb.gimp_selection_invert(image)
            # Delete what's selected.
            pdb.gimp_drawable_edit_clear(layer)
            # Clear the selection.
            pdb.gimp_selection_none(image)
        # Determine if it's necessary to scale the image.
        if dims_dict[asset_type].get('scale', False) == True:
            # This needs to be scaled (MUA1 skin or mannequin).
            # Scale the image accordingly.
            pdb.gimp_image_scale(image, 543, 1080)
            # Resize the layer to the image size.
            pdb.gimp_layer_resize_to_image_size(layer)
    except KeyError:
        # Create an error.
        pdb.gimp_message('ERROR: A layer with an unrecognized asset type (' + asset_type + ') was found. This layer was not exported.')
        # Update to indicate that the crop was not successful.
        crop_successful = False
    # Return the crop status
    return crop_successful

# This is the main operation.
def FullPreview(image, layer, game):
    # Verify that the image is 1920x1080.
    if not((image.width == 1920) and (image.height == 1080)):
        # Warn the user.
        pdb.gimp_message('ERROR: The image is not 1920 x 1080. This size is required for the locations to be correct. Nothing will be exported.')
    else:
        # It's okay to proceed.
        # Clear the selection (This is done just in case there is a selection, but there shouldn't be).
        pdb.gimp_selection_none(image)
        # Get the file path of the image.
        xcf_path = pdb.gimp_image_get_filename(image)
        # Save the file as an xcf.
        pdb.gimp_file_save(image, layer, xcf_path, xcf_path)
        # Start counters to keep track of the number of rows and columns in the final image.
        row_count = 1
        column_count = 1
        # Start a list to track the images that need to be added to the final preview.
        image_list = []
        # Start a counter to keep track of the current image for naming purposes.
        counter = 1
        # Loop through the layers in the current image.
        for asset_layer in image.layers:
            # Get the layer's name.
            layer_name = pdb.gimp_item_get_name(asset_layer)
            # Split the name to get the information.
            layer_name_split = layer_name.split(',')
            asset_type = layer_name_split[0]
            skin_num = layer_name_split[1]
            row = int(layer_name_split[2])
            column = int(layer_name_split[3])
            position = int(layer_name_split[4])
            descriptor = layer_name_split[5]
            # Start a new image for this asset.
            asset_image, new_layer = CreateNewImage(image.width, image.height)
            # Copy the asset layer and paste it in the new image.
            pdb.gimp_edit_copy(asset_layer)
            floating_layer = pdb.gimp_edit_paste(new_layer, False)
            pdb.gimp_floating_sel_anchor(floating_layer)
            # Get the active layer of the new image.
            active_layer = pdb.gimp_image_get_active_layer(asset_image)
            # Get the name of the file.
            out_file_path = GetAssetFileName(xcf_path, asset_type, skin_num, descriptor)
            # Crop the image accordingly.
            crop_successful = CropPreview(asset_image, active_layer, layer_name_split[0], game)
            # Verify that the crop was achieved successfully.
            if crop_successful == True:
                # Export the new image.
                pdb.file_png_save(asset_image, active_layer, out_file_path, out_file_path, 0, 9, 0, 0, 0, 0, 0)
                # Check if the number of rows or columns needs to be updated.
                if int(layer_name_split[2]) > row_count:
                    row_count = int(layer_name_split[2])
                if int(layer_name_split[3]) > column_count:
                    column_count = int(layer_name_split[3])
                # Set the image name for disambiguation purposes.
                pdb.gimp_image_set_filename(asset_image, 'image' + str(counter))
                counter += 1
                # Add the image to the preview list.
                image_list.append({'image': asset_image, 'row': int(layer_name_split[2]), 'column': int(layer_name_split[3]), 'position': int(layer_name_split[4])})
        # Create the image for the combined preview.
        combined_image, combined_layer = CreateNewImage(543 * column_count, 1080 * row_count)
        # Loop through the images to add to the combined preview.
        for asset_image_dict in image_list:
            # Get the active layer of the image.
            export_image_layer = pdb.gimp_image_get_active_layer(asset_image_dict['image'])
            # Copy the asset layer and paste it in the new image.
            pdb.gimp_edit_copy(export_image_layer)
            floating_layer = pdb.gimp_edit_paste(combined_layer, False)
            # Determine the goal positions.
            x_goals_dict = {
                '0': 0,
                '1': (100 - (asset_image_dict['image'].width / 2)),
                '2': (272 - (asset_image_dict['image'].width / 2)),
                '3': (443 - (asset_image_dict['image'].width / 2)),
                '4': (100 - (asset_image_dict['image'].width / 2)),
                '5': (443 - (asset_image_dict['image'].width / 2))
            }
            y_goals_dict = {
                '0': 0,
                '1': (100 - (asset_image_dict['image'].height / 2)),
                '2': (100 - (asset_image_dict['image'].height / 2)),
                '3': (100 - (asset_image_dict['image'].height / 2)),
                '4': (250 - (asset_image_dict['image'].height / 2)),
                '5': (250 - (asset_image_dict['image'].height / 2))
            }
            # Determine the offsets.
            x_offset, y_offset = floating_layer.offsets
            x_goal = (543 * (asset_image_dict['column'] - 1)) + x_goals_dict[str(asset_image_dict['position'])]
            y_goal = (1080 * (asset_image_dict['row'] - 1)) + y_goals_dict[str(asset_image_dict['position'])]
            x_offset = x_goal - x_offset
            y_offset = y_goal - y_offset
            pdb.gimp_layer_translate(floating_layer, x_offset, y_offset)
            # Anchor the layer.
            pdb.gimp_floating_sel_anchor(floating_layer)
            combined_layer = pdb.gimp_image_get_active_layer(combined_image)
        # Export the combined image.
        out_file_path = os.path.join(os.path.dirname(xcf_path), 'Full_3Full.png')
        pdb.file_png_save(combined_image, combined_layer, out_file_path, out_file_path, 0, 9, 0, 0, 0, 0, 0)
        # Crop the image accordingly.
        pdb.gimp_image_resize(combined_image, 543, 1080, 0, 0)
        # Resize the layer to the image size.
        pdb.gimp_layer_resize_to_image_size(combined_layer)
        # Export the combined image.
        out_file_path = os.path.join(os.path.dirname(xcf_path), 'Full_2HalfLarge.png')
        pdb.file_png_save(combined_image, combined_layer, out_file_path, out_file_path, 0, 9, 0, 0, 0, 0, 0)
        # Scale the image accordingly.
        pdb.gimp_image_scale(combined_image, 251, 500)
        # Resize the layer to the image size.
        pdb.gimp_layer_resize_to_image_size(combined_layer)
        # Export the combined image.
        out_file_path = os.path.join(os.path.dirname(xcf_path), 'Full_1HalfSmall.png')
        pdb.file_png_save(combined_image, combined_layer, out_file_path, out_file_path, 0, 9, 0, 0, 0, 0, 0)
        # Print the success message.
        pdb.gimp_message('SUCCESS: exported ' + xcf_path + ' at ' + str(datetime.now().strftime('%H:%M:%S')))