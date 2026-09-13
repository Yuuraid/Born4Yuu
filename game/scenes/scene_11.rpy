# label start:

label scene_11:

    scene inn entrance_2 with Dissolve(2.0)

        # # show lorong dekat pintu penginapan 
        # with Dissolve(1.0)

    nd_narrator_brown "Sepanjang perjalanan, aku selalu mendengar gosip tentang diriku, entah mengapa rasanya sangat cepat sekali."
    
    nd_narrator_brown "Entah seperti ada dua sejoli yang selalu menyebarkan informasi palsu di penginapan."
    
    show josua netral at left with dissolve
    nd_josua_brown "Bukannya itu Yuura yang dibilang sama Axiaregis ya ?"
    
    show ibe netral at right with dissolve
    nd_ibe_brown "Ihh iya tuh, keknya emang dia deh."
    
    hide ibe
    hide josua
    with dissolve

    nd_narrator_brown "Mendengar itu aku hanya bisa diam, tak peduli. Aku rasa ini semua hanya kesalahan dan akan segera selesai."
    
    show aergia netral at left, idle
    show axia netral at right, idle
    nd_narrator_brown "Sementara itu di tempat lain, Axiaregis bertemu dengan seseorang yang misterius. Wajahnya yang terlihat sangat lelah dengan semua ini membuatnya semakin suram. Dia berdiri diam menatap lukisan tak bergeming sedikit pun."
    
        # Aergia
    
    show aergia at speaking
    nd_unknown_brown "Ha... Lu lagi lu lagi, kenapa sih harus selalu lu yang ke tempat gua ?"
    show aergia at idle
    
    show axia sassy at speaking
    nd_axiaregis_brown "Kira-kira kenapa ya ? Apa jangan-jangan aku suka kamu kyahh."
    show axia at idle
    
    nd_narrator_brown "Api langsung membakar Axiaregis{nw}"
    show axia hurt at shake
    extend "."
    
    show aergia at speaking
    nd_unknown_brown "Bangsat ! Jijik banget anjing. Kenapa sih lu tiap dateng selalu bikin gua kesel ?"
    show aergia at idle
    
    show axia at speaking
    nd_axiaregis_brown "T-tolonggg ahhh panassss...{nw=0.3}"
    show axia netral
    extend "hehe..."
    show axia at idle
    
    show aergia at speaking
    nd_unknown_brown "Cukup ! Jelaskan alasan lu dan pergi dari sini !"
    show aergia at idle
        
    show axia cute at speaking
    nd_axiaregis_brown "Dinginnya... Apa kau tak bisa lembut pada orang seimut diriku ini ?"
    show axia at idle
    
    show aergia angry at speaking
    nd_unknown_brown "Bicara atau lu beneran gua jadiin femboy bakar."
    show aergia at idle
        
    show axia netral at speaking
    nd_axiaregis_brown "Baiklah-baiklah... Ini semua tentang Yuura."
    show axia at idle
    
    show aergia at speaking
    nd_unknown_brown "Yuura ? Ada apa dengannya ?"
    show aergia at idle
        
    show axia at speaking
    nd_axiaregis_brown "Sebenarnya..."
    show axia at idle
    
    hide axia with dissolve
    hide aergia with dissolve
    nd_narrator_brown "Aku berjalan melewati lorong yang semakin banyak anomali di dalamnya, ada seseorang yang sangat menyukai gundam bernama Ivan."
    
    nd_narrator_brown "Ada juga seseorang om-om berbaju batik putih yang sedang berkebun. Terus ada seseorang anak laki-laki yang sedang berbicara dengan kuda nil ? Ah entahlah aku tidak mengerti lagi."
    
    nd_narrator_brown "Dari jauh terdengar suara orang sedang bertengkar dari dalam kamar. Mereka bertengkar karena bermain kartu."
    
    camera:
        # Initial position (zoomed out at the right side)
        zoom 2.2
        xalign 0.0
        yalign 0.5
        
        # Pan across to the left over 5 seconds
        ease 15.0 xalign 0.0
    with dissolve
    
    nd_nicholas_brown "Oi Lark ! Cepet jalan."
    
    nd_lark_brown "Sabar, China !"
    
    nd_nicholas_brown "Kau juga China, anjeng !"
    
    nd_lark_brown "Mana ada aku orang China, anjeng !"
    
    nd_yc_brown "Udah-udah, kalian berdua sesama china ngapain berantem..."

    camera:
        zoom 1.0
        xalign 0.0
        yalign 0.0
    with dissolve

    show yuura netral at center, idle
    nd_narrator_brown "Aku benar-benar bingung dengan situasi di tempat ini, terkadang mereka terlihat santai dan tenang."
    
    nd_narrator_brown "Tapi terkadang mereka terlihat sangat ricuh."
    
    nd_narrator_brown "Aku terus bergerak, tanpa mempedulikan apa pun di sekitarku. Aku hanya ingin beristirahat dari semua keanehan ini."

    return