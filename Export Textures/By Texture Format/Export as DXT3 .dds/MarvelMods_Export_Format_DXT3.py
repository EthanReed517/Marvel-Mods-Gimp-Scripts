#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export an image in DXT3 format.
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 30Jan2023: First published version.
#   v2.0: 22Jan2024: Full rewrite to include error checking, Alchemy 5, and basic procedures.
#   v3.0: 12Dec2024: Full redesign for improved performance using an external module for common operations.

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
# Marvel Mods Operations
import Marvel_Mods_Basic_Gimp_Procedures as MMBGP


# ######### #
# FUNCTIONS #
# ######### #
# Define the main operation
def exportDXT3(image, layer, alchemyVersion, exportRGB, exportBGR):
    # Perform the initial operations
    (okayToExport, xcfPath) = MMBGP.initialOps(image, layer)
    # Determine if it's okay to proceed
    if okayToExport == True:
        # No errors, can proceed
        # Determine if an RGB version needs to be exported
        if exportRGB == 1:
            # RGB version needs to be exported
            # Export the RGB version
            MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", ddsCompression="DXT3", subFolder="DXT3 RGB")
        # Determine if a BGR version needs to be exported
        if exportBGR == 1:
            # BGR version needs to be exported
            # Check the Alchemy version
            if alchemyVersion == 0:
                # Alchemy 2.5
                # Export the BGR version
                MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", ddsCompression="DXT3", RGB_BGR=True, subFolder="DXT3 BGR")
            else:
                # Alchemy 5
                # Display the warning.
                pdb.gimp_message("WARNING: It is not necessary to RGB-BGR swap colors with Alchemy 5. No RGB-BGR-swapped texture was exported.")
        # Print the success message
        pdb.gimp_message("SUCCESS: exported " + xcfPath)


# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_format_dxt3",
    "Exports a texture to DXT3 format as a .dds.",
    "Exports a texture to DXT3 format as a .dds.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2024",
    "Export as DXT3 .dds",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "drawable", "Layer, mask or channel", None),
        (PF_OPTION, "alchemyVersion", "Alchemy Version:", 0, ["Alchemy 2.5","Alchemy 5"]),
        (PF_TOGGLE, "exportRGB", "Export in RGB?", 1),
        (PF_TOGGLE, "exportBGR", "Export RGB-BGR Swapped?", 1)
    ],
    [],
    exportDXT3,
    menu="<Image>/Marvel Mods/Export Textures/By Texture Format"
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()