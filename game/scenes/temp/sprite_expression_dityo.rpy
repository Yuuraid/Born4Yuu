label sprite_animation_dityo:

    "dityo"

    show dityo netral
    "testing expression: netral"

    show dityo angry
    "testing expression: angry"

    show dityo sad
    "testing expression: sad"
    
    show dityo happy
    "testing expression: happy"

    show dityo hurt
    "testing expression: hurt"

    # =====

    scene white
    play sound sfx_expression_angry
    show dityo netral eff_angry
    "testing effects: angry"
    
    scene black
    play sound sfx_expression_laugh
    show dityo netral eff_laugh_y
    "testing effects: happy yellow"

    scene white
    play sound sfx_expression_laugh
    show dityo netral eff_laugh_b
    "testing effects: happy black"

    scene black
    play sound sfx_expression_laugh
    show dityo netral eff_laugh_r
    "testing effects: happy red"

    play sound sfx_expression_shocked
    show dityo netral eff_surprise_y
    "testing effects: surpised yellow"

    play sound sfx_expression_shocked
    show dityo netral eff_surprise_r
    "testing effects: surpised red"

    scene black
    show dityo netral eff_sweat_w
    "testing effects: sweat white"

    show dityo netral eff_sweat_b
    "testing effects: sweat blue"

    play sound sfx_expression_surprised
    show dityo netral eff_exclamation_r
    "testing effects: exclamation red"

    play sound sfx_expression_surprised
    show dityo netral eff_exclamation_y
    "testing effects: exclamation yellow"

    play sound sfx_expression_confused
    show dityo netral eff_question_mark_r
    "testing effects: question mark red"

    play sound sfx_expression_confused
    show dityo netral eff_question_mark_y
    "testing effects: question mark"

    scene black
    show dityo netral eff_sleepy_w
    "testing effects: sleepy white"

    scene white
    show dityo netral eff_sleepy_b
    "testing effects: sleepy black"

    play sound sfx_expression_sleep
    show dityo netral eff_snot
    "testing effects: snot"

    play sound sfx_expression_sigh
    show dityo netral eff_sigh
    "testing effects: dissapointed"

    show dityo netral eff_pale
    "testing effects: pale"

    show dityo netral eff_confused
    "testing effects: confused"

    show dityo netral eff_inspiration_b
    "testing effects: inspiration black"

    show dityo netral eff_inspiration_y
    "testing effects: inspiration yellow"

    scene black
    show dityo netral eff_realization
    "testing effects: realization"

    show dityo netral eff_yelling
    "testing effects: yelling"

    scene black
    show dityo netral eff_sparkle
    "testing effects: sparkle"

    show dityo netral eff_heart
    "testing effects: heart"

    scene white
    show dityo netral eff_drowsy_b
    "testing effects: drowsy black"

    scene black
    show dityo netral eff_drowsy_w
    "testing effects: drowsy white"

    show dityo netral eff_drowsy_y
    "testing effects: drowsy yellow"

    scene white
    show dityo netral eff_tremble_b
    "testing effects: tremble black"

    scene black
    show dityo netral eff_tremble_w
    "testing effects: tremble white"

    hide dityo

    pause

    return