# Define the transition using your gradient image
define eye_open = ImageDissolve("assets/effects/eye_mask.png", 1.0, ramplen=64)
define eye_close = ImageDissolve("assets/effects/eye_mask.png", 1.0, ramplen=64, reverse=True)

define wipe_test = ImageDissolve("assets/effects/Apho_RenPyImageDissolveTransitions/wiperd.png", 0.2, ramplen=64, reverse=True)

init python:
    def wipe_j_atas(time=0.15):
        return ImageDissolve("assets/effects/Apho_RenPyImageDissolveTransitions/wiperd.png", time, ramplen=64, reverse=True)
    def wipe_j_bawah(time=0.15):
        return ImageDissolve("assets/effects/Apho_RenPyImageDissolveTransitions/wiperd.png", time, ramplen=64)

transform looping_shake:
    zoom 1.05
    xalign 0.5
    yalign 0.5
    linear 0.05 xoffset -5 yoffset 5
    linear 0.05 xoffset 5 yoffset -5
    linear 0.05 xoffset -3 yoffset -3
    linear 0.05 xoffset 3 yoffset 3
    linear 0.05 xoffset 0 yoffset 0
    repeat # This makes it loop indefinitely