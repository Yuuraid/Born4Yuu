label sprite_animation_dawam:

    "dawam"

    show dawam netral
    "testing expression: netral"

    show dawam angry
    "testing expression: angry"

    show dawam sad
    "testing expression: sad"
    
    show dawam happy
    "testing expression: happy"

    show dawam hurt
    "testing expression: hurt"

    show dawam hurt_smile
    "testing expression: hurt smile"

    # =====

    scene white
    play sound sfx_expression_angry
    show dawam netral eff_angry
    "testing effects: angry"
    
    scene black
    play sound sfx_expression_laugh
    show dawam netral eff_laugh_y
    "testing effects: happy yellow"

    scene white
    play sound sfx_expression_laugh
    show dawam netral eff_laugh_b
    "testing effects: happy black"

    scene black
    play sound sfx_expression_laugh
    show dawam netral eff_laugh_r
    "testing effects: happy red"

    play sound sfx_expression_shocked
    show dawam netral eff_surprise_y
    "testing effects: surpised yellow"

    play sound sfx_expression_shocked
    show dawam netral eff_surprise_r
    "testing effects: surpised red"

    scene black
    show dawam netral eff_sweat_w
    "testing effects: sweat white"

    show dawam netral eff_sweat_b
    "testing effects: sweat blue"

    play sound sfx_expression_surprised
    show dawam netral eff_exclamation_r
    "testing effects: exclamation red"

    play sound sfx_expression_surprised
    show dawam netral eff_exclamation_y
    "testing effects: exclamation yellow"

    play sound sfx_expression_confused
    show dawam netral eff_question_mark_r
    "testing effects: question mark red"

    play sound sfx_expression_confused
    show dawam netral eff_question_mark_y
    "testing effects: question mark"

    scene black
    show dawam netral eff_sleepy_w
    "testing effects: sleepy white"

    scene white
    show dawam netral eff_sleepy_b
    "testing effects: sleepy black"

    play sound sfx_expression_sleep
    show dawam netral eff_snot
    "testing effects: snot"

    play sound sfx_expression_sigh
    show dawam netral eff_sigh
    "testing effects: dissapointed"

    show dawam netral eff_pale
    "testing effects: pale"

    show dawam netral eff_confused
    "testing effects: confused"

    show dawam netral eff_inspiration_b
    "testing effects: inspiration black"

    show dawam netral eff_inspiration_y
    "testing effects: inspiration yellow"

    scene black
    show dawam netral eff_realization
    "testing effects: realization"

    show dawam netral eff_yelling
    "testing effects: yelling"

    scene black
    show dawam netral eff_sparkle
    "testing effects: sparkle"

    show dawam netral eff_heart
    "testing effects: heart"

    scene white
    show dawam netral eff_drowsy_b
    "testing effects: drowsy black"

    scene black
    show dawam netral eff_drowsy_w
    "testing effects: drowsy white"

    show dawam netral eff_drowsy_y
    "testing effects: drowsy yellow"

    scene white
    show dawam netral eff_tremble_b
    "testing effects: tremble black"

    scene black
    show dawam netral eff_tremble_w
    "testing effects: tremble white"

    hide dawam

    pause

    return