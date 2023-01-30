#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a skin
# This was designed with the intention to use it with modding processes for MarvelMods.com, though it can have other uses. 
# For detailed instructions, please reference the README.md file included with this download.
# (c) BaconWizard17 2023
#
#   History:
#   v1.0: 30Jan2023: First published version.

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
# Import the OS module to be able to check file paths
import os
# Import the gimpfu module so that scripts can be executed
from gimpfu import*


# ######### #
# FUNCTIONS #
# ######### #
# Define the size checking operation
def sizeCheck(currentWidth, currentHeight, texType):
    if texType == 0:
        criteria = 256
    else:
        criteria = 128
    if (currentWidth > criteria) or (currentHeight > criteria):
        oversized = True
    else:
        oversized = False
    return oversized

# Define the folder checking operation
def folderCheck(dirname, newFolder):
    # Append the paths
    outFolder = os.path.join(dirname, newFolder)
    # Check if the path exists
    outFolderExists = os.path.exists(outFolder)
    # If the path doesn't exist, create the new folder
    if outFolderExists == False:
        os.mkdir(outFolder)
    # Return the new path
    return outFolder
    
# Define the function for indexing colors
def convertIndexed(image, colors):
    # Index the colors
    pdb.gimp_image_convert_indexed(image, CONVERT_DITHER_NONE, CONVERT_PALETTE_GENERATE, colors, FALSE, FALSE, "")
    # Display the changes
    pdb.gimp_displays_flush()
    # Get the active layer
    layer = pdb.gimp_image_get_active_layer(image)
    # return the new layer
    return layer
    
def RGB_BGR(image, layer):
    # Perform the swap
    pdb.plug_in_colors_channel_mixer(image, layer, FALSE, 0, 0, 1, 0, 1, 0, 1, 0, 0)
    # Display the changes
    pdb.gimp_displays_flush()

