# Marvel Mods GIMP Plugins
by BaconWizard17

## Export as PNG4 .png
This plugin exports a texture as a .png file with PNG4 compression (4-bit/16 colors).

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The dimensions of the image must be powers of 2.

### Installation
1. This script can be installed using `update.bat` from the main folder of this release. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Texture Format` and choose the `Export as PNG4` plugin.
3. You will be presented with the following option:
    - **Preserve Transparency**:
	  - `Yes`: Choose if your texture needs to maintain transparency. This will keep the alpha channel on export.
	  - `No`: Choose if your texture should not have any transparency. This will flatten the image, removing the alpha channel.
4. If the file is not set up properly, you will receive an error with explanations. Otherwise, it will move on.
5. The .xcf will be saved and several additional operations will be run while the texture is being exported. A single .png texture will be exported. 
6. This script runs all processes in the background, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

### Export Compatibility
- All consoles

## Credits
- BaconWizard17: Script creation