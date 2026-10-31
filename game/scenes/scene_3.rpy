# label start:

label scene_3:
    play music bgm_scene3_forest_w_ambience volume 1.0 loop
    play sound sfx_ambience_grasak_grusuk_daun_scene3
    scene transition_screen orange concentrationline02_w with dissolve
    show yuura scared at center, speaking with easeinright
    nd_narrator_brown "Aku berlari, terus berlari. Tanpa sekalipun melihat ke belakangku, aku berlari tanpa henti berharap mereka semua tidak mengejar diriku lagi."
    
    show yuura at speaking
    nd_yuura_brown "*huft huft..."
    hide yuura with easeoutleft
    stop sound
    
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
    nd_yuura_brown "(Bagaimana aku bisa tiba-tiba berada di tempat ini. Apa yang telah terjadi? Mengapa ini semua terjadi? Dan kenapa aku bisa ada di sini?)"

    stop music fadeout 1.0
    play music bgm_scene3_pria_asing volume 1.0 fadein 2.0 fadeout 2.0 loop
    
    pause 0.2
    voice voice_1_3_19_pria_misterius
    nd_unknown_brown "Capek kan? Lari-lari"
    
    show yuura netral eff_exclamation at shake
    play sound sfx_expression_surprised
    nd_narrator_brown "Aku terkejut mendengar suara yang entah dari mana asalnya. Aku melihat sekitar dan merasakan adanya seseorang di balik pohon yang ku sandari."
    
    show yuura none at idle
    voice voice_1_3_20_pria_misterius
    nd_unknown_brown "Gausah takut, aku gak gigit"
    
    nd_narrator_brown "Aku merasa terkejut, bingung, sekaligus bertanya-tanya dari mana orang ini berasal. Aku tidak tahu apapun tentangnya, yang aku tahu suara ini adalah suara laki-laki."

    voice voice_1_3_21_pria_misterius
    nd_unknown_brown "Kamu.. bukan dari dunia ini kan?"

    play sound sfx_expression_angry
    show yuura angry eff_angry at face_flip, speaking
    nd_yuura_brown "S-siapa kamu??? CEPAT JAWAB DARIMANA KAMU TAHU TENTANGKU!"
    
    show yuura at face_flip, idle 
    voice voice_1_3_23_pria_misterius
    nd_unknown_brown "Intuisiku saja"
    
    show yuura sad eff_sweat_w at speaking
    show pria at idle
    nd_yuura_brown "Aku sudah tidak mengerti lagi dengan tempat ini, tadi orang-orang mengejarku." 
    
    nd_yuura_brown "Sekarang ada orang aneh yang berbicara denganku dari balik pohon! Lalu apa? aku akan melihat orang-orang masuk penjara?"


    show yuura at idle
    nd_unknown_brown "..."

    stop music
    play music bgm_scene3_pelukan volume 1.0 loop

    show yuura at speaking
    # show pria at idle
    nd_yuura_brown "Aku capek.. aku mau pulang.. tidak seharusnya aku disini.."
    
    show yuura at idle
    # show pria at speaking
    voice voice_1_3_27_pria_misterius
    nd_unknown_brown "Hey.. jangan menangis, aku gak sanggup melihat cewek nangis di hadapanku"

    stop music fadeout 1.0
    play music bgm_scene3_pelukan volume 1.0 fadein 2.0 fadeout 2.0 loop
    
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

    stop music
    play music bgm_scene1_jade_bottle volume 1.0 loop
    
    # DEMO END HERE

    # CG end here
    scene hutan taman 
    show yuura sad at right, idle
    show pria netral at left, idle
    with fade
    # Start BGM Jade

    nd_narrator_brown "Setelah cukup puas bercerita, aku menyadari sesuatu yang janggal."
    
    # show screen show_item("assets/props/jade_bottle.png", "Botol misterius") with Dissolve(0.2)
    show dark_overlay
    show jade_bottle at pos(y=0.3, r=45), speaking with dissolve

    nd_narrator_brown "Aku mengeluarkan sebuah botol yang sama dengan di kamar sebelumnya, membuatku bertanya-tanya bagaimana bisa dia terbawa bersamaku."

    show jade_bottle at pos(y=0.5, z=2.0, r=45) with dissolve
    
    nd_narrator_brown "Aku melihat sebuah ukiran bertuliskan dengan huruf jepang, Yozakura Yuura."

    hide dark_overlay
    hide jade_bottle
    with dissolve

    show yuura netral eff_surprise_y at right, speaking
    nd_narrator_brown "Aku terkejut bukan main."

    nd_yuura_brown "(Kenapa namaku ada di sini ? Bahkan cara menulisnya sama persis seperti diriku)"

    show yuura none at idle
    nd_narrator_brown "Aku semakin bingung dengan apa yang terjadi. Baru beberapa saat yang lalu aku dikejar oleh ratusan orang dan sekarang aku malah membawa benda berharga atas nama diriku sendiri."

    nd_narrator_brown "Aku benar-benar tidak mengerti sekaligus bingung setelah melihat ukiran nama pada botol itu."

    nd_narrator_brown "Tapi mana mungkin aku mampu membeli botol semahal itu, makan saja sudah sangat sulit. Mana mungkin aku punya uang untuk beli botol mewah."

    show pria at speaking
    voice voice_1_3_28_pria_misterius
    wd_unknown_brown "Oh? Kamu membawa benda yang menarik~"
    
    show pria at idle
    show yuura at speaking
    nd_yuura_brown "Apa maksudmu? Lagipula aku ingat dengan jelas bahwa botol ini tidak bersamaku?"
    
    show yuura at idle
    show pria at speaking
    voice voice_1_3_30_pria_misterius
    wd_unknown_brown "Lalu bagaimana benda itu bisa di sini?"
    
    show pria at idle
    show yuura at speaking
    nd_yuura_brown "Entahlah.. Jika botol ini ku bawa di dalam bajuku, sudah pasti akan sangat sulit membawanya sambil dikejar oleh banyak orang"
    
    show yuura at idle
    show pria at speaking
    voice voice_1_3_32_pria_misterius
    wd_unknown_brown "Mungkin saja takdir"
    
    show pria at idle
    show yuura at speaking
    nd_yuura_brown "Takdir? Apa maksudmu semua hal bodoh ini adalah takdir bagiku?"
    
    show yuura at idle
    show pria at speaking
    voice voice_1_3_34_pria_misterius
    wd_unknown_brown "Mungkin saja kan~"
    
    show pria at idle
    show yuura at speaking
    nd_yuura_brown "Ga, ga masuk akal. Mustahil, lebih baik aku pergi keluar dan menjual botol ini."
    
    show yuura at center, speaking with ease
    nd_narrator_brown "Aku berjalan melewati pria misterius itu"
    
    show yuura at idle
    show pria at speaking
    voice voice_1_3_36_pria_misterius
    wd_unknown_brown "Coba saja, kalau bisa" 
        # hide Unknown
        # with fade
    
    show pria at idle
    show yuura at speaking
    nd_yuura_brown "Apa maksud...mu???"
    hide pria with dissolve
    show yuura scared eff_exclamation at speaking
    nd_yuura_brown "Ke mana orang itu pergi ?"
    stop music
    show yuura at idle
    nd_narrator_brown "Aku terdiam sejenak, bertanya-tanya kemana pria itu pergi. Tapi aku langsung mengalihkan perhatianku saat ini, aku sudah tidak peduli lagi dan langsung pergi mencari jalan keluar dari sini."
    hide yuura with easeoutleft

    jump scene_4
