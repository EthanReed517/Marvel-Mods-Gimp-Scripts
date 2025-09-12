# Marvel Mods GIMP Plugins
by BaconWizard17

## Export 3D Asset - Advanced Texture
This plugin exports advanced textures (normal maps, spec maps, gloss/emissive maps, and environment masks) to be used with next-gen MUA1.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file, and its dimensions should be powers of 2. The texture can be for a skin, mannequin, bolton, power model, or map model. Normal maps should be set up in the green normal map format, while other textures can be any color. Resulting textures will only work with next-gen MUA1.

### Installation
1. This script can be installed using `update.bat` from the main folder of this release. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Export 3D Asset - Advanced Texture` plugin.
3. You will be presented with the following options:
    - **Advanced Texture Type**:
	  - `Normal Map`: Choose if you are exporting a normal map. Changes the export to DXT5. Adds "_n" to the end of the file name.
	  - `Specular Map`: Choose if you are exporting a specular map. Adds "_s" to the end of the file name.
	  - `Gloss/Emissive Map`: Choose if you are exporting a gloss/emissive map. Adds "_g" to the end of the file name.
	  - `Environment Mask`: Choose if you are exporting an environment mask. Adds "_m" to the end of the file name. For exporting environment maps, see the "Export Environment Maps" script.
	- **Steam/360 Normal Map Color**:
	  - `Yellow`: Choose this if you want the normal map to be the yellow format that is common to most Steam and Xbox 360 models.
	  - `Blue`: Choose this if you want the normal map to be the blue format that is common to fewer Steam and Xbox 360 models.
	  - **Note**: Regardless of what you choose for the color, the normal map will function the same way on the Steam and 360. The only change is whether the blue channel is fully black or white; it doesn't contain any actual information. This option is just here to cover both default styles. 
4. If one or both of the image dimensions is not a power of 2, you will get an error warning as such, and the process will be aborted. Alchemy only supports images whose dimensions are powers of 2.
5. The .xcf will be saved and several additional operations will be run while the texture is being exported. A single plain .png texture will be exported (except for normal maps, which will export 2).
6. This script runs all processes in the background, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Credits
- BaconWizard17: Script creation