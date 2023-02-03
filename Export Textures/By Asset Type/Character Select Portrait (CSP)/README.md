# Marvel Mods GIMP Plugins
by BaconWizard17
## Export Character Select Portrait (HUD)
This plugin exports a character select portrait (CSP) texture in several optimized formats.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The texture should be square.

### Installation
 1. This script can be installed using `runUpdateAdmin.bat` from my scripts, or it can be placed individually in your GIMP plugins directory. The standard location for this is `C:\Users\(your user)\AppData\Roaming\GIMP\2.10\plug-ins`. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Export Conversation Portrait (HUD)` plugin.
3. You will be presented with a series of options:
	- **Console**: Select which console you will be using. `All` will export to all available consoles based on later suggestions, while `PC Only` will export textures for PC only
	- **Game**: Select which game you will be using. `XML1` will export the texture for GameCube, PS2, and Xbox (but will export nothing if `PC Only` is selected for **Console**). `XML2` will export the texture for PC, GameCube, PS2, PSP, and Xbox (depending on the selection for **Console**).
4. The .xcf will be saved, the image will be flattened, and several additional operations will be run while the texture is being exported to the various folders in different formats. The operations will depend on the options selected. Textures that are the same will be grouped together. See below for a list of the texture types that will be exported for each console. 
5. All the steps are part of one undo group and can be undone with Ctrl+Z. Use this after running the script to return to the original state of the image and edit it further, if needed.

## Export Types
 - **PC**: The texture format will depend on the size of the image. If the texture is over 128x128, it will export as an RGB DXT1 .dds texture. If the texture is 128x128 or smaller, it will export as a PNG8 texture. 
 - **GameCube**: The texture will export as a 128x128 PNG8 texture. 
 - **PS2**: The texture will export as a 128x128 PNG8 texture. 
 - **PSP**: The texture will export as a 64x64 PNG8 texture. 
 - **Xbox**: The texture will export as a 128x128 PNG8 texture. 

## Credits
- BaconWizard17: Script creation