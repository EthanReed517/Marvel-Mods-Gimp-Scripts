# Marvel Mods GIMP Plugins
by BaconWizard17
## Export to DXT1 .dds
This plugin exports a texture as a .dds file with DXT1 compression.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The dimensions of the image must be powers of 2.

### Installation
 1. This script can be installed using `update.bat` from the main folder of this release, or it can be placed individually in your GIMP plugins directory. The standard location for this is `C:\Users\(your user)\AppData\Roaming\GIMP\2.10\plug-ins`. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Texture Format` and choose the `Export as DXT1 .dds` plugin.
3. A dialog will appear with options. You can toggle the following options:
	- **Alchemy Version**: Select the version of Alchemy being used. Select `Alchemy 2.5` if you're creating models in 3ds Max 5 with the Alchemy 2.5 export plugin. Select `Alchemy 5` if you're creating models in 3ds Max 10 or 12 with the Alchemy 5 export plugin. 
	- **Export in RGB?**: Select if you want the texture to be exported with its original RGB colors.
	- **Export RGB-BGR Swapped?**: Select if you want the texture to be exported the colors RGB-BGR-swapped. This is only necessary if you're using Alchemy 2.5 and creating the asset for next-gen MUA1 (PC, Steam, PS3, or Xbox 360).
4. If the file is not set up properly, you will receive an error with explanations. Otherwise, it will move on.
5. The .xcf will be saved and several additional operations will be run while the texture is being exported. If `Yes` was selected for **Export in RGB?**, the texture will be exported to a folder called `DXT1 RGB`. If `Yes` was selected for **Export RGB-BGR Swapped?** and `Alchemy 2.5` was selected for **Alchemy Version**, the texture will be exported to a folder called `DXT1 BGR`. See the section below called "Export Compatibility" for information on what consoles will support which format.
6. This script creates duplicate images to export, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

### Export Compatibility
 - Alchemy 2.5:
	- RGB version: GameCube, Wii, Xbox, XML2 PC
	- BGR version: Next-Gen MUA1 (PC, Steam, PS3, Xbox 360)
 - Alchemy 5:
    - RGB version: Wii, Next-Gen MUA1 (PC, Steam, PS3, Xbox 360)

## Credits
- BaconWizard17: Script creation