layeredimage yuura:

    group expression:
        attribute netral "assets/sprite/Yuura/yuura_main_netral.png"
        attribute angry "assets/sprite/Yuura/yuura_main_angry.png"
        attribute sad "assets/sprite/Yuura/yuura_main_sad.png"
        attribute happy "assets/sprite/Yuura/yuura_main_happy.png"
        attribute scared "assets/sprite/Yuura/yuura_main_scared.png"
        attribute hurt "assets/sprite/Yuura/yuura_main_hurt.png"

    group effect:
        attribute none default Null() # Default state (nothing rendered)
        attribute eff_angry:
            Transform(
                Movie(play="assets/effects/angry.webm", mask="assets/effects/angry.webm"),
                zoom=0.25, xpos=0.15, ypos=0.2
            )
        attribute eff_laugh:
            Transform(
                Movie(play="assets/effects/funny01-y.webm", mask="assets/effects/funny01-y.webm"),
                zoom=0.4, xpos=0.1, ypos=0.1, rotate=-90
            )