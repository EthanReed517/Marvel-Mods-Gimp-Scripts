# Marvel Mods GIMP Plugins
by BaconWizard17

## Export Comic Cover
This plugin creates comic cover textures from an image of a comic cover and exports them. It supports XML1, XML2, and MUA1 comic covers.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The image should be just the comic cover; it's not necessary to include the backgrounds, as they'll be automatically added from templates. The comic cover should be at least 885 pixels in height. The aspect ratio should be approximately 1.54 (height / width = 1.54). The script will still work if the aspect ratio or size isn't right, but the image may end up squished, stretched, or blurry.

### Installation
1. This script can be installed using `update.bat` from the main folder of this release. Check the main `README.md` file in this project for more details on proper installation.

### Usagex
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Export Comic Cover` plugin.
3. You will be presented with the following options:
	- **Alchemy Version**: Select which version of Alchemy you're using. `Alchemy 2.5` will export the textures to be set up in 3ds Max 5 with the Alchemy 2.5 plugin. `Alchemy 5` will export the textures to be set up in 3ds Max 10-12 with the Alchemy 5 plugin. `Alchemy 5 (Texture Replacement)` will export the textures in .tga format to use with the Alchemy 5 texture creation tools.
	- **Export a Comic Cover for XML1?**: Select if you want to export a comic cover for XML1.
	- **Export a Comic Cover for XML2?**: Select if you want to export a comic cover for XML2.
	- **Export a Comic Cover for MUA1?**: Select if you want to export a comic cover for MUA1.
4. The .xcf will be saved and several additional operations will be run while the texture is being exported. A single plain .png texture will be exported for each game.
5. This script creates duplicate images to export, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Credits
- BaconWizard17: Script creation