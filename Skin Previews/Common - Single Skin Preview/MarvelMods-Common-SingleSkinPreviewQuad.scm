; Quad grid skin preview for XML2/MUA1 skins
(define (script-fu-mua-xml2-quad-preview image layer)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(gimp-image-resize image 1086 2160 0 0)
	(gimp-layer-resize-to-image-size layer)
	(gimp-image-add-vguide image 643)
	(gimp-image-add-vguide image 815)
	(gimp-image-add-vguide image 986)
	(gimp-image-add-vguide image 1086)
	(gimp-image-add-hguide image 1180)
	(gimp-image-add-hguide image 1430)
	(gimp-image-add-hguide image 2160)
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-mua-xml2-quad-preview"
    "Quad Skin Preview"
    "Resizes the canvas to showcase four images of a skin."
    "BaconWizard17"
    "BaconWizard17"
    "September 2021"
    "*"
	SF-IMAGE        "Image"       0
    SF-DRAWABLE     "Layer"       0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-mua-xml2-quad-preview" "<Image>/Marvel Mods/Skin Previews/Single Skin Showcase")