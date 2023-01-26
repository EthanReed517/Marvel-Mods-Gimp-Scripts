# Marvel Mods GIMP Plugins
by BaconWizard17
## Export Single Skin Preview
This plugin exports a single skin showcase in 3 different sizes for different uses. 

### Compatibility
This script will only work correctly on a single skin showcase that was assembled using my scripts. It can have 1 or 2 rows/columns of 543x1080 previews. The image must be saved already. Generally, I save it as "Preview.xcf".

### Installation
 1. This script can be installed using `runUpdateAdmin.bat` from my scripts, or it can be placed individually in your GIMP plugins directory. The standard location for this is `C:\Users\(your user)\AppData\Roaming\GIMP\2.10\plug-ins`. Check the main `README.md` file in this project for more details on proper installation.

### Usage
1. Start with an image open in GIMP that you would like to scale. See the "Compatibility" section above for details on the image type.
2. In the toolbar, go to `Marvel Mods/Skin Previews/Skin Showcase` and choose the `Export Single Skin Preview` plugin.
3. The image will export at its original size to a file called `(filename)_3Full.png`, then it will be cropped to 543x1080 (the top left image) and exported as `(filename)_2HalfLarge.png`, and then it will be scaled to 251x1080 and exported as `(filename)_1HalfSmall.png`. 
4. The `_1HalfSmall` image is what I display on [my thread at MarvelMods.com](https://marvelmods.com/forum/index.php/topic,10629.0.html). The `_3Full` image is the full-sized preview that's linked when the `_1HalfSmall` images on my thread are clicked. The `_2HalfLarge` previews are used for the Visual Skin Catalog.
5. All the steps are part of one undo group and can be undone with Ctrl+Z.

## Credits
- BaconWizard17: Script creation