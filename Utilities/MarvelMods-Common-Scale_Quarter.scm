; Scales image to a quarter of its original size
(define (script-fu-mua-xml2-scale-quarter image)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(let*
		(
			(newWidth (car (gimp-image-width image)))
			(newHeight (car (gimp-image-height image)))
		)
		(gimp-image-scale image (/ newWidth 4) (/ newHeight 4))
	)
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-mua-xml2-scale-quarter"
    "Scale to Quarter Size"
    "Scales an image to quarter its size."
    "BaconWizard17"
    "BaconWizard17"
    "August 2022"
    "*"
	SF-IMAGE        "Image"       0
    SF-DRAWABLE     "Layer"       0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-mua-xml2-scale-quarter" "<Image>/Marvel Mods/Utilities")