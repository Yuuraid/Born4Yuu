# label start:

label scene_12:

    scene inn entrance_2 with Dissolve(2.0) 
    
    # show yuura netral at center, idle
    show yuura netral at face_flip, ease_custom(offscreenleft, left, 7.0)
    nd_narrator_brown "Tepat ketika aku tiba di dekat pintu depan, aku melihat seorang laki-laki berwajah masam.{w=1.0}{nw}"

    show aergia netral at ease_custom(offscreenright, right, 5.0), idle

    nd_narrator_brown "Kantung matanya sangat tebal, wajahnya terlihat sudah sangat lelah dan tidak karuan. Dia menghampiriku dan mencoba menyapaku."

    # show yuura at right
    # with move
        # Aergia
    show aergia at right, speaking
    with dissolve
    voice voice_2_12_181_aergia
    # nd_unknown_brown "Halo anee... Tidak. {w=0.5}Yuura... Apa kabar ?"
    nd_unknown_brown "ehh halo~, eh.. maksudnya Yuura, apa kabar yuur? hehe"
    show aergia at idle

    nd_narrator_brown "Aku terdiam sejenak, mencoba mencari tahu orang ini dari buku tamu yang kubawa."
    
    nd_narrator_brown "Sayangnya, di dalamnya tidak ada informasi apa pun mengenai orang ini."
        
    show yuura scared at face_flip, speaking
    nd_yuura_brown "Ah... H-halo {w}eh...mh..."
    show yuura at face_flip, idle

    show aergia at speaking
    # voice voice_2_12_183_aergia
    # nd_unknown_brown "Loh ? Kamu cari aku di buku tamu? Padahal gua gapernah ditulis di sana sama lu loh... Lu tahukan gua siapa, Yuur ?"
        # Ga konsisten gua gua, aku aku
    
    # TODO: find out how to implement the timing for textbox and audio

    voice voice_2_12_183_aergia
    nd_unknown_brown "Loh? kamu cari aku dibuku tamu? padahal gua ga pernah ditulis disana sama lu loh… lu tahukan gua siapa Yur?"
    show aergia at idle
        
    show yuura at face_flip, speaking
    nd_yuura_brown "A-ah g-ga dong, tentu saja aku tahu."
    
    nd_yuura_brown "(Sial, apakah aku akan ketahuan ?)"
    show yuura at face_flip, idle

    show aergia at speaking
    voice voice_2_12_185_aergia
    nd_unknown_brown "ehh..Beneran??? Yuura, inget kan sama gua iya kan? KAN? kan~?"
    show aergia at idle
    
    nd_narrator_brown "Dia menatapku dengan sangat tajam, membuatku merinding melihatnya. Dia sepertinya sudah sangat curiga padaku, tapi tiba-tiba saja dia tertawa."
    
    show aergia at speaking
    voice voice_2_12_186_aergia
    nd_unknown_brown "Hahaha... Bercanda kok, Yuur. Gua tahu pasti lu lagi capek banget. Lu ga mungkin lupa sama gua, iya kan ? {nw=0.5}"
    show aergia angry at shake
    extend "KAN !?"
    show aergia at idle
            
    show aergia at speaking
    voice voice_2_12_187_aergia
    nd_aergia_brown "Ehh, ini gua loh Yuur... gua Aergia, ingat kan?"
    show aergia at idle
        
    show yuura at face_flip, speaking
    nd_yuura_brown "Ah... Aergia ! Inget-inget hehe."
    show yuura at face_flip, idle

    show aergia at speaking
    voice voice_2_12_189_aergia
    nd_aergia_brown "nahhhh kan inget, eh tapi....kok. hmm kok rasanya ada yang aneh..lu beneran yuura kan?"
        
    show yuura at face_flip, speaking
    nd_yuura_brown "!!!"
    
    nd_yuura_brown "A-apa maksudmu ? A-aku Yuura, kok !"
    show yuura at face_flip, idle
        
    show aergia at speaking
    voice voice_2_12_192_aergia
    nd_aergia_brown "Lah lah, lah ko marah??" 
    
    voice voice_2_12_193_aergia
    nd_aergia_brown "emngnya gw salah kah? kok marah gitu sih?"
    show aergia at idle
        
    show aergia at speaking
    nd_yuura_brown "B-bukan begitu, cuma terlalu mendadak jadinya aku kaget."
    show yuura at face_flip, idle

    show aergia at speaking
    voice voice_2_12_195_aergia
    nd_aergia_brown "Oh... Gitu..."
    
    voice voice_2_12_196_aergia
    nd_aergia_brown "Maaf ya… kalo gua agak terlalu aneh buat lu… maaf ya Yur haha"
    show aergia at idle

    show aergia at ease_custom(right, offscreenleft, 10.0)

    nd_narrator_brown "Aergia langsung pergi dari sana, membuatku semakin bertanya-tanya dengan apa yang terjadi dan mengapa Yuura yang dulu sangat disayang oleh mereka."
    # hide aergia with dissolve
    
    nd_narrator_brown "Aku sudah tidak peduli, aku lelah dan hanya ingin beristirahat sejenak. Pada akhirnya aku duduk di teras dan menikmati waktu ku berdiam diri."

    jump scene_13
    
    return