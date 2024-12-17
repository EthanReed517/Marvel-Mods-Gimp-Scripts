# Marvel Mods GIMP Plugins
by BaconWizard17
## Export Comic Cover
This plugin creates comic cover textures from an image of a comic cover and exports them in several optimized formats. It supports XML1, XML2, and MUA1 comic covers.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The image should be just the comic cover; it's not necessary to include the backgrounds, as they'll be automatically added from templates. The comic cover should be at least 885 pixels in height. The aspect ratio should be approximately 1.54 (height / width = 1.54). The script will still work if the aspect ratio or size isn't right, but the image may end up squished, stretched, or blurry.

### Installation
 1. This script can be installed using `update.bat` from the main folder of this release. Check the main `README.md` file in this project for more details on proper installation.

### Usagex
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Export Comic Cover` plugin.
3. You will be presented with a series of options:
	- **Console**: Select which console you will be using. `All` will export to all available consoles based on later questions, while `PC Only` will export textures for PC only (including Steam for MUA1).
	- **Alchemy Version**: Select which version of Alchemy you're using. `Alchemy 2.5` will export the textures to be set up in 3ds Max 5 with the Alchemy 2.5 plugin. `Alchemy 5` will export the textures in .tga format to use with the Alchemy 5 texture creation tools.
	- **Export a Comic Cover for XML1?**: Select if you want to export a comic cover for XML1.
	- **Export a Comic Cover for XML2?**: Select if you want to export a comic cover for XML2.
	- **Export a Comic Cover for MUA1?**: Select if you want to export a comic cover for MUA1.
4. The .xcf will be saved and then several additional operations will be run while the texture is being exported to the various folders in different formats. The operations will depend on the options selected. Textures that are the same will be grouped together. See below for a list of the texture types that will be exported for each console.
5. This script creates duplicate images to export, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Export Types
 - If `Alchemy 5` is selected for **Alchemy Versions**, all textures will be uncompressed .tga images instead of what is listed below.
 - **XML1**:
   - Will not export if **Console** is set to `PC Only` or **Alchemy Version** is set to `Alchemy 5`.
   - **GameCube**: The texture will be a 512x512 DXT1 .dds texture.
   - **PS2**: The texture will be a 512x512 PNG8 .png texture.
   - **Xbox**: The texture will be a 1024x1024 DXT1 .dds texture.
 - **XML2**:
   - If **Console** is set to `PC Only`, only the PC version will export. If it is set to `All`, it will export for PC, GameCube, PS2, PSP, and Xbox.
   - If **Alchemy Version** is set to `Alchemy 2.5`, textures will be exported for all applicable versions of the game. If it is set to `Alchemy 5`, only the PSP will be exported.
   - **PC**: The texture will be a 1024x1024 DXT1 .dds texture.
   - **GameCube**: The texture will be a 512x512 DXT1 .dds texture.
   - **PS2**: The texture will be a 512x512 PNG8 .png texture.
   - **PSP**: The texture will be a 512x512 PNG8 .png texture. XML2 PSP uses 16:9 aspect ratio comic cover textures instead of 4:3 like the other versions of XML2.
   - **Xbox**: The texture will be a 1024x1024 DXT1 .dds texture.
 - **MUA1**: 
   - If **Console** is set to `PC Only`, only the PC and Steam version will export. If it is set to `All`, it will export for PC, Steam, PS2, PSP, PS3, Wii, Xbox, and Xbox 360.
   - If **Alchemy Version** is set to `Alchemy 2.5`, textures will be exported for all applicable versions of the game. If it is set to `Alchemy 5`, the PS2 and Xbox versions will not be exported.
   - **PC**: The texture will be a 2048x1024 RGB-BGR swapped DXT1 .dds texture.
   - **Steam**: The texture will be a 2048x1024 RGB-BGR swapped DXT1 .dds texture.
   - **PS2**: The texture will be a 512x512 PNG8 .png texture.
   - **PS3**: The texture will be a 2048x1024 RGB-BGR swapped DXT1 .dds texture.
   - **PSP**: The texture will be a 512x512 PNG8 .png texture.
   - **Wii**: The texture will be a 1024x1024 DXT1 .dds texture.
   - **Xbox**: The texture will be a 1024x1024 DXT1 .dds texture.
   - **Xbox 360**: The texture will be a 2048x1024 RGB-BGR swapped DXT1 .dds texture.

## Credits
- BaconWizard17: Script creation