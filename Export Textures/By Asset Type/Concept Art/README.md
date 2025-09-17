# Marvel Mods GIMP Plugins
by BaconWizard17

## Export Concept Art
This plugin exports a concept art texture.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The following texture sizes are supported:
- 4:3 aspect ratio:
   - 683 x 512: Console resolution
   - 1365 x 1024: Standard (SD) resolution
   - 2731 x 2048: HD resolution
- 16:9 aspect ratio:
   - 910 x 512: Console resolution
   - 1820 x 1024: Standard (SD) resolution
   - 3641 x 2048: HD resolution
My templates are recommended for use, as they are the correct dimensions. For more information, see the "Image Setup" section, below.

### Installation
1. This script can be installed using `update.bat` from the main folder of this release. Check the main `README.md` file in this project for more details on proper installation.

### Image Setup
In order for the script to work correctly, the image must use one of the recognized sizes (see "Compatibility", above). The script will automatically detect the aspect ratio from the size. 4:3 concept art textures are used with XML1 and XML2 (except PSP), and 16:9 concept art textures are used with XML2 PSP and MUA1. MUA2 does not use concept art. For 16:9 concept art textures, if a vertical guide is placed on the image, the concept art can also be cropped to 4:3; this allows you to create both 16:9 and 4:3 concept art textures from the same image. The vertical guide will act as the left edge of the 4:3 image. Its minimum X position is 0; the maximum X position is 227 for console resolution, 455 for SD resolution, and 910 for HD resolution. Only one guide should be placed in the image; otherwise, the script may be confused and perform incorrectly.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Concept Art` plugin.
3. You will be presented with the following option:
	- **Alchemy Version**: Select which version of Alchemy you're using. `Alchemy 2.5` will export the textures to be set up in 3ds Max 5 with the Alchemy 2.5 plugin. `Alchemy 5` will export the textures to be set up in 3ds Max 10-12 with the Alchemy 5 plugin. `Alchemy 5 (Texture Replacement)` will export the textures in .tga format to use with the Alchemy 5 texture creation tools.
4. If the file is not set up properly, you will receive an error with explanations. Otherwise, it will move on. The script will detect the size and aspect ratio automatically, as well as if there's a vertical guide to use to crop the 16:9 texture to 4:3.
5. The .xcf will be saved and several additional operations will be run while the texture is being exported. A single plain .png texture will be exported for each aspect ratio (as applicable).
6. This script creates duplicate images to export, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Credits
- BaconWizard17: Script creation