#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import*

def scale_half (theImage, theLayer):
    currentWidth = theImage.width
    currentHeight = theImage.height
    newWidth = currentWidth/2
    newHeight = currentHeight/2
    pdb.gimp_image_scale(theImage, newWidth, newHeight)

register(
    "python_fu_marvelmods_common_scale_half",
    "Scale image to half its original size.",
    "Scale image to half its original size.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2022",
    "<Image>/Marvel Mods/Image Scaling/Scale to Half Size",
    "*",
    [],
    [],
    scale_half)

main()