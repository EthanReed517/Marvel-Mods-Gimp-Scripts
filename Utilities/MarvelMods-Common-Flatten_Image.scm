; Flattens layers and converts to indexed palette with 256 colors
(define (script-fu-mua-xml2-flatten-image image layer)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(gimp-image-flatten image)
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-mua-xml2-flatten-image"
    "Flatten Image"
    "Flattens image."
    "BaconWizard17"
    "BaconWizard17"
    "December 2022"
    "*"
	SF-IMAGE        "Image"       0
    SF-DRAWABLE     "Layer"       0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-mua-xml2-flatten-image" "<Image>/Marvel Mods/Utilities")