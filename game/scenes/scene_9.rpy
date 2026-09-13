# label start:

label scene_9:

    # BG: Tangga menuju lantai 2
        # play music awkward and yoyu with fadein 1.0 -> define dulu
        # show tangga menuju lantai 2 with Dissolve (1.0)
    scene transition_screen orange concentrationline02_w with fade
    show yuura netral at ease_custom(offscreenleft, center, 0.5), speaking, face_flip

    nd_narrator_brown "Aku naik ke atas untuk menghindari dari orang-orang, segera berlari untuk mencari jalan keluar."

    show yuura at ease_custom(center, offscreenright, 0.5), speaking, face_flip

    scene inn lorong lantai_2
    show akasyah netral at right, idle
    with fade
    pause 1.0
    show yuura netral at center, idle, face_flip with easeinleft
    show yuura netral at collide_leftward
    show akasyah angry at collide_rightward, face_flip
    
    # Shake screen precisely upon impact (0.25s delay matches easein timing)
    $ renpy.pause(0.25, hard=True)
    with hpunch 

    nd_narrator_brown "Namun, tanpa sengaja aku menabrak salah seorang yang sedang berdiri menatap langit sambil minum susu."
        # play sound bruuk -> define dulu
    
    show yuura at reset_xoffset
    show akasyah at reset_xoffset 
    with ease

    show yuura at idle, face_flip
    show akasyah angry at right, speaking
    wd_unknown_brown "Dasar saus tartar ! Siapa yang berani bikin Yoyu gue jatoh !?"
    
    show yuura at left, face_flip with ease
    show akasyah at idle
    nd_narrator_brown "Dia terlihat sangat kesal karena minumannya tumpah di baju kesayangannya."
    
    show yuura angry at speaking
    nd_yuura_brown "Aduuhh apaan sih ! Ngapain coba berdiri di tengah jalan, dikira ini jalan punya nenek moyangnya apa gimana !?"
    
    show akasyah at speaking
    show yuura at idle
    wd_unknown_brown "Oh ! Jadi elu Yur ! Lu kalo jalan pake mata dong bang*** udah pendek, tua, nyusahin lagi."
    
    show akasyah at idle
    show yuura at speaking
    nd_yuura_brown "Kurang ajar kamu ya ! Kupukul-pukulin juga kamu !"
    
    show yuura at center with ease
    pause 0.3
    show yuura at left with ease
    nd_narrator_brown "Aku berusaha mendorong Akasyah. Tapi karena tubuhku kecil dan PENDEK, aku tidak bisa membuatnya bergeser."
    
    show akasyah at speaking
    show yuura at idle
    wd_unknown_brown "Lu bukannya ngalah sama yang muda ! Liat nih baju gue jadi kotor gara-gar lu !"
    
    show akasyah at idle
    show yuura at speaking
    nd_yuura_brown "Kok jadi salahku !? Kamu yang berdiri di tengah jalan, kok aku yang salah !?"
    
    show akasyah at speaking
    show yuura at idle
    wd_unknown_brown "Ah berisik lu, Yur !"
    
    show akasyah at idle
    show pe punch yellow transparent with CropMove(0.2, "wipeleft")
    pause 0.2
    hide pe punch yellow
    show akasyah at idle, zorder 5
    show yuura scared at custom_sprite_pos(x=-0.5)
    show seiya netral at custom_sprite_pos(x=1.3), idle
    with fade
    nd_narrator_brown "Sebuah tangan melesat ke arahku dengan sangat cepat, tapi beruntung aku tiba-tiba terteleporasi agak jauh dari Akasyah."
    
    show akasyah at speaking
    wd_unknown_brown "HM !? SEIYAAAAA !!!"
    
    show akasyah at idle
    nd_narrator_brown "Seiya muncul dari belakang orang itu dan langsung menahan pergerakannya."
    
    show seiya at speaking
    nd_seiya_brown "Sudah lama tidak bertemu Akasyah, apa kamu rindu denganku ?"
    
    show akasyah at speaking
    show seiya at idle
    wd_akasyah_brown "Brens*k ! LEPASKAN AKU SEKARANG JUGA !"
    
    show akasyah at idle
    show seiya at speaking
    nd_seiya_brown "Coba saja, itu pun jika kamu benar-benar ingin dipermalukan olehku~"
    
    show akasyah at speaking
    show seiya at idle
    wd_akasyah_brown "SIALAN ! AKU BILANG LEPAS !!!"
    
    show akasyah at center, idle with ease
    nd_narrator_brown "Akasyah berhasil lepas dengan kecepatannya yang luar biasa, dia langsung melompat ke arahku dengan penuh kemarahan."
    
    show akasyah at right with fade
    nd_narrator_brown "Tapi, Seiya langsung memindahkannya lagi dengan menggunakan manipulasi bayangan."
    
    show seiya at speaking
    with hpunch
    nd_seiya_brown "PERGI SEKARANG JUGA ! AKU TAK BISA MENAHANNYA TERLALU LAMA !"
        # show layer master at shake_custom
    
    show akasyah at speaking
    show seiya at idle
    wd_akasyah_brown "SEIYAAAAAA !!!!"
    
    hide yuura at face_flip with easeoutleft
    scene black with fade
    nd_narrator_black "Aku langsung lari dengan sangat cepat, sebisa mungkin menjauh dari mereka berdua. Aku terus mendengarkan erangan dari Akasyah dan suara ledakan di belakangku, tapi apa dayaku."
    
    nd_narrator_black "Aku hanya bisa lari untuk selamat dari semua bencana ini"
        # stop music

    jump scene_10