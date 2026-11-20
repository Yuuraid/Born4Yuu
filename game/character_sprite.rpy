layeredimage aergia:

    group expression:
        attribute netral "assets/sprite/Aergia/aergia_main_neutral.png"
        attribute angry "assets/sprite/Aergia/aergia_main_angry.png"
        attribute sad "assets/sprite/Aergia/aergia_main_sad.png"
        attribute hurt "assets/sprite/Aergia/aergia_main_hurt.png"
        attribute psycho "assets/sprite/Aergia/aergia_main_psycho.png"
        attribute furious "assets/sprite/Aergia/aergia_main_furious.png"
        
        attribute full_netral "assets/sprite/Aergia/aergia_full_neutral.png"
        attribute full_angry "assets/sprite/Aergia/aergia_full_angry.png"
        attribute full_sad "assets/sprite/Aergia/aergia_full_sad.png"
        attribute full_hurt "assets/sprite/Aergia/aergia_full_hurt.png"
        attribute full_psycho "assets/sprite/Aergia/aergia_full_psycho.png"
        attribute full_furious "assets/sprite/Aergia/aergia_full_furious.png"

    group effect:
        attribute none default Null() # Default state (nothing rendered)
        attribute eff_angry:
            Transform(
                Movie(play="assets/effects/anger01.webm", side_mask=True),
                zoom=0.25, xpos=0.23, ypos=0.1
            )
        attribute eff_laugh_y:
            Transform(
                Movie(play="assets/effects/funny01-y.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.15, ypos=0.06
            )
        attribute eff_laugh_r:
            Transform(
                Movie(play="assets/effects/funny01-r.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.15, ypos=0.06
            )
        attribute eff_laugh_b:
            Transform(
                Movie(play="assets/effects/funny01-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.15, ypos=0.06
            )
        attribute eff_surprise_y:
            Transform(
                Movie(play="assets/effects/surprise01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.16, ypos=0.09
            )
        attribute eff_surprise_r:
            Transform(
                Movie(play="assets/effects/surprise01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.16, ypos=0.09
            )
        attribute eff_sweat_w:
            Transform(
                Movie(play="assets/effects/sweat02-w.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2 # Flip
            )
        attribute eff_sweat_b:
            Transform(
                Movie(play="assets/effects/sweat02-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2 # Flip
            )
        attribute eff_exclamation_r:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.13, ypos=0.2, rotate=-20
            )
        attribute eff_exclamation_y:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.13, ypos=0.2, rotate=-20
            )
        attribute eff_question_mark_r :
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-r.webm", side_mask=True, loop=False),
                xzoom=1.0, zoom=0.25, xpos=0.13, ypos=0.2, rotate=-20
            )
        attribute eff_question_mark_y:
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-y.webm", side_mask=True, loop=False),
                xzoom=1.0, zoom=0.25, xpos=0.13, ypos=0.2, rotate=-20
            )
        attribute eff_sleepy_w:
            Transform(
                Movie(play="assets/effects/sleep02-w.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.0
            )
        attribute eff_sleepy_b:
            Transform(
                Movie(play="assets/effects/sleep02-bk.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.0
            )
        attribute eff_snot:
            Transform(
                Movie(play="assets/effects/snot-bubble01.webm", side_mask=True),
                zoom=0.2, xpos=0.17, ypos=0.23
            )
        attribute eff_sigh:
            Transform(
                Movie(play="assets/effects/sigh01.webm", side_mask=True, loop=False),
                xzoom=-1, zoom=0.4, xpos=0.145, ypos=0.29
            )
        attribute eff_pale:
            Transform(
                Movie(play="assets/effects/pale01.webm", side_mask=True, loop=False),
                zoom=0.3, xpos=0.2, ypos=0.0
            )
        attribute eff_confused:
            Transform(
                Movie(play="assets/effects/confused02.webm", side_mask=True),
                zoom=0.15, xpos=0.1, ypos=0.10
            )
        attribute eff_inspiration_b:
            Transform(
                Movie(play="assets/effects/inspiration01-bk.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.0
            )
        attribute eff_inspiration_y:
            Transform(
                Movie(play="assets/effects/inspiration01-y.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.0
            )
        attribute eff_realization:
            Transform(
                Movie(play="assets/effects/realization01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.5, xpos=0.13, ypos=0.03
            )
        attribute eff_yelling:
            Transform(
                Movie(play="assets/effects/pain01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.25
            )
        attribute eff_sparkle:
            Transform(
                Movie(play="assets/effects/sparkle01.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.4, xpos=0.1, ypos=0.16
            )
        attribute eff_heart:
            Transform(
                Movie(play="assets/effects/heart01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.16
            )
        attribute eff_drowsy_b:
            Transform(
                Movie(play="assets/effects/drowsiness01-b.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.14, ypos=0.15
            )
        attribute eff_drowsy_w:
            Transform(
                Movie(play="assets/effects/drowsiness01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.14, ypos=0.15
            )
        attribute eff_drowsy_y:
            Transform(
                Movie(play="assets/effects/drowsiness01-y.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.14, ypos=0.15
            )
        attribute eff_tremble_b:
            Transform(
                Movie(play="assets/effects/tremble01-bk.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.31, ypos=0.3, rotate=-30
            )
        attribute eff_tremble_w:
            Transform(
                Movie(play="assets/effects/tremble01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.31, ypos=0.3, rotate=-30
            )

layeredimage akasyah:

    group expression:
        attribute netral "assets/sprite/Akasyah/akasyah_main_happy.png"
        attribute hurt "assets/sprite/Akasyah/akasyah_main_hurt.png"
        attribute smug "assets/sprite/Akasyah/akasyah_main_smug.png"
        attribute angry "assets/sprite/Akasyah/akasyah_main_angry.png"

        attribute full_netral "assets/sprite/Akasyah/akasyah_full_happy.png"
        attribute full_hurt "assets/sprite/Akasyah/akasyah_full_hurt.png"
        attribute full_smug "assets/sprite/Akasyah/akasyah_full_smug.png"
        attribute full_angry "assets/sprite/Akasyah/akasyah_full_angry.png"

    group effect:
        attribute none default Null() # Default state (nothing rendered)
        attribute eff_angry:
            Transform(
                Movie(play="assets/effects/anger01.webm", side_mask=True),
                zoom=0.25, xpos=0.14, ypos=0.14
            )
        attribute eff_laugh_y:
            Transform(
                Movie(play="assets/effects/funny01-y.webm", side_mask=True),
                xzoom=1.0, zoom=0.4, xpos=0.3, ypos=0.1
            )
        attribute eff_laugh_r:
            Transform(
                Movie(play="assets/effects/funny01-r.webm", side_mask=True),
                xzoom=1.0, zoom=0.4, xpos=0.3, ypos=0.1
            )
        attribute eff_laugh_b:
            Transform(
                Movie(play="assets/effects/funny01-b.webm", side_mask=True),
                xzoom=1.0, zoom=0.4, xpos=0.3, ypos=0.1
            )
        attribute eff_surprise_y:
            Transform(
                Movie(play="assets/effects/surprise01-y.webm", side_mask=True, loop=False),
                xzoom=1.0, zoom=0.25, xpos=0.32, ypos=0.15
            )
        attribute eff_surprise_r:
            Transform(
                Movie(play="assets/effects/surprise01-r.webm", side_mask=True, loop=False),
                xzoom=1.0, zoom=0.25, xpos=0.32, ypos=0.15
            )
        attribute eff_sweat_w:
            Transform(
                Movie(play="assets/effects/sweat02-w.webm", side_mask=True),
                xzoom=1.0, zoom=0.4, xpos=0.32, ypos=0.2 # Flip
            )
        attribute eff_sweat_b:
            Transform(
                Movie(play="assets/effects/sweat02-b.webm", side_mask=True),
                xzoom=1.0, zoom=0.4, xpos=0.32, ypos=0.2 # Flip
            )
        attribute eff_exclamation_r:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.32, ypos=0.2, rotate=20
            )
        attribute eff_exclamation_y:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.32, ypos=0.2, rotate=20
            )
        attribute eff_question_mark_r :
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-r.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.32, ypos=0.2, rotate=20
            )
        attribute eff_question_mark_y:
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-y.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.32, ypos=0.2, rotate=20
            )
        attribute eff_sleepy_w:
            Transform(
                Movie(play="assets/effects/sleep02-w.webm", side_mask=True),
                zoom=0.25, xpos=0.20, ypos=0.1
            )
        attribute eff_sleepy_b:
            Transform(
                Movie(play="assets/effects/sleep02-bk.webm", side_mask=True),
                zoom=0.25, xpos=0.20, ypos=0.1
            )
        attribute eff_snot:
            Transform(
                Movie(play="assets/effects/snot-bubble01.webm", side_mask=True),
                xzoom=-1.0, zoom=0.2, xpos=0.26, ypos=0.27
            )
        attribute eff_sigh:
            Transform(
                Movie(play="assets/effects/sigh01.webm", side_mask=True, loop=False),
                xzoom=1, zoom=0.4, xpos=0.25, ypos=0.35
            )
        attribute eff_confused:
            Transform(
                Movie(play="assets/effects/confused02.webm", side_mask=True),
                zoom=0.15, xpos=0.35, ypos=0.23
            )
        attribute eff_pale:
            Transform(
                Movie(play="assets/effects/pale01.webm", side_mask=True, loop=False),
                zoom=0.3, xpos=0.15, ypos=0.1
            )
        attribute eff_inspiration_b:
            Transform(
                Movie(play="assets/effects/inspiration01-bk.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.23, ypos=0.1
            )
        attribute eff_inspiration_y:
            Transform(
                Movie(play="assets/effects/inspiration01-y.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.23, ypos=0.1
            )
        attribute eff_realization:
            Transform(
                Movie(play="assets/effects/realization01.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.5, xpos=0.3, ypos=0.1
            )
        attribute eff_yelling:
            Transform(
                Movie(play="assets/effects/pain01.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.4, xpos=0.3, ypos=0.35
            )
        attribute eff_sparkle:
            Transform(
                Movie(play="assets/effects/sparkle01.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.4, xpos=0.1, ypos=0.16
            )
        attribute eff_heart:
            Transform(
                Movie(play="assets/effects/heart01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.16
            )
        attribute eff_drowsy_b:
            Transform(
                Movie(play="assets/effects/drowsiness01-b.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.2, xpos=0.35, ypos=0.2
            )
        attribute eff_drowsy_w:
            Transform(
                Movie(play="assets/effects/drowsiness01-w.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.2, xpos=0.35, ypos=0.2
            )
        attribute eff_drowsy_y:
            Transform(
                Movie(play="assets/effects/drowsiness01-y.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.2, xpos=0.35, ypos=0.2
            )
        attribute eff_tremble_b:
            Transform(
                Movie(play="assets/effects/tremble01-bk.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.2, xpos=0.08, ypos=0.35, rotate=20
            )
        attribute eff_tremble_w:
            Transform(
                Movie(play="assets/effects/tremble01-w.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.2, xpos=0.08, ypos=0.35, rotate=20
            )

image axia_n_sequence = "assets/sprite/Axia/axia_main_cute.png"
image axia_b_sequence = "assets/sprite/Axia/axia_main_loli.png"


layeredimage axia:

    group expression:
        attribute netral "assets/sprite/Axia/axia_main_happy.png"
        attribute cute "assets/sprite/Axia/axia_main_cute.png"
        attribute sassy "assets/sprite/Axia/axia_main_sassy.png"
        attribute love "assets/sprite/Axia/axia_main_love.png"
        attribute hurt "assets/sprite/Axia/axia_main_hurt.png"
        attribute loli "assets/sprite/Axia/axia_main_loli.png"
    
    group effect:
        attribute none default Null() # Default state (nothing rendered)
        attribute eff_angry:
            Transform(
                Movie(play="assets/effects/anger01.webm", side_mask=True),
                zoom=0.25, xpos=0.25, ypos=0.15
            )
        attribute eff_laugh_y:
            Transform(
                Movie(play="assets/effects/funny01-y.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.1
            )
        attribute eff_laugh_r:
            Transform(
                Movie(play="assets/effects/funny01-r.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.1
            )
        attribute eff_laugh_b:
            Transform(
                Movie(play="assets/effects/funny01-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.1
            )
        attribute eff_surprise_y:
            Transform(
                Movie(play="assets/effects/surprise01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.2
            )
        attribute eff_surprise_r:
            Transform(
                Movie(play="assets/effects/surprise01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.2
            )
        attribute eff_sweat_w:
            Transform(
                Movie(play="assets/effects/sweat02-w.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2 # Flip
            )
        attribute eff_sweat_b:
            Transform(
                Movie(play="assets/effects/sweat02-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2 # Flip
            )
        attribute eff_exclamation_r:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_exclamation_y:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_question_mark_r :
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-r.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_question_mark_y:
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-y.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_sleepy_w:
            Transform(
                Movie(play="assets/effects/sleep02-w.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.1
            )
        attribute eff_sleepy_b:
            Transform(
                Movie(play="assets/effects/sleep02-bk.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.1
            )
        attribute eff_snot:
            Transform(
                Movie(play="assets/effects/snot-bubble01.webm", side_mask=True),
                zoom=0.2, xpos=0.185, ypos=0.28
            )
        attribute eff_sigh:
            Transform(
                Movie(play="assets/effects/sigh01.webm", side_mask=True, loop=False),
                xzoom=-1, zoom=0.4, xpos=0.145, ypos=0.35
            )
        attribute eff_confused:
            Transform(
                Movie(play="assets/effects/confused02.webm", side_mask=True),
                zoom=0.15, xpos=0.1, ypos=0.23
            )
        attribute eff_pale:
            Transform(
                Movie(play="assets/effects/pale01.webm", side_mask=True, loop=False),
                zoom=0.3, xpos=0.2, ypos=0.1
            )
        attribute eff_inspiration_b:
            Transform(
                Movie(play="assets/effects/inspiration01-bk.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.1
            )
        attribute eff_inspiration_y:
            Transform(
                Movie(play="assets/effects/inspiration01-y.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.1
            )
        attribute eff_realization:
            Transform(
                Movie(play="assets/effects/realization01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.5, xpos=0.1, ypos=0.1
            )
        attribute eff_yelling:
            Transform(
                Movie(play="assets/effects/pain01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.35
            )
        attribute eff_sparkle:
            Transform(
                Movie(play="assets/effects/sparkle01.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.4, xpos=0.1, ypos=0.16
            )
        attribute eff_heart:
            Transform(
                Movie(play="assets/effects/heart01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.16
            )
        attribute eff_drowsy_b:
            Transform(
                Movie(play="assets/effects/drowsiness01-b.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.13, ypos=0.2
            )
        attribute eff_drowsy_w:
            Transform(
                Movie(play="assets/effects/drowsiness01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.13, ypos=0.2
            )
        attribute eff_drowsy_y:
            Transform(
                Movie(play="assets/effects/drowsiness01-y.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.13, ypos=0.2
            )
        attribute eff_tremble_b:
            Transform(
                Movie(play="assets/effects/tremble01-bk.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.35, ypos=0.45, rotate=-14
            )
        attribute eff_tremble_w:
            Transform(
                Movie(play="assets/effects/tremble01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.35, ypos=0.45, rotate=-14
            )


layeredimage dawam:

    group expression:
        attribute netral "assets/sprite/Dawam/dawam_main_happy.png"
        attribute sad "assets/sprite/Dawam/dawam_main_sad.png"
        attribute happy "assets/sprite/Dawam/dawam_main_laugh.png"
        attribute angry "assets/sprite/Dawam/dawam_main_angry.png"
        attribute hurt "assets/sprite/Dawam/dawam_main_hurt.png"
        attribute hurt_smile "assets/sprite/Dawam/dawam_main_hurt_smile.png"

        attribute full_netral "assets/sprite/Dawam/dawam_full_happy.png"
        attribute full_sad "assets/sprite/Dawam/dawam_full_sad.png"
        attribute full_happy "assets/sprite/Dawam/dawam_full_laugh.png"
        attribute full_angry "assets/sprite/Dawam/dawam_full_angry.png"
        attribute full_hurt "assets/sprite/Dawam/dawam_full_hurt.png"

    group effect:
        attribute none default Null() # Default state (nothing rendered)
        attribute eff_angry:
            Transform(
                Movie(play="assets/effects/anger01.webm", side_mask=True),
                zoom=0.25, xpos=0.24, ypos=0.00
            )
        attribute eff_laugh_y:
            Transform(
                Movie(play="assets/effects/funny01-y.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.17, ypos=0
            )
        attribute eff_laugh_r:
            Transform(
                Movie(play="assets/effects/funny01-r.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.17, ypos=0
            )
        attribute eff_laugh_b:
            Transform(
                Movie(play="assets/effects/funny01-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.17, ypos=0
            )
        attribute eff_surprise_y:
            Transform(
                Movie(play="assets/effects/surprise01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.19, ypos=0.05
            )
        attribute eff_surprise_r:
            Transform(
                Movie(play="assets/effects/surprise01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.19, ypos=0.05
            )
        attribute eff_sweat_w:
            Transform(
                Movie(play="assets/effects/sweat02-w.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.15 # Flip
            )
        attribute eff_sweat_b:
            Transform(
                Movie(play="assets/effects/sweat02-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.15 # Flip
            )
        attribute eff_exclamation_r:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.05, rotate=-20
            )
        attribute eff_exclamation_y:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.05, rotate=-20
            )
        attribute eff_question_mark_r :
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-r.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.15, ypos=0.05, rotate=-20
            )
        attribute eff_question_mark_y:
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-y.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.15, ypos=0.05, rotate=-20
            )
        attribute eff_sleepy_w:
            Transform(
                Movie(play="assets/effects/sleep02-w.webm", side_mask=True),
                zoom=0.25, xpos=0.25, ypos=0.0
            )
        attribute eff_sleepy_b:
            Transform(
                Movie(play="assets/effects/sleep02-bk.webm", side_mask=True),
                zoom=0.25, xpos=0.25, ypos=0.0
            )
        attribute eff_snot:
            Transform(
                Movie(play="assets/effects/snot-bubble01.webm", side_mask=True),
                zoom=0.2, xpos=0.195, ypos=0.12
            )
        attribute eff_sigh:
            Transform(
                Movie(play="assets/effects/sigh01.webm", side_mask=True, loop=False),
                xzoom=-1, zoom=0.4, xpos=0.19, ypos=0.20
            )
        attribute eff_pale:
            Transform(
                Movie(play="assets/effects/pale01.webm", side_mask=True, loop=False),
                zoom=0.2, xpos=0.2, ypos=0.0
            )
        attribute eff_confused:
            Transform(
                Movie(play="assets/effects/confused02.webm", side_mask=True),
                zoom=0.15, xpos=0.15, ypos=0.10
            )
        attribute eff_inspiration_b:
            Transform(
                Movie(play="assets/effects/inspiration01-bk.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.23, ypos=0.0
            )
        attribute eff_inspiration_y:
            Transform(
                Movie(play="assets/effects/inspiration01-y.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.23, ypos=0.0
            )
        attribute eff_realization:
            Transform(
                Movie(play="assets/effects/realization01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.5, xpos=0.1, ypos=0.0
            )
        attribute eff_yelling:
            Transform(
                Movie(play="assets/effects/pain01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2
            )
        attribute eff_sparkle:
            Transform(
                Movie(play="assets/effects/sparkle01.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.4, xpos=0.1, ypos=0.06
            )
        attribute eff_heart:
            Transform(
                Movie(play="assets/effects/heart01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.06
            )
        attribute eff_drowsy_b:
            Transform(
                Movie(play="assets/effects/drowsiness01-b.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.15, ypos=0.1
            )
        attribute eff_drowsy_w:
            Transform(
                Movie(play="assets/effects/drowsiness01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.15, ypos=0.1
            )
        attribute eff_drowsy_y:
            Transform(
                Movie(play="assets/effects/drowsiness01-y.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.15, ypos=0.1
            )
        attribute eff_tremble_b:
            Transform(
                Movie(play="assets/effects/tremble01-bk.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.32, ypos=0.17, rotate=-60
            )
        attribute eff_tremble_w:
            Transform(
                Movie(play="assets/effects/tremble01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.32, ypos=0.17, rotate=-60
            )

layeredimage dityo:

    group expression:
        attribute netral "assets/sprite/Dityo/dityo_main_happy.png"
        attribute hurt "assets/sprite/Dityo/dityo_main_hurt.png"
        attribute happy "assets/sprite/Dityo/dityo_main_laugh.png"
        attribute angry "assets/sprite/Dityo/dityo_main_angry.png"
        attribute sad "assets/sprite/Dityo/dityo_main_gloom.png"
    
    group props:
        attribute mahakarya "assets/sprite/Dityo/dityo_main_props.png"

    group effect:
        attribute none default Null() # Default state (nothing rendered)
        attribute eff_angry:
            Transform(
                Movie(play="assets/effects/anger01.webm", side_mask=True),
                zoom=0.25, xpos=0.23, ypos=0.00
            )
        attribute eff_laugh_y:
            Transform(
                Movie(play="assets/effects/funny01-y.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0
            )
        attribute eff_laugh_r:
            Transform(
                Movie(play="assets/effects/funny01-r.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0
            )
        attribute eff_laugh_b:
            Transform(
                Movie(play="assets/effects/funny01-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0
            )
        attribute eff_surprise_y:
            Transform(
                Movie(play="assets/effects/surprise01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.05
            )
        attribute eff_surprise_r:
            Transform(
                Movie(play="assets/effects/surprise01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.05
            )
        attribute eff_sweat_w:
            Transform(
                Movie(play="assets/effects/sweat02-w.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.15 # Flip
            )
        attribute eff_sweat_b:
            Transform(
                Movie(play="assets/effects/sweat02-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.15 # Flip
            )
        attribute eff_exclamation_r:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.05, rotate=-20
            )
        attribute eff_exclamation_y:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.05, rotate=-20
            )
        attribute eff_question_mark_r :
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-r.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.15, ypos=0.05, rotate=-20
            )
        attribute eff_question_mark_y:
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-y.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.15, ypos=0.05, rotate=-20
            )
        attribute eff_sleepy_w:
            Transform(
                Movie(play="assets/effects/sleep02-w.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.0
            )
        attribute eff_sleepy_b:
            Transform(
                Movie(play="assets/effects/sleep02-bk.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.0
            )
        attribute eff_snot:
            Transform(
                Movie(play="assets/effects/snot-bubble01.webm", side_mask=True),
                zoom=0.2, xpos=0.15, ypos=0.13
            )
        attribute eff_sigh:
            Transform(
                Movie(play="assets/effects/sigh01.webm", side_mask=True, loop=False),
                xzoom=-1, zoom=0.4, xpos=0.145, ypos=0.20
            )
        attribute eff_pale:
            Transform(
                Movie(play="assets/effects/pale01.webm", side_mask=True, loop=False),
                zoom=0.3, xpos=0.2, ypos=0.0
            )
        attribute eff_confused:
            Transform(
                Movie(play="assets/effects/confused02.webm", side_mask=True),
                zoom=0.15, xpos=0.1, ypos=0.10
            )
        attribute eff_inspiration_b:
            Transform(
                Movie(play="assets/effects/inspiration01-bk.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.0
            )
        attribute eff_inspiration_y:
            Transform(
                Movie(play="assets/effects/inspiration01-y.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.0
            )
        attribute eff_realization:
            Transform(
                Movie(play="assets/effects/realization01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.5, xpos=0.1, ypos=0.0
            )
        attribute eff_yelling:
            Transform(
                Movie(play="assets/effects/pain01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2
            )
        attribute eff_sparkle:
            Transform(
                Movie(play="assets/effects/sparkle01.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.4, xpos=0.1, ypos=0.06
            )
        attribute eff_heart:
            Transform(
                Movie(play="assets/effects/heart01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.06
            )
        attribute eff_drowsy_b:
            Transform(
                Movie(play="assets/effects/drowsiness01-b.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.12, ypos=0.1
            )
        attribute eff_drowsy_w:
            Transform(
                Movie(play="assets/effects/drowsiness01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.12, ypos=0.1
            )
        attribute eff_drowsy_y:
            Transform(
                Movie(play="assets/effects/drowsiness01-y.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.12, ypos=0.1
            )
        attribute eff_tremble_b:
            Transform(
                Movie(play="assets/effects/tremble01-bk.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.28, ypos=0.2, rotate=-60
            )
        attribute eff_tremble_w:
            Transform(
                Movie(play="assets/effects/tremble01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.28, ypos=0.2, rotate=-60
            )

layeredimage haruto:

    group expression:
        attribute netral "assets/sprite/Haruto/haruto_main_netral.png"
        attribute sad "assets/sprite/Haruto/haruto_main_concern.png"
        attribute happy "assets/sprite/Haruto/haruto_main_happy.png"
        attribute angry "assets/sprite/Haruto/haruto_main_serious.png"
        attribute exhausted "assets/sprite/Haruto/haruto_main_exhausted.png"

    group effect:
        attribute none default Null() # Default state (nothing rendered)
        attribute eff_angry:
            Transform(
                Movie(play="assets/effects/anger01.webm", side_mask=True),
                zoom=0.25, xpos=0.17, ypos=0.05
            )
        attribute eff_laugh_y:
            Transform(
                Movie(play="assets/effects/funny01-y.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.15, ypos=0
            )
        attribute eff_laugh_r:
            Transform(
                Movie(play="assets/effects/funny01-r.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.15, ypos=0
            )
        attribute eff_laugh_b:
            Transform(
                Movie(play="assets/effects/funny01-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.15, ypos=0
            )
        attribute eff_surprise_y:
            Transform(
                Movie(play="assets/effects/surprise01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.17, ypos=0.05
            )
        attribute eff_surprise_r:
            Transform(
                Movie(play="assets/effects/surprise01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.17, ypos=0.05
            )
        attribute eff_sweat_w:
            Transform(
                Movie(play="assets/effects/sweat02-w.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2 # Flip
            )
        attribute eff_sweat_b:
            Transform(
                Movie(play="assets/effects/sweat02-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2 # Flip
            )
        attribute eff_exclamation_r:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.05, rotate=-20
            )
        attribute eff_exclamation_y:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.05, rotate=-20
            )
        attribute eff_question_mark_r :
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-r.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.15, ypos=0.05, rotate=-20
            )
        attribute eff_question_mark_y:
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-y.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.15, ypos=0.05, rotate=-20
            )
        attribute eff_sleepy_w:
            Transform(
                Movie(play="assets/effects/sleep02-w.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.0
            )
        attribute eff_sleepy_b:
            Transform(
                Movie(play="assets/effects/sleep02-bk.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.0
            )
        attribute eff_snot:
            Transform(
                Movie(play="assets/effects/snot-bubble01.webm", side_mask=True),
                zoom=0.2, xpos=0.194, ypos=0.185
            )
        attribute eff_sigh:
            Transform(
                Movie(play="assets/effects/sigh01.webm", side_mask=True, loop=False),
                xzoom=-1, zoom=0.4, xpos=0.145, ypos=0.25
            )
        attribute eff_pale:
            Transform(
                Movie(play="assets/effects/pale01.webm", side_mask=True, loop=False),
                zoom=0.3, xpos=0.2, ypos=0.0
            )
        attribute eff_confused:
            Transform(
                Movie(play="assets/effects/confused02.webm", side_mask=True),
                zoom=0.15, xpos=0.1, ypos=0.10
            )
        attribute eff_inspiration_b:
            Transform(
                Movie(play="assets/effects/inspiration01-bk.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.0
            )
        attribute eff_inspiration_y:
            Transform(
                Movie(play="assets/effects/inspiration01-y.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.0
            )
        attribute eff_realization:
            Transform(
                Movie(play="assets/effects/realization01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.5, xpos=0.1, ypos=0.0
            )
        attribute eff_yelling:
            Transform(
                Movie(play="assets/effects/pain01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.25
            )
        attribute eff_sparkle:
            Transform(
                Movie(play="assets/effects/sparkle01.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.4, xpos=0.1, ypos=0.06
            )
        attribute eff_heart:
            Transform(
                Movie(play="assets/effects/heart01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.06
            )
        attribute eff_drowsy_b:
            Transform(
                Movie(play="assets/effects/drowsiness01-b.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.12, ypos=0.1
            )
        attribute eff_drowsy_w:
            Transform(
                Movie(play="assets/effects/drowsiness01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.12, ypos=0.1
            )
        attribute eff_drowsy_y:
            Transform(
                Movie(play="assets/effects/drowsiness01-y.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.12, ypos=0.1
            )
        attribute eff_tremble_b:
            Transform(
                Movie(play="assets/effects/tremble01-bk.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.28, ypos=0.27, rotate=-60
            )
        attribute eff_tremble_w:
            Transform(
                Movie(play="assets/effects/tremble01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.28, ypos=0.27, rotate=-60
            )

layeredimage ibe:

    group expression:
        attribute netral "assets/sprite/Ibe/ibe_main_netral.png"

    group effect:
        attribute none default Null() # Default state (nothing rendered)
        attribute eff_angry:
            Transform(
                Movie(play="assets/effects/anger01.webm", side_mask=True),
                zoom=0.2, xpos=0.3, ypos=0.2
            )
        attribute eff_laugh_y:
            Transform(
                Movie(play="assets/effects/funny01-y.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.15
            )
        attribute eff_laugh_r:
            Transform(
                Movie(play="assets/effects/funny01-r.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.15
            )
        attribute eff_laugh_b:
            Transform(
                Movie(play="assets/effects/funny01-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.15
            )
        attribute eff_surprise_y:
            Transform(
                Movie(play="assets/effects/surprise01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.2
            )
        attribute eff_surprise_r:
            Transform(
                Movie(play="assets/effects/surprise01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.2
            )
        attribute eff_sweat_w:
            Transform(
                Movie(play="assets/effects/sweat02-w.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2 # Flip
            )
        attribute eff_sweat_b:
            Transform(
                Movie(play="assets/effects/sweat02-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2 # Flip
            )
        attribute eff_exclamation_r:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_exclamation_y:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_question_mark_r :
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-r.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_question_mark_y:
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-y.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_sleepy_w:
            Transform(
                Movie(play="assets/effects/sleep02-w.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.1
            )
        attribute eff_sleepy_b:
            Transform(
                Movie(play="assets/effects/sleep02-bk.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.1
            )
        attribute eff_snot:
            Transform(
                Movie(play="assets/effects/snot-bubble01.webm", side_mask=True),
                zoom=0.2, xpos=0.19, ypos=0.4
            )
        attribute eff_sigh:
            Transform(
                Movie(play="assets/effects/sigh01.webm", side_mask=True, loop=False),
                xzoom=-1, zoom=0.4, xpos=0.145, ypos=0.55
            )
        attribute eff_confused:
            Transform(
                Movie(play="assets/effects/confused02.webm", side_mask=True),
                zoom=0.15, xpos=0.1, ypos=0.23
            )
        attribute eff_pale:
            Transform(
                Movie(play="assets/effects/pale01.webm", side_mask=True, loop=False),
                zoom=0.3, xpos=0.25, ypos=0.15
            )
        attribute eff_inspiration_b:
            Transform(
                Movie(play="assets/effects/inspiration01-bk.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.1
            )
        attribute eff_inspiration_y:
            Transform(
                Movie(play="assets/effects/inspiration01-y.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.1
            )
        attribute eff_realization:
            Transform(
                Movie(play="assets/effects/realization01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.5, xpos=0.1, ypos=0.1
            )
        attribute eff_yelling:
            Transform(
                Movie(play="assets/effects/pain01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.5
            )
        attribute eff_sparkle:
            Transform(
                Movie(play="assets/effects/sparkle01.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.4, xpos=0.1, ypos=0.16
            )
        attribute eff_heart:
            Transform(
                Movie(play="assets/effects/heart01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.16
            )
        attribute eff_drowsy_b:
            Transform(
                Movie(play="assets/effects/drowsiness01-b.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.1, ypos=0.3
            )
        attribute eff_drowsy_w:
            Transform(
                Movie(play="assets/effects/drowsiness01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.1, ypos=0.3
            )
        attribute eff_drowsy_y:
            Transform(
                Movie(play="assets/effects/drowsiness01-y.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.1, ypos=0.3
            )
        attribute eff_tremble_b:
            Transform(
                Movie(play="assets/effects/tremble01-bk.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.35, ypos=0.57, rotate=-50
            )
        attribute eff_tremble_w:
            Transform(
                Movie(play="assets/effects/tremble01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.35, ypos=0.57, rotate=-50
            )

layeredimage josua:

    group expression:
        attribute netral "assets/sprite/Josua/josua_main_netral.png"

    group effect:
        attribute none default Null() # Default state (nothing rendered)
        attribute eff_angry:
            Transform(
                Movie(play="assets/effects/anger01.webm", side_mask=True),
                zoom=0.2, xpos=0.3, ypos=0.2
            )
        attribute eff_laugh_y:
            Transform(
                Movie(play="assets/effects/funny01-y.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.15
            )
        attribute eff_laugh_r:
            Transform(
                Movie(play="assets/effects/funny01-r.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.15
            )
        attribute eff_laugh_b:
            Transform(
                Movie(play="assets/effects/funny01-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.15
            )
        attribute eff_surprise_y:
            Transform(
                Movie(play="assets/effects/surprise01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.2
            )
        attribute eff_surprise_r:
            Transform(
                Movie(play="assets/effects/surprise01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.2
            )
        attribute eff_sweat_w:
            Transform(
                Movie(play="assets/effects/sweat02-w.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2 # Flip
            )
        attribute eff_sweat_b:
            Transform(
                Movie(play="assets/effects/sweat02-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2 # Flip
            )
        attribute eff_exclamation_r:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_exclamation_y:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_question_mark_r :
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-r.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_question_mark_y:
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-y.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_sleepy_w:
            Transform(
                Movie(play="assets/effects/sleep02-w.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.1
            )
        attribute eff_sleepy_b:
            Transform(
                Movie(play="assets/effects/sleep02-bk.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.1
            )
        attribute eff_snot:
            Transform(
                Movie(play="assets/effects/snot-bubble01.webm", side_mask=True),
                zoom=0.2, xpos=0.19, ypos=0.4
            )
        attribute eff_sigh:
            Transform(
                Movie(play="assets/effects/sigh01.webm", side_mask=True, loop=False),
                xzoom=-1, zoom=0.4, xpos=0.145, ypos=0.55
            )
        attribute eff_confused:
            Transform(
                Movie(play="assets/effects/confused02.webm", side_mask=True),
                zoom=0.15, xpos=0.1, ypos=0.23
            )
        attribute eff_pale:
            Transform(
                Movie(play="assets/effects/pale01.webm", side_mask=True, loop=False),
                zoom=0.3, xpos=0.25, ypos=0.15
            )
        attribute eff_inspiration_b:
            Transform(
                Movie(play="assets/effects/inspiration01-bk.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.1
            )
        attribute eff_inspiration_y:
            Transform(
                Movie(play="assets/effects/inspiration01-y.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.1
            )
        attribute eff_realization:
            Transform(
                Movie(play="assets/effects/realization01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.5, xpos=0.1, ypos=0.1
            )
        attribute eff_yelling:
            Transform(
                Movie(play="assets/effects/pain01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.5
            )
        attribute eff_sparkle:
            Transform(
                Movie(play="assets/effects/sparkle01.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.4, xpos=0.1, ypos=0.16
            )
        attribute eff_heart:
            Transform(
                Movie(play="assets/effects/heart01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.16
            )
        attribute eff_drowsy_b:
            Transform(
                Movie(play="assets/effects/drowsiness01-b.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.1, ypos=0.3
            )
        attribute eff_drowsy_w:
            Transform(
                Movie(play="assets/effects/drowsiness01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.1, ypos=0.3
            )
        attribute eff_drowsy_y:
            Transform(
                Movie(play="assets/effects/drowsiness01-y.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.1, ypos=0.3
            )
        attribute eff_tremble_b:
            Transform(
                Movie(play="assets/effects/tremble01-bk.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.35, ypos=0.57, rotate=-50
            )
        attribute eff_tremble_w:
            Transform(
                Movie(play="assets/effects/tremble01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.35, ypos=0.57, rotate=-50
            )

layeredimage pria:

    group expression:
        attribute netral "assets/sprite/Pria_M/pria_main_netral.png"
        attribute sad "assets/sprite/Pria_M/pria_main_sad.png"
        attribute happy "assets/sprite/Pria_M/pria_main_happy.png"

    group effect:
        attribute none default Null() # Default state (nothing rendered)
        attribute eff_angry:
            Transform(
                Movie(play="assets/effects/anger01.webm", side_mask=True),
                zoom=0.25, xpos=0.22, ypos=0.05
            )
        attribute eff_laugh_y:
            Transform(
                Movie(play="assets/effects/funny01-y.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0
            )
        attribute eff_laugh_r:
            Transform(
                Movie(play="assets/effects/funny01-r.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0
            )
        attribute eff_laugh_b:
            Transform(
                Movie(play="assets/effects/funny01-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0
            )
        attribute eff_surprise_y:
            Transform(
                Movie(play="assets/effects/surprise01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.05
            )
        attribute eff_surprise_r:
            Transform(
                Movie(play="assets/effects/surprise01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.05
            )
        attribute eff_sweat_w:
            Transform(
                Movie(play="assets/effects/sweat02-w.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0 # Flip
            )
        attribute eff_sweat_b:
            Transform(
                Movie(play="assets/effects/sweat02-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0 # Flip
            )
        attribute eff_exclamation_r:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.05, rotate=-20
            )
        attribute eff_exclamation_y:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.05, rotate=-20
            )
        attribute eff_question_mark_r :
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-r.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.10, ypos=0.05, rotate=-20
            )
        attribute eff_question_mark_y:
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-y.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.10, ypos=0.05, rotate=-20
            )
        attribute eff_question_mark_flip_r :
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.05, rotate=-20
            )
        attribute eff_question_mark_flip_y:
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.05, rotate=-20
            )
        attribute eff_sleepy_w:
            Transform(
                Movie(play="assets/effects/sleep02-w.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.0
            )
        attribute eff_sleepy_b:
            Transform(
                Movie(play="assets/effects/sleep02-bk.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.0
            )
        attribute eff_snot:
            Transform(
                Movie(play="assets/effects/snot-bubble01.webm", side_mask=True),
                zoom=0.2, xpos=0.16, ypos=0.175
            )
        attribute eff_sigh:
            Transform(
                Movie(play="assets/effects/sigh01.webm", side_mask=True, loop=False),
                xzoom=-1, zoom=0.4, xpos=0.145, ypos=0.25
            )
        attribute eff_pale:
            Transform(
                Movie(play="assets/effects/pale01.webm", side_mask=True, loop=False),
                zoom=0.3, xpos=0.2, ypos=0.0
            )
        attribute eff_confused:
            Transform(
                Movie(play="assets/effects/confused02.webm", side_mask=True),
                zoom=0.15, xpos=0.1, ypos=0.10
            )
        attribute eff_inspiration_b:
            Transform(
                Movie(play="assets/effects/inspiration01-bk.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.0
            )
        attribute eff_inspiration_y:
            Transform(
                Movie(play="assets/effects/inspiration01-y.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.0
            )
        attribute eff_realization:
            Transform(
                Movie(play="assets/effects/realization01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.5, xpos=0.1, ypos=0.0
            )
        attribute eff_yelling:
            Transform(
                Movie(play="assets/effects/pain01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.25
            )
        attribute eff_sparkle:
            Transform(
                Movie(play="assets/effects/sparkle01.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.4, xpos=0.1, ypos=0.06
            )
        attribute eff_heart:
            Transform(
                Movie(play="assets/effects/heart01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.06
            )
        attribute eff_drowsy_b:
            Transform(
                Movie(play="assets/effects/drowsiness01-b.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.12, ypos=0.1
            )
        attribute eff_drowsy_w:
            Transform(
                Movie(play="assets/effects/drowsiness01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.12, ypos=0.1
            )
        attribute eff_drowsy_y:
            Transform(
                Movie(play="assets/effects/drowsiness01-y.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.12, ypos=0.1
            )
        attribute eff_tremble_b:
            Transform(
                Movie(play="assets/effects/tremble01-bk.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.33, ypos=0.3, rotate=-24
            )
        attribute eff_tremble_w:
            Transform(
                Movie(play="assets/effects/tremble01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.33, ypos=0.3, rotate=-24
            )

layeredimage rian:

    group expression:
        attribute netral "assets/sprite/Rian/rian_main_netral.png"
        attribute happy "assets/sprite/Rian/rian_main_happy.png"
        attribute angry "assets/sprite/Rian/rian_main_angry.png"
        attribute hurt "assets/sprite/Rian/rian_main_hurt.png"

    group effect:
        attribute none default Null() # Default state (nothing rendered)
        attribute eff_angry:
            Transform(
                Movie(play="assets/effects/anger01.webm", side_mask=True),
                zoom=0.25, xpos=0.25, ypos=0.2
            )
        attribute eff_laugh_y:
            Transform(
                Movie(play="assets/effects/funny01-y.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.1
            )
        attribute eff_laugh_r:
            Transform(
                Movie(play="assets/effects/funny01-r.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.1
            )
        attribute eff_laugh_b:
            Transform(
                Movie(play="assets/effects/funny01-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.1
            )
        attribute eff_surprise_y:
            Transform(
                Movie(play="assets/effects/surprise01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.2
            )
        attribute eff_surprise_r:
            Transform(
                Movie(play="assets/effects/surprise01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.2
            )
        attribute eff_sweat_w:
            Transform(
                Movie(play="assets/effects/sweat02-w.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2 # Flip
            )
        attribute eff_sweat_b:
            Transform(
                Movie(play="assets/effects/sweat02-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2 # Flip
            )
        attribute eff_exclamation_r:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_exclamation_y:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_question_mark_r :
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-r.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_question_mark_y:
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-y.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_sleepy_w:
            Transform(
                Movie(play="assets/effects/sleep02-w.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.1
            )
        attribute eff_sleepy_b:
            Transform(
                Movie(play="assets/effects/sleep02-bk.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.1
            )
        attribute eff_snot:
            Transform(
                Movie(play="assets/effects/snot-bubble01.webm", side_mask=True),
                zoom=0.2, xpos=0.16, ypos=0.32
            )
        attribute eff_sigh:
            Transform(
                Movie(play="assets/effects/sigh01.webm", side_mask=True, loop=False),
                xzoom=-1, zoom=0.4, xpos=0.145, ypos=0.35
            )
        attribute eff_confused:
            Transform(
                Movie(play="assets/effects/confused02.webm", side_mask=True),
                zoom=0.15, xpos=0.1, ypos=0.23
            )
        attribute eff_pale:
            Transform(
                Movie(play="assets/effects/pale01.webm", side_mask=True, loop=False),
                zoom=0.3, xpos=0.2, ypos=0.1
            )
        attribute eff_inspiration_b:
            Transform(
                Movie(play="assets/effects/inspiration01-bk.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.1
            )
        attribute eff_inspiration_y:
            Transform(
                Movie(play="assets/effects/inspiration01-y.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.1
            )
        attribute eff_realization:
            Transform(
                Movie(play="assets/effects/realization01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.5, xpos=0.1, ypos=0.1
            )
        attribute eff_yelling:
            Transform(
                Movie(play="assets/effects/pain01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.35
            )
        attribute eff_sparkle:
            Transform(
                Movie(play="assets/effects/sparkle01.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.4, xpos=0.1, ypos=0.16
            )
        attribute eff_heart:
            Transform(
                Movie(play="assets/effects/heart01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.16
            )
        attribute eff_drowsy_b:
            Transform(
                Movie(play="assets/effects/drowsiness01-b.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.13, ypos=0.2
            )
        attribute eff_drowsy_w:
            Transform(
                Movie(play="assets/effects/drowsiness01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.13, ypos=0.2
            )
        attribute eff_drowsy_y:
            Transform(
                Movie(play="assets/effects/drowsiness01-y.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.13, ypos=0.2
            )
        attribute eff_tremble_b:
            Transform(
                Movie(play="assets/effects/tremble01-bk.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.29, ypos=0.45, rotate=-14
            )
        attribute eff_tremble_w:
            Transform(
                Movie(play="assets/effects/tremble01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.29, ypos=0.45, rotate=-14
            )

layeredimage seiya:

    group expression:
        attribute netral "assets/sprite/Seiya/seiya_main_netral.png"
        attribute happy "assets/sprite/Seiya/seiya_main_happy.png"
        attribute angry "assets/sprite/Seiya/seiya_main_angry.png"
        attribute hurt "assets/sprite/Seiya/seiya_main_hurt.png"
        attribute sassy "assets/sprite/Seiya/seiya_main_sassy.png"

    group effect:
        attribute none default Null() # Default state (nothing rendered)
        attribute eff_angry:
            Transform(
                Movie(play="assets/effects/anger01.webm", side_mask=True),
                zoom=0.25, xpos=0.22, ypos=0.03
            )
        attribute eff_laugh_y:
            Transform(
                Movie(play="assets/effects/funny01-y.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.0
            )
        attribute eff_laugh_r:
            Transform(
                Movie(play="assets/effects/funny01-r.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.0
            )
        attribute eff_laugh_b:
            Transform(
                Movie(play="assets/effects/funny01-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.0
            )
        attribute eff_surprise_y:
            Transform(
                Movie(play="assets/effects/surprise01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.13, ypos=0.05
            )
        attribute eff_surprise_r:
            Transform(
                Movie(play="assets/effects/surprise01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.13, ypos=0.05
            )
        attribute eff_sweat_w:
            Transform(
                Movie(play="assets/effects/sweat02-w.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.0 # Flip
            )
        attribute eff_sweat_b:
            Transform(
                Movie(play="assets/effects/sweat02-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.0 # Flip
            )
        attribute eff_exclamation_r:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.1, rotate=-20
            )
        attribute eff_exclamation_y:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.1, rotate=-20
            )
        attribute eff_question_mark_r :
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-r.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.10, ypos=0.1, rotate=-20
            )
        attribute eff_question_mark_y:
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-y.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.10, ypos=0.1, rotate=-20
            )
        attribute eff_sleepy_w:
            Transform(
                Movie(play="assets/effects/sleep02-w.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.0
            )
        attribute eff_sleepy_b:
            Transform(
                Movie(play="assets/effects/sleep02-bk.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.0
            )
        attribute eff_snot:
            Transform(
                Movie(play="assets/effects/snot-bubble01.webm", side_mask=True),
                zoom=0.2, xpos=0.145, ypos=0.155
            )
        attribute eff_sigh:
            Transform(
                Movie(play="assets/effects/sigh01.webm", side_mask=True, loop=False),
                xzoom=-1, zoom=0.4, xpos=0.145, ypos=0.2
            )
        attribute eff_pale:
            Transform(
                Movie(play="assets/effects/pale01.webm", side_mask=True, loop=False),
                zoom=0.3, xpos=0.2, ypos=0.0
            )
        attribute eff_confused:
            Transform(
                Movie(play="assets/effects/confused02.webm", side_mask=True),
                zoom=0.15, xpos=0.1, ypos=0.10
            )
        attribute eff_inspiration_b:
            Transform(
                Movie(play="assets/effects/inspiration01-bk.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.0
            )
        attribute eff_inspiration_y:
            Transform(
                Movie(play="assets/effects/inspiration01-y.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.0
            )
        attribute eff_realization:
            Transform(
                Movie(play="assets/effects/realization01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.5, xpos=0.1, ypos=0.0
            )
        attribute eff_yelling:
            Transform(
                Movie(play="assets/effects/pain01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.25
            )
        attribute eff_sparkle:
            Transform(
                Movie(play="assets/effects/sparkle01.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.4, xpos=0.1, ypos=0.06
            )
        attribute eff_heart:
            Transform(
                Movie(play="assets/effects/heart01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.06
            )
        attribute eff_drowsy_b:
            Transform(
                Movie(play="assets/effects/drowsiness01-b.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.12, ypos=0.1
            )
        attribute eff_drowsy_w:
            Transform(
                Movie(play="assets/effects/drowsiness01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.12, ypos=0.1
            )
        attribute eff_drowsy_y:
            Transform(
                Movie(play="assets/effects/drowsiness01-y.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.12, ypos=0.1
            )
        attribute eff_tremble_b:
            Transform(
                Movie(play="assets/effects/tremble01-bk.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.34, ypos=0.3, rotate=-30
            )
        attribute eff_tremble_w:
            Transform(
                Movie(play="assets/effects/tremble01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.34, ypos=0.3, rotate=-30
            )

image shark_n_sequence = "assets/sprite/Shark/shark_main_netral.png"
image shark_b_sequence = "assets/sprite/Shark/shark_main_beast.png"

layeredimage shark:

    group expression:
        attribute netral "assets/sprite/Shark/shark_main_netral.png"
        attribute happy "assets/sprite/Shark/shark_main_happy.png"
        attribute scared "assets/sprite/Shark/shark_main_scared.png"
        attribute hurt "assets/sprite/Shark/shark_main_hurt.png"
        attribute sad "assets/sprite/Shark/shark_main_worried.png"
        attribute beast "assets/sprite/Shark/shark_main_beast.png"
        attribute hurt_frame "assets/sprite/Shark/shark_main_hurt_frame.png"

        attribute full_netral "assets/sprite/Shark/shark_full_netral.png"
        attribute full_happy "assets/sprite/Shark/shark_full_happy.png"
        attribute full_scared "assets/sprite/Shark/shark_full_scared.png"
        attribute full_hurt "assets/sprite/Shark/shark_full_hurt.png"
        attribute full_sad "assets/sprite/Shark/shark_full_worried.png"
        attribute full_beast "assets/sprite/Shark/shark_full_beast.png"
    
    group effect:
        attribute none default Null() # Default state (nothing rendered)
        attribute eff_angry:
            Transform(
                Movie(play="assets/effects/anger01.webm", side_mask=True),
                zoom=0.25, xpos=0.22, ypos=0.05
            )
        attribute eff_laugh_y:
            Transform(
                Movie(play="assets/effects/funny01-y.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0
            )
        attribute eff_laugh_r:
            Transform(
                Movie(play="assets/effects/funny01-r.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0
            )
        attribute eff_laugh_b:
            Transform(
                Movie(play="assets/effects/funny01-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0
            )
        attribute eff_surprise_y:
            Transform(
                Movie(play="assets/effects/surprise01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.05
            )
        attribute eff_surprise_r:
            Transform(
                Movie(play="assets/effects/surprise01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.05
            )
        attribute eff_sweat_w:
            Transform(
                Movie(play="assets/effects/sweat02-w.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0 # Flip
            )
        attribute eff_sweat_b:
            Transform(
                Movie(play="assets/effects/sweat02-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0 # Flip
            )
        attribute eff_exclamation_r:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.05, rotate=-20
            )
        attribute eff_exclamation_y:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.05, rotate=-20
            )
        attribute eff_question_mark_r :
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-r.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.10, ypos=0.05, rotate=-20
            )
        attribute eff_question_mark_y:
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-y.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.10, ypos=0.05, rotate=-20
            )
        attribute eff_sleepy_w:
            Transform(
                Movie(play="assets/effects/sleep02-w.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.0
            )
        attribute eff_sleepy_b:
            Transform(
                Movie(play="assets/effects/sleep02-bk.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.0
            )
        attribute eff_snot:
            Transform(
                Movie(play="assets/effects/snot-bubble01.webm", side_mask=True),
                zoom=0.2, xpos=0.15, ypos=0.16
            )
        attribute eff_sigh:
            Transform(
                Movie(play="assets/effects/sigh01.webm", side_mask=True, loop=False),
                xzoom=-1, zoom=0.4, xpos=0.145, ypos=0.25
            )
        attribute eff_pale:
            Transform(
                Movie(play="assets/effects/pale01.webm", side_mask=True, loop=False),
                zoom=0.3, xpos=0.2, ypos=0.0
            )
        attribute eff_confused:
            Transform(
                Movie(play="assets/effects/confused02.webm", side_mask=True),
                zoom=0.15, xpos=0.1, ypos=0.10
            )
        attribute eff_inspiration_b:
            Transform(
                Movie(play="assets/effects/inspiration01-bk.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.0
            )
        attribute eff_inspiration_y:
            Transform(
                Movie(play="assets/effects/inspiration01-y.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.0
            )
        attribute eff_realization:
            Transform(
                Movie(play="assets/effects/realization01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.5, xpos=0.1, ypos=0.0
            )
        attribute eff_yelling:
            Transform(
                Movie(play="assets/effects/pain01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.25
            )
        attribute eff_sparkle:
            Transform(
                Movie(play="assets/effects/sparkle01.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.4, xpos=0.1, ypos=0.06
            )
        attribute eff_heart:
            Transform(
                Movie(play="assets/effects/heart01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.06
            )
        attribute eff_drowsy_b:
            Transform(
                Movie(play="assets/effects/drowsiness01-b.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.12, ypos=0.1
            )
        attribute eff_drowsy_w:
            Transform(
                Movie(play="assets/effects/drowsiness01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.12, ypos=0.1
            )
        attribute eff_drowsy_y:
            Transform(
                Movie(play="assets/effects/drowsiness01-y.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.12, ypos=0.1
            )
        attribute eff_tremble_b:
            Transform(
                Movie(play="assets/effects/tremble01-bk.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.3, ypos=0.3, rotate=-24
            )
        attribute eff_tremble_w:
            Transform(
                Movie(play="assets/effects/tremble01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.3, ypos=0.3, rotate=-24
            )


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
        attribute bittersweet "assets/sprite/Yuura/yuura_main_bs.png"

        attribute full_netral "assets/sprite/Yuura/yuura_full_netral.png"
        attribute full_angry "assets/sprite/Yuura/yuura_full_angry.png"
        attribute full_sad "assets/sprite/Yuura/yuura_full_sad.png"
        attribute full_happy "assets/sprite/Yuura/yuura_full_happy.png"
        attribute full_scared "assets/sprite/Yuura/yuura_full_scared.png"
        attribute full_hurt "assets/sprite/Yuura/yuura_full_hurt.png"

    group effect:
        attribute none default Null() # Default state (nothing rendered)
        attribute eff_angry:
            Transform(
                Movie(play="assets/effects/anger01.webm", side_mask=True),
                zoom=0.2, xpos=0.23, ypos=0.2
            )
        attribute eff_laugh_y:
            Transform(
                Movie(play="assets/effects/funny01-y.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.15
            )
        attribute eff_laugh_r:
            Transform(
                Movie(play="assets/effects/funny01-r.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.15
            )
        attribute eff_laugh_b:
            Transform(
                Movie(play="assets/effects/funny01-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.15
            )
        attribute eff_surprise_y:
            Transform(
                Movie(play="assets/effects/surprise01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.2
            )
        attribute eff_surprise_r:
            Transform(
                Movie(play="assets/effects/surprise01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.15, ypos=0.2
            )
        attribute eff_sweat_w:
            Transform(
                Movie(play="assets/effects/sweat02-w.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2 # Flip
            )
        attribute eff_sweat_b:
            Transform(
                Movie(play="assets/effects/sweat02-b.webm", side_mask=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.2 # Flip
            )
        attribute eff_exclamation_r:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-r.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_exclamation_y:
            Transform(
                Movie(play="assets/effects/exclamation-mark01-y.webm", side_mask=True, loop=False),
                xzoom=-1.0, zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_question_mark_r :
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-r.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_question_mark_y:
            Transform(
                Movie(play="assets/effects/exclamation-question-mark01-y.webm", side_mask=True, loop=False),
                zoom=0.25, xpos=0.10, ypos=0.2, rotate=-20
            )
        attribute eff_sleepy_w:
            Transform(
                Movie(play="assets/effects/sleep02-w.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.1
            )
        attribute eff_sleepy_b:
            Transform(
                Movie(play="assets/effects/sleep02-bk.webm", side_mask=True),
                zoom=0.25, xpos=0.2, ypos=0.1
            )
        attribute eff_snot:
            Transform(
                Movie(play="assets/effects/snot-bubble01.webm", side_mask=True),
                zoom=0.2, xpos=0.145, ypos=0.3
            )
        attribute eff_sigh:
            Transform(
                Movie(play="assets/effects/sigh01.webm", side_mask=True, loop=False),
                xzoom=-1, zoom=0.4, xpos=0.145, ypos=0.35
            )
        attribute eff_confused:
            Transform(
                Movie(play="assets/effects/confused02.webm", side_mask=True),
                zoom=0.15, xpos=0.1, ypos=0.23
            )
        attribute eff_pale:
            Transform(
                Movie(play="assets/effects/pale01.webm", side_mask=True, loop=False),
                zoom=0.3, xpos=0.2, ypos=0.1
            )
        attribute eff_inspiration_b:
            Transform(
                Movie(play="assets/effects/inspiration01-bk.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.1
            )
        attribute eff_inspiration_y:
            Transform(
                Movie(play="assets/effects/inspiration01-y.webm", side_mask=True, loop=False),
                zoom=0.15, xpos=0.2, ypos=0.1
            )
        attribute eff_realization:
            Transform(
                Movie(play="assets/effects/realization01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.5, xpos=0.1, ypos=0.1
            )
        attribute eff_yelling:
            Transform(
                Movie(play="assets/effects/pain01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.1, ypos=0.35
            )
        attribute eff_sparkle:
            Transform(
                Movie(play="assets/effects/sparkle01.webm", side_mask=True, loop=True),
                xzoom=1.0, zoom=0.4, xpos=0.1, ypos=0.16
            )
        attribute eff_heart:
            Transform(
                Movie(play="assets/effects/heart01.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.4, xpos=0.13, ypos=0.16
            )
        attribute eff_drowsy_b:
            Transform(
                Movie(play="assets/effects/drowsiness01-b.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.13, ypos=0.2
            )
        attribute eff_drowsy_w:
            Transform(
                Movie(play="assets/effects/drowsiness01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.13, ypos=0.2
            )
        attribute eff_drowsy_y:
            Transform(
                Movie(play="assets/effects/drowsiness01-y.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.13, ypos=0.2
            )
        attribute eff_tremble_b:
            Transform(
                Movie(play="assets/effects/tremble01-bk.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.27, ypos=0.15, rotate=-24
            )
        attribute eff_tremble_w:
            Transform(
                Movie(play="assets/effects/tremble01-w.webm", side_mask=True, loop=True),
                xzoom=-1.0, zoom=0.2, xpos=0.27, ypos=0.15, rotate=-24
            )
            

# game/assets/effects/conffused.webm 
# game/assets/effects/sigh01.webm 
# game/assets/effects/pale01.webm
