# Marvel Mods GIMP Plugins
by BaconWizard17
## Export Skin
This plugin exports a skin texture in several optimized formats.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. 

### Installation
 1. This script can be installed using `runUpdateAdmin.bat` from my scripts, or it can be placed individually in your GIMP plugins directory. The standard location for this is `C:\Users\(your user)\AppData\Roaming\GIMP\2.10\plug-ins`. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Asset Type` and choose the `Export Skin` plugin.
3. You will be presented with a series of options:
	- **Console**: Select which console you will be using. `All` will export to all available consoles based on later suggestions, while `PC Only` will export textures for PC only
	- **Skin Type**: Select what the skin type is. A `Primary` skin is a standard skin used by a character. A `Secondary` skin is a skin swap or other similar skin. `Secondary` skins will have half the resolution of a `Primary` skin for PS2, PSP, and GameCube.
	- **Texture Type**: Select what the texture type is. `Primary` is the main texture used by a skin, while `Secondary` is any additional textures used by the skin. `Secondary` textures will have half the resolution of a `Primary` texture for PS2, PSP, and GameCube
	- **Character Size**: Select the size of the character. `Standard` will apply to most characters. `Large` is for special bosses and enemies, like Galactus, Master Mold, Ymir, or Sentinels. If `Large` is selected, the texture for PS2 will be exported at the current size (regardless of what it is), and PSP/GameCube textures will be half that size. If `Standard` is selected, PS2 textures will be limited to a max size of 256x256 (unless additional modifiers are selected for **Skin Type** or **Texture Type** that will reduce the texture size), and PSP/GameCube textures will be half that size.
	- **Alchemy Version**: Select which version of the Alchemy Exporter is in your 3ds Max installation. If `Alchemy 2.5` is selected and `All` is selected for the **Console**, the texture will be exported for PC, GameCube, PS2, PSP, Wii, and Xbox. If `Alchemy 5` is selected and `All` is selected for the **Console**, the texture will be exported for PC, Next-Gen console MUA1, PS2, PSP, and Wii. 
	  - **Note**: If textures are being made for Next-Gen console MUA1, with `Alchemy 2.5`, the PC texture can be used. If the texture is over 256x256 for primary textures or over 128x128 for secondary textures, the texture exported to the `MUA1 PC` folder can be used without modification. If the texture is 256x256 or less for primary textures or 128x128 or less for secondary textures, the texture exported to the `PC` folder can be used, but the texture must be converted from PNG8 to DXT1 in Alchemy 5. Because other optimizations are needed to use Alchemy 2.5 models in Next-Gen console MUA1, this procedure can be added to those optimizations.
	- **PSP Texture Format**: Choose which texture format should be used for the PSP. `PNG4` will export to a PNG4 texture (16 colors), while `PNG8` will export to a PNG8 texture (256 colors). Both are used in MUA1 PSP, so the choice is up to you. PNG8 textures have a higher file size. 
	- For an explanation on how these options impact each console, see below for the list of texture types.
4. The .xcf will be saved, the image will be flattened, and several additional operations will be run while the texture is being exported to the various folders in different formats. The operations will depend on the options selected. Textures that are the same will be grouped together. See below for a list of the texture types that will be exported for each console. 
5. All the steps are part of one undo group and can be undone with Ctrl+Z. Use this after running the script to return to the original state of the image and edit it further, if needed.

## Export Types
 - **MUA1 PC**: The texture format will depend on the option selected for **Texture Type**. 
   - **Console**: No impact on MUA1 PC textures.
   - **Character Size**: No impact on MUA1 PC textures.
   - **Skin Type**: No impact on MUA1 PC textures.
   - **Texture Type**: If `Primary` is selected, textures above 256x256 will export as RGB DXT1 .dds textures, and textures that are 256x256 or smaller will export as PNG8 textures. If `Secondary` is selected, textures above 128x128 will export as RGB DXT1 .dds textures, and textures that are 128x128 or smaller will export as PNG8 textures.
   - **Alchemy Version**: No impact on MUA1 PC textures. 
   - **PSP Texture Format**: No impact on MUA1 PC textures.
 - **XML2 PC**: The texture format will depend on the option selected for **Texture Type**. 
   - **Console**: No impact on XML2 PC textures.
   - **Character Size**: No impact on XML2 PC textures.
   - **Skin Type**: No impact on XML2 PC textures.
   - **Texture Type**: If `Primary` is selected, textures above 256x256 will export as RGB DXT1 .dds textures, and textures that are 256x256 or smaller will export as PNG8 textures. If `Secondary` is selected, textures above 128x128 will export as RGB DXT1 .dds textures, and textures that are 128x128 or smaller will export as PNG8 textures.
   - **Alchemy Version**: If `Alchemy 2.5` is selected, XML2 PC textures will be exported. If `Alchemy 5` is selected, XML2 PC textures will not be exported.
   - **PSP Texture Format**: No impact on XML2 PC textures.
 - **GameCube**: The texture will export as a PNG8 texture regardless of the options selected.
   - **Console**: If `All` is selected, GameCube textures will be exported. If `PC Only` is selected, GameCube textures will not be exported.
   - **Character Size**: If `Standard` is selected, the max texture size for GameCube will be 128x128. If `Large` is selected, the GameCube texture will be exported at half the size of the original texture. **Skin Type** and **Texture Type** can reduce this size further.
   - **Skin Type**: If `Primary` is selected, the texture size for GameCube will not be reduced. If `Secondary` is selected, the texture size for GameCube will be reduced to half dimensions.
   - **Texture Type**: If `Primary` is selected, the texture size for GameCube will not be reduced. If `Secondary` is selected, the texture size for GameCube will be reduced to half dimensions.
   - **Alchemy Version**: If `Alchemy 2.5` is selected, GameCube textures will be exported. If `Alchemy 5` is selected, GameCube textures will not be exported.
   - **PSP Texture Format**: No impact on GameCube textures.
 - **PS2**: The texture will export as a PNG8 texture regardless of the options selected.
   - **Console**: If `All` is selected, PS2 textures will be exported. If `PC Only` is selected, PS2 textures will not be exported.
   - **Character Size**: If `Standard` is selected, the max texture size for PS2 will be 256x256. If `Large` is selected, the PS2 texture will be exported at the size of the original texture. **Skin Type** and **Texture Type** can reduce this size further.
   - **Skin Type**: If `Primary` is selected, the texture size for PS2 will not be reduced. If `Secondary` is selected, the texture size for PS2 will be reduced to half dimensions.
   - **Texture Type**: If `Primary` is selected, the texture size for PS2 will not be reduced. If `Secondary` is selected, the texture size for PS2 will be reduced to half dimensions.
   - **Alchemy Version**: No impact on PS2 textures.
   - **PSP Texture Format**: No impact on PS2 textures.
 - **PSP**: The texture format will depend on the option selected for **PSP Texture Format**.
   - **Console**: If `All` is selected, PSP textures will be exported. If `PC Only` is selected, PSP textures will not be exported.
   - **Character Size**: If `Standard` is selected, the max texture size for PSP will be 128x128. If `Large` is selected, the PSP texture will be exported at half the size of the original texture. **Skin Type** and **Texture Type** can reduce this size further.
   - **Skin Type**: If `Primary` is selected, the texture size for PSP will not be reduced. If `Secondary` is selected, the texture size for PSP will be reduced to half dimensions.
   - **Texture Type**: If `Primary` is selected, the texture size for PSP will not be reduced. If `Secondary` is selected, the texture size for PSP will be reduced to half dimensions.
   - **Alchemy Version**: No impact on PSP textures. 
   - **PSP Texture Format**: If `PNG4` is selected, the textures for PSP will be exported as PNG4 textures. If `PNG8` is selected, the textures for PSP will be exported as PNG8 textures. 
 - **Wii**: The texture will export as an RGB DXT1 .dds texture regardless of the options selected.
   - **Console**: If `All` is selected, Wii textures will be exported. If `PC Only` is selected, Wii textures will not be exported.
   - **Character Size**: No impact on Wii textures.
   - **Skin Type**: No impact on Wii textures.
   - **Texture Type**: If `Primary` is selected, the texture size for Wii will not be reduced. If `Secondary` is selected, the texture size for Wii will be reduced to half dimensions.
   - **Alchemy Version**: No impact on Wii textures.
   - **PSP Texture Format**: No impact on Wii textures.
 - **Xbox**: The texture format will depend on the option selected for **Texture Type**. 
   - **Console**: If `All` is selected, Xbox textures will be exported. If `PC Only` is selected, Xbox textures will not be exported.
   - **Character Size**: No impact on Xbox textures.
   - **Skin Type**: No impact on Xbox textures.
   - **Texture Type**: If `Primary` is selected, textures above 256x256 will export as RGB DXT1 .dds textures, and textures that are 256x256 or smaller will export as PNG8 textures. If `Secondary` is selected, textures above 128x128 will export as RGB DXT1 .dds textures, and textures that are 128x128 or smaller will export as PNG8 textures.
   - **Alchemy Version**: If `Alchemy 2.5` is selected, Xbox textures will be exported. If `Alchemy 5` is selected, Xbox textures will not be exported.
   - **PSP Texture Format**: No impact on Xbox textures.
## Credits
- BaconWizard17: Script creation