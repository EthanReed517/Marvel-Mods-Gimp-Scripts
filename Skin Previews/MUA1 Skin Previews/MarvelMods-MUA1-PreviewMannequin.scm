; MUA1 mannequin Preview Crop
(define (script-fu-mua1-mannequin-preview image layer)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(gimp-image-resize image 493 981 -713 -0)
	(gimp-layer-resize-to-image-size layer)
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-mua1-mannequin-preview"
    "MUA1 Mannequin Preview Crop"
    "Crops the preview window for MUA1 mannequins."
    "BaconWizard17"
    "BaconWizard17"
    "September 2021"
    "*"
    SF-IMAGE        "Image"       0
    SF-DRAWABLE     "Layer"       0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-mua1-mannequin-preview" "<Image>/Marvel Mods (Legacy)/Skin Previews/MUA1 PC")