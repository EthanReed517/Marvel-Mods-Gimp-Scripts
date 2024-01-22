# Marvel Mods GIMP Plugins
by BaconWizard17
## Export to PNG8 .png
This plugin exports a texture to PNG8 format

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. 

### Installation
 1. This script can be installed using `runUpdateAdmin.bat` from my scripts, or it can be placed individually in your GIMP plugins directory. The standard location for this is `C:\Users\(your user)\AppData\Roaming\GIMP\2.10\plug-ins`. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Texture Format` and choose the `Export as PNG8 .png` plugin.
3. The .xcf will be saved, and then the image will be flattened, indexed to 256 colors, and then exported as a .png to a `PNG8` folder in the same location as the .xcf file.
4. All the steps are part of one undo group and can be undone with Ctrl+Z. Use this after running the script to return to the original state of the image and edit it further, if needed.

## Credits
- BaconWizard17: Script creation