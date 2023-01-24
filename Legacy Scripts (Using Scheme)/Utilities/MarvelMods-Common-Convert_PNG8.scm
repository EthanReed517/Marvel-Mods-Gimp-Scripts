; Flattens layers and converts to indexed palette with 256 colors
(define (script-fu-mua-xml2-convert-png8 image layer)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(gimp-image-flatten image)
	(gimp-convert-indexed image 0 0 256 0 0 "A")
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-mua-xml2-convert-png8"
    "Convert to PNG8"
    "Flattens image, converts to indexed palette with 256 colors."
    "BaconWizard17"
    "BaconWizard17"
    "September 2021"
    "*"
	SF-IMAGE        "Image"       0
    SF-DRAWABLE     "Layer"       0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-mua-xml2-convert-png8" "<Image>/Marvel Mods (Legacy)/Utilities")