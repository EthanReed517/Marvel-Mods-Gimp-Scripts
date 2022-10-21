; Prepare 4-3 Standard Definition Loading Screen for Export
(define (script-fu-marvel-mods-4-3-SD-LS image layer)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(gimp-image-merge-visible-layers image 2)
	(let*
		(
			(squareSize (car (gimp-image-height image)))
		)
		(gimp-image-scale image squareSize squareSize)
	)
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-marvel-mods-4-3-SD-LS"
    "4-3 SD Load Screen Export Prep"
    "Collapses layers and scales to 1024x1024"
    "BaconWizard17"
    "BaconWizard17"
    "February 2022"
    "*"
	SF-IMAGE        "Image"       0
    SF-DRAWABLE     "Layer"       0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-marvel-mods-4-3-SD-LS" "<Image>/Marvel Mods/Utilities/Loading Screens")