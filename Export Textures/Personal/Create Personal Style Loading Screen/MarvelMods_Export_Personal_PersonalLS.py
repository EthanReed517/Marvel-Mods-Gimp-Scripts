#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to create a loading screen from a character screenshot
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 02Jan2025: First published version.   
#   v2.0: 11Sep2025: Reduced options, as all texture format conversion and resizing can now be done through ALchemy.

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
# This function splits a character's name.
def SplitCharName(char_name):
    # Split by spaces.
    char_name_split = char_name.split(' ')
    # Start a list that will contain the resulting names.
    char_name_list = []
    # Start a counter to track the index.
    index = 0
    # Start a list of indices that have been used.
    indices_used = []
    # Loop through the words.
    for word in char_name_split:
        # Determine if this index has been used.
        if index in indices_used:
            # This word has already been used.
            # Pass.
            pass
        else:
            # This word has not been used.
            # Check if this is the last word.
            if index == (len(char_name_split) - 1):
                # This is the last word.
                # Add it to the list.
                char_name_list.append(word)
                # Add the index to the list.
                indices_used.append(index)
            else:
                # This is not the last word.
                # Determine the length of this word and the next one.
                if len(word + ' ' + char_name_split[index + 1]) < 12:
                    # The length is less than 12, so the words can be combined.
                    # Append to the list.
                    char_name_list.append(word + ' ' + char_name_split[index + 1])
                    # Add the indices to the list.
                    indices_used.append(index)
                    indices_used.append(index + 1)
                else:
                    # Add just one word to the list.
                    char_name_list.append(word)
                    # Add the index to the list.
                    indices_used.append(index)
        # Increment the counter.
        index += 1
    # Return the list of words.
    return char_name_list

