#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a character select portrait (CSP) and conversation portrait (HUD)
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2025
#
#   History:
#   v1.0: 16Dec2024: First published version.
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
# This function checks for image errors.
def ErrorCheck(image, layer, okay_to_export, layer_list):
    # Make sure it's already okay to export.
    if okay_to_export == True:
        # No errors were found so far.
        # Check if the image is too small.
        if image.width >= 64:
            # Image is not too small, can proceed.
            # Initialize a variable to keep track of the number of correctly named layers.
            good_layers = 0
            # Loop through the layers to check.
            for layer_name in layer_list:
                # Look for layers based on name.
                test_layer = pdb.gimp_image_get_layer_by_name(image, layer_name)
                # Check if the layer exists.
                if test_layer == None:
                    # The layer does not exist.
                    # Announce the error.
                    pdb.gimp_message('ERROR: There is no layer named "' + layer_name + '".')
                else:
                    # The layer exists.
                    # Increase the count of good layers.
                    good_layers += 1
            # Check the number of layers that are named correctly.
            if not(good_layers == len(layer_list)):
                # Layers with all names are not present.
                # Don't allow the user to proceed.
                okay_to_export = False
        else:
            # The image is too small.
            # Give an error message.
            pdb.gimp_message('ERROR: The image dimensions are too small. The image should be at least 64x64, or else it will not be clear.')
            # Update the status.
            okay_to_export = False
    # Return whether or not the script can proceed, as well as the width and height
    return okay_to_export

# This function exports a standard portrait.
def ExportStandardPortrait(xcf_path, image, layer, template, alchemy_version, prefix, **kwargs):
    # Determine if the suffix is needed.
    if os.path.splitext(xcf_path)[0].endswith('_conversation'):
        # The file already ends with the correct suffix.
        # No need to add a suffix.
        suffix = ''
    else:
        # The file does not end with the correct suffix.
        # Add the suffix.
        suffix = '_conversation'
    # Determine the list of layers that need to be removed.
    if template == 'Combo':
        # This uses the combo HUD and CSP template.
        # Set up the CSP layers to be removed.
        layers_for_removal = ['XML1 CSP Frame', 'XML1 CSP Background', 'XML2 CSP Background']
    else:
        # This uses the HUD template only.
        # Nothing needs to be removed.
        layers_for_removal = []
    # Determine the Alchemy version.
    if alchemy_version == 2:
        # This is Alchemy 5 (texture replacement method).
        # Export the texture.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.tga', file_name_prefix = prefix, file_name_suffix = suffix, layers_to_remove = layers_for_removal, portrait_outline = kwargs.get('outline_choice', None))
    else:
        # This is any version in 3ds Max.
        # Export the texture.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = prefix, file_name_suffix = suffix, layers_to_remove = layers_for_removal, portrait_outline = kwargs.get('outline_choice', None))

# This function exports a next-gen style portrait.
def ExportNGPortrait(xcf_path, image, layer, template, alchemy_version):
    # Determine if the suffix is needed.
    if os.path.splitext(xcf_path)[0].endswith('_conversation'):
        # The file already ends with the correct suffix.
        # No need to add a suffix.
        suffix = ''
    else:
        # The file does not end with the correct suffix.
        # Add the suffix.
        suffix = '_conversation'
    # Determine the list of layers that need to be removed.
    if template == 'Combo':
        # This uses the combo HUD and CSP template.
        # Set up the CSP layers to be removed.
        layers_for_removal = ['XML1 CSP Frame', 'HUD Frame', 'HUD Background', 'XML1 CSP Background', 'XML2 CSP Background']
    else:
        # This uses the HUD template only.
        # Nothing needs to be removed.
        layers_for_removal = ['Frame', 'Background']
    # Determine the Alchemy version.
    if alchemy_version == 2:
        # This is Alchemy 5 (texture replacement method).
        # Export the texture.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.tga', file_name_prefix = 'ng_', file_name_suffix = suffix, layers_to_remove = layers_for_removal, transparent = True)
    else:
        # This is any version in 3ds Max.
        # Export the texture.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = 'ng_', file_name_suffix = suffix, layers_to_remove = layers_for_removal, transparent = True)

