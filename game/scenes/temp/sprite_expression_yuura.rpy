label sprite_animation_yuura:

    "yuura"

    show yuura netral
    "testing expression: netral"

    show yuura angry
    "testing expression: angry"

    show yuura sad
    "testing expression: sad"
    
    show yuura happy
    "testing expression: happy"

    show yuura scared
    "testing expression: scared"

    show yuura hurt
    "testing expression: hurt"

    hide yuura

    play sound sfx_expression_angry
    show yuura angry eff_angry
    "testing effects: angry"
    
    play sound sfx_expression_laugh
    show yuura netral eff_laugh
    "testing effects: happy"

    play sound sfx_expression_shocked
    show yuura scared eff_surprise_y
    "testing effects: surpised"

    show yuura scared eff_sweat_w
    "testing effects: sweat"

    play sound sfx_expression_surprised
    show yuura scared eff_exclamation
    "testing effects: exclamation"

    play sound sfx_expression_confused
    show yuura scared eff_question_mark
    "testing effects: question mark"

    show yuura sad eff_sleepy
    "testing effects: sleepy"

    play sound sfx_expression_sleep
    show yuura sad eff_snot
    "testing effects: snot"

    play sound sfx_expression_sigh
    show yuura sad eff_sigh
    "testing effects: dissapointed"

    show yuura sad eff_pale
    "testing effects: pale"

    
    show yuura sad eff_confused
    "testing effects: confused"

    hide yuura

    pause

    return