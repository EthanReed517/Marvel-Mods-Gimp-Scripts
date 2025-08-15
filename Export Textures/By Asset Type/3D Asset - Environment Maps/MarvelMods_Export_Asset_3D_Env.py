#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export environment maps to use with a 3D asset.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2025
#
#   History:
#   v1.0: 25Jan2024: First published version.
#   v1.1: 06Dec2024: Last-gen DXT1 normal maps are replaced with plain PNG, since Alchemy 2.5 doesn't support DXT1 normal maps
#   v2.0: 12Dec2024: Full redesign for improved performance using an external module for common operations.
#   v3.0: 15Aug2025: Reduced options, as all texture format conversion and resizing can now be done through ALchemy.

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
# This function checks for image errors.
def ErrorCheck(image, okay_to_export):
    # Check if any errors were found before.
    if okay_to_export == True:
        # No errors were found before.
        # Check if the image is too big.
        if image.width > 128:
            # The image is too big.
            # Warn the user.
            pdb.gimp_message('WARNING: The image size is greater than 128x128. The maximum recommended size is 128x128. Larger images will be reduced in size.')
        # Initialize a variable to keep track of the number of correctly named layers.
        good_layers = 0
        # Loop through the possible layer names.
        for layer_name in ['Up', 'Down', 'Left', 'Right', 'Front', 'Back']:
            # Look for layers based on this name.
            test_layer = pdb.gimp_image_get_layer_by_name(image, layer_name)
            # Check if the layer exists.
            if test_layer == None:
                # The layer does not exist.
                # Announce the error.
                pdb.gimp_message('ERROR: There is no layer named "' + layer_name + '".')
                # Update that it's not okay to export.
                okay_to_export = False
            else:
                # The layer exists.
                # Increase the count of good layers.
                good_layers += 1
        # Check the number of layers that are named correctly.
        if not(good_layers == 6):
            # Layers with all 6 names are not present.
            # Don't allow the user to proceed.
            okay_to_export = False
    # Return whether or not the script can proceed.
    return okay_to_export

# This funciton exports environment maps.
def ExportEnvMaps(image, layer, xcf_path, suffix, scale_factor_env):
    # Define the list of layer names
    layer_names = ['Up', 'Down', 'Left', 'Right', 'Front', 'Back']
    # Define the list of export suffixes
    suffixes = ['UP', 'DN', 'LF', 'RT', 'FR', 'BK']
    # Go through the layers
    for layer_name, env_suffix in zip(layer_names, suffixes):
        # Create the list of layers that can be removed
        layers_for_removal = []
        for layer_remove_name in layer_names:
            if not(layer_remove_name == layer_name):
                layers_for_removal.append(layer_remove_name)
        # Get the full suffix
        full_suffix = '_' + suffix + '_' + env_suffix
        # Export the image
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', scale_factor = scale_factor_env, file_name_suffix = full_suffix, layers_to_remove = layers_for_removal)

# Define the main operation
def Export3DEnv(image, layer, console):
    # Perform the initial operations
    (okay_to_export, xcf_path) = mmbgp.InitialOps(image, layer, check_square = True)
    okay_to_export = ErrorCheck(image, okay_to_export)
    # Determine if it's okay to proceed.
    if okay_to_export == True:
        # No errors, can proceed.
        # Determine the image size.
        if image.height > 128:
            # This is an oversized image.
            # Set the scale factors accordingly.
            l_scale_factor = 128 / float(image.height)
            m_scale_factor = 32 / float(image.height)
            s_scale_factor = 16 / float(image.height)
            xs_scale_factor = 8 / float(image.height)
        elif image.height > 32:
            # This is a 128x128 or 64x64 image.
            # Set the scale factors accordingly.
            l_scale_factor = 1.0
            m_scale_factor = 32 / float(image.height)
            s_scale_factor = 16 / float(image.height)
            xs_scale_factor = 8 / float(image.height)
        elif image.height > 16:
            # This is a 32x32 image.
            # Set the scale factors accordingly.
            l_scale_factor = 1.0
            m_scale_factor = 1.0
            s_scale_factor = 16 / float(image.height)
            xs_scale_factor = 8 / float(image.height)
        elif image.height > 8:
            # This is a 16x16 image.
            # Set the scale factors accordingly.
            l_scale_factor = 1.0
            m_scale_factor = 1.0
            s_scale_factor = 1.0
            xs_scale_factor = 8 / float(image.height)
        else:
            # This is an 8x8 image (or possibly smaller).
            # Set the scale factors accordingly.
            l_scale_factor = 1.0
            m_scale_factor = 1.0
            s_scale_factor = 1.0
            xs_scale_factor = 8 / float(image.height)
        # Export the texture for PC and next-gen (regardless of console).
        ExportEnvMaps(image, layer, xcf_path, 'L', l_scale_factor)
        # Determine the console.
        if console == 0:
            # This is for all consoles.
            # Export the remaining sizes.
            ExportEnvMaps(image, layer, xcf_path, 'M', m_scale_factor)
            ExportEnvMaps(image, layer, xcf_path, 'S', s_scale_factor)
            ExportEnvMaps(image, layer, xcf_path, 'XS', xs_scale_factor)
        # Print the success message.
        pdb.gimp_message('SUCCESS: exported ' + xcf_path + ' at ' + str(datetime.now().strftime('%H:%M:%S')))


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    'python_fu_marvelmods_export_asset_3d_env',
    'Exports a environment map textures in multiple sizes.\nWorks withskins, 3D heads, mannequins, boltons,\nand other models.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.',
    'Exports a environment map textures in multiple sizes. Works withskins, 3D heads, mannequins, boltons, and other models.',
    'BaconWizard17',
    'BaconWizard17',
    'August 2025',
    'Export 3D Asset - Environment Maps',
    '*',
    [
        (PF_IMAGE, 'image', 'Input image', None),
        (PF_DRAWABLE, 'layer', 'Layer, mask or channel', None),
        (PF_OPTION, 'console', 'Console:', 0, ['All', 'PC Only'])
    ],
    [],
    Export3DEnv,
    menu='<Image>/Marvel Mods/Export Textures/By Asset Type'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()
