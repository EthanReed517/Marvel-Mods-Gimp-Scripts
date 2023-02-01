#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a conversation portrait (HUD)
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 01Feb2023: First published version.

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
# Import the OS module to be able to check file paths
import os
# Import the gimpfu module so that scripts can be executed
from gimpfu import*


# ######### #
# FUNCTIONS #
# ######### #
# Define the main operation
def exportHUD(image, layer, console, outlineType):
    # Get the file path of the original image
    filePath = pdb.gimp_image_get_filename(image)    
    # Save the file in its original format before proceeding
    pdb.gimp_file_save(image, layer, filePath, filePath)
    # Get the folder and file name from the file path
    dirname = os.path.dirname(filePath)
    fileName = os.path.basename(filePath)
    # Get the current dimensions of the image
    currentWidth = image.width
    currentHeight = image.height
    # Determine if the image is oversized
    if (currentWidth > 128) or (currentHeight > 128):
        oversized == True
    # Start an undo group so that the entire operation can be undone at once
    pdb.gimp_image_undo_group_start(image)
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Flatten the Image
    layer = pdb.gimp_image_flatten(image)
    # Begin the Export
    # Pick if the texture is oversized or standard
    if oversized == True:
        # The texture is oversized
        # Export the image
        
        # RGB-BGR Swap
        
        # Export the image
        
        # BGR back to RGB
        
        # Determine if console export needs to happen
        if console == 0:
            # All consoles
            # Resize to 128x128
            
            # Export the image
            
            # Convert to PNG8
            
            # Export the image
            
            # Color mode back to RGB
            
            # Resize to half size
            
            # Convert to PNG8
            
            # Export the image
    else:
        # The texture is not oversized
        # Choose the console
        if console == 1:
            # PC only
            # Export the image
            
            # RGB-BGR Swap
            
            # Export the image
            
            # BGR back to RGB
            
        else:
            # All consoles
            # Export the image
            
            # RGB-BGR Swap
            
            # Export the image
            
            # BGR back to RGB
            
            # Resize to 128x128
            
            # Export the image
            
            # Convert to PNG8
            
            # Export the image
            
            # Color mode back to RGB
            
            # Resize to half size
            
            # Convert to PNG8
            
            # Export the image
            
    # End the undo group
    pdb.gimp_image_undo_group_end(image)

# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_hud",
    "Exports a conversation portrait (HUD) texture in multiple formats.",
    "Exports a conversation portrait (HUD) texture in multiple formats.",
    "BaconWizard17",
    "BaconWizard17",
    "February 2023",
    "Export Conversation Portrait (HUD)",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, 'drawable', 'Layer, mask or channel', None),
        (PF_OPTION,"p1","Console:", 0, ["All","PC Only"]),
        (PF_OPTION,"p1","Outline Type:", 0, ["Hero Outline","Villain Outline"]),
    ],
    [],
    exportSkin,
    menu='<Image>/Marvel Mods/Export Textures/By Asset Type'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()