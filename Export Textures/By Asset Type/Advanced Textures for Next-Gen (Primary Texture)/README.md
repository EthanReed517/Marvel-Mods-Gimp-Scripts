# Marvel Mods GIMP Plugins
by BaconWizard17
## Export Advanced Textures (Primary Texture)
This plugin exports advanced textures (normal maps, spec maps, gloss/emissive maps, and environment masks) in several optimized formats to be used with next-gen MUA1.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The texture can be for a skin, 3D head, or mannequin. Normal maps should be set up in the green normal map format, while other textures can be any color. Resulting textures will only work with next-gen MUA1.

### Installation
 1. This script can be installed using `update.bat` from the main folder of this release, or it can be placed individually in your GIMP plugins directory. The standard location for this is `C:\Users\(your user)\AppData\Roaming\GIMP\2.10\plug-ins`. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Export Advanced Textures for Next-Gen (Primary Texture)` plugin.
3. You will be presented with a series of options:
    - **Advanced Texture Type**:
	  - `Normal Map`: Choose if you are exporting a normal map. Changes the export to DXT5. Adds "_n" to the end of the file name.
	  - `Specular Map`: Choose if you are exporting a specular map. Adds "_s" to the end of the file name.
	  - `Gloss/Emissive Map`: Choose if you are exporting a gloss/emissive map. Adds "_g" to the end of the file name.
	  - `Environment Mask`: Choose if you are exporting an environment mask. Adds "_m" to the end of the file name. For exporting environment maps, see the "Export Environment Maps" script.
	- **Console**:
	  - `All`: Choose if you want to export textures for all available consoles.
	  - `PC only`: Choose if you want to export textures for the PC versions only.
	- **Alchemy Version**:
	  - `Alchemy 2.5`: Choose if your version of 3ds Max has the Alchemy 2.5 exporter. The Alchemy 2.5 exporter is included on the virtual machine version of 3ds Max 5.
	  - `Alchemy 5`: Choose if your version of 3ds Max has the Alchemy 5 exporter. The Alchemy 5 exporter is most commonly used with 3ds Max 10 and 3ds Max 12.
4. If one or both of the image dimensions is not a power of 2, you will get an error warning as such, and the process will be aborted. Alchemy only supports images whose dimensions are powers of 2.
5. The .xcf will be saved and several additional operations will be run while the texture is being exported to the various folders in different formats. The operations will depend on the options selected. Textures that are the same will be grouped together. See below for a list of the texture types that will be exported for each console. 
6. This script creates duplicate images to export, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Export Types
 - **PC**:
   - Textures over 256x256 will be exported as DXT1 dds files, and 256x256 or less will export as PNG8 files. This threshold can be modified by other settings.
   - **Advanced Texture Type**:
	 - `Normal Map`: Changes the export to DXT5 .dds. Adds "_n" to the end of the file name.
	 - `Specular Map`: Adds "_s" to the end of the file name.
	 - `Gloss/Emissive Map`: Adds "_g" to the end of the file name.
	 - `Environment Mask`: Adds "_m" to the end of the file name.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: Any dds textures for MUA1 PC will be RGB-BGR swapped.
     - `Alchemy 5`: This option will not change the texture
   - **Console** has no impact on PC textures.
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
   - **Console** have no impact on Steam textures.
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
   - **Console** have no impact on PS3 textures.
 - **Xbox 360**:
   - Textures over 256x256 will be exported as DXT1 dds files, and 256x256 or less will export as PNG8 files. This threshold can be modified by other settings.
   - Xbox 360 textures will presumably work on the Xbox One re-release, but this hasn't been confirmed.
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
## Credits
- BaconWizard17: Script creation