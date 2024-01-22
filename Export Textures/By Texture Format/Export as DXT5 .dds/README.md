# Marvel Mods GIMP Plugins
by BaconWizard17
## Export to DXT5 .dds
This plugin exports a texture to DXT5 format

### Compatibility
This script will only work correctly if the image has been saved as a .xcf file. 

### Installation
 1. This script can be installed using `runUpdateAdmin.bat` from my scripts, or it can be placed individually in your GIMP plugins directory. The standard location for this is `C:\Users\(your user)\AppData\Roaming\GIMP\2.10\plug-ins`. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to export. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Export Textures/By Texture Format` and choose the `Export as DXT5 .dds` plugin.
3. A dialog will appear with options. You can toggle the following options:
  - If the image will be saved with RGB colors (for use with XML2 PC, or for MUA1 PC or Next-Gen if Alchemy 5 is being used)
  - If the image will be saved with BGR colors (for use with MUA1 PC or Next-Gen if Alchemy 2.5 is being used)
  - If the image is to be flattened during export (will merge all layers and remove transparency)
4. The .xcf will be saved, and then the image will be flattened (if the option is chosen). If RGB export is selected, the image will be exported as a DXT5 dds to a `DXT5 RGB` folder in the same location as the .xcf file. If BGR export is selected, the image will be RGB-BGR swapped and then exported as a DXT5 dds to a `DXT5 RGB-BGR Swapped` folder in the same location as the .xcf file.
5. All the steps are part of one undo group and can be undone with Ctrl+Z. Use this after running the script to return to the original state of the image and edit it further, if needed.

## Credits
- BaconWizard17: Script creation