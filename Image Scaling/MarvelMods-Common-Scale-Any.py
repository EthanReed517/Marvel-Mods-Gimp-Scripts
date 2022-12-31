#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import*

def scale_any (theImage, theLayer, scale_factor):
    currentWidth = theImage.width
    currentHeight = theImage.height
    newWidth = currentWidth/scale_factor
    newHeight = currentHeight/scale_factor
    pdb.gimp_image_scale(theImage, newWidth, newHeight)

register(
    "python_fu_marvelmods_common_scale_any",
    "Scale image to any smaller power of 2.",
    "Scale image to any smaller power of 2.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2022",
    "<Image>/Marvel Mods/Image Scaling/Scale to Any Size",
    "*",
    [
        (PF_SLIDER, "scale_factor", "Divide size by:", 8, (2, 16, 2))
    ],
    [],
    scale_any)

main()