# label start:

label scene_3:
    # play music bgm_scene3_forest_w_ambience volume 1.0 loop
    play sound sfx_ambience_grasak_grusuk_daun_scene3
    scene transition_screen orange concentrationline02_w with dissolve
    show yuura scared at center, speaking with easeinright
    nd_narrator_brown "Aku berlari, terus berlari, tanpa sekalipun melihat ke belakang. Aku berlari tanpa henti, berharap mereka semua tidak mengejar diriku lagi."
    
    show yuura at speaking
    nd_you_brown "*huft huft..."
    hide yuura with easeoutleft
    stop sound
    
    play music bgm_scene3_forest_w_ambience fadeout 1.0 volume 0.7 loop
    scene hutan pohon with dissolve
    show yuura angry at center, speaking with easeinright #dissapointed/confused
    
    nd_you_brown "Arghhh.. ini gila! Bisa-bisanya aku terbangun di tempat kayak gini? Huah.."
    
    play sound sfx_expression_sweat
    show yuura scared eff_sweat_w at speak_in_mind
    nd_narrator_brown "Nafasku tersengal-sengal karena berlarian terus sepanjang waktu."
    
    hide yuura with easeoutleft
    scene hutan taman with dissolve
    show yuura scared at center, speaking with easeinright

    nd_narrator_brown "Aku melanjutkan perjalananku dengan rasa lelah yang luar biasa, sebelum akhirnya aku memutuskan untuk duduk di dekat sebuah pohon besar."
    
    nd_narrator_brown "Aku berusaha menenangkan diri, menarik nafas secara perlahan dan mulai memikirkan segalanya."
    
    play sound sfx_expression_angry
    show yuura angry eff_angry at speaking
    nd_you_brown "(Bagaimana aku bisa tiba-tiba berada di tempat ini? Apa yang telah terjadi? Mengapa ini semua terjadi? Dan kenapa aku bisa ada di sini?)"

    stop music fadeout 1.0
    play music bgm_scene3_pria_asing volume 1.0 fadein 2.0 fadeout 2.0 loop
    
    pause 0.2
    voice voice_1_3_19_pria_misterius
    wd_unknown_brown "Capek kan? Lari-lari."
    
    show yuura netral eff_exclamation_y at shake
    play sound sfx_expression_surprised
    nd_narrator_brown "Aku terkejut mendengar suara yang entah dari mana asalnya. Aku melihat sekitar dan merasakan adanya seseorang di balik pohon yang ku sandari."
    
    show yuura none at idle
    voice voice_1_3_20_pria_misterius
    wd_unknown_brown "Gausah takut, aku gak gigit."
    
    nd_narrator_brown "Aku merasa terkejut, bingung, sekaligus bertanya-tanya dari mana orang ini berasal. Aku tidak tahu apapun tentangnya, yang aku tahu suara ini adalah suara laki-laki."

    voice voice_1_3_21_pria_misterius
    wd_unknown_brown "Kamu.. bukan dari dunia ini kan?"

    play sound sfx_expression_angry
    show yuura angry eff_angry at face_flip, speaking
    nd_you_brown "S-Siapa kamu??? CEPAT JAWAB DARIMANA KAMU TAHU TENTANGKU!"
    
    show yuura at face_flip, idle 
    voice voice_1_3_23_pria_misterius
    wd_unknown_brown "Intuisiku saja."
    
    play sound sfx_expression_sweat
    show yuura sad eff_sweat_w at speaking
    show pria at idle
    nd_you_brown "Aku sudah tidak mengerti lagi dengan tempat ini, tadi orang-orang mengejarku." 
    
    nd_you_brown "Sekarang ada orang aneh entah dari mana yang berbicara denganku dari balik pohon! Lalu apa? Aku akan melihat orang-orang masuk penjara?"


    show yuura at idle
    wd_unknown_brown "..."

    # stop music
    # play music bgm_scene3_pelukan volume 1.0 loop

    play sound sfx_expression_sweat
    show yuura at speaking
    # show pria at idle
    nd_you_brown "Aku capek.. aku mau pulang.. tidak seharusnya aku disini.."
    
    show yuura at idle
    # show pria at speaking
    voice voice_1_3_27_pria_misterius
    wd_unknown_brown "Hey.. jangan menangis. Aku gak sanggup melihat cewek nangis di hadapanku."

    stop music fadeout 1.0
    play music bgm_scene3_pelukan volume 1. loop
    
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
    $ unlock_cg("cg_arc_1_scene_03_shoot_4")
    scene cg_arc_1_scene_03_shoot_4:
        zoom 1.05
        xalign 0.5
        yalign 0.5
        linear 2.0 zoom 1.0
    with Flash

    pause 1.5

    nd_narrator_brown "Aku mengangkat kepalaku dan melihat seseorang berdiri di hadapanku, dengan jubah panjang dan topi fedora yang menutupi wajahnya."
    
    $ unlock_cg("cg_arc_1_scene_03_shoot_5")
    scene cg_arc_1_scene_03_shoot_5:
        zoom 1.03
        xalign 0.5
        yalign 0.5
        linear 2.0 zoom 1.0
    with Flash

    nd_narrator_brown "Melihat sosoknya yang tinggi itu, membuatku tanpa sadar memeluknya dan langsung menangis."

    nd_narrator_brown "Di tempat yang serba asing ini, anehnya kehadiran orang yang benar-benar tidak aku kenali ini justru terasa...{w} familiar."
    
    scene cg_arc_1_scene_03_shoot_5:
        # zoom 1.03
        xalign 0.5
        yalign 0.5
        linear 5.0 zoom 1.8

    nd_narrator_brown "Aku menceritakan semuanya tanpa ku sadari, orang itu hanya diam membiarkan ku mengeluarkan semuanya."

    # stop music
    # play music bgm_scene1_jade_bottle volume 1.0 loop
    
    # DEMO END HERE

    # CG end here
    scene hutan taman 
    show yuura sad at right, idle
    show pria netral at left, idle, face_flip
    with fade
    # Start BGM Jade

    nd_narrator_brown "Setelah cukup puas bercerita, aku menyadari sesuatu yang janggal."
    
    play sound sfx_glass_bottle
    # show screen show_item("assets/props/jade_bottle.png", "Botol misterius") with Dissolve(0.2)
    show dark_overlay
    show jade_bottle at pos(y=0.3, r=45), speaking with dissolve

    nd_narrator_brown "Aku mengeluarkan sebuah botol yang sama dengan di kamar sebelumnya, membuatku bertanya-tanya bagaimana bisa dia terbawa bersamaku."

    play sound sfx_bottle_click
    show jade_bottle at pos(y=0.5, z=2.0, r=45) with dissolve
    
    nd_narrator_brown "Aku melihat sebuah ukiran bertuliskan dengan huruf jepang, Yozakura Yuura."

    hide dark_overlay
    hide jade_bottle
    with dissolve

    play sound sfx_expression_shocked
    show yuura scared eff_surprise_y at right, speaking
    nd_narrator_brown "Aku terkejut bukan main."

    nd_you_brown "(Nama ini----!)"

    show yuura none at idle
    nd_narrator_brown "Aku semakin bingung dengan apa yang terjadi. Baru beberapa saat yang lalu aku dikejar oleh ratusan orang dan sekarang aku malah menemukan barang yang tak ingat aku pernah ambil."

    #nd_narrator_brown "Aku benar-benar tidak mengerti sekaligus bingung setelah melihat ukiran nama pada botol itu."

    nd_narrator_brown "Belum lagi, nama yang terukir di atasnya..."


    # nd_narrator_brown "Tapi mana mungkin aku mampu membeli botol semahal itu, makan saja sudah sangat sulit. Mana mungkin aku punya uang untuk beli botol mewah."

    show pria happy at speaking
    voice voice_1_3_28_pria_misterius
    wd_unknown_brown "Oh? Kamu membawa benda yang menarik~"
    
    show pria at idle
    play sound sfx_expression_surprised
    show yuura angry eff_question_mark_r at speaking
    nd_you_brown "Apa maksudmu? Lagipula aku ingat dengan jelas bahwa botol ini tidak bersamaku?"
    
    show yuura none at idle
    play sound sfx_expression_surprised
    show pria netral eff_question_mark_flip_r at speaking
    voice voice_1_3_30_pria_misterius
    wd_unknown_brown "Lalu bagaimana benda itu bisa di sini?"
    
    show pria none at idle
    show yuura at speaking
    nd_you_brown "Entahlah.. Jika botol ini ku bawa di dalam bajuku, sudah pasti akan sangat sulit membawanya sambil dikejar oleh banyak orang."
    
    show yuura at idle
    show pria at speaking
    voice voice_1_3_32_pria_misterius
    wd_unknown_brown "Mungkin saja takdir."
    
    show pria at idle
    show yuura at speaking
    nd_you_brown "Takdir? Apa maksudmu semua hal bodoh ini adalah takdir bagiku?"
    
    show yuura at idle
    # play sound sfx_expression_laugh
    show pria happy eff_laugh_r at speaking
    voice voice_1_3_34_pria_misterius
    wd_unknown_brown "Mungkin saja kan~"
    
    show pria none at idle
    play sound sfx_expression_angry
    show yuura eff_angry at speaking
    nd_you_brown "Gak, gak masuk akal. Mustahil, lebih baik aku pergi keluar dan menjual botol ini."
    
    show yuura none at center with ease
    nd_narrator_brown "Aku berjalan melewati pria misterius itu."
    
    show yuura at idle
    show pria at speaking
    voice voice_1_3_36_pria_misterius
    wd_unknown_brown "Coba saja, kalau bisa." 
        # hide Unknown
        # with fade
    
    show pria at idle
    play sound sfx_expression_surprised
    show yuura eff_question_mark_r at speaking
    nd_you_brown "Apa maksudmu?!"

    play sound sfx_zoom
    hide pria with dissolve
    play sound sfx_expression_shocked
    show yuura scared eff_exclamation_y at speaking
    nd_you_brown "Ke mana orang itu pergi?"
    # stop music 
    show yuura at idle
    nd_narrator_brown "Aku terdiam sejenak, bertanya-tanya kemana pria itu pergi. Tapi aku langsung mengalihkan perhatianku saat ini, aku sudah tidak peduli lagi dan langsung pergi mencari jalan keluar dari sini."
    play sound sfx_action_whoosh_scene13_16
    hide yuura with easeoutleft

    stop music fadeout 1.0

    jump scene_4
