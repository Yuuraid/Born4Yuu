# image shark = "assets/sprite/Shark/shark_main_netral.png"
# image hiu = "assets/sprite/Shark/shark_main_hiu.png"


label shark_transform_01:
    show hiu at right
    "What? shark is evolving!"

    # Hide base sprite and show evolution animation
    hide hiu

    # Alternate showing and hiding both sprites rapidly
    show hiu at pokemon_evolution, right
    pause 1.2
    hide hiu

    show shark at pokemon_evolution, right
    pause 1.0

    # Keep final evolved form visible
    show shark at right
    "Congratulations! Your Charmander evolved into hiu!"

# White silhouette effect for Gen 3/4 style
# Define a quick white flash transition
define Flash = Fade(0.1, 0.0, 0.3, color="#ffffff")

# Turn sprite into solid white silhouette
transform silhouette_white:
    matrixcolor BrightnessMatrix(1.0)

label evolve_sequence:
    show shark_b_sequence at right
    # "What? shark_b_sequence is evolving!"

    # 1. Turn into white silhouette
    show shark_b_sequence at silhouette_white, right
    with Dissolve(0.4)

    # 2. Rapid flicker loop
    $ count = 0
    while count < 5:
        show shark_b_sequence at silhouette_white, right
        hide shark_n_sequence
        pause 0.12 - (count * 0.015)
        
        show shark_n_sequence at silhouette_white, right
        hide shark_b_sequence
        pause 0.12 - (count * 0.015)
        
        $ count += 1

    # 3. Flash to reveal full color final form
    hide shark_b_sequence
    show shark_n_sequence at right
    with Flash

    # "Congratulations! Your hiu evolved into shark_n_sequence!"

    return

label evolve_sequence_:
    show hiu at right
    "What? hiu is evolving!"

    # 1. Turn into white silhouette
    show hiu at silhouette_white, right
    with Dissolve(0.4)

    # 2. Rapid flicker loop
    $ count = 0
    while count < 5:
        show hiu at silhouette_white, right
        hide shark
        pause 0.12 - (count * 0.015)
        
        show shark at silhouette_white, right
        hide hiu
        pause 0.12 - (count * 0.015)
        
        $ count += 1

    # 3. Flash to reveal full color final form
    hide hiu
    show shark at right
    with Flash

    "Congratulations! Your hiu evolved into shark!"

    return