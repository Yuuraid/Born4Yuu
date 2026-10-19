# label start:

label scene_14:

    scene inn lorong malam with fade
    # play sound buk
    # nd_narrator_brown "Pantatku menghantam tanah duluan."
    
    show yuura scared at center, speaking
    with easeinleft
    show yuura scared at center, shake
    nd_yuura_brown "ADUH..."
    show yuura at idle
    
    show seiya netral at left, speaking, flip_image
    with moveinleft
    voice voice_3_14_205_seiya
    nd_unknown_brown "Ane gapapa ?"
    show seiya at idle
    
    show yuura at right
    with move
    nd_narrator_brown "Aku menyadari bahwa ada orang di dekatku, aku segera mundur berapa langkah karena reflek."
    
    nd_narrator_brown "Menyadari bahwa itu adalah Seiya, orang sudah membantuku sebelumnya, aku segera mendekat meski sedikit ragu."
    
    show yuura happy at speaking
    nd_yuura_brown "Seiya !"
    
    nd_yuura_brown "Makasih banget udah nolongin aku dari tendangan itu. Bisa mampus aku kalau bukan karena kamu."
    show yuura at idle
        
    show seiya at speaking
    voice voice_3_14_208_seiya
    nd_seiya_brown "Aman aja, Anee. Tapi saranku sekarang kamu lari."
    show seiya at idle
        
    show yuura netral at speaking
    nd_yuura_brown "Kenapa emangnya ?"
    show yuura at idle

    transform flip_image(horizontal=True, vertical=False):
        xzoom (-1.0 if horizontal else 1.0)
        yzoom (-1.0 if vertical else 1.0)

    transform movetoright(xalign_pos=0.5, duration=0.5):
        xalign 0.0
        easeout 0.15 xalign 0.8
    
    transform slightright(xalign_pos=0.5, duration=0.5):
        xalign 1.0
        linear 0.15 xalign 1.2

    transform movetoleft(xalign_pos=0.0, duration=0.5):
        xalign 0.25
        linear 0.15 xalign 0.0

    transform akasyah_sat_set:
        xalign 0 yoffset 0
        easein 0.1 xalign 0.7 yoffset -200
        pause .75
        easeout 0.2 xalign 0.3 yoffset -100
        pause .75
        easeout 0.2 xalign 0.6 yoffset -300
        pause .75
        ease 0.2 xalign 0 yoffset 0

    transform biji_melayang:
        yalign 0.0 zoom 0.5
        linear 0.1 xoffset -2000 
    transform biji_melayang2:
        yalign 0.1 zoom 0.5
        linear 0.1 xoffset -5000 
    transform biji_melayang3:
        yalign 0.5 zoom 0.5
        linear 0.1 xoffset 800
        pause .5
        rotate 210
        linear 0.5 xoffset 4000 yoffset -4000
    
    # show pe blue_projectile ball_0 transparent as p1 at biji_melayang, flip_image
    # with moveinright
    # pause .5
    # show pe blue_projectile ball_0 transparent as p2 at biji_melayang2, flip_image
    # with moveinright
    # pause .5
    # show pe blue_projectile ball_0 transparent as p3 at biji_melayang3, flip_image
    # with moveinright
    # pause .5

    show seiya at speaking
    voice voice_3_14_210_seiya
    nd_seiya_brown "Tempat ini sudah tidak aman, sebaik-{nw}"
    # show seiya at idle
    scene cg_arc_3_scene_14_shoot_1:
        zoom 1.0
        xalign 0.5
        linear 0.2 xalign 1.0 zoom 1.05
    pause 0.3
    scene pe dash blue with Flash
    show layer master at shake
    
    nd_narrator_brown "Belum sempat menyelesaikan bicaranya, Seiya mendengar suara yang sangat keras mengarah padanya.{w=3.0}{nw}"
    
    scene cg_arc_3_scene_14_shoot_2:
        xalign 0.7
        yalign 0.9
        linear 7.0 xalign 0.0 yalign 0.0
    with Flash
    pause 6.0
    # Start CG
# ----------recheck
    # show seiya:
    #     linear .5 xzoom -1.0 yzoom 1.0
    #     movetoright
    #     shake
