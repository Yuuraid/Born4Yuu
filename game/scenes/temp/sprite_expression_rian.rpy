label sprite_animation_rian:

    "rian"

    show rian netral
    "testing expression: netral"

    show rian angry
    "testing expression: angry"
    
    show rian happy
    "testing expression: happy"

    show rian hurt
    "testing expression: hurt"

    # =====

    scene white
    play sound sfx_expression_angry
    show rian netral eff_angry
    "testing effects: angry"
    
    scene black
    play sound sfx_expression_laugh
    show rian netral eff_laugh_y
    "testing effects: happy yellow"

    scene white
    play sound sfx_expression_laugh
    show rian netral eff_laugh_b
    "testing effects: happy black"

    scene black
    play sound sfx_expression_laugh
    show rian netral eff_laugh_r
    "testing effects: happy red"

    play sound sfx_expression_shocked
    show rian netral eff_surprise_y
    "testing effects: surpised yellow"

    play sound sfx_expression_shocked
    show rian netral eff_surprise_r
    "testing effects: surpised red"

    scene black
    show rian netral eff_sweat_w
    "testing effects: sweat white"

    show rian netral eff_sweat_b
    "testing effects: sweat blue"

    play sound sfx_expression_surprised
    show rian netral eff_exclamation_r
    "testing effects: exclamation red"

    play sound sfx_expression_surprised
    show rian netral eff_exclamation_y
    "testing effects: exclamation yellow"

    play sound sfx_expression_confused
    show rian netral eff_question_mark_r 
    "testing effects: question mark red"

    play sound sfx_expression_confused
    show rian netral eff_question_mark_y
    "testing effects: question mark"

    scene black
    show rian netral eff_sleepy_w
    "testing effects: sleepy white"

    scene white
    show rian netral eff_sleepy_b
    "testing effects: sleepy black"

    play sound sfx_expression_sleep
    show rian netral eff_snot
    "testing effects: snot"

    play sound sfx_expression_sigh
    show rian netral eff_sigh
    "testing effects: dissapointed"

    show rian netral eff_pale
    "testing effects: pale"

    show rian netral eff_confused
    "testing effects: confused"

    show rian netral eff_inspiration_b
    "testing effects: inspiration black"

    show rian netral eff_inspiration_y
    "testing effects: inspiration yellow"

    scene black
    show rian netral eff_realization
    "testing effects: realization"

    show rian netral eff_yelling
    "testing effects: yelling"

    scene black
    show rian netral eff_sparkle
    "testing effects: sparkle"

    show rian netral eff_heart
    "testing effects: heart"

    scene white
    show rian netral eff_drowsy_b
    "testing effects: drowsy black"

    scene black
    show rian netral eff_drowsy_w
    "testing effects: drowsy white"

    show rian netral eff_drowsy_y
    "testing effects: drowsy yellow"

    scene white
    show rian netral eff_tremble_b
    "testing effects: tremble black"

    scene black
    show rian netral eff_tremble_w
    "testing effects: tremble white"

    hide rian

    pause

    return