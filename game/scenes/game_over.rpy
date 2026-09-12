# label game_over_screen:
#     scene game_over with fade

#     pause

# Custom Game Over Screen
screen game_over_screen(reason_text="You made a fatal mistake..."):
    
    # Lock key input so the player can't advance dialogue behind the UI
    modal True

    # 1. Background Image
    add "assets/bg/Game_Over_Screen.png" fit "cover"  # Replace with your image path

    # # ATL transition for the screen contents
    # on "show" action Function(renpy.transition, fade)

    # 2. Main Container Box
    vbox:
        align (0.5, 0.75)
        spacing 25

        # Game Over Title
        # text "GAME OVER" :
        #     size 72
        #     color "#ff3333"
        #     bold True
        #     xalign 0.5
        #     outlines [(3, "#000000", 0, 0)]

        # Dynamic Subtext / Textbox Frame
        frame:
            xalign 0.5
            xsize 800
            # padding (30, 20)
            background Frame("gui/frame_borderless.png", 10, 10) # Uses default GUI frame

            text reason_text:
                xalign 0.5
                text_align 0.5
                size 26
                color "#ffffff"
                font "fonts/FOT-SlumpStd-DB.ttf"
                italic True

        null height 20

        # Action Buttons
        vbox:
            xalign 0.5
            spacing 15

            # Button 1: Reload most recent Auto Save
            textbutton "Reload Last Auto-Save":
                xalign 0.5
                action QuickLoad()  # Loads the latest auto-save / quick-save
                text_size 30
                text_hover_color "#ffc266"

            # Button 2: Load Game Screen (Manual Selection)
            textbutton "Load Game Menu":
                xalign 0.5
                action ShowMenu("load")
                text_size 28
                text_hover_color "#cccccc"

            # Button 3: Return to Main Menu
            textbutton "Main Menu":
                xalign 0.5
                action MainMenu(confirm=False)
                text_size 26
                text_hover_color "#aaaaaa"