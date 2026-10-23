# label start:

label scene_3_demo:
    # # scene hutan # sementara
    # scene hutan with Dissolve(2.0)
    # $ quick_menu = True
    
    # BG hutan taman

    play sound sfx_ambience_grasak_grusuk_daun_scene3
    scene transition_screen orange concentrationline02_w with dissolve
    show yuura scared at center, speaking with easeinright
    nd_narrator_brown "Aku berlari, terus berlari. Tanpa sekalipun melihat ke belakangku, aku berlari tanpa henti berharap mereka semua tidak mengejar diriku lagi."
        # show yuura normal animated at center
        # with Dissolve(2.0)
    
    show yuura at speaking
    nd_yuura_brown "*huft huft..."
    hide yuura with easeoutleft
    stop sound
    # play music "audio/bgm/hutan.ogg" fadein 1.0
    
    play music bgm_scene3_forest_w_ambience fadeout 1.0 volume 0.7 loop
    scene hutan taman with dissolve
    show yuura scared at center, speaking with easeinright
    
    nd_yuura_brown "Arghhh.. Ini gila! bisa-bisanya aku terbangun di tempat kayak gini? huah.."
    
    show yuura at idle
    nd_narrator_brown "Nafasku tersengal-sengal karena berlarian terus sepanjang waktu."
    
    nd_narrator_brown "Aku melanjutkan perjalanan ku dengan rasa lelah yang luar biasa, sebelum akhirnya aku memutuskan untuk duduk di dekat sebuah pohon besar."
    
    nd_narrator_brown "Aku berusaha menenangkan diriku, menarik nafas secara perlahan dan mulai memikirkan segalanya."
    
    play sound sfx_expression_angry
    show yuura angry eff_angry at speaking
    nd_yuura_brown "(Bagaimana aku bisa tiba-tiba berada di tempat ini. Apa yang telah terjadi? Mengapa ini semua terjadi? Dan kenapa aku bisa ada disini?)"

    play music bgm_scene3_forest_w_ambience fadeout 1.0 volume 0.7 loop

        # hide yuura normal animated
        # with fade
        # show yuura normal animated at left # harusnya cuma geser, tapi ga ngerti maenin x y nya
        # with Dissolve(1.0)
        # show Unknown at right # karakter terlalu kanan dan terlalu kiri
        # with Dissolve(1.0)
    show yuura at right, idle with ease
    show pria netral at left, silhouette, speaking with moveinleft
    pause 0.2
    voice voice_1_3_19_pria_misterius
    nd_unknown_brown "Capek kan? Lari-lari"
    
    show pria at silhouette, idle
    show yuura netral eff_exclamation at shake
    play sound sfx_expression_surprised
    nd_narrator_brown "Aku terkejut mendengar suara yang entah dari mana asalnya. Aku melihat sekitar dan merasakan adanya seseorang di balik pohon yang ku sandari."
    
    show pria at reveal_character, speaking with dissolve
    show yuura none at idle
    voice voice_1_3_20_pria_misterius
    wd_pria_brown "Gausah takut, aku gak gigit"
    
    show pria at idle
    nd_narrator_brown "Aku merasa terkejut, bingung, sekaligus bertanya-tanya dari mana orang ini berasal. Aku tidak tahu apapun tentangnya, yang aku tahu suara ini adalah suara laki-laki."

    show pria at speaking
    voice voice_1_3_21_pria_misterius
    wd_pria_brown "Kamu.. bukan dari dunia ini kan?"

    play sound sfx_expression_angry
    show yuura angry eff_angry at speaking
    show pria at idle
    nd_yuura_brown "S-siapa kamu??? CEPAT JAWAB DARIMANA KAMU TAHU TENTANGKU!"
    
    show yuura at idle
    show pria at speaking
    voice voice_1_3_23_pria_misterius
    wd_pria_brown "Intuisiku saja"
    
    show yuura sad eff_sweat_w at speaking
    show pria at idle
    nd_yuura_brown "Aku sudah tidak mengerti lagi dengan tempat ini, tadi orang-orang mengejarku." 
    
    nd_yuura_brown "Sekarang ada orang aneh yang berbicara denganku dari balik pohon! Lalu apa? aku akan melihat orang-orang masuk penjara?"
    
    show yuura at idle
    show pria at speaking
    wd_pria_brown "..."

    show yuura at speaking
    show pria at idle
    nd_yuura_brown "Aku capek.. aku mau pulang.. tidak seharusnya aku disini.."
    
    show yuura at idle
    show pria at speaking
    voice voice_1_3_27_pria_misterius
    wd_pria_brown "Hey.. jangan menangis, aku gak sanggup melihat cewek nangis di hadapanku"
    
    # CG hugging start here

    # show pria at idle
    # scene black
    scene cg_arc_1_scene_03_shoot_1:
        xpos 0.0
        linear 10.0 xalign 1.0
    with dissolve
    pause 4.0
    scene cg_arc_1_scene_03_shoot_2:
        xpos -1.0
        linear 10.0 xalign 0.0
    with dissolve
    pause 6.0
    scene cg_arc_1_scene_03_shoot_3:
        xalign 0.5
        ypos -0.5
        linear 5.0 ypos -0.4
    with dissolve
    pause 4.0
    scene cg_arc_1_scene_03_shoot_4:
        zoom 1.05
        xalign 0.5
        yalign 0.5
        linear 2.0 zoom 1.0
    with Flash

    pause 1.5

    nd_narrator_brown "Aku mengangkat kepalaku dan melihat seseorang berdiri di hadapanku, dengan jubah panjang dan topi fedora yang menutupi wajahnya."
    
    scene cg_arc_1_scene_03_shoot_5:
        zoom 1.03
        xalign 0.5
        yalign 0.5
        linear 2.0 zoom 1.0
    with Flash

    nd_narrator_brown "Melihat sosoknya yang tinggi itu, membuatku tanpa sadar memeluknya dan langsung menangis."
    
    scene cg_arc_1_scene_03_shoot_5:
        # zoom 1.03
        xalign 0.5
        yalign 0.5
        linear 5.0 zoom 1.8

    nd_narrator_brown "Aku menceritakan semuanya tanpa ku sadari, orang itu hanya diam membiarkan ku mengeluarkan semuanya."
    
    # DEMO END HERE

    stop music fadeout 2.0
    # pause 2.0

    scene black with dissolve
    play music bgm_scene8_awkward_yoyu_ver volume 0.9 loop

    show josua netral at center, cahaya_ilahi, speaking with easeinright
    pause 0.5

    nd_unknown_black "Penasaran yah kelanjutannya Yuur"

    nd_unknown_black "Penonton juga penasaran nggak?"

    nd_unknown_black "Kepoin aja twitter/X kita di @YuuraidFanClub untuk kelanjutannya"

    nd_unknown_black "..."

    nd_unknown_black "Kenape Yuur mencet-mencet terus?"

    nd_unknown_black "Butuh full versionnya sekarang kah?"

    nd_unknown_black "Asik kali rilis sistem +1 bulan"

    nd_unknown_black "ehek~"

    nd_unknown_black "Di tunggu yah"

    nd_unknown_black "Aku juga nggak sabar buat kalian mainin game ini nanti"

    nd_unknown_black "Tapi asik kali di gebuin aja kan Yuur~"

    nd_unknown_black ".{w=0.5}.{w=0.5}.{w=0.5}{nw}"

    show layer master at shake
    nd_unknown_black "{size=+20}ALAMAK{/size}{w=0.3}{nw}"

    nd_unknown_black "Ijin kabur dulu yah Yuur sama penonton~"

    hide josua with easeoutleft

    pause 1.0

    show ibe netral at ease_custom(offscreenright, offscreenleft, 0.5)

    nd_unknown_black "{size=+20}WOII JANGAN KABUR, \nKELARIN SANA GAMENYA!!{/size}"

    nd_narrator_black "With Love\n\nAdmint Yuuraid <3"

