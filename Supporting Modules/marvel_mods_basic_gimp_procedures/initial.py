#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to perform the initial operations on a texture.
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


# ######### #
# FUNCTIONS #
# ######### #
# This function performs the initial operations to check a texture.
def InitialOps(image, layer, **kwargs):
    # Begin with an initial assumption that it's okay to export the image.
    okay_to_export = True
    # Clear the selection (this is done just in case there is a selection, but there shouldn't be).
    pdb.gimp_selection_none(image)
    # Determine if the image's dimensions are powers of 2.
    po2_value = mmbgp.Po2Check(image, layer)
    # Determine if it's necessary to check for a square image.
    if kwargs.get('check_square', False) == True:
        # It's necessary to check if the image is square.
        # Check if the image is square.
        square_value = mmbgp.SquareCheck(image, layer)
    else:
        # It's not necessary to check if the image is square.
        # Set a fake value that the image is square. It may or may not be, but it doesn't matter. This value is just to make sure that the texture is okay for use.
        square_value = True
    # Verify that the image can be exported.
    if not((po2_value == True) and (square_value == True)):
        # It's not okay to export.
        # Update the value to reflect this.
        okay_to_export = False
        # Print an error for the user.
        pdb.gimp_message('ERROR: The image will not be exported.')
    # Get the file path of the image.
    xcf_path = pdb.gimp_image_get_filename(image)
    # Save the file as an xcf.
    pdb.gimp_xcf_save(0, image, layer, xcf_path, xcf_path)
    # Return the necessary values.
    return (okay_to_export, xcf_path)

# This function performs the initial optimizations to check a comic cover texture.
def InitialOpsComic(image, layer):
    # Clear the selection (this is done just in case there is a selection, but there shouldn't be).
    pdb.gimp_selection_none(image)
    # Check if the size is less than the minimum value.
    if image.height < 885:
        # The height is less than the minimum value.
        # Warn the user.
        pdb.gimp_message('WARNING: The image is shorter than 885 pixels in height. The image will still be exported, but it may appear blurry in the resulting textures.')
    # Check if the aspect ratio is correct.
    if not(((float(image.height) / image.width) > 1.52) and ((float(image.height) / image.width) < 1.55)):
        # The aspect ratio is not correct.
        # Warn the user.
        pdb.gimp_message('WARNING: The image does not have the correct aspect ration (approximately 1.54). The image will still be exported, but it may appear squashed or stretched in the resulting texture.')
    # Get the file path of the image.
    xcf_path = pdb.gimp_image_get_filename(image)
    # Save the file as an xcf.
    pdb.gimp_file_save(image, layer, xcf_path, xcf_path)
    # Return the necessary values.
    return xcf_path

# This function performs the initial optimizations to check a loading screen texture.
def InitialOpsLoading(image, layer):
    # Begin with an initial assumption that it's okay to export the image.
    okay_to_export = True
    # Initialize a value for the aspect ratio.
    aspect_ratio = None
    # Initialize a value for the guide position.
    guide_position = None
    # Clear the selection (this is done just in case there is a selection, but there shouldn't be).
    pdb.gimp_selection_none(image)
    # Determine if the image's height is an appropriate value.
    if not(image.height in [512, 1024, 2048]):
        # The image is not an acceptable height.
        # It's not okay to export.
        okay_to_export = False
        # Print an error for the user.
        pdb.gimp_message('ERROR: The image is not an appropriate height (512, 1024, or 2048). Only these heights can be used for loading screens.')
    else:
        # The image is an acceptable height.
        # Create the dictionary of possible widths.
        width_dict = {
            '512': {'4:3': 683, '16:9': 910, 'max_guide_pos': 227},
            '1024': {'4:3': 1365, '16:9': 1820, 'max_guide_pos': 455},
            '2048': {'4:3': 2731, '16:9': 3641, 'max_guide_pos': 910}
        }
        # Check the aspect ratio.
        if image.width == width_dict[str(image.height)]['4:3']:
            # This is a 4:3 image.
            # Set the aspect ratio.
            aspect_ratio = '4:3'
        elif image.width == width_dict[str(image.height)]['16:9']:
            # This is a 16:9 image.
            # Set the aspect ratio.
            aspect_ratio = '16:9'
            # Determine if there is a guide in the image.
            next_guide = pdb.gimp_image_find_next_guide(image, 0)
            # Determine if a guide was found.
            if next_guide > 0:
                # A guide was found.
                # Determine the guide's position.
                guide_position = pdb.gimp_image_get_guide_position(image, next_guide)
                # Verify that the guide's position is okay.
                if guide_position > width_dict[str(image.height)]['max_guide_pos']:
                    # The position is not okay.
                    # It's not okay to export.
                    okay_to_export = False
                    # Give an error to the user.
                    pdb.gimp_message('ERROR: The image has a guide that is in an improper position. For a 16:9 image that\'s ' + str(image.height) + ' in height, the maximum X position of the guide is ' + str(widthDict[str(image.height)]['maxGuidePos']) + '.')
        else:
            # The aspect ratio does not match.
            # It's not okay to export.
            okay_to_export = False
            # Give an error to the user.
            pdb.gimp_message('ERROR: The image does not have the correct width. For a loading screen with a height of ' + str(image.height) + ', a 4:3 loading screen should have a width of ' + str(widthDict[str(image.height)]['4:3']) + ', and a 16:9 loading screen should have a width of ' + str(widthDict[str(image.height)]['16:9']) + '.')
    # Get the file path of the image.
    xcf_path = pdb.gimp_image_get_filename(image)
    # Save the file as an xcf.
    pdb.gimp_xcf_save(0, image, layer, xcf_path, xcf_path)
    # Return the necessary values.
    return (okay_to_export, xcf_path, aspect_ratio, guide_position)