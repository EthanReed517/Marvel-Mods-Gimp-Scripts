#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export different texture types
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 12Dec2024: First published version.

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
# External modules
from os import remove, rename
import os.path
import subprocess


# ######### #
# FUNCTIONS #
# ######### #
# Define the function for resizing an image
def resizeImage(image, layer, scaleFactor):
    # Get the current image dimensions
    currentWidth = float(image.width)
    currentHeight = float(image.height)
    # Get the new sizes
    newWidth = scaleFactor * currentWidth
    newHeight = scaleFactor * currentHeight
    # scale the image accordingly
    pdb.gimp_image_scale(image, newWidth, newHeight)
    # Resize the layer to the image size
    pdb.gimp_layer_resize_to_image_size(layer)

# Define the function for converting to PNG8 after export (for png8 alpha)
def png8Alpha(outFilePath, colors):
    # Index the result file
    subprocess.call("pngquant --force --verbose " + str(colors) + " \"" + outFilePath + "\"")
    # Delete the original file
    remove(outFilePath)
    # Rename the new file to the old file's name
    newPath = os.path.splitext(outFilePath)[0] + "-fs8.png"
    rename(newPath, outFilePath)

# Define the function for exporting any image
def exportTextureMM(image, layer, xcfPath, extension, **kwargs):
    # Create a duplicate image for export and get its active layer
    exportImage = pdb.gimp_image_duplicate(image)
    exportLayer = pdb.gimp_image_get_active_layer(exportImage)
    # Loop through the layers to remove (default is none)
    for layer in kwargs.get("layersToRemove", []):
        # Get the layer by the name and remove it
        layerToRemove = pdb.gimp_image_get_layer_by_name(exportImage, layer)
        pdb.gimp_image_remove_layer(exportImage, layerToRemove)
    # Determine if an outline is needed
    if kwargs.get("portraitOutline", None) is not None:
        # An outline is needed
        # Generate an outline
        MMBGP.generatePortraitOutline(exportImage, kwargs["portraitOutline"])
    # Determine if the image uses transparency
    if kwargs.get("transparent", False) == True:
        # Transparency is needed
        # Merge the layers
        exportLayer = pdb.gimp_image_merge_visible_layers(exportImage, 1)
    else:
        # Transparency is not needed
        # Flatten the image
        exportLayer = pdb.gimp_image_flatten(exportImage)
    # Determine if the image needs to be scaled
    if not(kwargs.get("scale_factor", 1) == 1):
        # Scaling is needed
        resizeImage(exportImage, exportLayer, kwargs["scale_factor"])
    # Determine if RGB-BGR swapping is needed
    if kwargs.get("RGB_BGR", False) == True:
        # RGB-BGR swapping is needed
        MMBGP.RGB_BGR(exportImage, exportLayer)
    # Determine if indexing is needed
    if kwargs.get("indexColors", 0) > 0:
        # The image needs to be indexed
        # Index the colors
        exportLayer = MMBGP.indexColors(exportImage, kwargs["indexColors"])
    # Determine if a sub-folder is needed for the export
    if not(kwargs.get("subFolder") == ""):
        # Check for the subfolder and create it if needed
        MMBGP.folderCheck(xcfPath, kwargs["subFolder"])
    # Get the out file path
    xcfFolder = os.path.dirname(xcfPath)
    fileName = os.path.splitext(os.path.basename(xcfPath))[0]
    outFilePath = os.path.join(xcfFolder, kwargs.get("subFolder", ""), kwargs.get("fileNamePrefix","") + fileName + kwargs.get("fileNameSuffix", "") + extension)
    # Export based on the file extension
    if extension == ".png":
        pdb.file_png_save(exportImage, exportLayer, outFilePath, outFilePath, 0, 9, 0, 0, 0, 0, 0)
    elif extension == ".dds":
        # Set up a dictionary for compression types
        compressionTypeDict = {
            "DXT1": 1,
            "DXT3": 2,
            "DXT5": 3
        }
        # Export the file
        pdb.file_dds_save(exportImage, exportLayer, outFilePath, outFilePath, compressionTypeDict[kwargs.get("ddsCompression", "DXT1")], 0, 4, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0)
    elif extension == ".tga":
        pdb.file_tga_save(exportImage, exportLayer, outFilePath, outFilePath, 1, 0)
    # Determine if the image needs to be PNG8 alpha
    if kwargs.get("alphaIndexed", False) == True:
        # Perform alpha indexing
        png8Alpha(outFilePath, kwargs.get("alphaIndexColors", 256))