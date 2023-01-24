#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import*

def previewConvo (image, layer):
    # Start an undo group so that the entire operation can be undone at once
    pdb.gimp_image_undo_group_start(image)
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Crop the image accordingly
    pdb.gimp_image_resize(image, 169, 169, -90, -850)
    # Resize the layer to the image size
    pdb.gimp_layer_resize_to_image_size(layer)
    # Add an alpha channel just in case the layer doesn't currently have one
    pdb.gimp_layer_add_alpha(layer)
    # Create a circular (elliptical) selection for the portrait
    pdb.gimp_image_select_ellipse(image, CHANNEL_OP_ADD, 0, 0, 169, 169)
    # Invert the selection (because the stuff outside the circle needs to be deleted)
    pdb.gimp_selection_invert(image)
    # Delete what's selected
    pdb.gimp_drawable_edit_clear(layer)
    # Clear the selection
    pdb.gimp_selection_none(image)
    # Display the changes
    pdb.gimp_displays_flush()
    # End the undo group
    pdb.gimp_image_undo_group_end(image)

register(
    "python_fu_marvelmods_mua1_previewConvo",
    "Crops the preview window for MUA1 conversation portraits.",
    "Crops the preview window for MUA1 conversation portraits.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2022",
    "<Image>/Marvel Mods/Skin Previews/Crop Screenshots - MUA1/Crop Conversation Portrait Preview",
    "*",
    [],
    [],
    previewConvo)

main()