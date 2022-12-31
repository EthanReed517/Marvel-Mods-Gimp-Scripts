#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import*

def multiSkinPreviewAny (theImage, theLayer, columns, rows):
    # Establish the dimensions of the image based on the number of rows and columns
    theImageWidth = 543 * columns
    theImageHeight = 1080 * rows
    # Create the image
    theImage = pdb.gimp_image_new(theImageWidth, theImageHeight, RGB)
    # Create the main layer
    theLayer = pdb.gimp_layer_new(theImage, theImageWidth, theImageHeight, RGBA_IMAGE, "Background", 100, LAYER_MODE_NORMAL)
    # Add the layer to the image
    pdb.gimp_image_add_layer(theImage, theLayer, 0)
    # Add guides at the top left and bottom right
    guide = pdb.gimp_image_add_vguide(theImage, 0) 
    guide = pdb.gimp_image_add_hguide(theImage, 0)
    guide = pdb.gimp_image_add_vguide(theImage, theImageWidth) 
    guide = pdb.gimp_image_add_hguide(theImage, theImageHeight)
    i = 0
    # Add 1 vertical guide for every column
    while i < columns:
        xcoord = i * 543
        guide = pdb.gimp_image_add_vguide(theImage, xcoord)
        i += 1
    # Re-initiate the counter
    i = 0
    # Add 1 horizontal guide for every row
    while i < rows:
        ycoord = i * 1080
        guide = pdb.gimp_image_add_hguide(theImage, ycoord)
        i += 1
    # Display the new image
    display = pdb.gimp_display_new(theImage)

register(
    "python_fu_marvelmods_common_multiskinpreviewany",
    "Create template grid for skin preview images.",
    "Create template grid for skin preview images.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2022",
    "<Image>/Marvel Mods/Skin Previews/Skin Showcase/Create Multi Skin Preview",
    "",
    [
        (PF_SLIDER, "columns", "Number of Columns:", 2, (1, 8, 1)),
        (PF_SLIDER, "rows", "Number of Rows:", 2, (1, 8, 1))
    ],
    [],
    multiSkinPreviewAny)

main()