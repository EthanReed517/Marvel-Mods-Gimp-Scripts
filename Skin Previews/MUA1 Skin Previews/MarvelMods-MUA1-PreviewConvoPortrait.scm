; MUA1 Conversation Portrait Preview Crop
(define (script-fu-mua1-convo-preview image layer)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(gimp-image-resize image 169 169 -90 -850)
	(gimp-layer-resize-to-image-size layer)
	(gimp-image-select-ellipse image 0 0 0 169 169)
	(gimp-selection-invert image)
	(gimp-drawable-edit-clear layer)
	(gimp-selection-none image)	
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-mua1-convo-preview"
    "MUA1 Conversation Portrait Preview Crop"
    "Crops the preview window for MUA1 conversation portraits."
    "BaconWizard17"
    "BaconWizard17"
    "September 2021"
    "*"
    SF-IMAGE        "Image"       0
    SF-DRAWABLE     "Layer"       0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-mua1-convo-preview" "<Image>/Marvel Mods/Skin Previews/MUA1 PC")