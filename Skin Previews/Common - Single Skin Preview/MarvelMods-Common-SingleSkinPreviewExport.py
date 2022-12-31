#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import*

def singleSkinPreviewExport (theImage, backgroundLayer):
    filename = pdb.gimp_image_get_filename(image)

register(
    "python_fu_marvelmods_common_singleSkinPreviewExport",
    "Exports a single skin preview in the necessary sizes.",
    "Exports a single skin preview in the necessary sizes.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2022",
    "<Image>/Marvel Mods/Skin Previews/Single Skin Showcase/Export Single Skin Preview",
    "*",
    [],
    [],
    singleSkinPreviewExport)

main()