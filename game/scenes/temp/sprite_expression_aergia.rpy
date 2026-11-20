label sprite_animation_aergia:

    "aergia"

    show aergia netral
    "testing expression: netral"

    show aergia angry
    "testing expression: angry"

    show aergia sad
    "testing expression: sad"
    
    show aergia psycho
    "testing expression: psycho"

    show aergia furious
    "testing expression: furious"

    show aergia hurt
    "testing expression: hurt"

    hide aergia

    show aergia full_angry eff_angry:
        zoom 2.0
    "testing effects: angry"
    
    show aergia full_netral eff_laugh
    "testing effects: happy"

    show aergia full_netral eff_surprise_y
    "testing effects: surpised"

    show aergia full_netral eff_sweat_w
    "testing effects: sweat"

    show aergia full_netral eff_exclamation
    "testing effects: exclamation"

    show aergia full_netral eff_question_mark
    "testing effects: question mark"

    show aergia full_sad eff_sleepy
    "testing effects: sleepy"

    show aergia full_sad eff_snot
    "testing effects: snot"

    hide aergia

    # =====

    scene white
    play sound sfx_expression_angry
    show aergia netral eff_angry
    "testing effects: angry"
    
    scene black
    play sound sfx_expression_laugh
    show aergia netral eff_laugh_y
    "testing effects: happy yellow"

    scene white
    play sound sfx_expression_laugh
    show aergia netral eff_laugh_b
    "testing effects: happy black"

    scene black
    play sound sfx_expression_laugh
    show aergia netral eff_laugh_r
    "testing effects: happy red"

    play sound sfx_expression_shocked
    show aergia netral eff_surprise_y
    "testing effects: surpised yellow"

    play sound sfx_expression_shocked
    show aergia netral eff_surprise_r
    "testing effects: surpised red"

    scene black
    show aergia netral eff_sweat_w
    "testing effects: sweat white"

    show aergia netral eff_sweat_b
    "testing effects: sweat blue"

    play sound sfx_expression_surprised
    show aergia netral eff_exclamation_r
    "testing effects: exclamation red"

    play sound sfx_expression_surprised
    show aergia netral eff_exclamation_y
    "testing effects: exclamation yellow"

    play sound sfx_expression_confused
    show aergia netral eff_question_mark_r 
    "testing effects: question mark red"

    play sound sfx_expression_confused
    show aergia netral eff_question_mark_y
    "testing effects: question mark"

    scene black
    show aergia netral eff_sleepy_w
    "testing effects: sleepy white"

    scene white
    show aergia netral eff_sleepy_b
    "testing effects: sleepy black"

    play sound sfx_expression_sleep
    show aergia netral eff_snot
    "testing effects: snot"

    play sound sfx_expression_sigh
    show aergia netral eff_sigh
    "testing effects: dissapointed"

    show aergia netral eff_pale
    "testing effects: pale"

    show aergia netral eff_confused
    "testing effects: confused"

    show aergia netral eff_inspiration_b
    "testing effects: inspiration black"

    show aergia netral eff_inspiration_y
    "testing effects: inspiration yellow"

    scene black
    show aergia netral eff_realization
    "testing effects: realization"

    show aergia netral eff_yelling
    "testing effects: yelling"

    scene black
    show aergia netral eff_sparkle
    "testing effects: sparkle"

    show aergia netral eff_heart
    "testing effects: heart"

    scene white
    show aergia netral eff_drowsy_b
    "testing effects: drowsy black"

    scene black
    show aergia netral eff_drowsy_w
    "testing effects: drowsy white"

    show aergia netral eff_drowsy_y
    "testing effects: drowsy yellow"

    scene white
    show aergia netral eff_tremble_b
    "testing effects: tremble black"

    scene black
    show aergia netral eff_tremble_w
    "testing effects: tremble white"

    hide aergia

    pause

    return