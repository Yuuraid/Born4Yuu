# label start:

label scene_11:

    scene inn parkiran with Dissolve(2.0)

        # # show lorong dekat pintu penginapan 
        # with Dissolve(1.0)

    show yuura netral at face_flip, ease_custom(offscreenleft, offscreenright, 15.0) zorder 10
    pause 2.0
    show josua netral at ease_custom(offscreenright, left, 10.0), idle
    show ibe netral at ease_custom(offscreenright, right, 10.0), idle

    # nd_narrator_brown "Sepanjang perjalanan, aku selalu mendengar gosip tentang diriku, entah mengapa rasanya sangat cepat sekali."

    nd_narrator_brown "Sepanjang perjalanan, aku sangat bingung dengan semua yang terjadi seharian ini. Tapi aku harus bersikap normal agar tidak di curigai orang-orang."

    # nd_narrator_brown "Entah seperti ada dua anomali yang mana aku tidak mengerti apa yang mereka bicarakan."
    
    show josua at speaking
    voice voice_2_11_163_josua
    nd_josua_brown "{font=alien}Be be Yuura tadi Ibe, gokil juga baru nyampe udah ketemu artis kita{/font}\n(Be be Yuura tadi Ibe, gokil juga baru nyampe udah ketemu artis kita)"
    
    # show ibe netral at right with dissolve
    show ibe at speaking
    show josua at idle
    voice voice_2_11_164_ibe
    nd_ibe_brown "{font=alien}Yuura? kamu yakin itu Yuura?{/font}\n(Yuura? kamu yakin itu Yuura?)"

    show ibe at idle
    show josua at speaking
    voice voice_2_11_163_josua
    nd_josua_brown "{font=alien}Kok gitu? emangnya ada yang salah kah?{/font}\n(Kok gitu? emangnya ada yang salah kah?)"

    show ibe at speaking
    show josua at idle
    voice voice_2_11_164_ibe
    nd_ibe_brown "{font=alien}Nggak, cuma firasatku saja{/font}\n(Nggak, cuma firasatku saja)"

    show ibe at idle
    show josua at speaking
    voice voice_2_11_163_josua
    nd_josua_brown "{font=alien}Ah ngibul kamu, mending kita beli YOYU biar kamu nggak halusinasi {/font}\n(Ah ngibul kamu, mending kita beli YOYU biar kamu nggak halusinasi lagi)"
    
    # hide ibe
    # hide josua
    # with dissolve
    show josua at idle, ease_custom(left, offscreenleft, 7.0)
    show ibe at idle, ease_custom(right, offscreenleft, 6.0)

    # nd_narrator_brown "Mendengar itu aku hanya bisa diam, tak peduli. Aku rasa ini semua hanya kesalahan dan akan segera selesai."
    
    # TODO: they both in different places
    scene garden_2
    show aergia netral at left, silhouette
    with fade

    show axia netral at ease_custom(offscreenright, right, 5.0), idle

    nd_narrator_brown "Sementara itu di tempat lain, Axiaregis bertemu dengan seseorang yang misterius."
    
    nd_narrator_brown "Wajahnya yang terlihat sangat lelah dengan semua ini membuatnya semakin suram. Dia berdiri diam menatap orang pacaran di taman tanpa bergeming sedikit pun."
    
        # Aergia
    
    show aergia at silhouette, face_flip, speaking
    voice voice_2_11_165_aergia
    nd_unknown_brown "Ha... Lu lagi lu lagi, kenapa sih harus selalu lu yang ke tempat gua ?"
    show aergia at silhouette, idle
    
    show axia sassy at speaking
    voice voice_2_11_166_axiaregis
    nd_axiaregis_brown "Kira-kira kenapa ya ? Apa jangan-jangan aku suka kamu kyahh."
    show axia at idle
    
    show pe purple_flame flame_full at custom_sprite_pos(x=-3.0, y=0.5) with Dissolve(0.2)
    show axia hurt at shake
    nd_narrator_brown "Api langsung membakar Axiaregis{nw}"
    extend "."
    
    show aergia at silhouette, speaking
    voice voice_2_11_167_aergia
    nd_unknown_brown "Bangsat ! Jijik banget anjing." 
    
    voice voice_2_11_168_aergia
    nd_unknown_brown "Kenapa sih lu tiap dateng selalu bikin gua kesel ?"
    show aergia at silhouette, idle
    
    show axia at speaking
    voice voice_2_11_169_axiaregis
    nd_axiaregis_brown "T-tolonggg ahhh panassss...wuhahahaha.."
    hide pe purple_flame flame_full with dissolve
    show axia at idle
    
    show aergia at silhouette, speaking
    voice voice_2_11_170_aergia
    nd_unknown_brown "Cukup!, jelaskan alasan lu ada sini dan pergi dari sini sekarang!"
    show aergia at silhouette, idle
        
    show axia cute at speaking
    voice voice_2_11_171_axiaregis
    nd_axiaregis_brown "Dinginnya… apa kau tak bisa lembut pada orang seimut diriku ini?"
    show axia at idle
    
    show aergia angry at silhouette, speaking
    voice voice_2_11_172_aergia
    nd_unknown_brown "Ha.. ngomong atau lu mau beneran gua jadiin femboy bakar sekarang"
    show aergia at silhouette, idle
        
    show axia netral at speaking
    voice voice_2_11_173_axiaregis
    nd_axiaregis_brown "Baiklah-baiklah... Ini semua tentang Yuura."
    show axia at idle
    
    show aergia at silhouette, speaking
    voice voice_2_11_174_aergia
    nd_unknown_brown "Hah Yuura?! Emangnya, kenapa sama si Yuura?"
    show aergia at silhouette, idle
        
    show axia at speaking
    voice voice_2_11_175_axiaregis
    nd_axiaregis_brown "Sebenarnya..."
    show axia at idle
    
    # hide axia with dissolve
    # hide aergia with dissolve

    scene garden_1 with dissolve

    show yuura netral at ease_custom(offscreenright, offscreenleft, 20.0)

    nd_narrator_brown "Semakin lama aku berkeliling, semakin aku melihat banyak anomali-anomali di di sekitarku, ada seseorang yang sangat menyukai gundam bernama Ivan."
    
    nd_narrator_brown "Ada juga seseorang om-om berbaju batik putih yang sedang berkebun. Terus ada seorang anak laki-laki yang sedang berbicara dengan kuda nil? Ah entahlah aku tidak mengerti lagi."
    
    # nd_narrator_brown "Dari jauh terdengar suara orang sedang bertengkar dari dalam kamar. Mereka bertengkar karena bermain kartu."
    
    # camera:
    #     # Initial position (zoomed out at the right side)
    #     zoom 2.2
    #     xalign 0.0
    #     yalign 0.5
        
    #     # Pan across to the left over 5 seconds
    #     ease 15.0 xalign 0.0
    # with dissolve
    
    # nd_nicholas_brown "Oi Lark ! Cepet jalan."
    
    # nd_lark_brown "Sabar, China !"
    
    # nd_nicholas_brown "Kau juga China, anjeng !"
    
    # nd_lark_brown "Mana ada aku orang China, anjeng !"
    
    # nd_yc_brown "Udah-udah, kalian berdua sesama china ngapain berantem..."

    # camera:
    #     zoom 1.0
    #     xalign 0.0
    #     yalign 0.0
    # with dissolve

    # show yuura netral at center, idle
    nd_narrator_brown "Aku benar-benar bingung dengan situasi di tempat ini, terkadang mereka terlihat santai dan tenang."
    
    nd_narrator_brown "Tapi terkadang mereka terlihat sangat ricuh."
    
    nd_narrator_brown "Aku terus bergerak, tanpa memperdulikan apapun di sekitarku. Aku hanya ingin beristirahat dari semua keanehan ini."

    jump scene_12

    return