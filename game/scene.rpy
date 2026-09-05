# Define the transition using your gradient image
define eye_open = ImageDissolve("assets/effects/eye_mask.png", 1.0, ramplen=64)
define eye_close = ImageDissolve("assets/effects/eye_mask.png", 1.0, ramplen=64, reverse=True)
