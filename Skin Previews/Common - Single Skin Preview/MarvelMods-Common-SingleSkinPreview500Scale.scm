; Scale preview to 500 tall for XML2/MUA1 skins
(define (script-fu-mua-xml2-scale-preview image layer)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(gimp-image-scale image 251 500)
	(gimp-layer-resize-to-image-size layer)
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-mua-xml2-scale-preview"
    "Scale Preview to 500"
    "Scales the skin preview to 251x500."
    "BaconWizard17"
    "BaconWizard17"
    "September 2021"
    "*"
	SF-IMAGE        "Image"       0
    SF-DRAWABLE     "Layer"       0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-mua-xml2-scale-preview" "<Image>/Marvel Mods (Legacy)/Skin Previews/Single Skin Showcase")