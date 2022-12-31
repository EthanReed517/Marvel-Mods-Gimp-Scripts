; Flattens layers and converts to indexed palette with 256 colors
(define (script-fu-mua-xml2-convert-BGR image layer)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(gimp-image-flatten image)
    (set! layer (car (gimp-image-get-active-layer image)))
    (plug-in-colors-channel-mixer RUN-NONINTERACTIVE image layer FALSE 0 0 1 0 1 0 1 0 0)
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-mua-xml2-convert-BGR"
    "RGB-BGR Swap"
    "Performs an RGB-BGR swap on the image."
    "BaconWizard17"
    "BaconWizard17"
    "September 2021"
    "*"
	SF-IMAGE        "Image"       0
    SF-DRAWABLE     "Layer"       0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-mua-xml2-convert-BGR" "<Image>/Marvel Mods (Legacy)/Utilities")