# This function exports an XML1 CSP.
def ExportXML1CSP(xcf_path, image, layer, template, alchemy_version):
    # Determine the list of layers that need to be removed.
    if template == 'Combo':
        # This uses the combo HUD and CSP template.
        # Set up the CSP layers to be removed.
        layers_for_removal = ['HUD Frame', 'HUD Background', 'XML2 CSP Background']
    else:
        # This uses the CSP template only.
        # Nothing needs to be removed.
        layers_for_removal = ['XML2 Background']
    # Determine if the Alchemy version is correct.
    if alchemy_version == 0:
        # This is Alchemy 2.5.
        # Export the texture.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = 'x1c_', layers_to_remove = layers_for_removal, portrait_outline = 'XML1CSP')

# This function exports an XML2 CSP.
def ExportXML2CSP(xcf_path, image, layer, template, alchemy_version):
    # Determine the list of layers that need to be removed.
    if template == 'Combo':
        # This uses the combo HUD and CSP template.
        # Set up the CSP layers to be removed.
        layers_for_removal = ['HUD Frame', 'HUD Background', 'XML1 CSP Frame', 'XML1 CSP Background']
    else:
        # This uses the CSP template only.
        # Nothing needs to be removed.
        layers_for_removal = ['Frame', 'XML1 Background']
    # Determine the Alchemy version.
    if alchemy_version == 2:
        # This is Alchemy 5 (texture replacement method).
        # Export the texture.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.tga', file_name_prefix = 'x2c_', layers_to_remove = layers_for_removal)
    else:
        # This is any version in 3ds Max.
        # Export the texture.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = 'x2c_', layers_to_remove = layers_for_removal)

# This is the main operation.
def ExportPortraits(image, layer, alchemy_version, plain_choice, next_gen_choice, hero_outline_choice, red_villain_outline_choice, green_villain_outline_choice, xml1_choice, xml2_choice, template):
    # Get the list of layers based on the template.
    template_layer_list_dict = {
        'Combo': ['XML1 CSP Frame', 'HUD Frame', 'Character', 'HUD Background', 'XML1 CSP Background', 'XML2 CSP Background'],
        'CSP': ['Frame', 'Character', 'XML1 Background', 'XML2 Background'],
        'HUD': ['Frame', 'Character', 'Background']
    }
    layer_list = template_layer_list_dict[template]
    # Perform the initial operations.
    (okay_to_export, xcf_path) = mmbgp.InitialOps(image, layer, check_square = True)
    okay_to_export = ErrorCheck(image, layer, okay_to_export, layer_list)
    # Determine if it's okay to proceed.
    if okay_to_export == True:
        # There are no issues with the image.
        # Go through the different exports.
        if plain_choice == 1:
            ExportStandardPortrait(xcf_path, image, layer, template, alchemy_version, '')
        if hero_outline_choice == 1:
            ExportStandardPortrait(xcf_path, image, layer, template, alchemy_version, 'b_', outline_choice = 'HUDBlue')
        if red_villain_outline_choice == 1:
            ExportStandardPortrait(xcf_path, image, layer, template, alchemy_version, 'r_', outline_choice = 'HUDRed')
        if green_villain_outline_choice == 1:
            ExportStandardPortrait(xcf_path, image, layer, template, alchemy_version, 'g_', outline_choice = 'HUDGreen')
        if next_gen_choice == 1:
            ExportNGPortrait(xcf_path, image, layer, template, alchemy_version)
        if xml1_choice == 1:
            ExportXML1CSP(xcf_path, image, layer, template, alchemy_version)
        if xml2_choice == 1:
            ExportXML2CSP(xcf_path, image, layer, template, alchemy_version)
        # Print the success message.
        pdb.gimp_message('SUCCESS: exported ' + xcf_path + ' at ' + str(datetime.now().strftime('%H:%M:%S')))