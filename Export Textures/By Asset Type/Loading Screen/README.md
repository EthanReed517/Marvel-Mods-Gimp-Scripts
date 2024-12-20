# Marvel Mods GIMP Plugins
by BaconWizard17
## Export Loading Screen
This plugin exports a loading screen texture in several optimized formats.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The following texture sizes are supported:
- 4:3 aspect ratio:
   - 683 x 512: Console resolution
   - 1365 x 1024: Standard (SD) resolution
   - 2731 x 2048: HD resolution
- 16:9 aspect ratio:
   - 910 x 512: Console resolution
   - 1820 x 1024: Standard (SD) resolution
   - 3641 x 2048: HD resolution
My templates are recommended for use, as they are the correct dimensions. For more information, see the "Image Setup" section, below.

### Installation
 1. This script can be installed using `update.bat` from the main folder of this release. Check the main `README.md` file in this project for more details on proper installation.

### Image Setup
In order for the script to work correctly, the image must use one of the recognized sizes (see "Compatibility", above). The script will automatically detect the aspect ratio from the size. 4:3 loading screens are used with XML1 and XML2 (except PSP), and 16:9 loading screens are used with XML2 PSP, MUA1, and MUA2. For 16:9 loading screens, if a vertical guide is placed on the image, the loading screen can also be cropped to 4:3; this allows you to create both 16:9 and 4:3 loading screens from the same image. The vertical guide will act as the left edge of the 4:3 image. Its minimum X position is 0; the maximum X position is 227 for console resolution, 455 for SD resolution, and 910 for HD resolution. Only one guide should be placed in the image; otherwise, the script may be confused and perform incorrectly.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Loading Screen` plugin.
3. You will be presented with a series of options:
	- **Console**: Select which console you will be using. `All` will export to all available consoles based on later suggestions, while `PC Only` will export textures for PC only.
	- **Alchemy Version**: Select the version of Alchemy being used. Select `Alchemy 2.5` if you're exporting portraits in 3ds Max 5 with the Alchemy 2.5 export plugin. Select `Alchemy 5` if you're creating CSPs with the [Alchemy 5 Texture Replacement Method](https://marvelmods.com/forum/index.php/topic,11009.0.html).
4. If the file is not set up properly, you will receive an error with explanations. Otherwise, it will move on. The script will detect the size and aspect ratio automatically, as well as if there's a vertical guide to use to crop the 16:9 texture to 4:3.
5. The .xcf will be saved and several additional operations will be run while the texture is being exported to the various folders in different formats. The operations will depend on the options selected. Textures that are the same will be grouped together. See below for a list of the texture types that will be exported for each console. 
6. This script creates duplicate images to export, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Export Types
- **XML1**:
   - **GameCube**: 4:3 DXT1 .dds texture squished to 1:1 with a max size of 512 x 512.
   - **PS2**: 4:3 PNG8 .png texture squished to 1:1 with a max size of 512 x 512.
   - **Xbox**: 4:3 DXT1 .dds texture squished to 1:1 with a max size of 1024 x 1024.
   - If **Alchemy Version** is set to `Alchemy 5`, XML1 textures will not be exported.
- **XML2**:
   - **PC**: 4:3 DXT1 .dds texture squished to 1:1 with a max size of 2048 x 2048.
   - **GameCube**: 4:3 DXT1 .dds texture squished to 1:1 with a max size of 512 x 512.
   - **PS2**: 4:3 PNG8 .png texture squished to 1:1 with a max size of 512 x 512.
   - **PSP**: 16:9 PNG8 .png texture scaled to 480 x 271 and placed on a 512 x 512 black image.
   - **Xbox**: 4:3 DXT1 .dds texture squished to 1:1 with a max size of 1024 x 1024.
   - If **Alchemy Version** is set to `Alchemy 5`, XML2 textures will not be exported, except for PSP, which will export as an uncompressed .tga texture.
- **MUA1**:
   - **PC**: 16:9 RGB-BGR swapped DXT1 .dds texture stretched to 2:1 with a max size of 4096 x 2048.
   - **Steam**: 16:9 RGB-BGR swapped DXT1 .dds texture stretched to 2:1 with a max size of 4096 x 2048.
   - **PS2**: 16:9 PNG8 .png texture squished to 1:1 with a max size of 512 x 512.
   - **PSP**: 16:9 PNG8 .png texture squished to 1:1 with a max size of 512 x 512.
   - **PS3**: 16:9 RGB-BGR swapped DXT1 .dds texture stretched to 2:1 with a max size of 2048 x 1024.
   - **Wii**: 16:9 DXT1 .dds texture squished to 1:1 with a max size of 1024 x 1024.
   - **Xbox**: 16:9 DXT1 .dds texture squished to 1:1 with a max size of 1024 x 1024.
   - **Xbox 360**: 16:9 RGB-BGR swapped DXT1 .dds texture stretched to 2:1 with a max size of 2048 x 1024.
   - If **Alchemy Version** is set to `Alchemy 5`, MUA1 PS2 and Xbox textures will not be exported, and all other textures will export as an uncompressed .tga textures.
- **MUA2**:
   - **PS2**: 16:9 PNG8 .png texture squished to 1:1 with a max size of 512 x 512.
   - **PSP**: 16:9 PNG8 .png texture squished to 1:1 with a max size of 512 x 512.
   - **Wii**: 16:9 DXT1 .dds texture squished to 1:1 with a max size of 1024 x 1024.
   - If **Alchemy Version** is set to `Alchemy 5`, all textures will export as an uncompressed .tga textures.

## Credits
- BaconWizard17: Script creation