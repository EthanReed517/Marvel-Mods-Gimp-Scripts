# Marvel Mods GIMP Plugins
by BaconWizard17

## 3D Asset - Environment Maps
This plugin exports environment maps in several sizes.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file, and its dimensions should be powers of 2. The texture can be for a skin, 3D head, mannequin, bolton, power model, or map model. The texture should be square. My template is recommended for use, as it contains the correct layer names. See the "Templates" section for more information. The max supported texture size is 128x128, and anything higher will be reduced. If the environment map is set up in 3ds Max, it will be compatible with last-gen consoles. For application with Alchemy 5, the textures will only be compatible with next-gen MUA1.

### Installation
1. This script can be installed using `update.bat` from the main folder of this release. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `3D Asset - Environment Maps` plugin.
3. You will be presented with the following option:
	- **Console**:
	  - `All`: Choose if you want to export textures for all available consoles.
	  - `PC only`: Choose if you want to export textures for the PC versions only.
4. If one or both of the image dimensions is not a power of 2, you will get an error warning as such, and the process will be aborted. Alchemy only supports images whose dimensions are powers of 2.
5. The .xcf will be saved and several additional operations will be run while the texture is being exported. If `PC Only` was selected, 6 plain .png textures will be exported. Otherwise, additional plain .png textures will be exported.
6. This script runs all processes in the background, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Templates
In order for the script to function correctly, I've provided a template that can be used with it: `Template.xcf`. Here's how to use the template:
1. Open the template in GIMP. Save it as something else so that you always have the template available. The file name doesn't matter.
2. The images included in the template can be used, or you can replace them with your own.
3. There should be 6 layers:
    - **Up**: The up-facing part of the environment map.
    - **Down**: The down-facing part of the environment map.
    - **Left**: The left-facing part of the environment map.
    - **Right**: The right-facing part of the environment map.
    - **Front**: The front-facing part of the environment map.
    - **Back**: The back-facing part of the environment map.
	
## Credits
- BaconWizard17: Script creation