define config.font_name_map["alien"] = "fonts/number_one.ttf"

screen centered_typewriter(txt, speed=20, x_align=0.5, y_align=0.5):
    text "{cps=[speed]}" + txt + "{/cps}":
        xalign x_align
        yalign y_align
        text_align 0.0  # Centers multi-line text blocks
        color "#000000"
        xmaximum 1000
        size 64         # Customize font size as needed