; MUA1 Skin Preview Crop
(define (script-fu-mua-skin-preview image layer)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(gimp-image-resize image 395 785 -339 -196)
	(gimp-layer-resize-to-image-size layer)
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-mua-skin-preview"
    "MUA1 Skin Preview Crop"
    "Crops the preview window for MUA1 skins."
    "BaconWizard17"
    "BaconWizard17"
    "September 2021"
    "*"
    SF-IMAGE        "Image"       0
    SF-DRAWABLE     "Layer"       0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-mua-skin-preview" "<Image>/Marvel Mods/Skin Previews/MUA1 PC")