# Define the main operation
def exportSkin(image, layer, console, skinType, texType, charSize, alchemyVersion, PSPFormat):
    # Get the file path of the original image
    filePath = pdb.gimp_image_get_filename(image)
    # Save the file in its original format before proceeding
    pdb.gimp_file_save(image, layer, filePath, filePath)
    # Get the folder and file name from the file path
    dirname = os.path.dirname(filePath)
    fileName = os.path.basename(filePath)
    # Get the current dimensions of the image
    currentWidth = image.width
    currentHeight = image.height
    # Start an undo group so that the entire operation can be undone at once
    pdb.gimp_image_undo_group_start(image)
    # Clear the selection (This is done just in case there is a selection, but there shouldn't be)
    pdb.gimp_selection_none(image)
    # Flatten the Image
    layer = pdb.gimp_image_flatten(image)
    # Determine if the image is oversized
    oversized = sizeCheck(currentWidth, currentHeight, texType)
    # Begin the export
    if oversized == True:
        # The original texture size is above 256x256 for primary textures of 128x128 for secondary textures
        # Choose the console
        if console == 1:
            # PC only
            # Pick the version of Alchemy being used for skin creation
            if alchemyVersion == 0:
                # Alchemy 2.5
                print("export as RGB DXT1 to 'XML2 PC' folder")
                # RGB-BGR swap the image
                RGB_BGR(image, layer)
                print("export as BGR DXT1 to 'MUA1 PC' folder")
                # return from BGR to RGB
                RGB_BGR(image, layer)
            else:
                # Alchemy 5
                # RGB-BGR swap the image
                RGB_BGR(image, layer)
                print("export as BGR DXT1 to 'MUA1 PC' folder")                
        else: 
            # All consoles
            # Pick the version of Alchemy
            if alchemyVersion == 0:
                # Alchemy 2.5
                print("export as RGB DXT1 to 'Wii, Xbox, and XML2 PC' folder")
                # RGB-BGR swap the image
                RGB_BGR(image, layer)
                print("export as BGR DXT1 to 'MUA1 PC' folder")
                # BGR back to RGB
                RGB_BGR(image, layer)
                # Check if the character is oversized or standard
                if charSize == 0:
                    # standard size character
                    print("Resize so that max dimension is 256")
                # Convert to PNG8
                layer = convertIndexed(image, 256)
                print("Export as png to 'PS2' folder")
                # Color mode back to RGB
                pdb.gimp_image_convert_rgb(image)
                print("resize to half size")
                # Convert to PNG8
                layer = convertIndexed(image, 256)
                # Check which format is being used for PSP
                if PSPFormat == 0:
                    # Use PNG4 for PSP
                    print("Export as png to 'GameCube' folder")
                    # Color mode back to RGB
                    pdb.gimp_image_convert_rgb(image)
                    # Convert to PNG4
                    layer = convertIndexed(image, 16)
                    print("Export as png to 'PSP' folder")
                else:
                    # use PNG8 for PSP
                    print("Export as png to 'GameCube and PSP' folder")
            else:
                # Alchemy 5
                print("export as BGR DXT1 to 'Wii and MUA1 PC' folder")
                # Check if the character is oversized or standard
                if charSize == 0:
                    # standard size character
                    print("Resize so that max dimension is 256")
                # Convert to PNG8
                layer = convertIndexed(image, 256)
                print("Export as png to 'PS2' folder")
                # Color mode back to RGB
                pdb.gimp_image_convert_rgb(image)
                print("resize to half size")
                # Check which format is being used for PSP
                if PSPFormat == 0:
                    # Use PNG4 for PSP
                    # Convert to PNG4
                    layer = convertIndexed(image, 16)
                else:
                    # use PNG8 for PSP
                    # Convert to PNG8
                    layer = convertIndexed(image, 256)
                print("Export as png to 'PSP' folder")
    else: 
        # The original texture is 256x256 or less for primary textures or 128x128 for secondary textures
        # Choose the console
        if console == 1:
            # PC only
            # Alchemy version doesn't matter
            # Convert to PNG8
            layer = convertIndexed(image, 256)
            print("export as png to 'PC' folder")
        else:
            # All consoles
            # Pick the version of Alchemy
            if alchemyVersion == 0:
                # Alchemy 2.5
                print("Export as RGB DXT1 to 'Wii' folder")
                # Convert to PNG8
                layer = convertIndexed(image, 256)
                # Check if it is a primary or secondary skin
                if skinType == 0:
                    # Primary skin
                    print("Export as png to 'PC, PS2, and Xbox' folder")
                    # Color mode back to RGB
                    pdb.gimp_image_convert_rgb(image)
                    print("resize to half size")
                    # Convert to PNG8
                    layer = convertIndexed(image, 256)
                    # Check the texture format used by PSP
                    if PSPFormat == 1:
                        # PSP uses PNG8 format
                        print("Export as png to 'GameCube and PSP' folder")
                    else:
                        # PSP uses PNG4 format
                        print("Export as png to 'GameCube' folder")
                        # Color mode back to RGB
                        pdb.gimp_image_convert_rgb(image)
                        # Convert to PNG4
                        layer = convertIndexed(image, 16)
                        print("Export as png to 'PSP' folder")
                else:
                    # secondary skin
                    print("Export as png to 'PC and Xbox' folder")
                    # Color mode back to RGB
                    pdb.gimp_image_convert_rgb(image)
                    print("resize to half size")
                    # Convert to PNG8
                    layer = convertIndexed(image, 256)
                    print("export as png to 'PS2' folder")
                    # Color mode back to RGB
                    pdb.gimp_image_convert_rgb(image)
                    print("resize to half size")
                    # Convert to PNG8
                    layer = convertIndexed(image, 256)
                    # Check the texture format used by PSP
                    if PSPFormat == 1:
                        # PSP uses PNG8 format
                        print("Export as png to 'GameCube and PSP' folder")
                    else:
                        # PSP uses PNG4 format
                        print("Export as png to 'GameCube' folder")
                        # Color mode back to RGB
                        pdb.gimp_image_convert_rgb(image)
                        # Convert to PNG4
                        layer = convertIndexed(image, 16)
                        print("Export as png to 'PSP' folder")
            else:
                # Alchemy 5
                print("Export as RGB DXT1 to 'Wii' folder")
                # Check if it is a primary or secondary skin
                if skinType == 0:
                    # Primary skin
                    # Convert to PNG8
                    layer = convertIndexed(image, 256)
                    print("Export as png to 'PS2' folder")
                    # Color mode back to RGB
                    pdb.gimp_image_convert_rgb(image)
                    print("resize to half size")
                    # Check the texture format used by PSP
                    if PSPFormat == 1:
                        # PSP uses PNG8 format
                        # Convert to PNG8
                        layer = convertIndexed(image, 256)
                        print("Export as png to 'PSP' folder")
                    else:
                        # PSP uses PNG4 format
                        # Convert to PNG4
                        layer = convertIndexed(image, 16)
                        print("Export as png to 'PSP' folder")
                else:
                    # secondary skin
                    # Color mode back to RGB
                    pdb.gimp_image_convert_rgb(image)
                    print("resize to half size")
                    # Convert to PNG8
                    layer = convertIndexed(image, 256)
                    print("export as png to 'PS2' folder")
                    # Color mode back to RGB
                    pdb.gimp_image_convert_rgb(image)
                    print("resize to half size")
                    # Check the texture format used by PSP
                    if PSPFormat == 1:
                        # PSP uses PNG8 format
                        # Convert to PNG8
                        layer = convertIndexed(image, 256)
                        print("Export as png to 'PSP' folder")
                    else:
                        # PSP uses PNG4 format
                        # Convert to PNG4
                        layer = convertIndexed(image, 16)
                        print("Export as png to 'PSP' folder")
    # End the undo group
    pdb.gimp_image_undo_group_end(image)
    
    
    # Extra Stuff
    # Get the name of the export folder, check if it exists, and create it if it doesn't
        # outFolder = folderCheck(dirname, "PNG8")
    # Convert to PNG8
        # layer = convertPNG8(image)
    # Get the new file name
        # outFileName = fileName[0:-3] + "png"
    # Get the full save file path
        # outFilePath = os.path.join(outFolder, outFileName)
    # Export the image
        # pdb.file_png_save(image, layer, outFilePath, outFilePath, 0, 9, 0, 0, 0, 0, 0)

# ######## #
# REGISTER #
# ######## #
# Register the script in GIMP
register(
    "python_fu_marvelmods_export_skin",
    "Exports a skin texture in multiple formats.",
    "Exports a skin texture in multiple formats.",
    "BaconWizard17",
    "BaconWizard17",
    "January 2023",
    "Export Skin",
    "*",
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, 'drawable', 'Layer, mask or channel', None),
        (PF_OPTION,"p1","Console?:", 0, ["All","PC Only"]),
        (PF_OPTION,"p1","Skin Type?:", 0, ["Primary Skin","Secondary Skin"]),
        (PF_OPTION,"p1","Texture Type?:", 0, ["Primary Texture","Secondary Texture"]),
        (PF_OPTION,"p1","Character Size?:", 0, ["Standard","Large"]),
        (PF_OPTION,"p1","Alchemy Version?:", 0, ["Alchemy 2.5","Alchemy 5"]),
        (PF_OPTION,"p1","PSP Texture Format?:", 1, ["PNG4","PNG8"])
    ],
    [],
    exportSkin,
    menu='<Image>/Marvel Mods/Export Textures/By Asset Type'
)


# ############## #
# MAIN EXECUTION #
# ############## #
main()