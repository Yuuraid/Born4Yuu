
# transform panorama_kiri_ke_kanan:
#     xanchor 0.0 xpos 0.0
#     linear 4.0 xanchor 1.0 xpos 1.0



# transform dash_right:
#     # Set the starting X position
#     xpos 0.1
#     # Smoothly move to the end X position over 0.4 seconds
#     easein 0.4 xpos 0.7

# # Create a composite image with delayed afterimages
# image eileen_dash = Fixed(
#     # Ghost 3 (Farthest back, lowest opacity, delayed start)
#     At("eileen", Transform(alpha=0.25, matrixcolor=TintMatrix("#4a90e2"))),
#     # Ghost 2 (Middle afterimage)
#     At("eileen", Transform(alpha=0.45, matrixcolor=TintMatrix("#7eb0ee"))),
#     # Ghost 1 (Closest afterimage)
#     At("eileen", Transform(alpha=0.65)),
#     # Main Sprite (Front layer)
#     "eileen",
#     fit_first=True
# )

# A static blur (change 6 to a higher/lower number for more/less blur)
transform blurred:
    blur 30

# An animated transition that goes from clear to blurry over 1.0 second
transform enblur:
    blur 0
    linear 1.0 blur 30

# An animated transition that goes from blurry back to clear over 1.0 second
transform deblur:
    blur 30
    linear 1.0 blur 0