# This is the main operation.
def CreatePersonalLS(image, layer, hero_4_3_choice, vill_4_3_choice, hero_16_9_choice, vill_16_9_choice, char_name, char_squat, directory, desc):
    # Create a duplicate image of the character.
    char_image = pdb.gimp_image_duplicate(image)
    char_layer = pdb.gimp_image_get_active_layer(char_image)
    # Get the proper height and width.
    new_height = 800 * char_squat
    new_width = (char_image.width * (800 / float(char_image.height))) * char_squat
    # Scale the character image accordingly.
    pdb.gimp_image_scale(char_image, new_width, new_height)
    # Split the character name into a list.
    char_name_list = SplitCharName(char_name)
    # Set up the list for processing.
    screen_list = [
        {'variable': hero_4_3_choice, 'template_file_name': 'BW17_Load_Hero.xcf', 'color': (0, 131, 221), 'font_height': 75, 'font_height_outline': 80, 'char_center': 986, 'crop': True, 'folder': 'XML'},
        {'variable': vill_4_3_choice, 'template_file_name': 'BW17_Load_Villain.xcf', 'color': (156, 6, 0), 'font_height': 75, 'font_height_outline': 80, 'char_center': 986, 'crop': True, 'folder': 'XML', 'prefix': 'v_'},
        {'variable': hero_16_9_choice, 'template_file_name': 'BW17_Load_Hero.xcf', 'color': (0, 131, 221), 'font_height': 94, 'font_height_outline': 100, 'char_center': 1212, 'crop': False, 'folder': 'MUA'},
        {'variable': vill_16_9_choice, 'template_file_name': 'BW17_Load_Villain.xcf', 'color': (156, 6, 0), 'font_height': 94, 'font_height_outline': 100, 'char_center': 1212, 'crop': False, 'folder': 'MUA', 'prefix': 'v_'}
    ]
    # Loop through the list of possible loading screens to create.
    for screen in screen_list:
        # Determine if the variable is true.
        if screen['variable'] == True:
            # This should be processed.
            # Open the template image.
            temp_image = pdb.gimp_xcf_load(0, os.path.join(gimp.directory, 'plug-ins', 'MarvelModsTemplates', screen['template_file_name']), os.path.join(gimp.directory, 'plug-ins', 'MarvelModsTemplates', screen['template_file_name']))
            # Duplicate the template image and get its active layer.
            template_image = pdb.gimp_image_duplicate(temp_image)
            template_layer = pdb.gimp_image_get_active_layer(template_image)
            # Crop the image accordingly.
            if screen['crop'] == True:
                pdb.gimp_image_resize(template_image, 1365, 1024, -226, 0)
                # Resize the layer to the image size.
                pdb.gimp_layer_resize_to_image_size(template_layer)
            # Copy the asset layer and paste it in the new image.
            pdb.gimp_edit_copy(char_layer)
            floating_layer = pdb.gimp_edit_paste(template_layer, False)
            # Determine the offsets.
            x_offset, y_offset = floating_layer.offsets
            x_offset = (screen["char_center"] - (char_image.width / 2)) - x_offset
            y_offset = (913 - char_image.height) - y_offset
            pdb.gimp_layer_translate(floating_layer, x_offset, y_offset)
            # Anchor the layer.
            pdb.gimp_floating_sel_anchor(floating_layer)
            # Get the active layer again.
            template_layer = pdb.gimp_image_get_active_layer(template_image)
            # Set the color for the text.
            pdb.gimp_context_set_foreground(screen['color'])
            # Start a counter for the words.
            word_count = 0
            # Loop through the words.
            for word in char_name_list:
                # Set the color for the outline text.
                pdb.gimp_context_set_foreground(screen['color'])
                # Create the outline text.
                text_layer = pdb.gimp_text_fontname(template_image, template_layer, 100, (100 + (word_count * screen['font_height'])), word, 0, True, screen['font_height_outline'], 1, 'Gunship Outline')
                # Merge the layer.
                pdb.gimp_floating_sel_anchor(text_layer)
                # Get the active layer again.
                template_layer = pdb.gimp_image_get_active_layer(template_image)
                # Set the color for the white text.
                pdb.gimp_context_set_foreground((255, 255, 255))
                # Create the white text.
                text_layer = pdb.gimp_text_fontname(template_image, template_layer, 100, (100 + (word_count * screen['font_height'])), word, 0, True, screen['font_height'], 1, 'Gunship')
                # Merge the layer.
                pdb.gimp_floating_sel_anchor(text_layer)
                # Get the active layer again.
                template_layer = pdb.gimp_image_get_active_layer(template_image)
                # Increment the word count.
                word_count += 1
            # Display the image
            #display = pdb.gimp_display_new(template_image)
            # Flush displays
            #pdb.gimp_displays_flush()
            # Set up the file path.
            xcf_path = os.path.join(directory, 'Loading Screens (' + screen['folder'] + ')', desc, screen.get('prefix', '') + '12301.xcf')
            # Check if the folder exists.
            if os.path.exists(os.path.dirname(xcf_path)) == False:
                makedirs(os.path.dirname(xcf_path))
            # Save the file as an xcf.
            pdb.gimp_xcf_save(0, template_image, template_layer, xcf_path, xcf_path)
            pdb.gimp_image_set_filename(template_image, xcf_path)
            # Export the image.
            mmet.ExportConceptLoading(template_image, template_layer, 0, 0, 'loading', personal_preview = True)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    'python_fu_marvelmods_utilities_personalls',
    'Creates loading screens from character screenshots.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.',
    'Creates loading screens from character screenshots.',
    'BaconWizard17',
    'BaconWizard17',
    'January 2025',
    'Create Personal-Style Loading Screen',
    '*',
    [
        (PF_IMAGE, 'image', 'Input image', None),
        (PF_DRAWABLE, 'layer', 'Layer, mask or channel', None),
        (PF_TOGGLE, 'hero_4_3_choice', 'Create a 4:3 hero loading screen?', 1),
        (PF_TOGGLE, 'vill_4_3_choice', 'Create a 4:3 villain loading screen?', 0),
        (PF_TOGGLE, 'hero_16_9_choice', 'Create a 16:9 hero loading screen?', 1),
        (PF_TOGGLE, 'vill_16_9_choice', 'Create a 16:9 villain loading screen?', 0),
        (PF_STRING, 'char_name', 'Character name:', 'Character Name'),
        (PF_FLOAT, 'char_squat', 'Squat modifier:', 1.00),
        (PF_DIRNAME, 'directory', 'Character folder:', 'C:\\Users\\ethan\\Desktop\\Marvel Mods\\BaconWizard17-Custom-Models\\Characters'),
        (PF_STRING, 'desc', 'Loading screen description:', 'Description')
    ],
    [],
    CreatePersonalLS,
    menu='<Image>/Marvel Mods/Export Textures/Personal'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()