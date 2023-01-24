; 4x2 grid skin preview for XML2/MUA1 skins
(define (script-fu-mua-xml2-4x2-preview)
	(let*
		(
			; define our local variables
			; create a new image:
			(theImageWidth  2172)
			(theImageHeight 2160)
			(theImage
				(car
					(gimp-image-new
						theImageWidth
						theImageHeight
						RGB
					)
				)
			)
			; background layer
			(theLayer
				(car
					(gimp-layer-new
						theImage
						theImageWidth
						theImageHeight
						RGBA-IMAGE
						"Background"
						100
						LAYER-MODE-NORMAL
					)
				)
			)
		) ;end of our local variables
		; add the layers
		(gimp-image-add-layer theImage theLayer 0)
		; add the guides
		(gimp-image-add-hguide theImage 1080)
		(gimp-image-add-vguide theImage 543)
		(gimp-image-add-vguide theImage 1086)
		(gimp-image-add-vguide theImage 1629)
		; show the new image on the screen
		(gimp-display-new theImage)
    )
)
; populate script registration information
(script-fu-register 
    "script-fu-mua-xml2-4x2-preview"
    "4x2 Skin Preview"
    "Creates an image for a 4x2 grid preview for 8 skins."
    "BaconWizard17"
    "BaconWizard17"
    "September 2021"
    ""
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-mua-xml2-4x2-preview" "<Image>/Marvel Mods (Legacy)/Skin Previews/Multi Skin Showcase")