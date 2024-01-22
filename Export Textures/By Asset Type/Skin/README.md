# Marvel Mods GIMP Plugins
by BaconWizard17
## Export Skin
This plugin exports a skin texture in several optimized formats.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. The texture can be for a skin, 3D head, or mannequin.

### Installation
 1. This script can be installed using `runUpdateAdmin.bat` from my scripts, or it can be placed individually in your GIMP plugins directory. The standard location for this is `C:\Users\(your user)\AppData\Roaming\GIMP\2.10\plug-ins`. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Export Skin` plugin.
3. You will be presented with a series of options:
	- **Console**:
	  - `All`: Choose if you want to export textures for all available consoles.
	  - `PC only`: Choose if you want to export textures for the PC versions only.
	- **Skin Type**:
	  - `Primary`: Choose if you are exporting a texture for a primary skin. A primary skin is a main skin used by a character. This option will not change the standard export.
	  - `Secondary`: Choose if you are exporting a texture for a secondary skin. A secondary skin is a skin used during a power, such as a skin swap. For GameCube, PS2, and PSP textures, this reduces the texture size in half.
	- **Texture Type**:
	  - `Primary`: Choose if you are exporting a primary texture. A primary texture is the main/largest texture used by a skin. This option will not change the standard export.
	  - `Secondary`: Choose if you are exporting a secondary texture. A secondary texture is any additional/smaller texture used in a skin. For PC, this reduces the threshold for when dds textures are used in half. For GameCube, PS2, and PSP textures, this reduces the texture size in half.
	- **Character Size**:
	  - `Standard`: Choose if you are exporting a texture for a standard-sized character. Standard-sized characters are all playable characters and most NPCs (anyone who is not extremely large). Selecting this option limits the texture size to 256x256 on the PS2 and 128x128 on the PSP and GameCube, although **Skin Type** and **Texture Type** can reduce this further.
	  - `Large`: Choose if you are exporting a texture for a large character. Large characters are special oversized NPCs, like Galactus, Master Mold, Ymir, or Sentinels. This option will not change the standard export.
	- **Alchemy Version**:
	  - `Alchemy 2.5`: Choose if your version of 3ds Max has the Alchemy 2.5 exporter. The Alchemy 2.5 exporter is included on the virtual machine version of 3ds Max 5.
	  - `Alchemy 5`: Choose if your version of 3ds Max has the Alchemy 5 exporter. The Alchemy 5 exporter is most commonly used with 3ds Max 10 and 3ds Max 12.
    - **Transparency**:
	  - `Yes`: Choose if your texture needs to have partial or full transparency. This will export in a format that supports transparency (DXT5 compression for dds textures, no compression for png textures).
	  - `No`: Choose if your texture should not have any transparency. This will export in a format that does not support transparency (DXT1 compression for dds textures, PNG8 compression for png textures).
	- **PSP Texture Compression**:
	  - `PNG4`: Choose if you want to export PSP textures with PNG4 compression. PNG4 compression reduces the image to 16 colors. This results in a smaller texture size but worse texture quality. This is the standard format used by the PSP versions of XML2, MUA1, and MUA2.
	  - `PNG8`: Choose if you want to export PSP textures with PNG8 compression. PNG8 compression reduces the image to 256 colors. This results in better texture quality but a larger file size.
	  - Transparent textures do not use compression, so this option will be ignored if `Yes` is chosen for **Transparency**.
	- For an explanation on how these options impact each console, see below for the list of texture types.
4. If one or both of the image dimensions is not a power of 2, you will get an error warning as such, and the process will be aborted. Alchemy only supports images whose dimensions are powers of 2.
5. The .xcf will be saved and several additional operations will be run while the texture is being exported to the various folders in different formats. The operations will depend on the options selected. Textures that are the same will be grouped together. See below for a list of the texture types that will be exported for each console. 
6. This script creates duplicate images to export, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Export Types
 - **PC**:
   - Textures over 256x256 will be exported as dds files, and 256x256 or less will export as png files. This threshold can be modified by other settings.
   - **Texture Type**: 
     - `Primary`: This option will not change the texture. 
     - `Secondary`: This option will change the minimum size of a dds texture to 256x256.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: This option will export for XML2 PC and MUA1 PC. Any dds textures for MUA1 PC will be RGB-BGR swapped.
     - `Alchemy 5`: This option will export for MUA1 PC only.
   - **Transparency**: 
     - `Yes`: This option will export dds textures with DXT5 compression and png textures without compression. 
     - `No`: This option will export dds textures with DXT1 compression and png textures with PNG8 compression.
   - **Console**, **Character Size**, **Skin Type**, and **PSP Texture Compression** have no impact on PC textures.
 - **Steam**:
   - Textures will be exported as dds files.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: This option will RGB-BGR swap Steam textures.
     - `Alchemy 5`: This option will not RGB-BGR swap Steam textures.
   - **Transparency**: 
     - `Yes`: This option will export dds textures with DXT5 compression. 
     - `No`: This option will export dds textures with DXT1 compression.
   - **Console**, **Character Size**, **Skin Type**, **Texture Type**, and **PSP Texture Compression** have no impact on Steam textures.
 - **GameCube**: 
   - Textures will be exported as png files.
   - **Console**:
     - `All`: This option will export GameCube textures.
     - `PC Only`: This option will not export GameCube Textures.
   - **Character Size**: 
     - `Standard`: This option will limit the maximum texture size for GameCube to 128x128. 
     - `Large`: This option will reduce the texture size in half. 
     - **Skin Type** and **Texture Type** can reduce the size further.
   - **Skin Type**: 
     - `Primary`: This option will not change the texture. 
     - `Secondary`: This option will reduce the texture size in half.
   - **Texture Type**: 
     - `Primary`: This option will not change the texture. 
     - `Secondary`: This option will reduce the texture size in half.
   - **Alchemy Version**:
     - `Alchemy 2.5`: This option will export GameCube textures.
     - `Alchemy 5`: This option will not export GameCube textures.
   - **Transparency**: 
     - `Yes`: This option will export png textures without compression. 
     - `No`: This option will export png textures with PNG8 compression.
   - **PSP Texture Compression** has no impact on GameCube textures.
 - **PS2**: 
   - Textures will be exported as png files.
   - MUA2 PS2 will always export at half the texture size of other PS2 textures.
   - **Console**:
     - `All`: This option will export PS2 textures.
     - `PC Only`: This option will not export PS2 Textures.
   - **Character Size**: 
     - `Standard`: This option will limit the maximum texture size for PS2 to 256x256. 
     - `Large`: This option will not change the texture. 
     - **Skin Type** and **Texture Type** can reduce the size further.
   - **Skin Type**: 
     - `Primary`: This option will not change the texture. 
     - `Secondary`: This option will reduce the texture size in half.
   - **Texture Type**: 
     - `Primary`: This option will not reduce the texture size.
     - `Secondary`: This option will reduce the texture size in half.
   - **Transparency**: 
     - `Yes`: This option will export png textures without compression. 
     - `No`: This option will export png textures with PNG8 compression.
   - **Alchemy Version** and **PSP Texture Compression** have no impact on PS2 textures.
 - **PS3**:
   - Textures will be exported as dds files.
   - PS3 textures will presumably work on the PS4 re-release, but this hasn't been confirmed.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: This option will RGB-BGR swap PS3 textures.
     - `Alchemy 5`: This option will not RGB-BGR swap PS3 textures.
   - **Transparency**: 
     - `Yes`: This option will export dds textures with DXT5 compression. 
     - `No`: This option will export dds textures with DXT1 compression.
   - **Console**, **Character Size**, **Skin Type**, **Texture Type**, and **PSP Texture Compression** have no impact on Steam textures.
 - **PSP**: 
   - Textures will be exported as png files.
   - **Note**: XML2 PSP currently does not support custom skins.
   - **Console**:
     - `All`: This option will export PSP textures.
     - `PC Only`: This option will not export PSP Textures.
   - **Character Size**: 
     - `Standard`: This option will limit the maximum texture size for PSP to 128x128. 
     - `Large`: This option will not change the texture. 
     - **Skin Type** and **Texture Type** can reduce the size further.
   - **Skin Type**: 
     - `Primary`: This option will not change the texture. 
     - `Secondary`: This option will reduce the texture size in half.
   - **Texture Type**: 
     - `Primary`: This option will not reduce the texture size.
     - `Secondary`: This option will reduce the texture size in half.
   - **Transparency**: 
     - `Yes`: This option will export png textures without compression. 
     - `No`: This option will export png textures with the compression selected for **PSP Texture Compression**.
   - **PSP Texture Compression**:
     - `PNG4`: This option will apply PNG4 compression to the texture.
     - `PNG8`: This option will apply PNG8 compression to the texture. 
     - This option is ignored if `Yes` is chosen for **Transparency**
   - **Alchemy Version** has no impact on PSP textures.
 - **Wii**:
   - Textures will be exported as dds files.
   - **Console**:
     - `All`: This option will export Wii textures.
     - `PC Only`: This option will not export Wii Textures.
   - **Transparency**: 
     - `Yes`: This option will export dds textures with DXT5 compression. 
     - `No`: This option will export dds textures with DXT1 compression.
   - **Character Size**, **Skin Type**, **Texture Type**, **Alchemy Version**, and **PSP Texture Compression** have no impact on Wii textures.
 - **Xbox**:
   - Textures over 256x256 will be exported as dds files, and 256x256 or less will export as png files. This threshold can be modified by other settings.
   - **Console**:
     - `All`: This option will export Xbox textures.
     - `PC Only`: This option will not export Xbox Textures.
   - **Texture Type**: 
     - `Primary`: This option will not change the texture. 
     - `Secondary`: This option will change the minimum size of a dds texture to 256x256.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: Xbox textures will be exported.
     - `Alchemy 5`: Xbox textures will not be exported.
   - **Transparency**: 
     - `Yes`: This option will export dds textures with DXT5 compression and png textures without compression. 
     - `No`: This option will export dds textures with DXT1 compression and png textures with PNG8 compression.
   - **Character Size**, **Skin Type**, and **PSP Texture Compression** have no impact on Xbox textures.
 - **Xbox 360**:
   - Textures over 256x256 will be exported as dds files, and 256x256 or less will export as png files. This threshold can be modified by other settings.
   - Xbox 360 textures will presumably work on the Xbox One re-release, but this hasn't been confirmed.
   - **Texture Type**: 
     - `Primary`: This option will not change the texture. 
     - `Secondary`: This option will change the minimum size of a dds texture to 256x256.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: This option will RGB-BGR dds textures.
     - `Alchemy 5`: This option will not change the texture.
   - **Transparency**: 
     - `Yes`: This option will export dds textures with DXT5 compression and png textures without compression. 
     - `No`: This option will export dds textures with DXT1 compression and png textures with PNG8 compression.
   - **Console**, **Character Size**, **Skin Type**, and **PSP Texture Compression** have no impact on Xbox 360 textures.
## Credits
- BaconWizard17: Script creation