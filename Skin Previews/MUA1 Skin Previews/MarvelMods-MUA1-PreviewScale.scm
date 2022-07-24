; MUA1 Skin Preview Crop
(define (script-fu-mua-preview-scale image layer)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(gimp-image-scale image 543 1080)
	(gimp-layer-resize-to-image-size layer)
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-mua-preview-scale"
    "MUA1 Preview Scale"
    "Scales MUA1 previews to 543x1080."
    "BaconWizard17"
    "BaconWizard17"
    "September 2021"
    "*"
    SF-IMAGE        "Image"       0
    SF-DRAWABLE     "Layer"       0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-mua-preview-scale" "<Image>/Marvel Mods/Skin Previews/MUA1 PC")