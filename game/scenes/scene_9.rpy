# label start:

label scene_9:
    play music bgm_scene8_awkward_yoyu_ver_1st_part_only volume 1.0 loop
    scene transition_screen orange concentrationline02_w with fade
    show yuura netral at ease_custom(offscreenleft, center, 0.5), speaking, face_flip

    nd_narrator_brown "Aku melanjutkan pencarian jalan keluar."

    show yuura at ease_custom(center, offscreenright, 0.5), speaking, face_flip

    scene inn lorong lantai_2
    show akasyah netral at right
    with fade
    pause 1.0
    show yuura netral at center, face_flip with easeinleft
    show layer master at shake
    play sound sfx_punch_impact_03
    show yuura angry eff_angry at collide_leftward
    show akasyah angry eff_angry at collide_rightward, face_flip
    
    # # Shake screen precisely upon impact (0.25s delay matches easein timing)
    # $ renpy.pause(0.25, hard=True)
    # with hpunch 

    nd_narrator_brown "Namun, tanpa sengaja aku menabrak salah seorang yang sedang berdiri menikmati minumannya."

        # play sound bruuk 
    # stop music
    # play music bgm_scene8_awkward_yoyu_ver volume 1.0 loop
    
    show yuura at reset_xoffset
    show akasyah at reset_xoffset 
    with ease

    show yuura at idle, face_flip
    show akasyah angry at right, speaking
    voice voice_2_9_87_akasyah
    wd_unknown_brown "Dasar saus tartar! Siapa yang berani bikin Yoyu gue jatoh!"
    
    show yuura at left, face_flip with ease
    show akasyah at idle
    nd_narrator_brown "Dia terlihat sangat kesal karena minumannya tumpah dilantai."
    
    show yuura angry at speaking
    nd_you_brown "Aduuhh apaan sih! Ngapain coba berdiri di tengah jalan, dikira ini jalan punya nenek moyangnya apa gimana!?"
    
    show akasyah at speaking
    show yuura at idle
    voice voice_2_9_89_akasyah
    wd_unknown_brown "Oh! Jadi elu Yur! Lu kalo jalan pake mata dong bang** udah pendek, tua, nyusahin lagi"
    
    show akasyah at idle
    show yuura at speaking
    nd_you_brown "Kurang ajar kamu ya! Kupukul-pukulin juga kamu!"
    
    show yuura at center with ease
    pause 0.3
    show yuura at left with ease
    nd_narrator_brown "Aku berusaha mendorong orang itu. Tapi karena tubuhku kecil dan PENDEK, aku tidak bisa membuatnya bergeser."
    
    show akasyah at speaking
    show yuura at idle
    voice voice_2_9_91_akasyah
    wd_unknown_brown "Lu bukannya ngalah sama yang muda! liat nih baju gue jadi kotor gara-gara lu!"
    
    show akasyah at idle
    show yuura at speaking
    nd_you_brown "Kok jadi salahku!? Kamu yang berdiri di tengah jalan, kok aku yang salah!?"
    
    show akasyah at speaking
    show yuura at idle
    voice voice_2_9_93_akasyah
    wd_unknown_brown "Ah berisik lu Yur!"
    play sound sfx_punch_2
    stop music
    show akasyah at idle
    show pe punch yellow transparent with CropMove(0.2, "wipeleft")
    pause 0.2
    hide pe punch yellow
    show akasyah at idle, zorder 5
    show yuura scared none at custom_sprite_pos(x=-0.5)
    show seiya netral at custom_sprite_pos(x=1.3), idle
    with fade
    play music bgm_scene1_rock
    nd_narrator_brown "Sebuah tangan melesat ke arahku dengan sangat cepat, tapi beruntung aku tiba-tiba berpindah tempat agak jauh dari orang itu."
    
    show akasyah at speaking
    voice voice_2_9_94_akasyah
    wd_unknown_brown "HM?! SEIYAAAAAAAAA!!!"
    
    show akasyah at idle
    nd_narrator_brown "Tiba-tiba muncul orang dari belakang orang itu dan langsung menahan pergerakannya."
    
    show seiya at speaking
    voice voice_2_9_95_seiya
    nd_seiya_brown "Sudah lama tidak bertemu Akasyah, apa kamu rindu denganku?"
    
    show akasyah at speaking
    show seiya at idle
    voice voice_2_9_96_akasyah
    wd_akasyah_brown "BRENGSEK! LEPASIN GUA SEKARANG JUGA WOY"
    
    show akasyah at idle
    show seiya at speaking
    voice voice_2_9_97_seiya
    nd_seiya_brown "Coba saja, itu pun jika kamu benar-benar ingin dipermalukan olehku~"
    
    show akasyah at speaking
    show seiya at idle
    voice voice_2_9_98_akasyah
    wd_akasyah_brown "SIALAN! GUA BILANG LEPAS!!!!"
    
    play sound sfx_action_whoosh_scene13_16
    show akasyah at center, idle with ease
    nd_narrator_brown "Dengan kecepatan luar biasa, Akasyah lolos dan langsung menerjangku penuh amarah!{w=1}{nw}"
    
    play sound sfx_shadow_teleport
    show akasyah at right with fade
    nd_narrator_brown "Tapi, Seiya langsung memindahkannya lagi dengan menggunakan manipulasi bayangan."
    
    show seiya eff_exclamation_r at speaking
    with hpunch
    voice voice_2_9_99_seiya
    nd_seiya_brown "PERGI SEKARANG JUGA! AKU TAK BISA MENAHANNYA TERLALU LAMA!"
        # show layer master at shake_custom
    
    show akasyah at speaking
    show seiya none at idle
    voice voice_2_9_100_akasyah
    wd_akasyah_brown "SEIYAAAAAAAAA!!!!!!"
    
    play sound sfx_action_whoosh_scene13_16
    hide yuura at face_flip with easeoutleft
    scene black with fade
    nd_narrator_black "Aku langsung lari dengan sangat cepat, sebisa mungkin menjauh dari mereka berdua." 
    
    play sound sfx_explode
    nd_narrator_black "Aku terus mendengarkan suara ledakan dari tempat itu seraya aku menjauh."
    
    nd_narrator_black "Aku hanya bisa lari untuk selamat dari semua bencana ini"

    # stop music

    jump scene_10