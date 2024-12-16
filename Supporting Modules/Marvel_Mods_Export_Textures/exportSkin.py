#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ########### #
# INFORMATION #
# ########### #
# GIMP plugin to export a skin, 3D head, or mannequin texture.
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


# ######### #
# FUNCTIONS #
# ######### #
# Define the size checking operation
def sizeCheck(currentWidth, currentHeight):
    # compare the criteria to the current texture size
    if (currentWidth > 256) or (currentHeight > 256):
        oversized = True
    else:
        oversized = False
    return oversized

# Define the function for resizing to the max size for PNG8
def getMaxPS2Size(image, skinType, primary):
    # Determine the max size based on the texture type
    if primary == True:
        # Primary texture
        if skinType == 0:
            # primary skin
            maxSize = 256
        else:
            # secondary skin
            maxSize = 128
    else:
        # Primary texture
        if skinType == 0:
            # primary skin
            maxSize = 128
        else:
            # secondary skin
            maxSize = 64
    # Get the current dimensions of the image
    currentWidth = float(image.width)
    currentHeight = float(image.height)
    # Check which is bigger
    if currentWidth >= currentHeight:
        # Wide image or square
        scaleFactor = maxSize / currentWidth
    else:
        # Tall image
        scaleFactor = maxSize / currentHeight
    # Return the scale factor
    return scaleFactor

