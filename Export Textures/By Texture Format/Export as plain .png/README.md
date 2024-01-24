# Marvel Mods GIMP Plugins
by BaconWizard17
## Export to plain .png
This plugin exports a texture as a .png file with no compression. This script should only be used to export textures that require transparency. If the texture does not need transparency, the model will appear incorrectly in the game. This format also produces the largest file size. Necessary post-processing operations are required to allow proper transparency in-game.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The dimensions of the image must be powers of 2.

### Installation
 1. This script can be installed using `runUpdateAdmin.bat` from my scripts, or it can be placed individually in your GIMP plugins directory. The standard location for this is `C:\Users\(your user)\AppData\Roaming\GIMP\2.10\plug-ins`. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Texture Format` and choose the `Export as plain .png` plugin.
3. The .xcf will be saved and several additional operations will be run while the texture is being exported. The file will be exported as a .png to a `Plain PNG` folder in the same location as the .xcf file. See the section below called "Export Compatibility" for information on what consoles will support which format.
4. This script creates duplicate images to export, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

### Export Compatibility
- All consoles

## Credits
- BaconWizard17: Script creation