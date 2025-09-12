#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export an image in PNG8 format.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2025
#
#   History:
#   v1.0: 30Jan2023: First published version.
#   v2.0: 22Jan2024: Full rewrite to include error checking and basic procedures.
#   v3.0: 12Dec2024: Full redesign for improved performance using an external module for common operations.
#   v4.0: 11Sep2025: Rewrite to fit my current code formatting.

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
# This is the main operation.
def ExportPNG8(image, layer, transparency):
    # Perform the initial operations.
    (okay_to_export, xcf_path) = mmbgp.InitialOps(image, layer)
    # Determine if it's okay to proceed.
    if okay_to_export == True:
        # No errors, can proceed.
        # Determine if transparency is required.
        if transparency == 0:
            # Transparency is not needed.
            # Export the texture.
            mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', index_colors = 256)
        else:
            # Transparency is needed.
            # Export the texture.
            mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', transparent = 1, alpha_index_colors = 256)
        # Print the success message.
        pdb.gimp_message('SUCCESS: exported ' + xcf_path + ' at ' + str(datetime.now().strftime('%H:%M:%S')))


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    'python_fu_marvelmods_export_format_png8',
    'Exports a texture in PNG8 format.',
    'Exports a texture in PNG8 format.',
    'BaconWizard17',
    'BaconWizard17',
    'September 2025',
    'Export as PNG8 .png',
    '*',
    [
        (PF_IMAGE, 'image', 'Input image', None),
        (PF_DRAWABLE, 'drawable', 'Layer, mask or channel', None),
        (PF_OPTION, 'transparency', 'Preserve Transparency:', 0, ['No', 'Yes'])
    ],
    [],
    ExportPNG8,
    menu='<Image>/Marvel Mods/Export Textures/By Texture Format'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()