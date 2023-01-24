; XML2 Conversation Portrait Preview Crop
(define (script-fu-xml2-convo-preview image layer)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(gimp-image-resize image 152 152 -280 -496)
	(gimp-layer-resize-to-image-size layer)
	(gimp-image-select-ellipse image 0 0 0 152 152)
	(gimp-selection-invert image)
	(gimp-drawable-edit-clear layer)
	(gimp-selection-none image)	
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-xml2-convo-preview"
    "XML2 Conversation Portrait Preview Crop"
    "Crops the preview window for XML2 conversation portraits."
    "BaconWizard17"
    "BaconWizard17"
    "September 2021"
    "*"
    SF-IMAGE        "Image"       0
    SF-DRAWABLE     "Layer"       0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-xml2-convo-preview" "<Image>/Marvel Mods (Legacy)/Skin Previews/XML2 PC")