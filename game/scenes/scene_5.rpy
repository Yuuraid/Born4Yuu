# label start:

label scene_5:
    show yuura netral eff_exclamation_y at face_flip

    nd_narrator_brown "Setelah ditinggal oleh Haruto, pandangaku tertuju di gerbang tempat ini"
    
    nd_narrator_brown "Entah mengapa setelah melihat gerbang pintu ini. Aku..."

    play music bgm_scene1_foto_foto_kenangan volume 1.0 loop
    camera:
        zoom 2.0
        xalign 0.45
        yalign 0.3
    scene inn entrance_2
    show yuura netral none at face_flip, center
    # nd_narrator_brown "Setelah ditinggal oleh Haruto, entah mengapa rasa lelahku kembali, rasanya sangat berat sekali untuk melangkah."
    
    show layer master at shake
    show yuura hurt eff_tremble_w at speaking
    nd_you_brown "ADUH!!"
        # show yuura normal animated at center
        # with Dissolve(1.0)
    
    show yuura at speak_in_mind
    nd_you_brown "(Kepalaku pusing, apakah aku kecapean habis lari seharian ini?)"

    scene inn entrance_2 at enblur
    show yuura hurt eff_confused at center 
    camera:
        zoom 2.0
        xalign 0.45
        yalign 0.3
    with dissolve

    pause 0.2

    show yuura hurt eff_confused at custom_sprite_pos(x=0.4) with ease

    nd_narrator_brown "Aku berjalan dengan terhuyung-huyung, badanku gemetar, penglihatanku mulai kabur."

    # stop music
    $ renpy.music.set_volume(0.5, channel="music")
    #sfx jatuh

    show yuura at fall_down
    $ renpy.pause(0.6, hard=True) # Waits for the falling animation to finish
    show layer master at shake
    play sound sfx_action_fall_down_scene5_14
    hide yuura

    nd_narrator_brown "Tiba tiba tubuhku tersungkur tak berdaya, aku melihat seorang sedang berdiri diam di kejauhan."
    
    # pause 0.5
    # scene black
    # with fade

    show taro netral at left, silhouette with easeinleft

    nd_narrator_brown "Tanganku berusaha menggapainya, suaraku yang sudah serak berusaha berteriak ke arahnya."
    
    scene black with eye_close

    #play sound ears ringing
    nd_you_black "Tolong..."
    
    voice voice_1_5_59_taro
    wd_unknown_black "Anee? ANEEE!?"
    
    nd_narrator_black "Orang itu langsung berlari menghampiriku, dengan tangannya yang lembut dia berusaha membangunkanku."
    
    voice voice_1_5_60_taro
    wd_unknown_black "Anee, bangun anee! Siapapun tolong! Anee tidak sadarkan diri!"
    
    nd_narrator_black "Mendengar teriakan orang itu, anak penginapan langsung berlari ke arahku, membantu mengangkatku untuk masuk ke dalam penginapan."
    
    camera:
        zoom 1.0
        xalign 0.0
        yalign 0.0

        # $ quick_menu = False

    jump scene_6