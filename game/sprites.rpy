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

transform reveal_character:
    matrixcolor None