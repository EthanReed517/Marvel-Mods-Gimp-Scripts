#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export power icons
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2025
#
#   History:
#   v1.0: 01Feb2023: First published version.
#   v2.0: 12Dec2024: Full redesign for improved performance using an external module for common operations.
#   v3.0: 16Sep2025: Reduced options, as all texture format conversion and resizing can now be done through ALchemy.

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
def ExportIcons(image, layer, game, alchemy_version):
    # Perform the initial operations.
    (okay_to_export, xcf_path) = mmbgp.initialOps(image, layer, check_square = True)
    # Verify that it's okay to export.
    if okay_to_export == True:
        # It's okay to export.
        # Set the transparency based on the game.
        if game in ['XML1', 'XML2']:
            transparency = False
        else:
            transparency = True
        # Export a plain png copy as a preview.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = '!Preview - ', transparent = transparency)
        # Pick the console.
        if game == 0:
            # XML1.
            # Determine if the image is oversized (only check width because it was confirmed to be square).
            if image.width > 128:
                # The image is oversized, so set the scale_factor_set.
                scale_factor_set = 128 / float(image.width)
            else:
                # No scaling is needed.
                scale_factor_set = 1
            # Determine the Alchemy version.
            if alchemy_version == 0:
                # 3ds Max.
                # Export the image.
                mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', scale_factor = scale_factor_set, file_name_prefix = 'XML1_')
        elif game == 1:
            # XML2.
            # Determine if an icons2 file is needed.
            if ((image.width > 128) and (alchemy_version == 0)):
                # An icons2 file is needed.
                # Export the icons2 file.
                mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = 'XML2_', file_name_suffix = '2')
            # Determine the Alchemy version.
            if alchemy_version == 0:
                # 3ds Max.
                # Export the icons1 file.
                mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', file_name_prefix = 'XML2_', file_name_suffix = '1', scale_factor = 128 / float(image.width))
            else:
                # Texture replacement.
                # Export the icons1 file.
                mmbgp.ExportTextureMM(image, layer, xcf_path, '.tga', file_name_prefix = 'XML2_', file_name_suffix = '1', scale_factor = 128 / float(image.width))
        elif game == 2:
            # MUA1.
            # Determine if the image is oversized.
            if image.width > 256:
                scale_factor_set = 256 / float(image.width)
            else:
                scale_factor_set = 1
            # Determine the Alchemy version.
            if alchemy_version == 0:
                # 3ds Max.
                # Export the icons1 file.
                mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', scale_factor = scale_factor_set, file_name_prefix = 'MUA1_', transparent = True)
            else:
                # Texture replacement.
                # Export the icons1 file.
                mmbgp.ExportTextureMM(image, layer, xcf_path, '.tga', scale_factor = scale_factor_set, file_name_prefix = 'MUA1_', transparent = True)
        else:
            # MUA2.
            # Determine if the image is oversized.
            if image.width > 128:
                scale_factor_set = 128 / float(image.width)
            else:
                scale_factor_set = 1
            # Determine the Alchemy version.
            if alchemy_version == 0:
                # 3ds Max.
                # Export the icons1 file.
                mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', scale_factor = scale_factor_set, file_name_prefix = 'MUA2_', transparent = True)
            else:
                # Texture replacement.
                # Export the icons1 file.
                mmbgp.ExportTextureMM(image, layer, xcf_path, '.tga', scale_factor = scale_factor_set, file_name_prefix = 'MUA2_', transparent = True)
        # Print the success message.
        pdb.gimp_message('SUCCESS: exported ' + xcf_path + ' at ' + str(datetime.now().strftime('%H:%M:%S')))


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    'python_fu_marvelmods_export_asset_icons',
    'Exports a power icons texture.\n\nCheck the README.md file included with the\ndownload for more clarity on the options.',
    'Exports a power icons texture.',
    'BaconWizard17',
    'BaconWizard17',
    'December 2024',
    'Export Power Icons',
    '*',
    [
        (PF_IMAGE, 'image', 'Input image', None),
        (PF_DRAWABLE, 'layer', 'Layer, mask or channel', None),
        (PF_OPTION, 'game', 'Game:', 0, ['XML1', 'XML2', 'MUA1', 'MUA2']),
        (PF_OPTION, 'alchemy_version', 'Export Method:', 0, ['3ds Max', 'Alchemy 5 Texture Replacement'])
    ],
    [],
    ExportIcons,
    menu='<Image>/Marvel Mods/Export Textures/By Asset Type'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()