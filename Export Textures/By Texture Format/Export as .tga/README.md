# Marvel Mods GIMP Plugins
by BaconWizard17

## Export as .tga
This plugin exports a texture as a .tga file. This script should only be used to export textures that are being used with the [Alchemy 5 Texture Replacement Method](https://marvelmods.com/forum/index.php/topic,11009.0.html). TGA textures do not work well in the 3ds Max exporters, and other formats are recommended.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The dimensions of the image must be powers of 2.

### Installation
1. This script can be installed using `update.bat` from the main folder of this release. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Texture Format` and choose the `Export as .tga` plugin.
3. This script runs without any options.
4. If the file is not set up properly, you will receive an error with explanations. Otherwise, it will move on.
5. The .xcf will be saved and several additional operations will be run while the texture is being exported. A single .tga texture will be exported. 
6. This script runs all processes in the background, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Credits
- BaconWizard17: Script creation