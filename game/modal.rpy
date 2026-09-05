# Modal Item
screen show_item(item_img, item_name=""):

    modal True

    add Solid("#00000088")

    frame:
        xalign 0.5
        yalign 0.2
        padding (30, 30)

        vbox:
            spacing 15
            xalign 0.5

            textbutton "X":
                xalign 1.0
                yalign 0.0
                action Hide("show_item")

            add item_img:
                xalign 0.5

            if item_name:
                text item_name:
                    xalign 0.5
                    size 28