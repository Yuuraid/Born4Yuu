label sprite_animation_akasyah:

    "akasyah"

    show akasyah netral
    "testing expression: netral"

    show akasyah angry
    "testing expression: angry"

    show akasyah smug
    "testing expression: smug"

    show akasyah hurt
    "testing expression: hurt"

    hide akasyah

    "akasyah full"

    show akasyah full_netral:
        zoom 1.0
    "testing expression: netral"

    show akasyah full_angry
    "testing expression: angry"

    show akasyah full_smug
    "testing expression: sad"

    show akasyah full_hurt
    "testing expression: hurt"

    hide akasyah

    # =====

    scene white
    play sound sfx_expression_angry
    show akasyah netral eff_angry
    "testing effects: angry"
    
    scene black
    play sound sfx_expression_laugh
    show akasyah netral eff_laugh_y
    "testing effects: happy yellow"

    scene white
    play sound sfx_expression_laugh
    show akasyah netral eff_laugh_b
    "testing effects: happy black"

    scene black
    play sound sfx_expression_laugh
    show akasyah netral eff_laugh_r
    "testing effects: happy red"

    play sound sfx_expression_shocked
    show akasyah netral eff_surprise_y
    "testing effects: surpised yellow"

    play sound sfx_expression_shocked
    show akasyah netral eff_surprise_r
    "testing effects: surpised red"

    scene black
    show akasyah netral eff_sweat_w
    "testing effects: sweat white"

    show akasyah netral eff_sweat_b
    "testing effects: sweat blue"

    play sound sfx_expression_surprised
    show akasyah netral eff_exclamation_r
    "testing effects: exclamation red"

    play sound sfx_expression_surprised
    show akasyah netral eff_exclamation_y
    "testing effects: exclamation yellow"

    play sound sfx_expression_confused
    show akasyah netral eff_question_mark_r 
    "testing effects: question mark red"

    play sound sfx_expression_confused
    show akasyah netral eff_question_mark_y
    "testing effects: question mark"

    scene black
    show akasyah netral eff_sleepy_w
    "testing effects: sleepy white"

    scene white
    show akasyah netral eff_sleepy_b
    "testing effects: sleepy black"

    play sound sfx_expression_sleep
    show akasyah netral eff_snot
    "testing effects: snot"

    play sound sfx_expression_sigh
    show akasyah netral eff_sigh
    "testing effects: dissapointed"

    show akasyah netral eff_pale
    "testing effects: pale"

    show akasyah netral eff_confused
    "testing effects: confused"

    show akasyah netral eff_inspiration_b
    "testing effects: inspiration black"

    show akasyah netral eff_inspiration_y
    "testing effects: inspiration yellow"

    scene black
    show akasyah netral eff_realization
    "testing effects: realization"

    show akasyah netral eff_yelling
    "testing effects: yelling"

    scene black
    show akasyah netral eff_sparkle
    "testing effects: sparkle"

    show akasyah netral eff_heart
    "testing effects: heart"

    scene white
    show akasyah netral eff_drowsy_b
    "testing effects: drowsy black"

    scene black
    show akasyah netral eff_drowsy_w
    "testing effects: drowsy white"

    show akasyah netral eff_drowsy_y
    "testing effects: drowsy yellow"

    scene white
    show akasyah netral eff_tremble_b
    "testing effects: tremble black"

    scene black
    show akasyah netral eff_tremble_w
    "testing effects: tremble white"

    hide akasyah

    pause

    return