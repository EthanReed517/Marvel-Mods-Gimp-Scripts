; Marvel Ultimate Alliance Blue Outline Glow
(define (script-fu-mua-glow-blue image drawable)
	(script-fu-drop-shadow image drawable 0 0 20 '(116 201 245) 100 0)
)
(script-fu-register 
    "script-fu-mua-glow-blue"
    "MUA Portrait Outline - Blue Glow"
    "Adds a blue glow around the portrait."
    "BaconWizard17"
    "BaconWizard17"
    "September 2021"
    "*"
	SF-IMAGE       "Input image" 0
	SF-DRAWABLE    "Input drawable" 0
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-mua-glow-blue" "<Image>/Marvel Mods (Legacy)/Utilities/Portraits/")