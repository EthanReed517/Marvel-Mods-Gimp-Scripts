#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a single skin preview in 3 different formats.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 25Jan2023: First published version.

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
# Import the gimpfu module so that scripts can be executed
from gimpfu import*


# ######## #
# FUNCTION #
# ######## #
# Define the operation
def loadingScreenExport(image, layer, exportOption, alchemyOption):
    #fill this out

# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_common_loadingScreenExport",
    "Exports a loading screen texture to different formats and sizes.\nCheck the README.md file included with the download for more\nclarity on the options.",
    "Exports a loading screen texture to different formats and sizes.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2024",
    "Export Loading Screen",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, 'drawable', 'Layer, mask or channel', None),
        (PF_OPTION,"p1","Size:", 0, ["16:9","4:3","Both"]),
        (PF_OPTION, "p16", "Alchemy Version:", 0, ["Alchemy 2.5","Alchemy 5"])
    ],
    [],
    loadingScreenExport,
    menu='<Image>/Marvel Mods/Export Textures'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()