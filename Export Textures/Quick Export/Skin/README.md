# Marvel Mods GIMP Plugins
by BaconWizard17
## Quick Export - Export Skin
This is a quick version of my `Export Skin` plugin that runs without a dialog and uses my preferred settings. This plugin exports a skin texture in several optimized formats. 

The following values are selected:
 - **Console**: `All`
 - **Skin Type**: `Primary`
 - **Texture Type**: `Primary`
 - **Character Size**: `Standard`
 - **Alchemy Version**: `Alchemy 2.5`
 - **Transparency**: `No`
 - **PSP Texture Compression**: `PNG8` 
For more information on these settings, see the "Export Skin" plugin. 

This plugin contains all functionality of the full version, so the hard-coded settings can be changed by editing the `.py` file.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The texture can be for a skin, 3D head, or mannequin.

### Installation
 1. This script can be installed using `runUpdateAdmin.bat` from my scripts, or it can be placed individually in your GIMP plugins directory. The standard location for this is `C:\Users\(your user)\AppData\Roaming\GIMP\2.10\plug-ins`. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/Quick Exporters` and choose the `Export Skin` plugin.
3. If one or both of the image dimensions is not a power of 2, you will get an error warning as such, and the process will be aborted. Alchemy only supports images whose dimensions are powers of 2.
4. The .xcf will be saved and several additional operations will be run while the texture is being exported to the various folders in different formats. The operations will depend on the options selected. Textures that are the same will be grouped together. See below for a list of the texture types that will be exported for each console. 
5. This script creates duplicate images to export, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Export Types
See the "Export Skin" plugin for more information

## Credits
- BaconWizard17: Script creation