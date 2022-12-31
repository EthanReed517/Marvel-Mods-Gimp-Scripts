#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import*

def scale_quarter (theImage, theLayer):
    currentWidth = theImage.width
    currentHeight = theImage.height
    newWidth = currentWidth/4
    newHeight = currentHeight/4
    pdb.gimp_image_scale(theImage, newWidth, newHeight)

register(
    "python_fu_marvelmods_common_scale_quarter",
    "Scale image to a quarter of its original size.",
    "Scale image to a quarter of its original size.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2022",
    "<Image>/Marvel Mods/Image Scaling/Scale to Quarter Size",
    "*",
    [],
    [],
    scale_quarter)

main()