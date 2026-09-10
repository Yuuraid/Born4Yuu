layeredimage aergia:

    group expression:
        attribute netral "assets/sprite/Aergia/aergia_main_neutral.png"
        attribute angry "assets/sprite/Aergia/aergia_main_angry.png"
        attribute sad "assets/sprite/Aergia/aergia_main_sad.png"
        attribute hurt "assets/sprite/Aergia/aergia_main_hurt.png"
        attribute psycho "assets/sprite/Aergia/aergia_main_psycho.png"
        attribute furious "assets/sprite/Aergia/aergia_main_furious.png"

layeredimage akasyah:

    group expression:
        attribute netral "assets/sprite/Akasyah/akasyah_main_happy.png"
        attribute hurt "assets/sprite/Akasyah/akasyah_main_hurt.png"
        attribute smug "assets/sprite/Akasyah/akasyah_main_smug.png"
        attribute angry "assets/sprite/Akasyah/akasyah_main_angry.png"
        attribute hurt "assets/sprite/Akasyah/akasyah_main_hurt.png"

layeredimage axia:

    group expression:
        attribute netral "assets/sprite/Axia/axia_main_happy.png"
        attribute cute "assets/sprite/Axia/axia_main_cute.png"
        attribute sassy "assets/sprite/Axia/axia_main_sassy.png"
        attribute love "assets/sprite/Axia/axia_main_love.png"
        attribute hurt "assets/sprite/Axia/axia_main_hurt.png"
        attribute loli "assets/sprite/Axia/axia_main_loli.png"

layeredimage dawam:

    group expression:
        attribute netral "assets/sprite/Dawam/dawam_main_happy.png"
        attribute sad "assets/sprite/Dawam/dawam_main_sad.png"
        attribute happy "assets/sprite/Dawam/dawam_main_laugh.png"
        attribute angry "assets/sprite/Dawam/dawam_main_angry.png"
        attribute hurt "assets/sprite/Dawam/dawam_main_hurt.png"

layeredimage dityo:

    group expression:
        attribute netral "assets/sprite/Dityo/dityo_main_happy.png"
        attribute hurt "assets/sprite/Dityo/dityo_main_hurt.png"
        attribute happy "assets/sprite/Dityo/dityo_main_laugh.png"
        attribute angry "assets/sprite/Dityo/dityo_main_angry.png"
        attribute sad "assets/sprite/Dityo/dityo_main_gloom.png"

layeredimage haruto:

    group expression:
        attribute netral "assets/sprite/Haruto/haruto_main_netral.png"
        attribute sad "assets/sprite/Haruto/haruto_main_concern.png"
        attribute happy "assets/sprite/Haruto/haruto_main_happy.png"
        attribute angry "assets/sprite/Haruto/haruto_main_serious.png"
        attribute exhausted "assets/sprite/Haruto/haruto_main_exhausted.png"

    group effect:
        attribute none default Null() # Default state (nothing rendered)
        attribute eff_exclamation:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-r.webm", mask="assets/effects/exclamation-mark01-r.webm", loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.14, ypos=0.1, rotate=-20
            )

layeredimage pria:

    group expression:
        attribute netral "assets/sprite/Pria_M/pria_main_netral.png"
        attribute sad "assets/sprite/Pria_M/pria_main_sad.png"
        attribute happy "assets/sprite/Pria_M/pria_main_happy.png"

layeredimage rian:

    group expression:
        attribute netral "assets/sprite/Rian/rian_main_netral.png"
        attribute happy "assets/sprite/Rian/rian_main_happy.png"
        attribute angry "assets/sprite/Rian/rian_main_angry.png"
        attribute hurt "assets/sprite/Rian/rian_main_hurt.png"

layeredimage seiya:

    group expression:
        attribute netral "assets/sprite/Seiya/seiya_main_netral.png"
        attribute happy "assets/sprite/Seiya/seiya_main_happy.png"
        attribute angry "assets/sprite/Seiya/seiya_main_angry.png"
        attribute hurt "assets/sprite/Seiya/seiya_main_hurt.png"
        attribute sassy "assets/sprite/Seiya/seiya_main_sassy.png"

layeredimage shark:

    group expression:
        attribute netral "assets/sprite/Shark/shark_main_netral.png"
        attribute happy "assets/sprite/Shark/shark_main_happy.png"
        attribute scared "assets/sprite/Shark/shark_main_scared.png"
        attribute hurt "assets/sprite/Shark/shark_main_hurt.png"
        attribute sad "assets/sprite/Shark/shark_main_worried.png"
        attribute beast "assets/sprite/Shark/shark_main_beast.png"

layeredimage taro:

    group expression:
        attribute netral "assets/sprite/Taro/taro_main_netral.png"
        attribute disgusted "assets/sprite/Taro/taro_main_disgusted.png"
        attribute happy "assets/sprite/Taro/taro_main_smile.png"
        attribute sad "assets/sprite/Taro/taro_main_sad.png"
        attribute huh "assets/sprite/Taro/taro_main_speak.png"

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
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.1
            )
        attribute eff_surprise_y:
            Transform(
                Movie(play="assets/effects/surprise01-y.webm", mask="assets/effects/surprise01-y.webm", loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.2
            )
        attribute eff_sweat_w:
            Transform(
                Movie(play="assets/effects/sweat02-w.webm", mask="assets/effects/sweat02-w.webm"),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2 # Flip
            )
        attribute eff_exclamation:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-r.webm", mask="assets/effects/exclamation-mark01-r.webm", loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_question_mark:
            Transform(
                Movie(play="assets/effects/question-mark02-r.webm", mask="assets/effects/question-mark02-r.webm", loop=False),
                zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_sleepy:
            Transform(
                Movie(play="assets/effects/sleep02-w.webm", mask="assets/effects/sleep02-w.webm"),
                zoom=0.25, xpos=0.2, ypos=0.1
            )
        attribute eff_snot:
            Transform(
                Movie(play="assets/effects/snot-bubble01.webm", mask="assets/effects/snot-bubble01.webm"),
                zoom=0.4, xpos=0.145, ypos=0.3
            )
