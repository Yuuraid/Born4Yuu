transform shake:
        linear 0.05 xoffset 15
        linear 0.05 xoffset -15
        linear 0.05 xoffset 10
        linear 0.05 xoffset -10
        linear 0.05 xoffset 0
transform panorama_kiri_ke_kanan:
        xanchor 0.0 xpos 0.0
        linear 4.0 xanchor 1.0 xpos 1.0

# Overshoot jump (sprite enters quickly and slightly overshoots its height before settling)
transform jump_in_bottom(xalign_pos=0.5, duration=0.5):
    yanchor 1.0
    xanchor 0.5
    xpos xalign_pos
    ypos 1.5           # Start off-screen below
    alpha 0.0          # Hidden initially
    
    easein_back duration ypos 1.0 alpha 1.0   # Adjust speed (0.5s) as needed

transform jump_in_right(xalign_pos=0.75, duration=0.5):
    yanchor 1.0
    xanchor 0.5
    xpos xalign_pos
    ypos 1.5          
    alpha 0.0         
    
    easein_back duration ypos 1.0 alpha 1.0

transform speaking:
    matrixcolor None
    parallel:
        easein 1.5 yoffset 20
        easeout 1 yoffset 0
        repeat

transform idle:
    matrixcolor TintMatrix("#777777") # Hex color code to darken/tint the sprite

transform silhouette:
    matrixcolor TintMatrix("#000000")

# Define the transition using your gradient image
define eye_open = ImageDissolve("assets/effects/eye_mask.png", 1.0, ramplen=64)
define eye_close = ImageDissolve("assets/effects/eye_mask.png", 1.0, ramplen=64, reverse=True)

# Define a repeatable transform for pacing/looking around
transform pacing_left_right:
    # Start at center
    xoffset 0
    # Move right
    ease 0.6 xoffset 80
    pause 0.2
    # Move left past center
    ease 1.2 xoffset -80
    pause 0.2
    # Move back to center
    ease 0.6 xoffset 0
    # Repeat the loop
    repeat

# Modal Item
screen show_item(item_img, item_name=""):

    modal True

    add Solid("#00000088")

    frame:
        xalign 0.5
        yalign 0.2
        padding (30, 30)

        vbox:
            spacing 15
            xalign 0.5

            textbutton "X":
                xalign 1.0
                yalign 0.0
                action Hide("show_item")

            add item_img:
                xalign 0.5

            if item_name:
                text item_name:
                    xalign 0.5
                    size 28

transform dash_right:
    # Set the starting X position
    xpos 0.1
    # Smoothly move to the end X position over 0.4 seconds
    easein 0.4 xpos 0.7

# Create a composite image with delayed afterimages
image eileen_dash = Fixed(
    # Ghost 3 (Farthest back, lowest opacity, delayed start)
    At("eileen", Transform(alpha=0.25, matrixcolor=TintMatrix("#4a90e2"))),
    # Ghost 2 (Middle afterimage)
    At("eileen", Transform(alpha=0.45, matrixcolor=TintMatrix("#7eb0ee"))),
    # Ghost 1 (Closest afterimage)
    At("eileen", Transform(alpha=0.65)),
    # Main Sprite (Front layer)
    "eileen",
    fit_first=True
)