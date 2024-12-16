# Marvel Mods GIMP Plugins
by BaconWizard17
## Create All MUA1 Previews
This plugin takes a file with layers consisting of MUA1 screenshots, individually exports them appropriately cropped and named, and then exports a combined preview image with all skin elements.

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. All screenshots should be taken with the resolution set to 1920x1080. The screenshots should be taken at the following times:
- Skins: Taken in the character select screen when the character's details are being viewed.
- HUDs: Taken during normal gameplay when one character is on the team.
- Mannequins: Taken in the character select screen when the mannequin is highlighted.

Each screenshot must go on its own layer, and the layers must be named accordingly for them to be assembled properly. See "Layer Setup", below, for more information. An example (`example.xcf`) is provided to help.

### Installation
 1. This script can be installed using `update.bat` from the main folder of this release. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to crop and combine. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Skin Previews/Crop Screenshots - MUA1` and choose the `Create All Previews` plugin.
3. Each layer will be cropped and exported according to the information in the layer name. 
4. After each layer is cropped and exported, the resulting images will be combined into the proper preview.

### Layer Setup
For the screenshots to export and combine properly, the layers should be named properly. For an example, see the `Example.xcf` file. Each layer should contain a screenshot that has not been cropped. The layers should be named with the following naming convention:
`(asset type),(skin number),(row),(column),(position),(descriptor)`
Each value should be populated as follows:
- `(asset type)`: can be `Skin` (for skins), `Mann` (for mannequins), or `HUD` for HUDs.
- `(skin number)`: The 4 or 5 digit skin number. Can end in XX or be a full number.
- `(row)`: Must be an integer, 1 or greater. This corresponds to the row in the combined preview image where this image will appear.
- `(column)`: Must be an integer, 1 or greater. This corresponds to the column in the combined preview image where this image will appear.
- `(position)`: Must be an integer. For skins and mannequins, this should be 0. For HUDs, it can be between 1 and 5, and it corresponds with the position of the portrait within the row/column on the combined preview.
   - 1: top left spot
   - 2: top middle spot
   - 3: top right spot
   - 4: bottom left spot
   - 5: bottom right spot
- `(descriptor)`: An additional descriptor for the model. For example, a next-gen style hud could have a descriptor that says `Next-Gen Style`. Put `None` if there isn't an additional descriptor.

## Credits
- BaconWizard17: Script creation