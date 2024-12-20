# Marvel Mods GIMP Plugins
by BaconWizard17
## Export Advanced Textures (Secondary Texture)
This plugin exports advanced textures (normal maps, spec maps, gloss/emissive maps, and environment masks) in several optimized formats to be used with next-gen MUA1. This script is for secondary textures so that the texture format can be matched up with the primary texture regardless of size. For the primary (largest) texture, see the `Export Advanced Textures (Primary Texture)` script.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file, and its dimensions should be powers of 2. The texture can be for a skin, mannequin, bolton, or power model. The texture should be a secondary (smaller) texture for the model. Normal maps should be set up in the green normal map format, while other textures can be any color. Resulting textures will only work with next-gen MUA1.

### Installation
 1. This script can be installed using `update.bat` from the main folder of this release. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Export Advanced Textures for Next-Gen (Secondary Texture)` plugin.
3. You will be presented with a series of options:
	- **Primary Texture Size**:
	  - `256x256 or less`: Choose if the primary texture for the asset is 256x256 or less.
	  - `Over 256x256`: Choose if the primary texture for the asset is over 256x256.
    - **Advanced Texture Type**:
	  - `Normal Map`: Choose if you are exporting a normal map. Changes the export to DXT5. Adds "_n" to the end of the file name.
	  - `Specular Map`: Choose if you are exporting a specular map. Adds "_s" to the end of the file name.
	  - `Gloss/Emissive Map`: Choose if you are exporting a gloss/emissive map. Adds "_g" to the end of the file name.
	  - `Environment Mask`: Choose if you are exporting an environment mask. Adds "_m" to the end of the file name. For exporting environment maps, see the "Export Environment Maps" script.
	- **Console**:
	  - `All`: Choose if you want to export textures for all available consoles.
	  - `PC only`: Choose if you want to export textures for the PC versions only.
	- **Alchemy Version**:
	  - `Alchemy 2.5`: Choose if you're using the older Alchemy 2.5 tool to add advanced textures.
	  - `Alchemy 5`: Choose if you're using the newer Alchemy 5 tool to add advanced textures (recommended).
	- **Steam/360 Normal Map Color**:
	  - `Yellow`: Choose this if you want the normal map to be the yellow format that is common to most Steam and Xbox 360 models.
	  - `Blue`: Choose this if you want the normal map to be the blue format that is common to fewer Steam and Xbox 360 models.
	  - **Note**: Regardless of what you choose for the color, the normal map will function the same way on the Steam and 360. The only change is whether the blue channel is fully black or white; it doesn't contain any actual information. This option is just here to cover both default styles. 
4. If one or both of the image dimensions is not a power of 2, you will get an error warning as such, and the process will be aborted. Alchemy only supports images whose dimensions are powers of 2.
5. The .xcf will be saved and several additional operations will be run while the texture is being exported to the various folders in different formats. The operations will depend on the options selected. Textures that are the same will be grouped together. See below for a list of the texture types that will be exported for each console. 
6. This script creates duplicate images to export, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Export Types
 - **PC**:
   - Textures will be exported as DXT1 dds files or as PNG8 .png files depending on the settings.
   - **Primary Texture Size**:
     - `256x256 or less`: Exports as a PNG8 .png file.
	 - `Over 256x256`: Exports as a DXT1 .dds file.
   - **Advanced Texture Type**:
	 - `Normal Map`: Changes the export to DXT5 .dds. Adds "_n" to the end of the file name.
	 - `Specular Map`: Adds "_s" to the end of the file name.
	 - `Gloss/Emissive Map`: Adds "_g" to the end of the file name.
	 - `Environment Mask`: Adds "_m" to the end of the file name.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: Any dds textures for MUA1 PC will be RGB-BGR swapped.
     - `Alchemy 5`: This option will not change the texture
   - **Console** and **Steam/360 Normal Map Color** have no impact on PC textures.
 - **Steam**:
   - Textures will be exported as DXT1 dds files.
   - **Advanced Texture Type**:
	 - `Normal Map`: Modifies the texture to the yellow normal map style required by the Steam version. Adds "_n" to the end of the file name.
	 - `Specular Map`: Adds "_s" to the end of the file name.
	 - `Gloss/Emissive Map`: Adds "_g" to the end of the file name.
	 - `Environment Mask`: Adds "_m" to the end of the file name.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: This option will RGB-BGR swap Steam textures.
     - `Alchemy 5`: This option will not RGB-BGR swap Steam textures.
   - **Steam/360 Normal Map Color**:
     - `Yellow`: This option will make normal maps yellow.
	 - `Blue`: This option will make normal maps blue.
	 - **Note**: Regardless of what you choose for the color, the normal map will function the same way. The only change is whether the blue channel is fully black or white; it doesn't contain any actual information. This option is just here to cover both default styles. 
   - **Console** has no impact on Steam textures.
 - **PS3**:
   - Textures will be exported as DXT1 dds files.
   - PS3 textures will presumably work on the PS4 re-release, but this hasn't been confirmed.
   - **Advanced Texture Type**:
	 - `Normal Map`: Changes the export to DXT5 .dds. Adds "_n" to the end of the file name.
	 - `Specular Map`: Adds "_s" to the end of the file name.
	 - `Gloss/Emissive Map`: Adds "_g" to the end of the file name.
	 - `Environment Mask`: Adds "_m" to the end of the file name.
   - **Console**:
     - `All`: This option will export PS3 textures.
     - `PC Only`: This option will not export PS3 Textures.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: This option will RGB-BGR swap PS3 textures.
     - `Alchemy 5`: This option will not RGB-BGR swap PS3 textures.
   - **Steam/360 Normal Map Color** has no impact on PC textures.
 - **Xbox 360**:
   - Textures will be exported as DXT1 dds files or as PNG8 .png files depending on the settings.
   - Xbox 360 textures will presumably work on the Xbox One re-release, but this hasn't been confirmed.
   - **Primary Texture Size**:
     - `256x256 or less`: Exports as a PNG8 .png file.
	 - `Over 256x256`: Exports as a DXT1 .dds file.
   - **Advanced Texture Type**:
	 - `Normal Map`: Modifies the texture to the yellow normal map style required by the Xbox 360 version. Adds "_n" to the end of the file name.
	 - `Specular Map`: Adds "_s" to the end of the file name.
	 - `Gloss/Emissive Map`: Adds "_g" to the end of the file name.
	 - `Environment Mask`: Adds "_m" to the end of the file name.
   - **Console**:
     - `All`: This option will export Xbox 360 textures.
     - `PC Only`: This option will not Xbox 360 Textures.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: Any dds textures for Xbox 360 will be RGB-BGR swapped.
     - `Alchemy 5`: This option will not change the texture
   - **Steam/360 Normal Map Color**:
     - `Yellow`: This option will make normal maps yellow.
	 - `Blue`: This option will make normal maps blue.
	 - **Note**: Regardless of what you choose for the color, the normal map will function the same way. The only change is whether the blue channel is fully black or white; it doesn't contain any actual information. This option is just here to cover both default styles. 
## Credits
- BaconWizard17: Script creation