# -----------recheck
    scene cg_arc_3_scene_14_shoot_3 with Flash

    
    nd_narrator_brown "Dia berbalik dan menangkis tendangan mendadak dari pria yang berpakaian serba coklat yang membuat pria itu mundur beberapa langkah, sedangkan lengan Seiya sedikit berasap akibat tendangan tersebut."


    scene inn lorong malam
    show yuura sad at idle, custom_sprite_pos(x=0.8)
    show seiya hurt at idle, right
    show akasyah angry at left, speaking
    with fade
    
    voice voice_3_14_211_akasyah
    nd_akasyah_brown "KETEMU LU BANGSAT !"
    show akasyah at idle
        
    # show seiya angry at flip_image, speaking
    # voice voice_3_14_212_seiya
    # nd_seiya_brown "FAHH"
    
    voice voice_3_14_213_seiya
    show seiya at speaking
    nd_seiya_brown "Apa yang kau coba lakukan !?"
    
    voice voice_3_14_214_seiya
    nd_seiya_brown "Apa kau ga capek bikin masalah terus buat Yuura ?"
    show seiya at idle
            
    show akasyah at speaking
    voice voice_3_14_215_akasyah
    nd_akasyah_brown "MASALAH ??? LU PIKIR APA YANG LU LAKUIN SEKARANG ?"
    
    voice voice_3_14_216_akasyah
    nd_akasyah_brown "MINGGIR ! JANGAN GANGGU RENCANA GUA !"
    show akasyah at idle
        
    show seiya at speaking
    voice voice_3_14_217_seiya
    nd_seiya_brown "Rencana ? Maksudmu dengan mau menghajar Yuura ? APA ITU YANG KAU SEBUT RENCANA !?"
    show seiya at idle
            
    show akasyah at speaking
    voice voice_3_14_218_akasyah
    nd_akasyah_brown "Mata lu buta apa gimana ?"
    
    voice voice_3_14_219_akasyah
    nd_akasyah_brown "Apa emang lu gabisa bedain Yuura yang asli sama yang palsu ?"
    show akasyah at idle
        
    show seiya at speaking
    voice voice_3_14_220_seiya
    nd_seiya_brown "Apa sih maksudmu ? Apa kamu kebanyakan minum sake siang-siang ?"
    show seiya at idle
    
    nd_narrator_brown "Akasyah melempar sebuah linting."
            
    show akasyah at speaking
    voice voice_3_14_221_akasyah
    nd_akasyah_brown "OI YUUR ! Lu tau ga benda apa ini ?"
    show akasyah at idle
    
    nd_narrator_brown "Aku kaget melihat benda yang dia lempar, aku tidak mengerti untuk apa benda itu dan mengapa dia menanyakan padaku."
            
    show akasyah at speaking
    voice voice_3_14_222_akasyah
    nd_akasyah_brown "Kok diem ? Jawab bangsat !"
    show akasyah at idle
        
    show yuura at speaking
    nd_yuura_brown "Ah...um...ituu..."
    
    nd_yuura_brown "(ARGH SIAL, aku gatau linting apaan ! Lagian sejak kapan aku punya uang untuk melakukan kebiasaan yang sama seperti orang-orang kaya !)"
    show yuura at idle
        
    show akasyah at speaking
    voice voice_3_14_225_akasyah
    nd_akasyah_brown "Hahaha... Udah gua duga lu pasti gabisa jawab pertanyaan gua."
    
    voice voice_3_14_226_akasyah
    nd_akasyah_brown "Sekarang minggir dan biar gua hajar si palsu ini !"
    show akasyah at idle
    
    nd_narrator_brown "Aku melihat senyum lebar di wajah Akasyah yang berhasil mengungkap fakta yang selama ini kututupi."
    
    nd_narrator_brown "Badanku gemetar karena merasa takut bahwa aku tidak akan bisa keluar dari sini hidup-hidup, aku menoleh ke arah Seiya dan mulai melihat raut wajah ragu padanya."
    
    show seiya at custom_sprite_pos(x=0.6)
    show yuura at custom_sprite_pos(x=0.9) 
    with ease
    nd_narrator_brown "Meski begitu Seiya berdiri depan untuk melindungiku."
            
    show akasyah at speaking
    voice voice_3_14_227_akasyah
    nd_akasyah_brown "Lu goblok apa gimana ?"
    
    voice voice_3_14_228_akasyah
    nd_akasyah_brown "Masih mau ngelindungin si peniru sialan ini ? Seiya Seiya..."
    show akasyah at idle
    
    # TODO: im here
    show seiya at speaking
    voice voice_3_14_229_seiya
    nd_seiya_brown "Mau palsu atau bukan, itu bukan urusanmu !"
    show seiya at idle
            
    show akasyah at speaking
    voice voice_3_14_230_akasyah
    nd_akasyah_brown "Oh jelas..."
    voice voice_3_14_231_akasyah
    nd_akasyah_brown "ITU URUSAN GUA !!!"
    show akasyah at idle
    
    # TODO: I want this to be behind seiya
    show yuura behind seiya at consumed_by_darkness
    show pe purple_flame flame_full behind seiya at custom_sprite_pos(x=-2.0, y=0.5), silhouette
    pause 0.2
    hide pe purple_flame flame_full with dissolve
    
    # Use CG here
    scene black with fast_fade
    show pe punch yellow transparent as punch_1:
        zoom 1.1
        xalign 0.5
        yalign 0.5
    with wipe_j_atas(0.25)
    nd_narrator_black "Dalam sekejap, Akasyah berpindah dan memberikan serangan akurat kepada Seiya."
    
    show pe kick serangan_seiya transparent as punch_2:
        zoom 1.1
        xalign 0.5
        yalign 0.5
    with wipe_j_atas()

    nd_narrator_black "Seiya berhasil memprediksi serangan itu dan menangkisnya dengan tangan yang sudah diselimuti oleh bayangan hitam."
    
    hide punch_2 with wipe_j_atas(0.30)

    pause 0.1

    # Resize punch_1 without affecting anything else:
    show pe punch yellow transparent as punch_1:
        # zoom 0.9  # Change this to whatever zoom level you want
        xalign 0.5
        yalign 0.5
        ease 0.25 zoom 0.9

    pause 0.1

    show pe punch yellow transparent as punch_3:
        zoom 1.8
        rotate -90
        xalign 0.75
        yalign 0.7
    with wipe_j_bawah()

    pause 0.1

    # show pe punch yellow transparent as punch_1:
    #     # zoom 0.9  # Change this to whatever zoom level you want
    #     # xalign 0.5
    #     # yalign 0.5
    #     ease 0.25 zoom 0.7
    # show pe punch yellow transparent as punch_3:
    #     # zoom 0.9  # Change this to whatever zoom level you want
    #     xalign 0.75
    #     yalign 0.7
    #     ease 0.25 zoom 1.5

    show pe punch yellow transparent as punch_4:
        zoom 1.5
        rotate -225
        xalign 0.7
        yalign 0.5
    with wipe_j_atas(0.5)

    nd_narrator_black "Tak berhenti di sana, Akasyah mulai menghantam Seiya dengan tinju dan tendangan yang berulang."

    scene inn lorong malam:
        xzoom -1
        zoom 1.3
        xalign 0.0
    show seiya netral at center
    with wipe_kiri(0.5)

    pause 0.2

    scene inn lorong malam:
        xzoom -1
        zoom 1.3
        xalign 1.0
    show seiya netral at right
    with ease

    scene pe blue_projectile full_CG
    camera:
        zoom 2 
    with Dissolve(.15)
    pause .1
    camera:
        zoom 2 xpos -1920 ypos -1080
    with Dissolve(.15)
    pause .1
    camera:
        zoom 2 xpos 0 ypos -1080
    with Dissolve(.15)
    pause .1
    camera:
        zoom 2 xpos -1920 ypos 0
    with Dissolve(.15)
    pause .1 
    camera:
        zoom 1 xpos 0 ypos 0
    with Dissolve(.15)
    # pause .5

    nd_narrator_black "Tak tinggal diam, Seiya melancarkan serangan berupa sihir proyektil yang mengarah ke Akasyah."
    
    scene inn lorong malam
    show akasyah angry at center
    with wipe_kiri(0.5)

    show akasyah at startled_jump
    pause 0.5
    
    show akasyah:
        linear 0.1 xalign 0.3

    show pe blue_projectile ball_0 transparent:
        xzoom -1
        zoom 0.5
        xalign 2.0
        yalign 0.8
        linear 0.5 xalign -1.5
    
    pause 0.5

    show akasyah:
        linear 0.1 xalign 0.8

    show pe blue_projectile ball_0 transparent behind akasyah:
        xzoom -1
        zoom 0.5
        xalign 2.0
        yalign 0.6
        linear 0.5 xalign -1.5

    pause 0.5

    show akasyah:
        linear 0.1 xalign 0.5

    show pe blue_projectile ball_0 transparent:
        xzoom -1
        zoom 0.5
        xalign 2.0
        yalign 0.5
        linear 0.2 xalign 0.9
    pause 0.2
    hide pe blue_projectile ball_0 transparent
    
    show pe blue_projectile ball_0 transparent:
        rotate -30
        zoom 0.5
        xalign 0.9
        yalign 0.5
        linear 0.2 xalign 1.5 yalign 0.0

    show akasyah:
        ease 0.2 xalign 0.0

    # pause

    nd_narrator_brown "Akasyah sesekali menepis serangan itu sebelum akhirnya mundur beberapa langkah untuk menghindar."

    scene inn lorong malam:
        xzoom -1
        zoom 1.3
        xalign 1.0
    show seiya netral at right
    with wipe_kiri(0.2)

    pause 0.5

    hide seiya at consumed_by_darkness
    show pe purple_flame flame_full behind seiya at custom_sprite_pos(x=-2.0, y=0.5), silhouette
    pause 0.2
    hide pe purple_flame flame_full with dissolve

    scene inn lorong malam
    show akasyah angry at left
    with wipe_kanan(0.2)

    show seiya netral behind akasyah at face_flip, custom_sprite_pos(x=-0.3), emerge_from_darkness
    
    pause 0.3

    scene pe kick serangan_seiya with wipe_j_atas(0.2)
    show layer master at shake

    # , silhouette
    # pause 0.2
    # hide pe purple_flame flame_full with dissolve

    # TODO: in this part seiya and akasyah switch side

    nd_narrator_black "Tak melewatkan kesempatan, Seiya muncul dari portal bayangan dan melayangkan tinjunya."

    show pe kick kick_set_alter transparent as aka_counter_1:
        rotate 180
        xalign 0.5
        yalign 0.5
    with wipe_j_bawah(0.2)

    nd_narrator_black "Sayangnya, Akasyah berpindah dan memberikan tendangan telak ke belakang Seiya."
    
    scene inn lorong malam:
        # xzoom -1
        zoom 1.3
        xalign 1.0
    with wipe_kiri(0.2)

    pause 0.2
    scene inn lorong malam:
        # xzoom -1
        zoom 1.3
        xalign 0.0
    with ease
    show seiya hurt at face_flip, ease_custom(offscreenright, center, 0.5)

    nd_narrator_brown "Meski terpental, Seiya berhasil mengikat kaki Akasyah dan memanfaatkan momentum untuk menarik kakinya dan membantingkan tubuhnya ke lantai."
    
    show layer master at shake

    # play sound lantai kayu patah
    nd_narrator_brown "Seiya berhasil memberikan serangan telak, tapi nampaknya itu tak terlalu berefek karena ketika kepulan debu memudar, terlihat Akasyah yang masih berdiri meski dengan darah yang mengalir dari mulutnya."

    scene inn lorong malam:
        xzoom -1
        zoom 1.3
        xalign 1.0
    show akasyah angry at face_flip, speaking, center
    with wipe_kiri(0.2)
            
    voice voice_3_14_232_akasyah
    nd_akasyah_brown "Segitu doang serangan lu ? GUA JUGA BISA !"
    # show akasyah at idle
    
    # Another CG?
    scene black with wipe_j_bawah(0.2)

    show pe kick serangan_seiya transparent:
        # zoom 0.9
        xalign 0.5
        yalign 0.5
        # rotate 60
    with wipe_j_atas(0.2)

    nd_narrator_black "Baru menutup bicaranya, Seiya muncul dari portal bayangan dan melancarkan tinju yang diselimuti energi hitam." 
    
    # TODO: add more sequence
    show pe kick kick_set_alter transparent:
        # zoom 0.9
        xzoom -1
        xalign 0.5
        yalign 0.5
        # rotate 60
    with wipe_j_atas(0.2)

    nd_narrator_black "Akasyah yang sudah memprediksi serangannya langsung menahan serangan Seiya. Akasyah menyeringai membuat Seiya mundur karena merasakan sesuatu yang salah pada Akasyah."

    scene inn lorong malam
    show seiya hurt at face_flip, left, idle
    show akasyah angry at face_flip, right, speaking
    with fade

    voice voice_3_14_233_akasyah
    nd_akasyah_brown "Udah puas ? Now, it's my turn..."
    # show akasyah at idle
    
    scene black with wipe_j_bawah(0.2)

    pause 0.2

    show pe punch yellow transparent:
        # rotate 45
        xzoom -1
        yzoom -1
        rotate 45
        zoom 1.0
        xalign 0.5
        yalign 0.5
    with wipe_j_bawah(0.2)

    pause 0.2

    show serangan_seiya transparent:
        zoom 1.0
        # yzoom -1
        xzoom -1
        xalign 0.5
        yalign 0.5
    with wipe_j_bawah(0.2)

    nd_narrator_black "Akasyah berpindah dan melancarkan serangan pada Seiya, berpindah dan menyerang secara berulang. Seiya lumayan dapat mengikuti alur pertarungan." 

    nd_narrator_black "Namun, nampaknya itu memang rencananya Akasyah supaya Seiya terpancing dalam jebakannya."
    
    scene black
    show pe dash negative_blue:
        zoom 1.0
        xalign 0.5
        yalign 0.5
        ease 0.3 zoom 1.2

    pause 0.3

    hide pe dash

    nd_narrator_black "Akasyah menendang kaki Seiya.{w=1.0}{nw}"
    
    show seiya at speaking
    voice voice_3_14_234_seiya
    nd_seiya_black "Urghhh !!!"
    show seiya at idle
    
    show pe punch swipe transparent with wipe_j_bawah(0.2)

    nd_narrator_black "Seiya kehilangan keseimbangannya karena tak menyadari serangan dadakan itu dan Akasyah segera memanfaatkan kesempatan itu."
    
    show yellow transparent:
        yzoom -1
        zoom 0.8
        rotate -55
        xalign 0.5
        yalign 0.7
    with wipe_j_atas(0.2)

    pause 0.3 
    
    hide yellow transparent
    hide pe punch swipe transparent
    with wipe_j_atas(0.3)

    show yellow transparent:
        # yzoom -1
        zoom 1.5
        rotate 90
        xalign 0.5
        yalign 0.5
    with wipe_j_atas(0.2)

    nd_narrator_black "Akasyah berpindah dan melancarkan tinju ke ulu hati Seiya yang membuatnya tersentak. Tak berhenti, Akasyah menendang ulu hati Seiya dengan lututnya dan menendang Seiya ke atas."
    
    hide yellow transparent

    show yellow transparent:
        # yzoom -1
        xzoom -1
        zoom 1.5
        rotate 130
        xalign 0.5
        yalign 0.4
    with wipe_j_atas(0.2)

    nd_narrator_black "Seiya belum sempat berkutik, sedangkan Akasyah berpindah ke atasnya dan menendang Seiya ke bawah."
    
    scene inn lorong malam
    show seiya hurt at face_flip, left, idle
    show akasyah angry at face_flip, right, speaking
    with fade

        # play sound lantai kayu patah
    # show akasyah at speaking
    voice voice_3_14_235_akasyah
    nd_akasyah_brown "Udah nih? Seiya-Seiya"
    
    voice voice_3_14_236_akasyah
    nd_akasyah_brown "SEKARANG LAH AKHIRNYA ! BYE BYE PAHLAWAN KESIANGAN !"
    
    hide akasyah with easeoutright

    pause 0.1

    scene inn lorong malam:
        xzoom -1
    with wipe_j_bawah(0.2)

    show akasyah angry at face_flip, center with easeinleft

    nd_narrator_brown "Akasyah yang sedari tadi melayang di udara mengangkat satu kakinya tinggi-tinggi dan berpindah tepat di tempat jatuh Seiya, melancarkan serangan."
    
    show flame_front behind akasyah at custom_sprite_pos(x=0.5, y=0.5), silhouette
    show flame_behind at custom_sprite_pos(x=0.5, y=0.5), silhouette
    with wipe_atas(0.2)

        # play sound serangan lilitan
    # nd_narrator_brown "Energi hitam melilit kaki Akasyah yang membuatnya terpaksa terhenti. Disaat kepulan debu mulai memudar, Seiya muncul dalam keadaan terduduk dengan posisi tangan sedang mengikat suatu."
    
    nd_narrator_brown "Energi hitam melilit kaki Akasyah yang membuatnya terpaksa terhenti."

    # nd_narrator_brown "Kondisinya buruk, mungkin karena sempat menghantam lantai kayu yang langsung mengenai tubuhnya."
        
    # show seiya at face_flip, speaking
    # voice voice_3_14_237_seiya
    # nd_seiya_brown "Ha... Hah.. Hah" # kasih jeda
    # show seiya at face_flip, idle
            
    show akasyah at face_flip, speaking
    voice voice_3_14_238_akasyah
    nd_akasyah_brown "Kau pikir bisa nahan gw dengan ngikat kaki gw ?"
    
    voice voice_3_14_239_akasyah
    nd_akasyah_brown "DITYO !!{nw}" # shake
    # show akasyah at idle
    
    show dityo netral at right with easeinright

    scene black

    show pe blue_meteor full_CG:
        yzoom -1
        zoom 1.5
        xalign 0.3
        yalign 0.2
        ease 2.0 zoom 1.0
        ease 8.0 zoom 4.0 yalign 0.5 xalign 0.5
    with wipe_j_bawah(0.2)

    nd_narrator_black "Seiya tak menyadari bahwa Dityo telah tiba dan segera menembakkan serangan proyektil tepat ke arahku.{w=5}{nw}"
    
    show inn lorong malam
    show yuura netral at center
    with wipe_j_atas(0.2)

    show layer master at looping_shake

    # show seiya at speaking
    voice voice_3_14_240_seiya
    nd_seiya_brown "SIALAN ! ANEEEE !!!!{nw}"
    # show seiya at idle
    
    scene black with eye_close
    # show yuura netral at slightright, idle
    # nd_yuura_brown "*Menutup mata"
    
        # show black with Dissolve(1.0)
        # play sound gigit roket
    nd_yuura_black "!!" # improvisasi? Wkwkwkwk hapus aja kalo ga butuh
    
    scene cg_arc_3_scene_14_shark_shoot_01 with Flash
    pause 0.2
    scene cg_arc_3_scene_14_shark_shoot_02 with Flash
    pause 0.2
    scene cg_arc_3_scene_14_shark_shoot_03 with Flash
    pause 0.2
    scene cg_arc_3_scene_14_shark_shoot_04 with Flash

    # nd_yuura_brown "*Membuka mata"

    # show yuura at idle

    # show lorong teras penginapan with Dissolve(1.0)
    nd_narrator_brown "Aku terkejut mendapati Shark yang tiba-tiba berada didepanku, sembari menahan alat Dityo dengan giginya"
    
    # show shark at speaking
    voice voice_3_14_241_shark
    nd_shark_brown "Aw... Aw... sakit juga nahan rudal pake gigi."
    # show shark at idle
    
    # This two suppose to speak the same time
    
    nd_yuura_brown "Shark !"
    # voice voice_3_14_242_seiya
    # nd_seiya_brown "Shark !"

    show inn lorong malam
    show seiya netral at face_flip, left, idle
    show yuura netral at face_flip, center, idle
    with fade

    pause 1.0
    show shark beast at right with moveinright
    pause 1.0
    hide shark beast
    call evolve_sequence from _evolve_sequence_2
    hide shark

    show shark netral at right, speaking
    voice voice_3_14_243_shark
    nd_shark_brown "Ah... Anu... Maaf membuat kalian menunggu."
    show shark at idle
    
    nd_narrator_brown "Kini situasi imbang, dua lawan dua. Meski begitu, melihat dari raut wajah Seiya, aku tahu bahwa perkara ini belum usai."
        
    show seiya at face_flip, speaking
    voice voice_3_14_244_seiya
    nd_seiya_brown "Aneki, pergilah !"
    show seiya at face_flip, idle
        
    show yuura at speaking
    nd_yuura_brown "T-tapi..."
    show yuura at idle
    
    show seiya at face_flip, speaking
    voice voice_3_14_246_seiya
    nd_seiya_brown "Serahkan urusan ini padaku dan Shark! Oke"
    show seiya at face_flip, idle
    
    nd_narrator_brown "Meski enggan, aku berbalik dan lari meninggalkan mereka berdua."

    hide yuura with easeoutleft
        
    # show akasyah at speaking
    voice voice_3_14_247_akasyah
    nd_akasyah_brown "WOI MAU KE MANA LU NENEK !!!"
    # show akasyah at idle
    
    scene black with fade

    nd_narrator_black "Akasyah berusaha menyerangku tapi Seiya langsung menghentikan gerakannya dengan bayangannya."
        
    show seiya at speaking
    voice voice_3_14_248_seiya
    nd_seiya_black "Lawanmu adalah aku."
    show seiya at idle

    jump scene_15

    return

