# Marvel Mods GIMP Plugins
by BaconWizard17
## Export Skin (Quick)
This is a quick version of my `Export Skin` plugint that runs without a dialog and uses my preferred settings. This plugin exports a skin texture in several optimized formats. It will run with the following options: all consoles, standard character size, primary skin, primary texture, Alchemy 2.5, and PNG8 format for the PSP. The plugin contains all functionality of the full version, so the hard-coded settings can be changed by editing the `.py` file.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The texture can be for a skin, 3D head, or mannequin.

### Installation
 1. This script can be installed using `runUpdateAdmin.bat` from my scripts, or it can be placed individually in your GIMP plugins directory. The standard location for this is `C:\Users\(your user)\AppData\Roaming\GIMP\2.10\plug-ins`. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Export Skin` plugin.
3. The .xcf will be saved, the image will be flattened, and several additional operations will be run while the texture is being exported to the various folders in different formats. The operations will depend on the options selected. Textures that are the same will be grouped together. See below for a list of the texture types that will be exported for each console. 
4. All the steps are part of one undo group and can be undone with Ctrl+Z. Use this after running the script to return to the original state of the image and edit it further, if needed.

## Export Types
 - **MUA1 PC**: Textures over 256x256 will export as RGB-BGR swapped DXT1 .dds textures. Otherwise, they will export as PNG8 textures.
 - **XML2 PC**: Textures over 256x256 will export as RGB DXT1 .dds textures. Otherwise, they will export as PNG8 textures.
 - **GameCube**: The texture will export as a PNG8 texture with half the size of the original texture (capped at 128x128).
 - **PS2**: The texture will export as a PNG8 texture with the same size as the original texture (capped at 256x256).
 - **PSP**: The texture will export as a PNG8 texture with half the size of the original texture (capped at 128x128).ed, the textures for PSP will be exported as PNG8 textures. 
 - **Wii**: The texture will export as an RGB DXT1 .dds texture with the same size as the original texture.
 - **Xbox**: Textures over 256x256 will export as RGB DXT1 .dds textures. Otherwise, they will export as PNG8 textures.

## Credits
- BaconWizard17: Script creation