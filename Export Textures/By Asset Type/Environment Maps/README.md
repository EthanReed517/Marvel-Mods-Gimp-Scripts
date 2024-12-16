# Marvel Mods GIMP Plugins
by BaconWizard17
## Export Environment Maps
This plugin exports environment maps in several optimized formats.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file, and its dimensions should be powers of 2. The texture can be for a skin, 3D head, or mannequin. The texture should be square. My template is recommended for use, as it contains the correct layer names. See the "Templates" section for more information. The max supported texture size is 128x128, and anything higher will be reduced. If the environment map is set up in 3ds Max, it will be compatible with last-gen consoles. For application with Raven MUA Setup Material, the textures will only be compatible with next-gen MUA1.

### Installation
 1. This script can be installed using `update.bat` from the main folder of this release. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Export Environment Map` plugin.
3. You will be presented with a series of options:
    - **Primary Texture Size**:
	  - `256x256 or less`: Choose if the primary texture for the model is 256x256 or smaller.
	  - `"Over 256x256`: Choose if the primary texture for the model is over 256x256.
	- **Console**:
	  - `All`: Choose if you want to export textures for all available consoles.
	  - `PC only`: Choose if you want to export textures for the PC versions only.
	- **3ds Max Version**:
	  - `Alchemy 2.5`: Choose if your version of 3ds Max has the Alchemy 2.5 exporter. The Alchemy 2.5 exporter is included on the virtual machine version of 3ds Max 5.
	  - `Alchemy 5`: Choose if your version of 3ds Max has the Alchemy 5 exporter. The Alchemy 5 exporter is most commonly used with 3ds Max 10 and 3ds Max 12.
	  - Regardless of 3ds Max Version, only the last-gen textures will be exported to be set up in 3ds Max. The next-gen MUA1 textures will always be exported to use with the Raven MUA Setup Material script.
	- **PSP Texture Compression**:
	  - `PNG4`: Choose if you want to export PSP textures with PNG4 compression. PNG4 compression reduces the image to 16 colors. This results in a smaller texture size but worse texture quality. This is the standard format used by the PSP versions of XML2, MUA1, and MUA2.
	  - `PNG8`: Choose if you want to export PSP textures with PNG8 compression. PNG8 compression reduces the image to 256 colors. This results in better texture quality but a larger file size.
4. If one or both of the image dimensions is not a power of 2, you will get an error warning as such, and the process will be aborted. Alchemy only supports images whose dimensions are powers of 2.
5. The .xcf will be saved and several additional operations will be run while the texture is being exported to the various folders in different formats. The operations will depend on the options selected. Textures that are the same will be grouped together. See below for a list of the texture types that will be exported for each console. 
6. This script creates duplicate images to export, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Export Types
 - **XML2 PC**:
   - The texture format depends on other options.
   - **Primary Texture Size**:
     - `256x256 or less`: Textures will be exported as PNG8 .png files.
	 - `over 256x256`: Textures will be exported as plain .png files.
   - **3ds Max Version**:
     - `Alchemy 2.5`: This option will export XML2 PC textures.
	 - `Alchemy 5`: This option will not export XML2 PC textures.
   - **Console** and **PSP Texture Compression** have no impact on XML2 PC textures.
 - **MUA1 PC**:
   - The texture format depends on other options.
   - **Primary Texture Size**:
     - `256x256 or less`: Textures will be exported as PNG8 .png files.
	 - `over 256x256`: Textures will be exported as DXT1 .dds files.
   - **3ds Max Version**, **Console**, and **PSP Texture Compression** have no impact on MUA1 PC textures.
 - **Steam**:
   - Textures will be exported as DXT1 dds files.
   - No settings have an impact on Steam textures.
 - **GameCube**:
   - Textures will be exported as PNG8 textures.
   - **Console**:
     - `All`: This option will export GameCube textures.
     - `PC Only`: This option will not export GameCube Textures.
   - **3ds Max Version**: 
     - `Alchemy 2.5`: This option has no impact on GameCube textures.
     - `Alchemy 5`: This option will not export GameCube textures.
   - **Primary Texture Size** and **PSP Texture Format** have no impact on GameCube textures.
 - **PS2**:
   - Textures will be exported as PNG8 textures.
   - **Console**:
     - `All`: This option will export PS2 textures.
     - `PC Only`: This option will not export PS2 Textures.
   - **Primary Texture Size**, **3ds Max Version**, and **PSP Texture Format** have no impact on PS2 textures.
 - **PS3**:
   - Textures will be exported as DXT1 dds files.
   - PS3 textures will presumably work on the PS4 re-release, but this hasn't been confirmed.
   - **Console**:
     - `All`: This option will export PS3 textures.
     - `PC Only`: This option will not export PS3 Textures.
   - **Primary Texture Size**, **3ds Max Version**, and **PSP Texture Format** have no impact on PS3 textures.
 - **PSP**:
   - The texture format depends on other options.
   - **Console**:
     - `All`: This option will export PSP textures.
     - `PC Only`: This option will not export PSP Textures.
   - **PSP Texture Format**:
     - `PNG4`: This option will apply PNG4 compression to the texture.
     - `PNG8`: This option will apply PNG8 compression to the texture. 
   - **Primary Texture Size** and **3ds Max Version** has no impact on PSP textures.
 - **Wii**:
   - The texture format depends on other options.
   - **Console**:
     - `All`: This option will export Wii textures.
     - `PC Only`: This option will not export Wii Textures.
   - **3ds Max Version**: 
     - `Alchemy 2.5`: Textures will be exported as plain png textures.
     - `Alchemy 5`: Textures will be exported as DXT1 .dds files.
   - **Primary Texture Size** and **PSP Texture Format** have no impact on Wii textures.
 - **Xbox**:
   - The texture format depends on other options.
   - **Primary Texture Size**:
     - `256x256 or less`: Textures will be exported as PNG8 .png files.
	 - `over 256x256`: Textures will be exported as plain .png files.
   - **Console**:
     - `All`: This option will export Xbox textures.
     - `PC Only`: This option will not export Xbox Textures.
   - **3ds Max Version**:
     - `Alchemy 2.5`: This option will export Xbox textures.
	 - `Alchemy 5`: This option will not export Xbox textures.
   - **PSP Texture Format** has no impact on Xbox textures.
 - **Xbox 360**:
   - The texture format depends on other options.
   - Xbox 360 textures will presumably work on the Xbox One re-release, but this hasn't been confirmed.
   - **Primary Texture Size**:
     - `256x256 or less`: Textures will be exported as PNG8 .png files.
	 - `over 256x256`: Textures will be exported as DXT1 .dds files.
   - **Console**:
     - `All`: This option will export Xbox 360 textures.
     - `PC Only`: This option will not Xbox 360 Textures.
   - **3ds Max Version** and **PSP Texture Format** have no impact on Xbox 360 textures.

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