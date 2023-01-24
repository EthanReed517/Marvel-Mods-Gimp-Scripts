; XML2 Skin Preview Crop
(define (script-fu-xml2-skin-preview image layer)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(gimp-image-resize image 543 1080 -222 -0)
	(gimp-layer-resize-to-image-size layer)
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-xml2-skin-preview"
    "XML2 Skin Preview Crop"
    "Crops the preview window for XML2 skins."
    "BaconWizard17"
    "BaconWizard17"
    "September 2021"
    "*"
    SF-IMAGE        "Image"       0
    SF-DRAWABLE     "Layer"       0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-xml2-skin-preview" "<Image>/Marvel Mods (Legacy)/Skin Previews/XML2 PC")