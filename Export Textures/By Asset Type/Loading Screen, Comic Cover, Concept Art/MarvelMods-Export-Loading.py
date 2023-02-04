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
def exportLoading(image, layer, game, console, asset):
    print("Temp")

# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_loading",
    "Exports a loading screen, comic book cover, or\n concept art texture to different formats and\n sizes. Check the README.md file included with\n the download for more clarity on the options.",
    "Exports a loading screen, comic book cover, or concept art texture to different formats and sizes.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2024",
    "Export Loading Screen, Comic, or Concept Art",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, 'drawable', 'Layer, mask or channel', None),
        (PF_OPTION,"p1","Game:", 0, ["XML1/XML2","MUA1"]),
        (PF_OPTION,"p1","Console:", 0, ["All (Except PSP)","PC Only","PSP Only"]),
        (PF_OPTION,"p1","Asset Type:", 0, ["Loading Screen","Comic Cover","Concept Art"])
    ],
    [],
    exportLoading,
    menu='<Image>/Marvel Mods/Export Textures/By Asset Type'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()