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