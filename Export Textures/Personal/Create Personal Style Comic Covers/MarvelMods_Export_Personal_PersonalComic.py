#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to create a comic cover from a character screenshot
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2025
#
#   History:
#   v1.0: 02Jan2025: First published version.   
#   v2.0: 16Aug2025: Reduced options, as all texture format conversion and resizing can now be done through ALchemy.

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
import marvel_mods_export_textures as mmet
# External modules
from os import makedirs
import os.path


# ######### #
# FUNCTIONS #
# ######### #
# This is the main operation.
def CreatePersonalComic(image, layer, xml1_choice, xml2_choice, mua1_choice, char_squat, big_logo, small_logo, directory, desc):
    # Set the character height.
    char_height = 1500
    # Create a duplicate image of the character.
    char_image = pdb.gimp_image_duplicate(image)
    char_layer = pdb.gimp_image_get_active_layer(char_image)
    # Get the proper height and width.
    new_height = char_height * char_squat
    new_width = (char_image.width * (char_height / float(char_image.height))) * char_squat
    # Scale the character image accordingly.
    pdb.gimp_image_scale(char_image, new_width, new_height)
    # Open the template image.
    temp_image = pdb.gimp_xcf_load(0, os.path.join(gimp.directory, 'plug-ins', 'MarvelModsTemplates', 'BW17_Comic.xcf'), os.path.join(gimp.directory, 'plug-ins', 'MarvelModsTemplates', 'BW17_Comic.xcf'))
    # Duplicate the template image.
    template_image = pdb.gimp_image_duplicate(temp_image)
    # Set up the list of icons to add.
    icon_list = [
        {'path': big_logo, 'x_pos': 738, 'y_pos': 36},
        {'path': small_logo, 'x_pos': 112, 'y_pos': 133}
    ]
    # Loop through the icons.
    for icon in icon_list:
        # Get the active layer of the template.
        template_layer = pdb.gimp_image_get_active_layer(template_image)
        # Open the icon's image.
        icon_image = pdb.gimp_xcf_load(0, icon['path'], icon['path'])
        # Get the active layer of the icon image.
        icon_layer = pdb.gimp_image_get_active_layer(icon_image)
        # Copy the icon layer and paste it in the new image.
        pdb.gimp_edit_copy(icon_layer)
        floating_layer = pdb.gimp_edit_paste(template_layer, False)
        # Determine the offsets.
        x_offset, y_offset = floating_layer.offsets
        x_offset = icon['x_pos'] - x_offset
        y_offset = icon['y_pos'] - y_offset
        pdb.gimp_layer_translate(floating_layer, x_offset, y_offset)
        # Anchor the layer.
        pdb.gimp_floating_sel_anchor(floating_layer)
    # Get the active layer again.
    template_layer = pdb.gimp_image_get_active_layer(template_image)
    # Create a new layer for the character.
    template_char_layer = pdb.gimp_layer_new(template_image, template_image.width, template_image.height, 1, 'Character', 100, 28)
    pdb.gimp_image_add_layer(template_image, template_char_layer, 0)
    # Copy the asset layer and paste it in the new image.
    pdb.gimp_edit_copy(char_layer)
    floating_layer = pdb.gimp_edit_paste(template_char_layer, False)
    # Determine the offsets.
    x_offset, y_offset = floating_layer.offsets
    x_offset = (642 - (charImage.width / 2)) - x_offset
    y_offset = (1800 - charImage.height) - y_offset
    pdb.gimp_layer_translate(floating_layer, x_offset, y_offset)
    # Anchor the layer.
    pdb.gimp_floating_sel_anchor(floating_layer)
    # Create the outline.
    pdb.python_fu_gegl_dropshadow(template_image, template_char_layer, 0.0, 0.0, 20.0, 1, 10, (0, 0, 0), 0.75)
    # Get the active layer again.
    template_layer = pdb.gimp_image_get_active_layer(template_image)
    # Display the image.
    #display = pdb.gimp_display_new(template_image)
    # Flush displays.
    #pdb.gimp_displays_flush()
    # Set up the file path.
    xcf_path = os.path.join(directory, 'Comic Covers', desc, os.path.basename(directory).replace(' ', '_').lower() + '_cov.xcf')
    # Check if the folder exists.
    if os.path.exists(os.path.dirname(xcf_path)) == False:
        makedirs(os.path.dirname(xcf_path))
    # Save the file as an xcf.
    pdb.gimp_xcf_save(0, template_image, template_layer, xcf_path, xcf_path)
    pdb.gimp_image_set_filename(template_image, xcf_path)
    # Export the image.
    mmet.ExportComic(template_image, template_layer, 0, 0, xml1_choice, xml2_choice, mua1_choice, personal_preview = True)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    'python_fu_marvelmods_utilities_personalcomic',
    'Creates comic covers from character screenshots.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.',
    'Creates comic covers from character screenshots.',
    'BaconWizard17',
    'BaconWizard17',
    'August 2025',
    'Create Personal-Style Comic Cover',
    '*',
    [
        (PF_IMAGE, 'image', 'Input image', None),
        (PF_DRAWABLE, 'layer', 'Layer, mask or channel', None),
        (PF_TOGGLE, 'xml1Choice', 'Create an XML1 comic cover?', 0),
        (PF_TOGGLE, 'xml2Choice', 'Create an XML2 comic cover?', 1),
        (PF_TOGGLE, 'mua1Choice', 'Create an MUA1 comic cover?', 1),
        (PF_FLOAT, 'charSquat', 'Squat modifier:', 1.00),
        (PF_FILE, 'bigLogo', 'Big Logo:', os.path.join(gimp.directory, 'plug-ins', 'MarvelModsTemplates', 'Logos', 'Big', 'X-Men.xcf')),
        (PF_FILE, 'smallLogo', 'Small Logo:', os.path.join(gimp.directory, 'plug-ins', 'MarvelModsTemplates', 'Logos', 'Small', 'X-Men.xcf')),
        (PF_DIRNAME, 'directory', 'Character folder:', 'C:\\Users\\ethan\\Desktop\\Marvel Mods\\BaconWizard17-Custom-Models\\Characters'),
        (PF_STRING, 'desc', 'Comic cover description:', 'Description')
    ],
    [],
    CreatePersonalComic,
    menu='<Image>/Marvel Mods/Export Textures/Personal'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()