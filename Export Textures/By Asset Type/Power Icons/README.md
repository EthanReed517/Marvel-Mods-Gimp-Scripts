# Marvel Mods GIMP Plugins
by BaconWizard17

## Export Power Icons
This plugin exports a power icons texture. It supports XML1, XML2, MUA1, and MUA2 power icons. 

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The texture should be square. Use one of the provided templates to get the correct size and layout for each game. For XML2, the script will automatically add a `1` or `2` to the end of the texture name depending on if the icon is suitable for use as an icons2 file. The .xcf file does not need to include a number at the end of the file name. 
- For example, Cyclops's icons would just need to be saved as `cyclops_icons.xcf`. The larger texture size will be exported as `cyclops_icons2.png`, and the smaller texture size will be exported as `cyclops_icons1.png`.

### Installation
1. This script can be installed using `update.bat` from the main folder of this release. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Export Power Icons` plugin.
3. You will be presented with a series of options:
	- **Game**: Select which game you will be using. `XML1` will export the texture for the applicable version of XML1 (but will export nothing if `PC Only` is selected for **Console**). `XML2` will export the texture for the applicable version of XML2 . `MUA1` will export the textures for the applicable version of MUA1. `MUA2` will export the texture for the applicable version of MUA2 (but will export nothing if `PC Only` is selected for **Console**). 
4. The .xcf will be saved, the image will be flattened, and several additional operations will be run while the texture is being exported to the various folders in different formats. The operations will depend on the options selected. Textures that are the same will be grouped together. See below for a list of the texture types that will be exported for each console.
5. This script creates duplicate images to export, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Credits
- BaconWizard17: Script creation