layeredimage aergia:

    group expression:
        attribute netral "sprite/Aergia/aergia_main_neutral.png"
        attribute angry "sprite/Aergia/aergia_main_angry.png"
        attribute sad "sprite/Aergia/aergia_main_sad.png"
        attribute hurt "sprite/Aergia/aergia_main_hurt.png"
        attribute psycho "sprite/Aergia/aergia_main_psycho.png"
        attribute furious "sprite/Aergia/aergia_main_furious.png"

layeredimage akasyah:

    group expression:
        attribute netral "sprite/Akasyah/akasyah_main_happy.png"
        attribute hurt "sprite/Akasyah/akasyah_main_hurt.png"
        attribute smug "sprite/Akasyah/akasyah_main_smug.png"
        attribute angry "sprite/Akasyah/akasyah_main_angry.png"
        attribute hurt "sprite/Akasyah/akasyah_main_hurt.png"

layeredimage axia:

    group expression:
        attribute netral "sprite/Axia/axia_main_happy.png"
        attribute cute "sprite/Axia/axia_main_cute.png"
        attribute sassy "sprite/Axia/axia_main_sassy.png"
        attribute love "sprite/Axia/axia_main_love.png"
        attribute hurt "sprite/Axia/axia_main_hurt.png"
        attribute loli "sprite/Axia/axia_main_loli.png"

layeredimage dawam:

    group expression:
        attribute netral "sprite/Dawam/dawam_main_happy.png"
        attribute sad "sprite/Dawam/dawam_main_sad.png"
        attribute happy "sprite/Dawam/dawam_main_laugh.png"
        attribute angry "sprite/Dawam/dawam_main_angry.png"
        attribute hurt "sprite/Dawam/dawam_main_hurt.png"

layeredimage dityo:

    group expression:
        attribute netral "sprite/Dityo/dityo_main_happy.png"
        attribute hurt "sprite/Dityo/dityo_main_hurt.png"
        attribute happy "sprite/Dityo/dityo_main_laugh.png"
        attribute angry "sprite/Dityo/dityo_main_angry.png"
        attribute sad "sprite/Dityo/dityo_main_gloom.png"

layeredimage haruto:

    group expression:
        attribute netral "sprite/Haruto/haruto_main_netral.png"
        attribute sad "sprite/Haruto/haruto_main_concern.png"
        attribute happy "sprite/Haruto/haruto_main_happy.png"
        attribute angry "sprite/Haruto/haruto_main_serious.png"
        attribute exhausted "sprite/Haruto/haruto_main_exhausted.png"

layeredimage pria:

    group expression:
        attribute netral "sprite/Pria_M/pria_main_netral.png"
        attribute sad "sprite/Pria_M/pria_main_sad.png"
        attribute happy "sprite/Pria_M/pria_main_happy.png"

layeredimage rian:

    group expression:
        attribute netral "sprite/Rian/rian_main_netral.png"
        attribute happy "sprite/Rian/rian_main_happy.png"
        attribute angry "sprite/Rian/rian_main_angry.png"
        attribute hurt "sprite/Rian/rian_main_hurt.png"

layeredimage seiya:

    group expression:
        attribute netral "sprite/Seiya/seiya_main_netral.png"
        attribute happy "sprite/Seiya/seiya_main_happy.png"
        attribute angry "sprite/Seiya/seiya_main_angry.png"
        attribute hurt "sprite/Seiya/seiya_main_hurt.png"
        attribute sassy "sprite/Seiya/seiya_main_sassy.png"

layeredimage shark:

    group expression:
        attribute netral "sprite/Shark/shark_main_netral.png"
        attribute happy "sprite/Shark/shark_main_happy.png"
        attribute scared "sprite/Shark/shark_main_scared.png"
        attribute hurt "sprite/Shark/shark_main_hurt.png"
        attribute sad "sprite/Shark/shark_main_worried.png"
        attribute beast "sprite/Shark/shark_main_beast.png"

layeredimage taro:

    group expression:
        attribute netral "sprite/Taro/taro_main_netral.png"
        attribute disgusted "sprite/Taro/taro_main_disgusted.png"
        attribute happy "sprite/Taro/taro_main_smile.png"
        attribute sad "sprite/Taro/taro_main_sad.png"
        attribute huh "sprite/Taro/taro_main_speak.png"

layeredimage yuura:

    group expression:
        attribute netral "sprite/Yuura/yuura_main_netral.png"
        attribute angry "sprite/Yuura/yuura_main_angry.png"
        attribute sad "sprite/Yuura/yuura_main_sad.png"
        attribute happy "sprite/Yuura/yuura_main_happy.png"
        attribute scared "sprite/Yuura/yuura_main_scared.png"
        attribute hurt "sprite/Yuura/yuura_main_hurt.png"

    group effect:
        attribute none default Null() # Default state (nothing rendered)
        attribute eff_angry:
            Transform(
                Movie(play="effects/angry.webm", mask="effects/angry.webm"),
                zoom=0.25, xpos=0.15, ypos=0.2
            )
        attribute eff_laugh:
            Transform(
                Movie(play="effects/funny01-y.webm", mask="effects/funny01-y.webm"),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.1
            )
        attribute eff_surprise_y:
            Transform(
                Movie(play="effects/surprise01-y.webm", mask="effects/surprise01-y.webm", loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.2
            )
        attribute eff_sweat_w:
            Transform(
                Movie(play="effects/sweat02-w.webm", mask="effects/sweat02-w.webm"),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2 # Flip
            )
        attribute eff_exclamation:
            Transform(
                Movie(play="effects/exclamation-mark01-r.webm", mask="effects/exclamation-mark01-r.webm", loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_question_mark:
            Transform(
                Movie(play="effects/question-mark02-r.webm", mask="effects/question-mark02-r.webm", loop=False),
                zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_sleepy:
            Transform(
                Movie(play="effects/sleep02-w.webm", mask="effects/sleep02-w.webm"),
                zoom=0.25, xpos=0.2, ypos=0.1
            )
        attribute eff_snot:
            Transform(
                Movie(play="effects/snot-bubble01.webm", mask="effects/snot-bubble01.webm"),
                zoom=0.4, xpos=0.145, ypos=0.3
            )
