; XML2 Character Select Portrait Preview Crop
(define (script-fu-xml2-csp-preview image layer)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(gimp-image-resize image 163 163 -360 -320)
	(gimp-layer-resize-to-image-size layer)
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-xml2-csp-preview"
    "XML2 Character Select Portrait Preview Crop"
    "Crops the preview window for XML2 character select portraits."
    "BaconWizard17"
    "BaconWizard17"
    "September 2021"
    "*"
    SF-IMAGE        "Image"       0
    SF-DRAWABLE     "Layer"       0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-xml2-csp-preview" "<Image>/Marvel Mods (Legacy)/Skin Previews/XML2 PC")