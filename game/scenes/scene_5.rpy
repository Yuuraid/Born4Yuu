# label start:

label scene_5:
    # scene black #sementara
    # $ quick_menu = True
    # # play music 
    # # scene teras penginapan pagi with Dissolve(2.0)
    # BG teras penginapan pagi
    scene inn entrance_2
    show yuura netral at center, idle
    nd_narrator_brown "Setelah ditinggal oleh Haruto, entah mengapa rasa lelahku kembali, rasanya sangat berat sekali untuk melangkah."
    
    nd_narrator_brown "Kaki sakit, kepalaku pusing, rasanya seperti aku akan pingsan saat ini juga."
        # show yuura normal animated at center
        # with Dissolve(1.0)
    
    show yuura at speaking
    nd_yuura_brown "Ah... Kakiku sudah tak sanggup melangkah, apakah pada akhirnya...apakah aku..."
    
    scene inn entrance_2 at enblur
    show yuura netral at center, idle 
    with fade

    nd_narrator_brown "Aku berjalan dengan terhuyung-huyung, badanku gemetar, penglihatanku mulai kabur."

    show yuura at fall_down
    $ renpy.pause(0.6, hard=True) # Waits for the falling animation to finish
    show layer master at shake
    hide yuura
        # # bgm stop
        # hide yuura normal animated with moveoutbottom
        # show layer master at shake_custom
    nd_narrator_brown "Tiba tiba tubuhku tersungkur tak berdaya, aku melihat seorang sedang berdiri diam di kejauhan."
    
    nd_narrator_brown "Tanganku berusaha menggapainya, suaraku yang sudah serak berusaha berteriak ke arahnya."
    
    scene black with eye_close

    nd_yuura_black "Tolong..."
        # show Unknown at center with Dissolve(1.0)
    
    voice voice_1_5_59_taro
    wd_unknown_black "Anee? ANEEE!?"
    
    nd_narrator_black "Orang itu langsung berlari menghampiriku, dengan tangannya yang lembut dia berusaha membangunkanku."
    
    voice voice_1_5_60_taro
    wd_unknown_black "Anee, bangun anee! Siapapun tolong! Anee tidak sadarkan diri!"
    
    nd_narrator_black "Mendengar teriakan orang itu, anak penginapan langsung berlari ke arahku, membantu mengangkatku untuk masuk ke dalam penginapan."
    
        # $ quick_menu = False

    jump scene_6