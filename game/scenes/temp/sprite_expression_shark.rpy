label sprite_animation_shark:

    "shark"

    show shark netral
    "testing expression: netral"

    show shark beast
    "testing expression: beast"

    show shark sad
    "testing expression: sad"
    
    show shark happy
    "testing expression: happy"

    show shark scared
    "testing expression: scared"

    show shark hurt_frame
    "testing expression: hurt"

    show shark hurt
    "testing expression: hurt"

    # =====

    scene white
    play sound sfx_expression_angry
    show shark netral eff_angry
    "testing effects: angry"
    
    scene black
    play sound sfx_expression_laugh
    show shark netral eff_laugh_y
    "testing effects: happy yellow"

    scene white
    play sound sfx_expression_laugh
    show shark netral eff_laugh_b
    "testing effects: happy black"

    scene black
    play sound sfx_expression_laugh
    show shark netral eff_laugh_r
    "testing effects: happy red"

    play sound sfx_expression_shocked
    show shark netral eff_surprise_y
    "testing effects: surpised yellow"

    play sound sfx_expression_shocked
    show shark netral eff_surprise_r
    "testing effects: surpised red"

    scene black
    show shark netral eff_sweat_w
    "testing effects: sweat white"

    show shark netral eff_sweat_b
    "testing effects: sweat blue"

    play sound sfx_expression_surprised
    show shark netral eff_exclamation_r
    "testing effects: exclamation red"

    play sound sfx_expression_surprised
    show shark netral eff_exclamation_y
    "testing effects: exclamation yellow"

    play sound sfx_expression_confused
    show shark netral eff_question_mark_r 
    "testing effects: question mark red"

    play sound sfx_expression_confused
    show shark netral eff_question_mark_y
    "testing effects: question mark"

    scene black
    show shark netral eff_sleepy_w
    "testing effects: sleepy white"

    scene white
    show shark netral eff_sleepy_b
    "testing effects: sleepy black"

    play sound sfx_expression_sleep
    show shark netral eff_snot
    "testing effects: snot"

    play sound sfx_expression_sigh
    show shark netral eff_sigh
    "testing effects: dissapointed"

    show shark netral eff_pale
    "testing effects: pale"

    show shark netral eff_confused
    "testing effects: confused"

    show shark netral eff_inspiration_b
    "testing effects: inspiration black"

    show shark netral eff_inspiration_y
    "testing effects: inspiration yellow"

    scene black
    show shark netral eff_realization
    "testing effects: realization"

    show shark netral eff_yelling
    "testing effects: yelling"

    scene black
    show shark netral eff_sparkle
    "testing effects: sparkle"

    show shark netral eff_heart
    "testing effects: heart"

    scene white
    show shark netral eff_drowsy_b
    "testing effects: drowsy black"

    scene black
    show shark netral eff_drowsy_w
    "testing effects: drowsy white"

    show shark netral eff_drowsy_y
    "testing effects: drowsy yellow"

    scene white
    show shark netral eff_tremble_b
    "testing effects: tremble black"

    scene black
    show shark netral eff_tremble_w
    "testing effects: tremble white"

    hide shark

    pause

    return