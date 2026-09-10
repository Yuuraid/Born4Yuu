transform shake:
    linear 0.05 xoffset 15
    linear 0.05 xoffset -15
    linear 0.05 xoffset 10
    linear 0.05 xoffset -10
    linear 0.05 xoffset 0

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

transform ease_custom(start, end, time):
    subpixel True
    start
    easein time end

transform flip_loop_left:
    # Start at center
    xoffset 0
    xzoom 1.0

    # Move right
    xzoom -1.0
    ease 0.6 xoffset 80
    pause 0.2
    
    # Move left past center
    xzoom 1.0
    ease 1.2 xoffset -80
    pause 0.2
    
    # Move back to center
    xzoom -1.0
    ease 0.6 xoffset 0
    # Repeat the loop
    repeat

transform face_default:
    xzoom 1.0  # Default orientation

transform face_flip:
    xzoom -1.0 # Horizontally mirrored orientation

transform fall_down:
    # Keeps the sprite's horizontal position but starts at the default vertical position
    yanchor 0.0
    ypos 0.0
    # Smoothly moves the sprite completely below the screen (ypos 1.5) over 0.6 seconds
    easein 0.6 ypos 1.5