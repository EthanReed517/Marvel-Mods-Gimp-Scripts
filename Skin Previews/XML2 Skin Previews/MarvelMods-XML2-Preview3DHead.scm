; XML2 3D Head Preview Crop
(define (script-fu-xml2-3dhead-preview image layer)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(gimp-image-resize image 141 141 -146 -777)
	(gimp-layer-resize-to-image-size layer)
	(gimp-image-select-ellipse image 0 0 0 141 141)
	(gimp-selection-invert image)
	(gimp-drawable-edit-clear layer)
	(gimp-selection-none image)	
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-xml2-3dhead-preview"
    "XML2 3D Head Preview Crop"
    "Crops the preview window for XML2 3d heads."
    "BaconWizard17"
    "BaconWizard17"
    "September 2021"
    "*"
    SF-IMAGE        "Image"       0
    SF-DRAWABLE     "Layer"       0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-xml2-3dhead-preview" "<Image>/Marvel Mods (Legacy)/Skin Previews/XML2 PC")