; Prepare 16-9 Standard Definition Loading Screen for Export
(define (script-fu-marvel-mods-16-9-SD-LS image layer)
	(gimp-image-undo-group-start image)
	(gimp-selection-none image)
	(gimp-image-merge-visible-layers image 2)
	(let*
		(
			(squareSize (car (gimp-image-height image)))
		)
		(gimp-image-scale image (* squareSize 2) squareSize)
	)
    (set! layer (car (gimp-image-get-active-layer image)))
    (plug-in-colors-channel-mixer RUN-NONINTERACTIVE image layer FALSE 0 0 1 0 1 0 1 0 0)
	(gimp-displays-flush)
	(gimp-image-undo-group-end image)
)
; populate script registration information
(script-fu-register 
    "script-fu-marvel-mods-16-9-SD-LS"
    "16-9 SD Load Screen Export Prep"
    "Collapses layers, RGB-BGR swaps, and scales to 2048x1024"
    "BaconWizard17"
    "BaconWizard17"
    "February 2022"
    "*"
	SF-IMAGE        "Image"          0
    SF-DRAWABLE     "Layer"          0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-marvel-mods-16-9-SD-LS" "<Image>/Marvel Mods/Utilities/Loading Screens")