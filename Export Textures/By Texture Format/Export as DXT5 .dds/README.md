# Marvel Mods GIMP Plugins
by BaconWizard17

## Export as DXT5 .dds
This plugin exports a texture as a .dds file with DXT5 compression.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The dimensions of the image must be powers of 2.

### Installation
1. This script can be installed using `update.bat` from the main folder of this release. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Texture Format` and choose the `Export as DXT5 .dds` plugin.
3. A dialog will appear with options. You can toggle the following options:
	- **Export in RGB?**: Select if you want the texture to be exported with its original RGB colors.
	- **Export RGB-BGR Swapped?**: Select if you want the texture to be exported the colors RGB-BGR-swapped. This is only necessary if you're using Alchemy 2.5 and creating the asset for next-gen MUA1 (PC, Steam, PS3, or Xbox 360).
    - **Preserve Transparency**:
	  - `Yes`: Choose if your texture needs to maintain transparency. This will keep the alpha channel on export.
	  - `No`: Choose if your texture should not have any transparency. This will flatten the image, removing the alpha channel.
4. If the file is not set up properly, you will receive an error with explanations. Otherwise, it will move on.
5. The .xcf will be saved and several additional operations will be run while the texture is being exported. The necessary .dds textures with DXT5 compression will be exported. 
6. This script runs all processes in the background, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Credits
- BaconWizard17: Script creation