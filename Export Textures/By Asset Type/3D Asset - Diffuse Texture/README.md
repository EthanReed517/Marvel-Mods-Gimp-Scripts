# Marvel Mods GIMP Plugins
by BaconWizard17

## Export 3D Asset - Diffuse Texture
This plugin exports a 3D asset's diffuse texture.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file, and its dimensions should be powers of 2. The texture can be for a skin, mannequin, 3D head, bolton, power model, or map model.

### Installation
1. This script can be installed using `update.bat` from the main folder of this release. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Export 3D Asset - Diffuse Texture` plugin.
3. You will be presented with the following option:
	- **Export Method**: Select which version of Alchemy you're using.
	  - `3ds Max` will export the textures to be set up in 3ds Max.
	  - `Alchemy 5 Texture Replacment` will export the textures in .tga format to use with the Alchemy 5 texture creation tools.
    - **Preserve Transparency**:
	  - `Yes`: Choose if your texture needs to maintain transparency. This will keep the alpha channel on export.
	  - `No`: Choose if your texture should not have any transparency. This will flatten the image, removing the alpha channel.
4. If one or both of the image dimensions is not a power of 2, you will get an error warning as such, and the process will be aborted. Alchemy only supports images whose dimensions are powers of 2.
5. The .xcf will be saved and several additional operations will be run while the texture is being exported. A single plain .png texture will be exported.
6. This script runs all processes in the background, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Credits
- BaconWizard17: Script creation