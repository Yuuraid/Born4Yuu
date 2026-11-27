# label start:

label scene_18:
    scene black with dissolve
    # $ renpy.music.set_volume(0.01, channel="rocket_audio")
    pause 0.2
    scene inn gudang outside with eye_open
    play music bgm_scene16_trigger volume 1.0 loop
    nd_narrator_brown "Aku terbangun dan mendengar suara samar, ketika aku mencoba untuk duduk, aku melihat Dawam dan Aergia yang masing-masing di antara mereka telah menyiapkan kuda-kuda, sudah jelas itu merupakan serangan pengakhiran untuk mengakhiri pertempuran panjang mereka."
    show aergia hurt at right, shake, speaking with easeinright
    voice voice_3_18_584_aergia
    nd_aergia_brown "Uhuk uhuk... Mati aja lu!!"
    show aergia at idle
    show dawam hurt at left, speaking with easeinleft
    voice voice_3_18_585_dawam
    wd_dawam_brown "Sesuai permintaanmu!"
    show dawam at idle
    nd_narrator_brown "Tepat disaat itu, sebuah perasaan aneh mengalir kuat didalam tubuhku. Entah mengapa tubuhku yang sebelumnya dihajar habis-habisan dapat dengan mudahnya berdiri seperti tak terjadi apa-apa sebelumnya"

    show dawam behind aergia at custom_sprite_pos(x=0.3)
    show aergia at custom_sprite_pos(x=0.7)
    with ease
    
    pause 0.2

    play sound sfx_shadow_dash_2
    scene pe dash negative_blue:
        zoom 0.95
        rotate 0
        xzoom -1
        xalign 0.5
        yalign 0.5
        linear 0.5 zoom 1.5 rotate 10
    with Flash

    nd_narrator_brown "Aku berlari ke tengah-tengah pertarungan, untuk menghentikan hal yang tak ada gunanya ini."
    # play sound melangkah
    # show dawam at speaking
    # show dawam at shake
    # show aergia at speaking
    # show aergia at shake
    # voice voice_3_18_586_aergia
    # voice voice_3_18_587_dawam
    # nd_narrator_brown "ARRGGGHH!!!" #aergia and dawam scream
    # # play sound lesatan cepat
    # show aergia at idle
    # show dawam at idle
    # nd_narrator_brown "..."
    # # play sound dentingan jam dinding
    # show aergia at shake
    # show dawam at shake
    # nd_narrator_brown "Aergia dan Dawam terkejut."
    # stop music
    # play music jade bottle
    
    scene inn gudang outside
    show yuura angry at center, idle
    show dawam hurt behind yuura at custom_sprite_pos(x=0.3), idle
    show aergia hurt behind yuura at custom_sprite_pos(x=0.7), idle
    with wipe_j_bawah(0.1)

    pause 0.1
    play sound sfx_punch_impact_01
    show aergia at right, idle
    show dawam at left, idle
    with ease
    stop music
    play music bgm_scene1_jade_bottle volume 1.0 loop

    nd_narrator_brown "Aku menangkap tangan mereka masing-masing dengan tanganku, dalam sekejap menghentikan semua serangan pamungkas mereka tanpa sisa."
    show yuura angry at center, idle
    show dawam at speaking
    voice voice_3_18_588_dawam
    wd_dawam_brown "No-nona Yuura?"
    show dawam at idle
    show yuura at speaking
    show yuura at shake
    wd_yuura_brown "{size=+20}CUKUP!{/size}"
    show yuura at idle
    show aergia at speaking
    voice voice_3_18_590_aergia
    nd_aergia_brown "Minggir, Yuur!"
    show aergia at idle
    show yuura at face_flip, speaking
    wd_yuura_brown "{size=+20}Aku bilang CUKUP!{/size}"
    
    wd_yuura_brown "Kalian mau ngelanjutin ini sampai kapan sih? Sampai penginapan ini hancur?"
    show yuura at face_flip, idle
    show aergia at speaking 
    voice voice_3_18_593_aergia
    nd_aergia_brown "Emang lu tau apa sih? Lu itu kan bukan Yuura." 
    show aergia at idle
    show yuura at shake, face_flip, speaking
    # show yuura at shake
    wd_yuura_brown "{size=+20}YA TERUS KENAPA?{/size}"
    
    wd_yuura_brown "APA AKU BUKAN YUURA? KARENA AKU DARI DUNIA YANG BERBEDA?"
    show yuura at face_flip, idle
    show aergia at speaking
    voice voice_3_18_596_aergia
    nd_aergia_brown "T-tapi Yuur..."

    play music bgm_scene4 loop

    show aergia at idle
    show yuura netral at face_flip, speaking
    wd_yuura_brown "Aer..."

    wd_yuura_brown "Maaf yah, kalo aku selalu lupa akan dirimu."
    show yuura at face_flip, idle
    show aergia angry at speaking
    voice voice_3_18_599_aergia
    wd_aergia_brown "A-apaan sih, hmph~"
    
    voice voice_3_18_600_aergia
    wd_aergia_brown "Lagian siapa gua bisa sampe diinget orang-orang."
    show aergia at idle
    show yuura at face_flip, speaking
    wd_yuura_brown "Kata siapa?"
    show yuura happy
    wd_yuura_brown "Aer, kita adalah keluarga. Jangan selalu merasa bahwa dirimu sendirian di dunia ini."
    
    wd_yuura_brown "Tak peduli seperti apapun dirimu, kamu sudah berusaha yang terbaik."
    show yuura at face_flip, idle
    show aergia sad at speaking
    voice voice_3_18_604_aergia
    wd_aergia_brown "Yuura..."
    show aergia furious
    voice voice_3_18_605_aergia
    wd_aergia_brown "Alah nyocot doang, lu kira bakalan mem-"
    show aergia sad
    voice voice_3_18_606_aergia
    wd_aergia_brown "Eh iya makasih ya...ehek ehek"
    show aergia at idle
    nd_narrator_brown "Aergia menangis dan mulai menyadari bahwa dirinya tidak sendirian lagi."
    show yuura at speaking
    wd_yuura_brown "Dawam... Maaf ya aku bikin kamu terluka."
    show yuura at idle
    show dawam at speaking
    voice voice_3_18_608_dawam
    wd_dawam_brown "Tidak masalah Nona, ini semua adalah tugas yang diperintahkan oleh tuan muda."
    show dawam at idle
    show yuura at speaking
    wd_yuura_brown "Ga... Itu adalah keinginanmu sendiri."
    
    wd_yuura_brown "Gausahlah nurutin si Risol-Risol itu, jadilah dirimu sendiri. Karena kamu adalah Yuuraid."
    show yuura at idle
    show dawam sad at speaking
    voice voice_3_18_611_dawam
    wd_dawam_brown "Nona..."
    show dawam at idle
    
    stop music fadeout 1.0
    
    show dawam behind yuura at custom_sprite_pos(x=0.3), idle
    show aergia behind yuura at custom_sprite_pos(x=0.7), idle
    with ease
    
    pause 0.5

    scene black with fade

    nd_narrator_black "Aku mengelus kepala mereka dengan lembut, sebelum meninggalkan mereka berdua. Aku berlari menuju tempat pertarungan lainnya."

    stop music
    play music bgm_scene16_trigger volume 1.0 loop

    scene arena
    show axia netral at right, idle
    show rian angry at left, idle
    with Dissolve(1.0)

    pause 1.0

    # show yuura at speaking
    # show yuura at shake
    wd_yuura_brown "{size=+20}EDY!!{/size}"
    # show yuura at idle

    show axia at face_flip

    nd_narrator_brown "Axiaregis yang sedang fokus bertarung terkejut karena mendengar nama panggilannya."
    play sound sfx_fathanil_roar_only
    voice voice_3_18_613_axiaregis
    wd_axiaregis_brown "A-anee???{nw}"

    stop music

    play sound sfx_shadow_dash_2
    show kuda_nill behind rian at ease_custom(offscreenleft, offscreenright, 0.7):
        yalign -2.0
        xzoom -1
    pause 0.2
    show axia at ease_custom(right, offscreenright, 0.5)
    show layer master at shake
    
    pause 0.3

    scene inn ruang_tamu_2
    # show axia netral at right, idle
    show rian angry at left, idle
    with Flash

    # nd_narrator_brown "Axiaregis sekali lagi ditabrak oleh kuda nil, membuatnya terjatuh tepat di hadapan diriku."
    # show axia hurt at jump_in_right(duration=1.0), idle
    # pause 2.0
    # show rian angry at left, speaking

    # pause 1.0

    show rian at speaking
    voice voice_3_18_614_rian
    wd_rian_brown "Edy, maaf... Aku ga sengaja."
    

    play music bgm_scene8_awkward
    show yuura scared at right with easeinright

    show rian happy
    voice voice_3_18_615_rian
    wd_rian_brown "Loh? Anee?"
    show rian at idle
    show yuura happy at speaking, zorder 5
    wd_yuura_brown "Rian, kerja bagus!"
    show yuura at center, idle with ease
    nd_narrator_brown "Aku mengelus kepala Rian, membuatnya senang seperti anak kecil."

    show axia netral at face_flip, right, idle with easeinright

    pause 0.5

    show yuura at face_flip, speaking
    wd_yuura_brown "Maaf ya, Edy... Aku berbuat jahat padamu."
    
    wd_yuura_brown "Tapi lain kali tolong jangan kayak gitu lagi."

    show rian behind yuura at custom_sprite_pos(x=0.25), idle
    show axia behind yuura at custom_sprite_pos(x=0.7), idle
    with ease

    show yuura at idle
    nd_narrator_brown "Aku memeluk Axiaregis dan menenangkan dirinya. Membuat dia perlahan mulai menyadari kesalahannya."

    show axia at face_flip, speaking
    voice voice_3_18_619_axiaregis
    wd_axiaregis_brown "Aneeeee... Maafiiin akuuuu."
    show axia at face_flip, idle
    show yuura at speaking
    wd_yuura_brown "Iya, aku maafin kok."
    show yuura at idle
    show axia at face_flip, speaking
    voice voice_3_18_621_axiaregis
    wd_axiaregis_brown "Huaaaaaa aku cinta kamu Aneee."
    show axia at face_flip, idle
    nd_narrator_brown "Aku mengelus Axiaregis dan membuatnya menangis sangat kencang dalam pelukanku."
    
    show rian at left
    show axia at right
    with ease

    nd_narrator_brown "Setelah puas mengeluarkan semua emosinya, Axiaregis dan Rian menawarkan dirinya untuk membantu dalam menyelesaikan masalah lainnya."
    show yuura at speaking
    wd_yuura_brown "Tidak, biar aku saja yang menyelesaikannya."
    
    wd_yuura_brown "Dimana Akasyah dan lainnya?"
    show yuura at idle
    show axia at speaking
    voice voice_3_18_624_axiaregis
    wd_axiaregis_brown "Di sana Anee."
    
    voice voice_3_18_625_axiaregis
    wd_axiaregis_brown "Tapi kamu yakin, Anee? Mereka berdua berbahaya."
    show axia at idle
    show rian at speaking
    voice voice_3_18_626_rian
    wd_rian_brown "Betul kata Edy, Anee. Sebaiknya kami membantu."
    show rian at idle
    show yuura at speaking
    wd_yuura_brown "Tidak apa, biar aku saja."
    
    wd_yuura_brown "Tapi...{w=1.0} kalian bisa bantu aku sesuatu nggak?"

    scene black with dissolve
    pause 0.5
    scene garden_fight_1 
    show akasyah angry at right, face_flip, speaking
    with dissolve

    stop music 
    play music bgm_scene15_pursuit volume 1.0 loop

    voice voice_3_18_629_akasyah
    nd_akasyah_brown "SEIYAAAAA!!"

    hide akasyah with easeoutleft

    # show akasyah at idle
    scene garden_fight_4 
    show seiya angry at face_flip, speaking

    # show seiya at shake
    voice voice_3_18_630_seiya
    wd_seiya_brown "AKASYAHHH!!"
    hide seiya with easeoutright

    play sound sfx_punch_12
    show cg_arc_3_scene_18_yuura_nahan_shoot_1 with Flash
    pause 0.1
    play sound sfx_punch_12
    show cg_arc_3_scene_18_yuura_nahan_shoot_2 with Flash
    pause 0.1
    play sound sfx_action_sweeping_blow_scene16
    $ unlock_cg("cg_arc_3_scene_18_yuura_nahan_shoot_3")
    show cg_arc_3_scene_18_yuura_nahan_shoot_3 with slash

    # play sound cartoonish punch
    # show seiya at idle
    nd_narrator_brown "Sebelum mereka berhasil menyerang satu sama lain, aku langsung berdiri di antara keduanya. Mematikan serangan pamungkas mereka."


    hide yuura
    hide akasyah
    hide seiya

    $ renpy.music.set_volume(0.5, channel="music")

    scene garden_fight_2
    show seiya netral at left, face_flip, idle
    show akasyah angry at right, face_flip, idle
    show yuura angry at center, idle
    with fade

    show akasyah at face_flip, speaking
    voice voice_3_18_631_akasyah
    nd_akasyah_brown "LU NGAPAIN SIH, YUUR!"
    
    voice voice_3_18_632_akasyah
    nd_akasyah_brown "GANGGU BANGET, LAGI SERU JUGA."
    
    voice voice_3_18_633_akasyah
    nd_akasyah_brown "MINGGIR GA? ATAU LU...{nw}"
    # show akasyah at idle
    # stop music
    # play music awkward yoyu
    
    stop music
    $ renpy.music.set_volume(1.0, channel="music")
    play music bgm_scene8_awkward_yoyu_ver volume 1.0 loop

    $ unlock_cg("cg_arc_3_scene_18_lempar_yoyu_shoot_4")
    show cg_arc_3_scene_18_lempar_yoyu_shoot_1:
        ypos -1.0
        ease 0.2 ypos 0.0
    # with Flash

    pause 0.2

    show cg_arc_3_scene_18_lempar_yoyu_shoot_3:
        xpos -1.0
        ease 0.2 xpos 0.0

    pause 0.2

    show cg_arc_3_scene_18_lempar_yoyu_shoot_2:
        xpos 1.0
        ease 0.2 xpos 0.0
        


    nd_narrator_brown "Aku melempar sebuah minuman berlabel Yoyu kepada Akasyah."

    show cg_arc_3_scene_18_lempar_yoyu_shoot_1:
        zoom 1.0
        xalign 0.5
        yalign 0.5
        ease 0.5 zoom 1.2
        speaking
    # with ease

    # show yuura happy at center, speaking
    wd_yuura_brown "Nih, kuganti yang sebelumnya."
    
    wd_yuura_brown "Maaf yah, aku malah bikin kamu marah."
    
    hide cg_arc_3_scene_18_lempar_yoyu_shoot_1
    hide cg_arc_3_scene_18_lempar_yoyu_shoot_2
    hide cg_arc_3_scene_18_lempar_yoyu_shoot_3
    show seiya netral at left, face_flip, idle
    show akasyah netral at right, face_flip, idle
    show yuura happy at center, face_flip, speaking
    with dissolve

    wd_yuura_brown "Sini-sini, aku peluk."
    show yuura at face_flip, idle
    show akasyah angry at speaking
    voice voice_3_18_637_akasyah
    wd_akasyah_brown "Apaan sih, Yuur. Lu kira gua anak kecil?"
    
    show akasyah netral at idle
    nd_narrator_brown "Akasyah meminum Yoyu yang diberikan dan mulai sedikit tenang."
    show akasyah at face_flip, idle
    show seiya netral at face_flip, speaking
    voice voice_3_18_638_seiya
    wd_seiya_brown "Apa yang terjadi padamu, Anee?"
    
    voice voice_3_18_639_seiya
    wd_seiya_brown "Bukankah, kamu seperti orang yang berbeda sekarang?"
    show seiya at face_flip, idle
    show yuura at speaking
    wd_yuura_brown "Memang ya, Seiya ini."
    
    wd_yuura_brown "Mau yang tadi atau sekarang, aku tetaplah Yuura, bukan?"
    show yuura at idle
    show seiya at face_flip, speaking
    voice voice_3_18_642_seiya
    wd_seiya_brown "Hahaha...ya... Kamu benar.{w=1}{nw}"
    # stop music
    # play music pursuit ver 2
    # play sound angin berhembus sepoi sepoi
    show seiya at face_flip, idle

    $ renpy.music.set_pause(True, channel="music")
    
    show rocket_greenscreen zorder 6:
        xzoom -1
        zoom 1.3
        xalign 0.5
        yalign 0.5

    nd_narrator_brown "Disaat kita lagi mengobrol tiba tiba..{w=2}{nw}"

    # $ renpy.pause(1.5, hard=True)

    show akasyah angry at face_flip, center zorder 5 with ease 
    voice voice_3_18_643_akasyah
    wd_akasyah_brown "Yuur!!!{w=1}{nw}"
    
    # hide seiya 
    # hide akasyah 
    # hide yuura 
    scene black 
    with dissolve

    # sink sprite?
    nd_narrator_black "Akasyah melompat untuk menyelamatkan diriku, dia menjadikan dirinya sebagai tameng hidup demi diriku. Beruntung Seiya berhasil memindahkan roket itu sebelum hal buruk terjadi."

    $ renpy.music.set_pause(False, channel="music")

    scene garden_fight_1
    show dityo angry eff_sweat_w at right, speaking
    with fade

    voice voice_3_18_644_dityo
    nd_dityo_brown "Aduh sorry, ga sengaja kelempar ke sini."
    
    voice voice_3_18_645_dityo
    nd_dityo_brown "Kalian gapapa kan?"

    scene garden_fight_2
    show seiya hurt at left, face_flip, idle
    show yuura happy at custom_sprite_pos(x=0.2), face_flip, speaking
    show akasyah hurt at center, face_flip, idle
    with dissolve

    # show dityo netral at idle
    # show yuura happy at center, speaking, zorder 5
    wd_yuura_brown "Dityo!"
    hide yuura with easeoutright

    scene garden_fight_1
    show dityo angry at right, idle
    with fade

    show yuura happy at center, face_flip, idle with easeinleft

    nd_narrator_brown "Aku menghampiri Dityo dan memberikannya sebuah lukisan yang aku rusak siang tadi."
    show yuura at face_flip, speaking
    wd_yuura_brown "Ini, aku berhasil memperbaikinya."
    show yuura at face_flip

    show dark_overlay
    play sound sfx_paper
    show mahakarya_fixed at pos(r=2):
        xalign -0.3
        yalign 5.0
        ease 0.5 yalign 0.65

    pause

    show yuura at speaking
    wd_yuura_brown "Maaf, aku mendorong dirimu tanpa sengaja dan bertindak kasar padamu."

    wd_yuura_brown "Aku dibantu Edy dan Rian memperbaiki ini"
    show yuura at face_flip

    show dityo at speaking
    voice voice_3_18_649_dityo
    wd_dityo_brown "Anee..."
    show yuura at idle
    show dityo at idle

    play sound sfx_action_whoosh_scene13_16
    show mahakarya_fixed at pos(r=2):
        xalign -0.3
        yalign 0.65
        ease 0.2 yalign 7.0 xalign 5.0
    hide dark_overlay with dissolve

    play sound sfx_glass_throw
    pause 0.7
    play sound sfx_tom_scream_ow

    pause 1.0

    show yuura at speaking
    # show dityo at idle
    wd_yuura_brown "Maaf yah Dityo"

    show dityo at idle
    show yuura at idle
    show shark hurt_frame at custom_sprite_pos(x=1.4), speaking with easeinright
    voice voice_3_18_650_shark
    wd_shark_brown "Kalian gapapa kan?"
    show shark at speaking
    voice voice_3_18_651_shark
    wd_shark_brown "L-loh Anee?"
    show shark at idle
    show yuura at speaking
    wd_yuura_brown "Shark, kok kamu..."
    show yuura at idle
    show shark at speaking
    voice voice_3_18_653_shark
    wd_shark_brown "A-aman aja Anee, luka begini doang mah kecil."
    show shark at idle
    show yuura at custom_sprite_pos(x=1.0) with ease
    nd_narrator_brown "Aku menarik tangannya dan melihat luka yang ada disana. Aku mengoleskan sebuah salep di luka tersebut, untuk membuatnya menjadi lebih baik."
    # stop music
    # play music awkward
    show shark at speaking
    voice voice_3_18_654_shark
    wd_shark_brown "Huh.. A-ane???"
    show shark at idle
    show yuura at center, speaking with ease
    wd_yuura_brown "Lebih baik?"
    show yuura at idle
    show shark at speaking
    voice voice_3_18_656_shark
    wd_shark_brown "I-iya..."
    show shark at idle
    show yuura at speaking
    wd_yuura_brown "Makasih ya, udah ngelindungin aku."
    
    wd_yuura_brown "Kamu imut deh."
    show yuura at idle
    show shark eff_heart at speaking
    voice voice_3_18_659_shark
    wd_shark_brown "D-dihh...  Diem deh..."
    show shark none at idle
    # stop music
    # play music scene 4
    
    nd_narrator_brown "Aku tertawa kecil karena merasa sangat senang menjahili dirinya."
    
    scene garden_fight_3 with fade

    show aergia netral at custom_sprite_pos(x=0.7), idle with easeinright
    show dawam netral behind aergia at custom_sprite_pos(x=1.1), idle with easeinright
    show rian netral at custom_sprite_pos(x=0.3), idle with easeinleft
    show axia netral behind rian at custom_sprite_pos(x=-0.2), idle with easeinleft

    nd_narrator_brown "Mendengar bunyi roket tadi, semua orang di penginapan datang menghampiriku."
    # hide dityo
    show aergia netral at speaking
    voice voice_3_18_660_aergia
    wd_aergia_brown "Yuur, lu gapapa?"
    show aergia at idle
    hide shark
    show axia netral at speaking
    voice voice_3_18_661_axiaregis
    wd_axiaregis_brown "Anee gapapah?"
    show axia at idle
    # hide aergia
    show dawam netral at speaking
    voice voice_3_18_662_dawam
    wd_dawam_brown "Nona gapapa?"
    show dawam at idle
    # hide axia
    show rian netral at speaking
    voice voice_3_18_663_rian
    wd_rian_brown "Aneeki aman?"
    # hide rian
    # hide dawam

    play music bgm_scene4 fadein 1.0
    scene garden_fight_1
    show dityo angry at right, idle
    show shark hurt_frame at custom_sprite_pos(x=1.4), idle
    show yuura scared at center, speaking
    # with fade

    wd_yuura_brown "Maaf..."
    show yuura sad at idle
    nd_narrator_brown "Air mataku mulai turun seraya tubuhku mulai terduduk lemas."
    # show yuura at speaking

    scene cg_arc_3_scene_17_shoot_01 with fade
    pause 0.2
    scene cg_arc_3_scene_17_shoot_02 with dissolve
    pause 0.2
    scene cg_arc_3_scene_17_shoot_01 with dissolve
    wd_yuura_brown "Maaf..."
    
    scene cg_arc_3_scene_17_shoot_02 with dissolve
    pause 0.2
    scene cg_arc_3_scene_17_shoot_01 with dissolve
    wd_yuura_brown "Maaf kalau aku bukan Yuura yang kalian kenal."    
    
    scene cg_arc_3_scene_17_shoot_02 with dissolve
    pause 0.2
    scene cg_arc_3_scene_17_shoot_01 with dissolve
    wd_yuura_brown "Maaf kalau aku berubah."
    
    scene cg_arc_3_scene_17_shoot_02 with dissolve
    pause 0.2
    scene cg_arc_3_scene_17_shoot_01 with dissolve
    wd_yuura_brown "Maaf kalau aku selalu mengecewakan kalian."
    
    scene cg_arc_3_scene_17_shoot_02 with dissolve
    wd_yuura_brown "Maaf."
    
    scene cg_arc_3_scene_17_shoot_03 with dissolve
    wd_yuura_brown "Maaf..."
    # hide yuura

    scene garden_fight_3
    show aergia angry at custom_sprite_pos(x=0.7), speaking
    show dawam netral behind aergia at custom_sprite_pos(x=1.1), idle
    show rian netral at custom_sprite_pos(x=0.3), idle
    show axia netral behind rian at custom_sprite_pos(x=-0.2), idle

    # show aergia angry at speaking
    voice voice_3_18_671_aergia
    wd_aergia_brown "Apaan dah? lu tuh ga salah, harusnya gua yang minta maaf. Gua kok yang salah, gua"
    
    voice voice_3_18_672_aergia
    wd_aergia_brown "Coba aja kalau gua ga goblok. Maaf ya, Yuur."
    show aergia at idle
    show axia sassy at speaking
    voice voice_3_18_673_axiaregis
    wd_axiaregis_brown "Apaan, ini semua salahku, Anee."
    
    voice voice_3_18_674_axiaregis
    wd_axiaregis_brown "Karena aku semuanya jadi gini."
    show axia at idle
    # hide aergia

    scene garden_fight_1
    show dityo sad at right, speaking
    show shark hurt_frame at custom_sprite_pos(x=1.4), idle
    show yuura sad at center, idle

    # show dityo sad at left, speaking
    voice voice_3_18_675_dityo
    wd_dityo_brown "Ga, ini semua salahku..."
    
    voice voice_3_18_676_dityo
    wd_dityo_brown "Seandainya aku lebih sabar mungkin ga bakal kayak gini."
    show dityo at idle

    show akasyah smug at left, idle with easeinleft
    pause 0.2
    play music bgm_scene8_awkward
    show akasyah at speaking
    voice voice_3_18_677_akasyah
    wd_akasyah_brown "Au, lu pada ngapain coba kayak gitu?"
    show akasyah at idle
    show dityo at speaking
    show dityo at shake
    show shark at speaking
    show shark at shake
    show yuura angry at speaking
    show yuura at shake
    # voice voice_3_18_678_dityo
    # show axia at speaking
    # show axia at shake
    # voice voice_3_18_679_axiaregis
    voice voice_3_18_678_dityo
    # voice voice_3_18_678_9_Dityo_Axia
    
    wd_narrator_brown "{size=+20}Kamu juga.{/size}" # dityo dan aergia
    show dityo at idle
    show shark at idle
    # show axia at idle
    # show aergia netral at left, speaking
    # voice voice_3_18_680_aergia
    # nd_aergia_brown "Lu juga."
    # show aergia at idle
    show yuura happy at idle
    nd_narrator_brown "Mereka mulai bertengkar lagi di hadapanku, membuatku yang menangis menjadi tertawa."
    # hide akasyah
    camera:
        zoom 2.0
        xalign 0.5
        yalign 0.45
    show yuura happy at center, speaking
    wd_yuura_brown "Emang yah, Yuuraid itu aneh banget hahaha."

    show yuura at idle
    # hide aergia
    camera:
        zoom 2.0
        xalign 0.2
        yalign 0.45
    show akasyah smug at left, speaking
    voice voice_3_18_682_akasyah
    wd_akasyah_brown "Nah gitu dong, Yuur! Ketawa hehe."
    # show akasyah at idle
    scene white with dissolve
    nd_narrator_brown "Mereka semua memelukku, mengingatkan kembali kehangatan yang selama ini aku inginkan."
    
    nd_narrator_brown "Memang benar, bahwa diriku bukanlah Yuura yang sebelumnya. Tapi aku tetaplah Yuura, dan mereka tetaplah Yuuraid."
    
    nd_narrator_brown "Yang perlu kami lakukan adalah memulai kembali semuanya dibalik kekacauan yang aneh ini."
    
    nd_narrator_brown "Kesalahpahaman sering terjadi, kecerobohan adalah hal yang biasa. Tapi yang pasti kami adalah keluarga, dan tak ada yang bisa melupakan fakta itu."
    jump scene_19

    return