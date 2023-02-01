# Marvel Mods GIMP Plugins
by BaconWizard17
## Export Conversation Portrait (HUD)
This plugin exports a conversation portrait (HUD) texture in several optimized formats.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The texture should be square.

### Installation
 1. This script can be installed using `runUpdateAdmin.bat` from my scripts, or it can be placed individually in your GIMP plugins directory. The standard location for this is `C:\Users\(your user)\AppData\Roaming\GIMP\2.10\plug-ins`. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Export Conversation Portrait (HUD)` plugin.
3. You will be presented with a series of options:
	- **Console**: Select which console you will be using. `All` will export to all available consoles based on later suggestions, while `PC Only` will export textures for PC only
	- **Outline Type**: Select what the outline type is. A `Hero Outline` will export the normal way. A `Villain Outline` will export with `vil_` at the start of the file name. This is for cases where there are variants of the same portrait with different color outlines for hero and villain versions.
4. The .xcf will be saved, the image will be flattened, and several additional operations will be run while the texture is being exported to the various folders in different formats. The operations will depend on the options selected. Textures that are the same will be grouped together. See below for a list of the texture types that will be exported for each console. 
5. All the steps are part of one undo group and can be undone with Ctrl+Z. Use this after running the script to return to the original state of the image and edit it further, if needed.

## Export Types
 - **MUA1 PC**: The texture format will depend on the size of the image. If the texture is over 128x128, it will export as an RGB-BGR swapped DXT1 .dds texture. If the texture is 128x128 or smaller, it will export as a PNG8 texture. 
 - **XML2 PC**: The texture format will depend on the size of the image. If the texture is over 128x128, it will export as an RGB DXT1 .dds texture. If the texture is 128x128 or smaller, it will export as a PNG8 texture. 
 - **GameCube**: The texture will export as a 128x128 PNG8 texture. 
 - **PS2**: The texture will export as a 128x128 PNG8 texture. 
 - **PSP**: The texture will export as a 64x64 PNG8 texture. 
 - **Wii**: The texture will export as a 128x128 RGB DXT1 .dds texture.
 - **Xbox**: The texture will export as a 128x128 PNG8 texture. 

## Credits
- BaconWizard17: Script creation