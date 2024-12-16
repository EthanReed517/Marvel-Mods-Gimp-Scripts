# Marvel Mods GIMP Plugins
by BaconWizard17
## Export Power Icons
This plugin exports a power icons texture in several optimized formats. It supports XML1, XML2, MUA1, and MUA2 power icons. If you're using Alchemy 5, it's recommended to use the [Alchemy 5 Texture Replacement Method](https://marvelmods.com/forum/index.php/topic,11009.0.html) instead.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The texture should be square. Use one of the provided templates to get the correct size and layout for each game.

### Installation
 1. This script can be installed using `update.bat` from the main folder of this release. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Export Power Icons` plugin.
3. You will be presented with a series of options:
	- **Console**: Select which console you will be using. `All` will export to all available consoles based on later suggestions, while `PC Only` will export textures for PC only (including Steam for MUA1).
	- **Game**: Select which game you will be using. `XML1` will export the texture for the applicable version of XML1 (but will export nothing if `PC Only` is selected for **Console**). `XML2` will export the texture for the applicable version of XML2 . `MUA1` will export the textures for the applicable version of MUA1. `MUA2` will export the texture for the applicable version of MUA2 (but will export nothing if `PC Only` is selected for **Console**). 
4. The .xcf will be saved, the image will be flattened, and several additional operations will be run while the texture is being exported to the various folders in different formats. The operations will depend on the options selected. Textures that are the same will be grouped together. See below for a list of the texture types that will be exported for each console.
5. This script creates duplicate images to export, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Export Types
 - **XML1**: The texture will export as a 128x128 PNG8 image
 - **XML2**: The texture format and number of textures will depend on the size of the image. 
   - If the texture size is over 128x128, an **icons2** set will be exported. **icons2** sets are higher resolution icons that can be used in the character select screen for PC, PSP, and Xbox. The name of the exported texture will have the number 2 at the end. 
     - If the texture size is 512x512 or larger, the **icons2** set will export as a DXT1 .dds texture for PC and then scale down to 256x256 to export as a PNG8 texture for PSP and Xbox. 
	 - If the texture size is 256x256, the **icons2** set will export as a 256x256 PNG8 texture for PC, PSP, and Xbox. 
	 - Regardless of initial texture size, the texture will then be scaled to 128x128 and exported as a PNG8 for the **icons1** set for all consoles.
   - If the texture size is 128x128, only an **icons1** set will be exported. See above for details.
 - **MUA1**: A 256x256 plain PNG texture will be exported for the next-gen console versions. For the Xbox and Wii, a 128x128 plain PNG texture will be exported. For the PS2 and PSP, a 128x128 indexed-alpha PNG texture will be exported.
 - **MUA2**: For the Wii, a 128x128 plain PNG texture will be exported. For the PS2 and PSP, a 128x128 indexed-alpha PNG texture will be exported.

## Credits
- BaconWizard17: Script creation