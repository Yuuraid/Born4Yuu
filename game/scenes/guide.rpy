init python:
    # Define your slides as a list of dictionaries
    tutorial_slides = [
        {
            "image": "images/slide1.png",
            "title": "Welcome to the Game",
            "text": "Here is the first slide. You can put lore, instructions, or a gallery entry here."
        },
        {
            "image": "images/slide2.png",
            "title": "Combat Basics",
            "text": "Click on targets to attack. Watch your stamina bar on the top left!"
        },
        {
            "image": "images/slide3.png",
            "title": "Inventory",
            "text": "Press 'I' at any time to open your bag and equip new items."
        }
    ]

screen tutorial_viewer(slides):
    modal True  # Blocks clicking the dialogue behind the screen
    default current_index = 0
    $ slide = slides[current_index]

    # Dimmed background
    add Solid("#000000cc")

    frame:
        align (0.5, 0.5)
        xsize 1200
        ysize 650
        padding (40, 40)

        vbox:
            spacing 20
            xfill True
            yfill True

            # MAIN CONTENT: Image on the left, Text on the right
            hbox:
                spacing 40
                yalign 0.5
                ysize 480

                # Left side: Image
                frame:
                    background None
                    xsize 520
                    yfill True
                    add slide["image"] align (0.5, 0.5) fit "contain"

                # Right side: Scrollable Text
                viewport:
                    xsize 540
                    yfill True
                    scrollbars "vertical"
                    mousewheel True

                    vbox:
                        spacing 15
                        text slide["title"] size 36 bold True
                        text slide["text"] size 24

            # BOTTOM NAVIGATION: Previous, Page Counter, Next / Close
            hbox:
                xfill True
                yalign 1.0

                textbutton "← Previous":
                    align (0.0, 0.5)
                    sensitive (current_index > 0)
                    action SetScreenVariable("current_index", current_index - 1)

                text "[current_index + 1] / [len(slides)]":
                    align (0.5, 0.5)
                    size 22

                if current_index < len(slides) - 1:
                    textbutton "Next →":
                        align (1.0, 0.5)
                        action SetScreenVariable("current_index", current_index + 1)
                else:
                    textbutton "Close":
                        align (1.0, 0.5)
                        action Return()