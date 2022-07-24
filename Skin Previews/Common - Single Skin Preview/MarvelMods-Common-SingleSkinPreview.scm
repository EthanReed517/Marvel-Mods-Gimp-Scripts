;Single skin preview for XML2/MUA1 skins
(define (script-fu-mua-xml2-single-preview)
	(let*
		(
			; define our local variables
			; create a new image:
			(theImageWidth  543)
			(theImageHeight 1080)
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
			(backgroundLayer
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
			;layer that holds the portraits
			(portraitLayer
				(car
					(gimp-layer-new
						theImage
						theImageWidth
						theImageHeight
						RGBA-IMAGE
						"portraits"
						100
						LAYER-MODE-NORMAL
					)
				)
			)
		) ;end of our local variables
		; add the layers
		(gimp-image-add-layer theImage backgroundLayer 0)
		(gimp-image-add-layer theImage portraitLayer 0)
		; add the guides
		(gimp-image-add-hguide theImage 100)
		(gimp-image-add-hguide theImage 250)
		(gimp-image-add-hguide theImage 1080)
		(gimp-image-add-vguide theImage 100)
		(gimp-image-add-vguide theImage 272)
		(gimp-image-add-vguide theImage 443)
		(gimp-image-add-vguide theImage 543)
		(gimp-image-set-active-layer theImage backgroundLayer)
		; show the new image on the screen
		(gimp-display-new theImage)
    )
)
; populate script registration information
(script-fu-register 
    "script-fu-mua-xml2-single-preview"
    "Single Skin Preview"
    "Creates an image for a preview for 1 skin."
    "BaconWizard17"
    "BaconWizard17"
    "September 2021"
    ""
)
; register the script within gimp menu
(script-fu-menu-register "script-fu-mua-xml2-single-preview" "<Image>/Marvel Mods/Skin Previews/Single Skin Showcase")