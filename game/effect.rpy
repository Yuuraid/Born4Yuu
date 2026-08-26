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
transform jump_in_bottom(xalign_pos=0.5):
    yanchor 1.0
    xanchor 0.5
    xpos xalign_pos
    ypos 1.5           # Start off-screen below
    alpha 0.0          # Hidden initially
    
    easein_back 0.5 ypos 1.0 alpha 1.0   # Adjust speed (0.5s) as needed

transform speaking:
    matrixcolor None
    parallel:
        easein 1.5 yoffset 20
        easeout 1 yoffset 0
        repeat

transform idle:
    matrixcolor TintMatrix("#777777") # Hex color code to darken/tint the sprite