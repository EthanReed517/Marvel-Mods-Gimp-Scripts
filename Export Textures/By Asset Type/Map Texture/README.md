# Marvel Mods GIMP Plugins
by BaconWizard17
## Export Map Texture
This plugin exports a map texture in several optimized formats. 

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file, and its dimensions should be powers of 2. The texture can be for any texture used in a map.

### Installation
 1. This script can be installed using `update.bat` from the main folder of this release. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Export Map Texture` plugin.
3. You will be presented with a series of options:
	- **Console**:
	  - `All`: Choose if you want to export textures for all available consoles.
	  - `PC only`: Choose if you want to export textures for the PC versions only.
	- **Alchemy Version**:
	  - `Alchemy 2.5`: Choose if your version of 3ds Max has the Alchemy 2.5 exporter. The Alchemy 2.5 exporter is included on the virtual machine version of 3ds Max 5.
	  - `Alchemy 5`: Choose if your version of 3ds Max has the Alchemy 5 exporter. The Alchemy 5 exporter is most commonly used with 3ds Max 10 and 3ds Max 12.
    - **Transparency**:
	  - `Yes`: Choose if your texture needs to have partial or full transparency. This will export in a format that supports transparency. For Alchemy 2.5, this will always be uncompressed/plain png. For Alchemy 5, this will be DXT5 for dds textures and uncompressed/plain png for png textures.
	  - `No`: Choose if your texture should not have any transparency. This will export in a format that does not support transparency (DXT1 compression for dds textures, PNG8 compression for png textures).
	- **Next-Gen Size**:
	  - `Double`: Choose if the texture needs to be twice as big for the next-gen versions of MUA1 (PC, Steam, PS3, and 360).
	  - `Same as Wii, Xbox, and XML2 PC`: Choose if the texture needs to be the same size for the next-gen versions of MUA1 (PC, Steam, PS3, and 360) as the Wii, Xbox, and XML2 PC.
	- For an explanation on how these options impact each console, see below for the list of texture types.
4. If one or both of the image dimensions is not a power of 2, you will get an error warning as such, and the process will be aborted. Alchemy only supports images whose dimensions are powers of 2.
5. The .xcf will be saved and several additional operations will be run while the texture is being exported to the various folders in different formats. The operations will depend on the options selected. Textures that are the same will be grouped together. See below for a list of the texture types that will be exported for each console. 
6. This script creates duplicate images to export, so you will not see any changes on your texture. Wait for the status bar to finish before proceeding with any further operations to your texture. Once it's done running, a message will announce that the export is complete.

## Export Types
 - Unlike other scripts that export textures with a balance of quality and texture size, this script will only export the textures in a format as close to the console's native format as possible, which makes the texture size as small as possible.
 - **XML2 PC**:
   - The texture format depends on the chosen settings.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: This option will export for XML2 PC.
     - `Alchemy 5`: This option will not export for XML2 PC.
   - **Transparency**: 
     - `Yes`: This option will export the textures as uncompressed png files.
     - `No`: This option will export the textures as DXT1 .dds textures.
   - **Console** and **Next-Gen Size** have no impact on XML2 PC textures.
 - **MUA1 PC**:
   - The texture format depends on the chosen settings.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: This option will RGB-BGR swap DXT1 .dds textures and export transparent textures as plain .png textures.
     - `Alchemy 5`: This option will not RGB-BGR swap DXT1 .dds textures and will export transparent textures as DXT5 .dds textures.
   - **Transparency**: 
     - `Yes`: This option will export the textures as uncompressed png files for Alchemy 2.5 and DXT5 .dds textures for Alchemy 5.
     - `No`: This option will export the textures as DXT1 .dds textures.
   - **Console** and **Next-Gen Size** have no impact on MUA1 PC textures.
 - **Steam**:
   - The texture format depends on the chosen settings.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: This option will RGB-BGR swap DXT1 .dds textures and export transparent textures as plain .png textures.
     - `Alchemy 5`: This option will not RGB-BGR swap DXT1 .dds textures and will export transparent textures as DXT5 .dds textures.
   - **Transparency**: 
     - `Yes`: This option will export the textures as uncompressed png files for Alchemy 2.5 and DXT5 .dds textures for Alchemy 5.
     - `No`: This option will export the textures as DXT1 .dds textures.
   - **Console** and **Next-Gen Size** have no impact on Steam textures.
 - **GameCube**: 
   - The texture format depends on the chosen settings.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: This option will export for GameCube.
     - `Alchemy 5`: This option will not export for GameCube.
   - **Transparency**: 
     - `Yes`: This option will export the textures as uncompressed png files.
     - `No`: This option will export the textures as DXT1 .dds textures.
   - **Console**:
     - `All`: This option will export GameCube textures.
     - `PC Only`: This option will not export GameCube Textures.
   - **Next-Gen Size**:
     - `Double`: This option will export the GameCube textures with the dimensions divided by 4.
	 - `Same as Wii, Xbox, and XML2 PC`: This option will export GameCube textures with the dimensions divided by 2.
 - **PS2**: 
   - Textures will be exported as png files with PNG8 compression.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: This option will export for PS2.
     - `Alchemy 5`: This option will not export for PS2.
   - **Transparency**: 
     - `Yes`: This option will export the textures as standard PNG8 textures.
     - `No`: This option will export the textures as alpha-PNG8 textures.
   - **Console**:
     - `All`: This option will export PS2 textures.
     - `PC Only`: This option will not export PS2 Textures.
   - **Next-Gen Size**:
     - `Double`: This option will export the PS2 textures with the dimensions divided by 4.
	 - `Same as Wii, Xbox, and XML2 PC`: This option will export PS2 textures with the dimensions divided by 2.
 - **PS3**:
   - The texture format depends on the chosen settings.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: This option will RGB-BGR swap DXT1 .dds textures and export transparent textures as plain .png textures.
     - `Alchemy 5`: This option will not RGB-BGR swap DXT1 .dds textures and will export transparent textures as DXT5 .dds textures.
   - **Transparency**: 
     - `Yes`: This option will export the textures as uncompressed png files for Alchemy 2.5 and DXT5 .dds textures for Alchemy 5.
     - `No`: This option will export the textures as DXT1 .dds textures.
   - **Console**:
     - `All`: This option will export PS3 textures.
     - `PC Only`: This option will not export PS3 Textures.
   - **Next-Gen Size** has no impact on PS3 textures.
 - **PSP**: 
   - Textures will be exported as png files with PNG4 compression.
   - **Transparency**: 
     - `Yes`: This option will export the textures as standard PNG4 textures.
     - `No`: This option will export the textures as alpha-PNG4 textures.
   - **Console**:
     - `All`: This option will export PSP textures.
     - `PC Only`: This option will not export PSP Textures.
   - **Next-Gen Size**:
     - `Double`: This option will export the PSP textures with the dimensions divided by 4.
	 - `Same as Wii, Xbox, and XML2 PC`: This option will export PSP textures with the dimensions divided by 2.
   - **Alchemy Version** has no impact on PSP textures.
 - **Wii**:
   - The texture format depends on the chosen settings.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: This option will export transparent textures as plain .png textures.
     - `Alchemy 5`: This option will export transparent textures as DXT5 .dds textures.
   - **Transparency**: 
     - `Yes`: This option will export the textures as uncompressed png files for Alchemy 2.5 and DXT5 .dds textures for Alchemy 5.
     - `No`: This option will export the textures as DXT1 .dds textures.
   - **Console**:
     - `All`: This option will export Wii textures.
     - `PC Only`: This option will not export Wii Textures.
   - **Next-Gen Size**:
     - `Double`: This option will export the Wii textures with the dimensions divided by 2.
	 - `Same as Wii, Xbox, and XML2 PC`: This option will export Wii textures with the source image's dimensions.
 - **Xbox**:
   - The texture format depends on the chosen settings.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: This option will export Xbox textures.
     - `Alchemy 5`: This option will not export Xbox textures.
   - **Transparency**: 
     - `Yes`: This option will export the textures as uncompressed png files.
     - `No`: This option will export the textures as DXT1 .dds textures.
   - **Console**:
     - `All`: This option will export Xbox textures.
     - `PC Only`: This option will not export Xbox Textures.
   - **Next-Gen Size**:
     - `Double`: This option will export the Xbox textures with the dimensions divided by 2.
	 - `Same as Wii, Xbox, and XML2 PC`: This option will export Xbox textures with the source image's dimensions.
 - **Xbox 360**:
   - The texture format depends on the chosen settings.
   - **Alchemy Version**: 
     - `Alchemy 2.5`: This option will RGB-BGR swap DXT1 .dds textures and export transparent textures as plain .png textures.
     - `Alchemy 5`: This option will not RGB-BGR swap DXT1 .dds textures and will export transparent textures as DXT5 .dds textures.
   - **Transparency**: 
     - `Yes`: This option will export the textures as uncompressed png files for Alchemy 2.5 and DXT5 .dds textures for Alchemy 5.
     - `No`: This option will export the textures as DXT1 .dds textures.
   - **Console**:
     - `All`: This option will export Xbox 360 textures.
     - `PC Only`: This option will not export Xbox 360 textures.
   - **Next-Gen Size** has no impact on Xbox 360 textures.
## Credits
- BaconWizard17: Script creation