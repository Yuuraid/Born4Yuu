# label start:

label scene_4:
    # scene black #sementara
    # $ quick_menu = True
    # # scene Kuil kecil with Dissolve(2.0)
    # # play music "audio/bgm/kuil.ogg" fadein 1.0
    # show Yuura at center
    # with Dissolve(1.0)
    scene transition_screen orange concentrationline02_w with dissolve
    show yuura scared at center, speaking with easeinright
    nd_narrator_brown "Aku terus berjalan, melewati pepohonan yang entah kenapa sangat familiar bagiku. Sepertinya aku sudah berputar-putar di tempat ini selama berjam-jam tanpa menemukan jalan keluar."

    nd_narrator_brown "Kaki ku lemas, rasanya sangat sakit sekali. Aku benar-benar berjalan-jalan sepanjang hari tapi tetap saja berakhir di tempat yang sama."
    
    scene hutan kuil with fade
    show yuura netral at center, speaking with easeinright
    nd_narrator_brown "Sampai akhirnya aku mendengar suara dari sebuah gitar yang menuntunku menuju sebuah kuil kecil di dalam hutan."
    
    show yuura at flip_loop_left
    nd_narrator_brown "Aku melihat sekitar, seraya mencari siapa yang memainkan gitar di hutan ini."
    
    show yuura eff_sweat_w
    nd_narrator_brown "Aku berjalan dengan tubuh yang terhuyung-huyung, rasanya sangat tubuhku seperti dipukul palu besar."
    
    nd_narrator_brown "Aku mencari disekitar dengan harapan bahwa aku akan bertemu seseorang."
    
    hide yuura
    # show yuura none netral at right, speaking
    show yuura none netral at right, face_flip, speaking
    with fade
    show haruto happy at left with easeinleft
    pause 0.5
    show yuura eff_surprise_y netral at right, face_default, speaking
    nd_narrator_brown "Tanpa ku sadari seseorang datang menghampiriku dari belakang, membuatku berteriak kencang"
    
    show yuura none netral
    nd_yuura_brown "AHH !!" # buat gimmick biar karakternya loncat
        # hide Yuura # harusnya geser aja ke kiri
        # show Yuura at left
        # show Haruto at right
        # with Dissolve(0.5)
    
    show haruto eff_exclamation at speaking
    show yuura at idle
    voice voice_1_4_39_haruto
    wd_unknown_brown "Aneeki? Kenapa kamu bisa ada disini?" 
    
    show haruto none at idle
    show yuura at speaking
    nd_yuura_brown "(Sepertinya dia mengenaliku, sebaiknya aku berpura-pura mengenalnya saja)"
    
    nd_yuura_brown "AH... em aku sedang jalan-jalan saja kok."
    
    show haruto at speaking
    show yuura at idle
    voice voice_1_4_41_haruto
    wd_unknown_brown "Oh begitukah? bukannya jam segini harusnya kamu masih di penginapan?"
    
    show haruto at idle
    show yuura at speaking
    nd_yuura_brown "Ah... Em... Aku hanya bosan saja hahaha."
    
    show haruto at speaking
    show yuura at idle
    voice voice_1_4_43_haruto
    wd_unknown_brown "Kenapa kamu terlihat sangat berantakan? apa kamu baik-baik saja?"
    
    show haruto at idle
    show yuura at speaking
    nd_yuura_brown "I-itu tidak penting sekarang, b-bisakah kamu menemani ku menuju jalan keluar dari hutan ini ?"
    
    show haruto at speaking
    show yuura at idle
    voice voice_1_4_45_haruto
    wd_unknown_brown "Tentu? tapi tumben banget kamu ingin ditemani seperti ini. Biasanya juga kamu pergi sendiri" 
    
    show haruto at idle
    show yuura at speaking
    nd_yuura_brown "K-karena aku sudah terlalu lelah berkeliling hutan ini, makanya aku minta ditemani."
    
    show haruto at idle
    show yuura at speaking
    nd_narrator_brown "Dia tampak bingung dengan alibiku, tapi dia tetap percaya padaku dengan sepenuh hatinya."
    
    show haruto at speaking
    show yuura at idle
    voice voice_1_4_47_haruto
    wd_unknown_brown "Baiklah biar aku antarkan kamu kembali ke penginapan" 
    
    show haruto at idle
    show yuura at speaking
    nd_yuura_brown "Penginapan? Bangunan besar yang bergaya jepang itu ? K-kenapa kita harus kesana ?"
    
    show haruto at speaking
    show yuura at idle
    voice voice_1_4_50_haruto
    wd_unknown_brown "Loh? Bukannya jalan keluar dari hutan ini memang di penginapan?" 
    
    voice voice_1_4_51_haruto
    wd_unknown_brown "Anee kamu yakin baik-baik saja?"
    
    show haruto at idle
    show yuura at speaking
    nd_yuura_brown "Y-ya.. aku baik-baik saja, um.."
    
    show haruto at speaking
    show yuura at idle
    voice voice_1_4_53_haruto
    wd_haruto_brown "Haruto anee, namaku Haruto" 
    
    show haruto at idle
    show yuura at idle
    nd_narrator_brown "Haruto hanya bisa terdiam dan tertawa kecil melihat diriku yang seperti orang linglung."
    
    show haruto at idle
    show yuura at speaking
    nd_yuura_brown "Haruto, mengapa kamu mau membantuku ?"
    
    nd_narrator_brown "Aku menatapnya dengan keheranan, karena sepanjang tadi pagi aku terus saja mengalami kesialan membuatku curiga padanya."
    
    show haruto at speaking
    show yuura at idle
    voice voice_1_4_56_haruto
    wd_haruto_brown "Hahaha.. pertanyaan macam apa itu Anee? tentu saja aku membantumu karena kamu selalu membantuku"
    
    show haruto at idle
    show yuura at speaking
    nd_narrator_brown "Aku bingung dengan maksudnya, tapi aku seperti merasakan sesuatu yang nostalgia dalam dirinya."
    
    scene inn entrance_2 with fade
    show haruto happy at ease_custom(offscreenright, left, 1.3)
    show yuura happy at ease_custom(offscreenright, right, 2.0)
    nd_narrator_brown "Haruto pun mengantarkan diriku sampai di depan gerbang penginapan" 
    
    show haruto at ease_custom(left, offscreenright, 1.8)
    show yuura at center with ease
    nd_narrator_brown "Dia pun pamit karena masih ada banyak hal yang harus dia lakukan."
    
    nd_narrator_brown "Aku berterimakasih banyak pada Haruto atas kebaikannya. Dia hanya tersenyum sembari berjalan menjauh menuju hutan, dan menghilang dari pandanganku."
        # $ quick_menu = False

    jump scene_5