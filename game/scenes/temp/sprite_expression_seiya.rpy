label sprite_animation_seiya:

    "seiya"

    show seiya netral
    "testing expression: netral"

    show seiya angry
    "testing expression: angry"

    show seiya sassy
    "testing expression: sassy"
    
    show seiya happy
    "testing expression: happy"

    show seiya hurt
    "testing expression: hurt"

    # =====

    scene white
    play sound sfx_expression_angry
    show seiya netral eff_angry
    "testing effects: angry"
    
    scene black
    play sound sfx_expression_laugh
    show seiya netral eff_laugh_y
    "testing effects: happy yellow"

    scene white
    play sound sfx_expression_laugh
    show seiya netral eff_laugh_b
    "testing effects: happy black"

    scene black
    play sound sfx_expression_laugh
    show seiya netral eff_laugh_r
    "testing effects: happy red"

    play sound sfx_expression_shocked
    show seiya netral eff_surprise_y
    "testing effects: surpised yellow"

    play sound sfx_expression_shocked
    show seiya netral eff_surprise_r
    "testing effects: surpised red"

    scene black
    show seiya netral eff_sweat_w
    "testing effects: sweat white"

    show seiya netral eff_sweat_b
    "testing effects: sweat blue"

    play sound sfx_expression_surprised
    show seiya netral eff_exclamation_r
    "testing effects: exclamation red"

    play sound sfx_expression_surprised
    show seiya netral eff_exclamation_y
    "testing effects: exclamation yellow"

    play sound sfx_expression_confused
    show seiya netral eff_question_mark_r 
    "testing effects: question mark red"

    play sound sfx_expression_confused
    show seiya netral eff_question_mark_y
    "testing effects: question mark"

    scene black
    show seiya netral eff_sleepy_w
    "testing effects: sleepy white"

    scene white
    show seiya netral eff_sleepy_b
    "testing effects: sleepy black"

    play sound sfx_expression_sleep
    show seiya netral eff_snot
    "testing effects: snot"

    play sound sfx_expression_sigh
    show seiya netral eff_sigh
    "testing effects: dissapointed"

    show seiya netral eff_pale
    "testing effects: pale"

    show seiya netral eff_confused
    "testing effects: confused"

    show seiya netral eff_inspiration_b
    "testing effects: inspiration black"

    show seiya netral eff_inspiration_y
    "testing effects: inspiration yellow"

    scene black
    show seiya netral eff_realization
    "testing effects: realization"

    show seiya netral eff_yelling
    "testing effects: yelling"

    scene black
    show seiya netral eff_sparkle
    "testing effects: sparkle"

    show seiya netral eff_heart
    "testing effects: heart"

    scene white
    show seiya netral eff_drowsy_b
    "testing effects: drowsy black"

    scene black
    show seiya netral eff_drowsy_w
    "testing effects: drowsy white"

    show seiya netral eff_drowsy_y
    "testing effects: drowsy yellow"

    scene white
    show seiya netral eff_tremble_b
    "testing effects: tremble black"

    scene black
    show seiya netral eff_tremble_w
    "testing effects: tremble white"

    hide seiya

    pause

    return