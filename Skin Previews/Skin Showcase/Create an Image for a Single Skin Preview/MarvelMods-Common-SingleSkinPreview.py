#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import*

def singleSkinPreview (theImage, backgroundLayer, previews):
    # Establish the dimensions of the image
    if previews<=2:
        imageHeight = 1080
    else:
        imageHeight = 2160
    if previews==1:
        imageWidth = 543
    else:
        imageWidth = 1086
    # Create the image
    theImage = pdb.gimp_image_new(imageWidth, imageHeight, RGB)
    # Create the main layer
    backgroundLayer = pdb.gimp_layer_new(theImage, imageWidth, imageHeight, RGBA_IMAGE, "Background", 100, LAYER_MODE_NORMAL)
    # Create the portrait layer
    portraitLayer = pdb.gimp_layer_new(theImage, imageWidth, imageHeight, RGBA_IMAGE, "Portraits", 100, LAYER_MODE_NORMAL)
    # Add the layers to the image
    pdb.gimp_image_add_layer(theImage, backgroundLayer, 0)
    pdb.gimp_image_add_layer(theImage, portraitLayer, 0)
    # Add guides in necessary positions
    # These guides are for all preview sizes
    guide = pdb.gimp_image_add_hguide(theImage, 100)
    guide = pdb.gimp_image_add_hguide(theImage, 250)
    guide = pdb.gimp_image_add_hguide(theImage, 1080)
    guide = pdb.gimp_image_add_vguide(theImage, 100)
    guide = pdb.gimp_image_add_vguide(theImage, 272)
    guide = pdb.gimp_image_add_vguide(theImage, 443)
    guide = pdb.gimp_image_add_vguide(theImage, 543)
    # For anything bigger, need more guides
    if previews>=2:
        guide = pdb.gimp_image_add_vguide(theImage, 643)
        guide = pdb.gimp_image_add_vguide(theImage, 815)
        guide = pdb.gimp_image_add_vguide(theImage, 986)
        guide = pdb.gimp_image_add_vguide(theImage, 1086)
    if previews>=3:
        guide = pdb.gimp_image_add_hguide(theImage, 1180)
        guide = pdb.gimp_image_add_hguide(theImage, 1430)
        guide = pdb.gimp_image_add_hguide(theImage, 2160)
    # Background layer should be active since we are pasting there
    pdb.gimp_image_set_active_layer(theImage, backgroundLayer)
    # Display the image
    display = pdb.gimp_display_new(theImage)

register(
    "python_fu_marvelmods_common_singleSkinPreview",
    "Creates an image for a preview for 1 skin.",
    "Creates an image for a preview for 1 skin.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2022",
    "<Image>/Marvel Mods/Skin Previews/Skin Showcase/Create Single Skin Preview",
    "",
    [
        (PF_SLIDER, "previews", "Number of Previews Needed:", 2, (1, 4, 1))
    ],
    [],
    singleSkinPreview)

main()