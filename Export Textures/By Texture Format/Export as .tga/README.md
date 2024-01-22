# Marvel Mods GIMP Plugins
by BaconWizard17
## Export to .tga
This plugin exports a texture as a .tga file. This script should only be used to export textures that are being used with the [Alchemy 5 Texture Replacement Method](https://marvelmods.com/forum/index.php/topic,11009.0.html). TGA textures do not work well in the 3ds Max exporters, and other formats are recommended.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The dimensions of the image must be powers of 2.

### Installation
 1. This script can be installed using `runUpdateAdmin.bat` from my scripts, or it can be placed individually in your GIMP plugins directory. The standard location for this is `C:\Users\(your user)\AppData\Roaming\GIMP\2.10\plug-ins`. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Texture Format` and choose the `Export as .tga` plugin.
3. A dialog will appear with options. You can toggle the following options:
	- **Flatten Image?**: Select if you want the image to be flattened. Flattening the image collapses the layers and removes transparency. Select `No` if the texture needs transparency (such as a normal map or anything that needs a transparent area). Select `Yes` for all other textures.
4. The .xcf will be saved and several additional operations will be run while the texture is being exported. The file will be exported as a .png to a `TGA` folder in the same location as the .xcf file. 
5. This script creates duplicate images to export, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Credits
- BaconWizard17: Script creation