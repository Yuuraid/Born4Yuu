init python:
    # Define your slides as a list of dictionaries
    credits_slides = [

        {
            "image": "scenes/credits_meme/slide__0025_slide_1.png",
            "title": "Project Lead",
            "text": "Koto Shirabe / Ibe"
        },
        {
            "image": "scenes/credits_meme/slide__0024_slide_2.png",
            "title": "Project Coordinator",
            "text": "Nicholas Lim"
        },
        {
            "image": "scenes/credits_meme/slide__0023_slide_3.png",
            "title": "Game Director",
            "text": "Risol"
        },
        {
            "image": "scenes/credits_meme/slide__0022_slide_4.png",
            "title": "Scenario Writer",
            "text": "Haruto"
        },
        {
            "image": "scenes/credits_meme/slide__0021_slide_5.png",
            "title": "Screenwriter & VA Director",
            "text": "Mirai Naisei / Cyber"
        },
        {
            "image": "scenes/credits_meme/slide__0020_slide_6.png",
            "title": "VA",
            "text": "Aergia as himself\n\nAkasyah as himself\n\nAxiaregis / Edy as themselves (?)\n\nDawam as himself\n\nDityo as himself\n\nRian as himself\n\nSeiya as himself\n\nShark as himself\n\nRisol as Yuuraid"
        },
        {
            "image": "scenes/credits_meme/slide__0019_slide_7.png",
            "title": "Supporting Character VA",
            "text": "Haruto\n\nTarochips"
        },
        {
            "image": "scenes/credits_meme/slide__0018_slide_8.png",
            "title": "Game Designer",
            "text": "Josua"
        },
        {
            "image": "scenes/credits_meme/slide__0017_slide_9.png",
            "title": "Story Editor",
            "text": "Arzi\n\nRisol\n\nJosua\n\nIbe"
        },
        {
            "image": "scenes/credits_meme/slide__0016_slide_10.png",
            "title": "Lead Artist",
            "text": "Tarochips"
        },
        {
            "image": "scenes/credits_meme/slide__0015_slide_11.png",
            "title": "CG Artist",
            "text": "Niver\n\nGiri\n\nGadjeman\n\nTofu\n\nStephen\n\nTarochips"
        },
        {
            "image": "scenes/credits_meme/slide__0014_slide_12.png",
            "title": "Sprite Artist",
            "text": "Niver\n\nTofu\n\nGadjeman\n\nGiri\n\nStephen\n\nTarochips\n\nBli Ari"
        },
        {
            "image": "scenes/credits_meme/slide__0013_slide_13.png",
            "title": "Partial Effects",
            "text": "LarkMeto"
        },
        {
            "image": "scenes/credits_meme/slide__0012_slide_14.png",
            "title": "Asset Artist",
            "text": "LarkMeto\n\nGiri\n\nGadjeman"
        },
        {
            "image": "scenes/credits_meme/slide__0011_slide_15.png",
            "title": "Background Source",
            "text": "Eggy Hakaze"
        },
        {
            "image": "scenes/credits_meme/slide__0010_slide_16.png",
            "title": "Pahlawan kesiagan",
            "text": "STEP Pheepi Chuupi"
        },
        {
            "image": "scenes/credits_meme/slide__0009_slide_17.png",
            "title": "Game UI",
            "text": "LarkMeto\n\nJosua"
        },
        {
            "image": "scenes/credits_meme/slide__0008_slide_18.png",
            "title": "Music Composer",
            "text": "Kurozen\n\nJack"
        },
        {
            "image": "scenes/credits_meme/slide__0007_slide_19.png",
            "title": "Sound Designer",
            "text": "Lafi"
        },
        {
            "image": "scenes/credits_meme/slide__0006_slide_20.png",
            "title": "Sound Engineer",
            "text": "Jack\n\nYC\n\nNett"
        },
        {
            "image": "scenes/credits_meme/slide__0005_slide_21.png",
            "title": "Programmer",
            "text": "Hiko\n\nNanafi\n\nJosua"
        },
        {
            "image": "scenes/credits_meme/slide__0004_slide_22.png",
            "title": "Asset Manager",
            "text": "Yudes"
        },
        {
            "image": "scenes/credits_meme/slide__0003_slide_23.png",
            "title": "Tech Support",
            "text": "Nepgust\n\nZeita"
        },
        {
            "image": "scenes/credits_meme/slide__0002_slide_24.png",
            "title": "Playtester",
            "text": "Yudes\n\nTarochips\n\nNanafi\n\nSanataTri"
        },
        {
            "image": "scenes/credits_meme/slide__0001_slide_25.png",
            "title": "Publishing",
            "text": "Nanafi"
        },
        {
            "image": "scenes/credits_meme/slide__0000_slide_26.png",
            "title": "Special Thanks",
            "text": "Yuuraid\n\nLivium\n\nPenjara Livium\n\nUdi Dolken\n\nYuura Yozakura"
        },
    ]

screen slide_viewer(slides):
    modal True
    default current_index = 0
    $ slide = slides[current_index]

    # Solid or dimmed full-screen backdrop
    add Solid("#ffffff")

    # Full-screen container
    frame:
        background None
        xfill True
        yfill True
        padding (80, 120)

        vbox:
            spacing 30
            xfill True
            yfill True

            # MAIN CONTENT: Takes up remaining vertical space above the nav bar
            hbox:
                spacing 60
                xfill True
                yfill True

                # Left side: Full-height image column
                frame:
                    background None
                    xsize 860
                    yfill True
                    add slide["image"] align (0.5, 0.5) fit "contain"

                # Right side: Scrollable text column
                viewport:
                    xfill True
                    yfill True
                    # scrollbars "vertical"
                    mousewheel True

                    vbox:
                        spacing 24
                        xfill True
                        text slide["title"] size 48 color "#000000" font "fonts/FOT-SlumpStd-DB.ttf"
                        text slide["text"] size 28 color "#000000" font "fonts/FOT-SlumpStd-DB.ttf"

            # BOTTOM NAVIGATION: Anchored along the bottom edge
            hbox:
                xfill True
                ysize 50

                textbutton "← Previous":
                    align (0.0, 0.5)
                    text_size 26
                    sensitive (current_index > 0)
                    action SetScreenVariable("current_index", current_index - 1)

                text "[current_index + 1] / [len(slides)]":
                    align (0.5, 0.5)
                    size 24
                    color "#000000"

                if current_index < len(slides) - 1:
                    textbutton "Next →":
                        align (1.0, 0.5)
                        text_size 26
                        action SetScreenVariable("current_index", current_index + 1)
                else:
                    textbutton "Close":
                        align (1.0, 0.5)
                        text_size 26
                        action Return()

    key "K_LEFT" action If(current_index > 0, SetScreenVariable("current_index", current_index - 1))
    key "K_RIGHT" action If(current_index < len(slides) - 1, SetScreenVariable("current_index", current_index + 1))


label scene_credits:
    scene white
    # "this is credits"

    # "Let's review the rules before we begin."

    call screen slide_viewer(credits_slides)

    # "Now that you're ready, let's go!"
    pause

    return