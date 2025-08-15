#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export 3D asset's diffuse texture.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2025
#
#   History:
#   v1.0: 12Dec2024: First published version.
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


# ######### #
# FUNCTIONS #
# ######### #
# This is the main operation.
def Export3DDiffuse(image, layer, transparency):
    # Perform the initial operations.
    (okay_to_export, xcf_path) = mmbgp.InitialOps(image, layer)
    # Determine if it's okay to proceed.
    if okay_to_export == True:
        # No errors, can proceed.
        # Export the texture.
        mmbgp.ExportTextureMM(image, layer, xcf_path, '.png', transparent = transparency)
        # Print the success message.
        pdb.gimp_message('SUCCESS: exported ' + xcf_path + ' at ' + str(datetime.now().strftime('%H:%M:%S')))