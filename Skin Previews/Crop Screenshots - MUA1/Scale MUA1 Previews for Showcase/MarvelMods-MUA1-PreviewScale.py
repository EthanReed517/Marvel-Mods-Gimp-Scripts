#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gimpfu import*

def previewScale (image, layer):
    # Start an undo group so that the entire operation can be undone at once
    pdb.gimp_image_undo_group_start(image)
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Scale the image accordingly
    pdb.gimp_image_scale(image, 543, 1080)
    # Resize the layer to the image size
    pdb.gimp_layer_resize_to_image_size(layer)
    # Display the changes
    pdb.gimp_displays_flush()
    # End the undo group
    pdb.gimp_image_undo_group_end(image)

register(
    "python_fu_marvelmods_mua1_previewScale",
    "Scales the previews for MUA1 skins and mannequins.",
    "Scales the previews for MUA1 skins and mannequins.",
    "BaconWizard17",
    "BaconWizard17",
    "December 2022",
    "<Image>/Marvel Mods/Skin Previews/Crop Screenshots - MUA1/Scale Previews",
    "*",
    [],
    [],
    previewScale)

main()