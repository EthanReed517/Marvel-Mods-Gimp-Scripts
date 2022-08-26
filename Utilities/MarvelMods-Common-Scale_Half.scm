; Flattens layers and converts to indexed palette with 256 colors
(define (script-fu-mua-xml2-scale-half image)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(let*
		(
			(newWidth (car (gimp-image-width image)))
			(newHeight (car (gimp-image-height image)))
		)
		(gimp-image-scale image (/ newWidth 2) (/ newHeight 2))
	)
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-mua-xml2-scale-half"
    "Scale to Half Size"
    "Scales an image to half its size."
    "BaconWizard17"
    "BaconWizard17"
    "August 2022"
    "*"
	SF-IMAGE        "Image"       0
    SF-DRAWABLE     "Layer"       0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-mua-xml2-scale-half" "<Image>/Marvel Mods/Utilities")