# Define the main operation
def exportSkin(image, layer, console, skinType, charSize, alchemyVersion, transparency, pspFormat, primary, **kwargs):
    # Perform the initial operations
    (okayToExport, xcfPath) = MMBGP.initialOps(image, layer)
    # Determine if it's okay to proceed
    if okayToExport == True:
        # No errors, can proceed
        # Determine if the image is oversized
        if primary == True:
            oversized = sizeCheck(image.width, image.height)
        else:
            oversized = kwargs["primary_size"]
        # Determine if the image is oversized
        if oversized == True:
            # The image is oversized
            # Determine the console
            if console == 1:
                # PC Only
                # Determine if the image needs transparency
                if transparency == 0:
                    # The image is transparent
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for PC and MUA1 Steam
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="PC and MUA1 Steam")
                    else:
                        # Alchemy 5
                        # Export for MUA1 PC and Steam
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", transparent=True, subFolder="MUA1 PC and Steam", ddsCompression="DXT5")
                else:
                    # The image is not transparent
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for XML2 PC
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", transparent=True, subFolder="XML2 PC")
                        # Export for MUA1 PC and Steam
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", transparent=True, RGB_BGR=True, subFolder="MUA1 PC and Steam")
                    else:
                        # Alchemy 5
                        # Export for MUA1 PC and Steam
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", transparent=True, subFolder="MUA1 PC and Steam")
            else:
                # All consoles
                # Determine if the image needs transparency
                if transparency == 0:
                    # The image is transparent
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Determine the character size
                        if charSize == 0:
                            # Standard size character
                            # Export for many consoles
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="PC, Wii, Xbox, MUA1 Steam, PS3, and 360")
                            # Reduce to the max size for PS2 per the parameters
                            scaleFactor = getMaxPS2Size(image, skinType)
                            # Export for PS2
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=scaleFactor, subFolder="PS2")
                        else:
                            # Big character
                            # No scale factor is needed
                            scaleFactor = 1
                            # Export for many consoles
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="PC, PS2, Wii, Xbox, MUA1 Steam, PS3, and 360")
                        # Set the scale factor to half the size
                        scaleFactor = scaleFactor * 0.5
                        # Export for GameCube, PSP, and MUA2 PS2
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=scaleFactor, subFolder="GameCube, PSP, and MUA2 PS2")
                    else:
                        # Alchemy 5
                        # Export for Wii
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="Wii")
                        # Export for MUA1 PC, Steam, PS3, and 360
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", transparent=True, subFolder="MUA1 PC, Steam, PS3, and 360", ddsCompression="DXT5")
                        # Determine the character size
                        if charSize == 0:
                            # Standard size character
                            # Reduce to the max size for PS2 per the parameters, times 0.5 for the smaller consoles
                            scaleFactor = getMaxPS2Size(image, skinType) * 0.5
                        else:
                            # The small consoles need the texture to be half size
                            scaleFactor = 0.5
                        # Export for PSP, and MUA2 PS2
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=scaleFactor, subFolder="PSP and MUA2 PS2")
                else:
                    # The image is not transparent
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export the main textures
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="Wii, Xbox, and XML2 PC")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 PC, Steam, PS3, and 360")
                        # Determine the character size
                        if charSize == 0:
                            # Standard size character
                            # Reduce to the max size for PS2 per the parameters
                            scaleFactor = getMaxPS2Size(image, skinType)
                        else:
                            # Big character
                            # No scale factor is needed
                            scaleFactor = 1
                        # Export for PS2
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, scale_factor=scaleFactor, subFolder="PS2")
                        # Resize to half size
                        scaleFactor = scaleFactor * 0.5
                        # Determine the PSP format
                        if pspFormat == 0:
                            # PNG4
                            # Export for PSP
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=16, scale_factor=scaleFactor, subFolder="PSP")
                            # Export for GameCube and MUA2 PS2
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, scale_factor=scaleFactor, subFolder="GameCube and MUA2 PS2")
                        else:
                            # PNG8
                            # Export for GameCube, PSP, and MUA2 PS2
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, scale_factor=scaleFactor, subFolder="GameCube, PSP, and MUA2 PS2")
                    else:
                        # Alchemy 5
                        # Export for Wii and next-gen MUA1
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="Wii, MUA1 PC, Steam, PS3, and 360")
                        # Determine the character size
                        if charSize == 0:
                            # Standard size character
                            # Reduce to the max size for PS2 per the parameters
                            scaleFactor = getMaxPS2Size(image, skinType)
                        else:
                            # Big character
                            # No scale factor is needed
                            scaleFactor = 1
                        # Resize to half size
                        scaleFactor = scaleFactor * 0.5
                        # Determine the PSP format
                        if pspFormat == 0:
                            # PNG4
                            # Export for PSP
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=16, scale_factor=scaleFactor, subFolder="PSP")
                            # Export for GameCube and MUA2 PS2
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, scale_factor=scaleFactor, subFolder="MUA2 PS2")
                        else:
                            # PNG8
                            # Export for GameCube, PSP, and MUA2 PS2
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, scale_factor=scaleFactor, subFolder="PSP and MUA2 PS2")
        else:
            # The image is not oversized
            # Determine the console
            if console == 1:
                # PC Only
                # Determine if the image needs transparency
                if transparency == 0:
                    # The image is transparent
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for PC and Steam
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="PC and MUA1 Steam")
                    else:
                        # Alchemy 5
                        # Export for PC and Steam
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="MUA1 PC")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", transparent=True, subFolder="MUA1 Steam", ddsCompression="DXT5")
                else:
                    # The image is not transparent
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for PC and Steam
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder="PC")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 Steam")
                    else:
                        # Alchemy 5
                        # Export for PC
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder="MUA1 PC")
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="MUA1 Steam")
            else:
                # All consoles
                # Determine if the image needs transparency
                if transparency == 0:
                    # The image is transparent
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Determine the skin type
                        if skinType == 0:
                            # Primary skin
                            # No scale factor is needed
                            scaleFactor = 1
                            # Export for main consoles
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="PC, PS2, Xbox, Wii, MUA1 Steam, PS3, and 360")
                        else:
                            # Secondary skin
                            # Export for main consoles (not PS2)
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="PC, Xbox, Wii, MUA1 Steam, PS3, and 360")
                            # Resize to half size
                            scaleFactor = 0.5
                            # Export for PS2
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=scaleFactor, subFolder="PS2")
                        # Halve the scalefactor again
                        scaleFactor = scaleFactor * 0.5
                        # Export for GameCube, PSP, and MUA2 PS2
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=scaleFactor, subFolder="GameCube, PSP, and MUA2 PS2")
                    else:
                        # Alchemy 5
                        # Export for Wii, PC, and 360
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, subFolder="Wii, MUA1 PC and 360")
                        # Export for Steam
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", transparent=True, subFolder="MUA1 Steam and PS3", ddsCompression="DXT5")
                        # Determine the skin type
                        if skinType == 0:
                            # Primary skin
                            # Resize to half size
                            scaleFactor = 0.5
                        else:
                            # Secondary skin
                            # Resize to quarter size
                            scaleFactor = 0.25
                        # Export for GameCube, PSP, and MUA2 PS2
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", transparent=True, scale_factor=scaleFactor, subFolder="GameCube, PSP, and MUA2 PS2")
                else:
                    # The image is not transparent
                    # Determine the Alchemy version
                    if alchemyVersion == 0:
                        # Alchemy 2.5
                        # Export for Wii
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="Wii")
                        # Export for Steam and PS3
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", RGB_BGR=True, subFolder="MUA1 Steam and PS3")
                        # Determine if this is a primary or secondary skin
                        if skinType == 0:
                            # Primary
                            # Export for PC, PS2, Xbox, and MUA1 360
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder="PC, PS2, Xbox, and MUA1 360")
                            # No scale factor is needed
                            scaleFactor = 1
                        else:
                            # Secondary
                            # Export for PC, Xbox, and MUA1 360
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder="PC, Xbox, and MUA1 360")
                            # Resize to half size
                            scaleFactor = 0.5
                            # Export for PS2
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=scaleFactor, indexColors=256, subFolder="PS2")
                        # Resize to half size
                        scaleFactor = scaleFactor * 0.5
                        # Determine the PSP format
                        if pspFormat == 0:
                            # PNG4
                            # Export for PSP
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=scaleFactor, indexColors=16, subFolder="PSP")
                            # Export for GameCube and MUA2 PS2
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=scaleFactor, indexColors=256, subFolder="GameCube and MUA2 PS2")
                        else:
                            # PNG8
                            # Export for GameCube, PSP, and MUA2 PS2
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=scaleFactor, indexColors=256, subFolder="GameCube, PSP, and MUA2 PS2")
                    else:
                        # Alchemy 5
                        # Export for PC
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".png", indexColors=256, subFolder="MUA1 PC and 360")
                        # Export for Steam
                        MMBGP.exportTextureMM(image, layer, xcfPath, ".dds", subFolder="Wii, MUA1 Steam and PS3")
                        # Determine the skin type
                        if skinType == 0:
                            # Primary skin
                            # Resize to half size
                            scaleFactor = 0.5
                        else:
                            # Secondary skin
                            # Resize to quarter size
                            scaleFactor = 0.25
                        # Determine the PSP format
                        if pspFormat == 0:
                            # PNG4
                            # Export for PSP
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=scaleFactor, indexColors=16, subFolder="PSP")
                            # Export for GameCube and MUA2 PS2
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=scaleFactor, indexColors=256, subFolder="MUA2 PS2")
                        else:
                            # PNG8
                            # Export for GameCube, PSP, and MUA2 PS2
                            MMBGP.exportTextureMM(image, layer, xcfPath, ".png", scale_factor=scaleFactor, indexColors=256, subFolder="PSP and MUA2 PS2")
        # Print the success message
        pdb.gimp_message("SUCCESS: exported " + xcfPath)