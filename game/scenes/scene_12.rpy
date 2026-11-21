# label start:

label scene_12:

    scene inn entrance_2 with Dissolve(2.0) 
    play music bgm_scene8_awkward volume 1.0 loop
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
    # nd_unknown_brown "Halo anee... Tidak. {w=0.5}Yuura... Apa kabar?"
    nd_unknown_brown "ehh halo~, eh.. uuhh ma-maksudnya Yuura, apa kabar yuur? hehe"
    show aergia at idle

    nd_narrator_brown "Aku terdiam sejenak, mencoba mencari tahu orang ini dari buku tamu yang kubawa."
    
    nd_narrator_brown "Sayangnya, di dalamnya tidak ada informasi apa pun mengenai orang ini."
        
    show yuura scared at face_flip, speaking
    nd_yuura_brown "Ah... H-halo... {w}eh...mh..."
    show yuura at face_flip, idle

    show aergia at speaking
    # voice voice_2_12_183_aergia
    # nd_unknown_brown "Loh? Kamu cari aku di buku tamu? Padahal gua gapernah ditulis di sana sama lu loh... Lu tahukan gua siapa, Yuur?"
        # Ga konsisten gua gua, aku aku
    
    # TODO: find out how to implement the timing for textbox and audio

    voice voice_2_12_183_aergia
    nd_unknown_brown "Lololololoh? Kamu cari aku dibuku tamu? Padahal gua ga pernah ditulis disana sama lu... loh, bentar, lu tahukan gua siapa Yur?"
    show aergia at idle
        
    show yuura at face_flip, speaking
    nd_yuura_brown "A-ah g-ga dong, tentu saja aku tahu."
    
    nd_yuura_brown "(Sial, apakah aku akan ketahuan?)"
    show yuura at face_flip, idle

    show aergia at speaking
    voice voice_2_12_185_aergia
    nd_unknown_brown "Ehh... beneran??? Yuura, inget kan sama gua iya kan? KAN? kan~?"
    show aergia at idle
    
    nd_narrator_brown "Dia menatapku dengan sangat tajam. Aku mulai merasa sedikit merinding."
    nd_narrator_brown "Nampaknya, orang ini sudah sangat curiga denganku. Tapi, dia tiba-tiba mulai tertawa tanpa alasan yang jelas."
    
    show aergia at speaking
    voice voice_2_12_186_aergia
    nd_unknown_brown "Hahaha... Bercanda kok, Yuur. Gua tahu pasti lu tuh lagi capek banget. Lu ga mungkin lupa sama gua, iya kan? {nw=0.5}"
    show aergia angry at shake
    play music bgm_scene15_judgment volume 1.0 loop fadein 1.0
    $ renpy.music.set_volume(0.4, channel="music")
    extend "KAN!?"
    show aergia at idle
            
    show aergia at speaking
    voice voice_2_12_187_aergia
    nd_aergia_brown "Ehh, ini gua loh Yuur... gua Aergia, ingat kan?"
    show aergia at idle
        
    show yuura at face_flip, speaking
    nd_yuura_brown "Ah... Aergia! Inget-inget hehe."
    show yuura at face_flip, idle

    show aergia at speaking
    voice voice_2_12_189_aergia
    nd_aergia_brown "Nahhhh kan inget, eh tapi....kok. hmm kok rasanya ada yang aneh ya..lu...lu beneran yuura kan?"
    show aergia at idle

    show yuura at face_flip, speaking
    nd_yuura_brown "!!!"
    
    nd_yuura_brown "A-apa maksudmu? A-aku Yuura, kok!"
    show yuura at face_flip, idle
        
    show aergia at speaking
    voice voice_2_12_192_aergia
    nd_aergia_brown "Lah lah, lah ko marah??" 

    voice voice_2_12_193_aergia
    nd_aergia_brown "emngnya gw salah kah? kok marah gitu sih?"
    show aergia at idle
        
    show yuura at face_flip, speaking
    nd_yuura_brown "B-bukan begitu, cuma terlalu mendadak jadinya aku kaget."
    show aergia at idle
    show yuura at face_flip, idle

    show aergia at speaking
    voice voice_2_12_195_aergia
    nd_aergia_brown "Oh... Gitu..."
    
    voice voice_2_12_196_aergia
    nd_aergia_brown "Maaf ya… kalo gua agak terlalu aneh buat lu haha… maaf ya Yuur haha."
    show aergia at idle

    show aergia at ease_custom(right, offscreenleft, 10.0)

    nd_narrator_brown "Aergia langsung pergi tanpa lanjut bertanya-tanya."
    scene black with dissolve
    nd_narrator_brown "Aku terdiam sejenak."
    nd_yuura_brown "...lagi-lagi begini."
    nd_narrator_brown "Kemanapun aku pergi,{w=0.5} selalu ada orang-orang yang menyapa dan bertanya."
    nd_narrator_brown "Meski tidak semuanya bersikap ramah,{w=0.5} ditambah kelakuan mereka yang kadang aneh dan menjengkelkan...{w=0.5} tidak bisa dipungkiri bahwa mereka sangat peduli dengan 'Yuura.'"
    nd_yuura_brown "...kamu sebenarnya siapa sih?"
    nd_narrator_brown "Kenapa kamu bisa begitu dicari?"
    nd_narrator_brown "Kenapa banyak yang begitu peduli?"
    nd_narrator_brown "Kenapa...{w=0.5} kamu bisa begitu dicintai?"
    nd_yuura_brown "..."

    # hide aergia with dissolve
    
    nd_narrator_brown "Tidak ada gunanya memikirkan ini."
    nd_narrator_brown "Aku lelah dan hanya ingin beristirahat sejenak."
    nd_narrator_brown "Pada akhirnya aku duduk di teras dan menghabiskan waktu ku berdiam diri.{w=0.5} Berharap jeda kecil ini akan membantu pelarian ku dari sini."
    
    stop music

    jump scene_13
    
    return