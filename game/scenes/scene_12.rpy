# label start:

label scene_12:

    scene inn entrance_2 with Dissolve(2.0) 
    
    show yuura netral at center, idle
    nd_narrator_brown "Tepat ketika aku tiba di dekat pintu depan, aku melihat seorang laki-laki berwajah masam."
    
    nd_narrator_brown "Kantung matanya sangat tebal, wajahnya terlihat sudah sangat lelah dan tidak karuan. Dia menghampiriku dan mencoba menyapaku."

    show yuura at right
    with move
        # Aergia
    show aergia netral at left, speaking, flip_image
    with dissolve
    voice voice_2_12_181_aergia
    nd_unknown_brown "Halo anee... Tidak. {w=0.5}Yuura... Apa kabar ?"
    show aergia at idle

    nd_narrator_brown "Aku terdiam sejenak, mencoba mencari tahu orang ini dari buku tamu yang kubawa."
    
    nd_narrator_brown "Sayangnya, di dalamnya tidak ada informasi apa pun mengenai orang ini."
        
    show yuura scared at speaking
    nd_yuura_brown "Ah... H-halo {w}eh...mh..."
    show yuura at idle

    show aergia at speaking
    # voice voice_2_12_183_aergia
    # nd_unknown_brown "Loh ? Kamu cari aku di buku tamu? Padahal gua gapernah ditulis di sana sama lu loh... Lu tahukan gua siapa, Yuur ?"
        # Ga konsisten gua gua, aku aku
    
    voice voice_2_12_183_aergia
    nd_unknown_brown "Loh ? Lu cari gua di buku tamu ? Padahal gua ga pernah ditulis di sana sama lu loh... Lu tahukan gua siapa, Yuur ?"
    show aergia at idle
        
    show yuura at speaking
    nd_yuura_brown "A-ah g-ga dong, tentu saja aku tahu."
    
    nd_yuura_brown "(Sial, apakah aku akan ketahuan ?)"
    show yuura at idle

    show aergia at speaking
    voice voice_2_12_185_aergia
    nd_unknown_brown "Beneran ??? Yuura inget sama gua kan ? KAN ? KAN ?"
    show aergia at idle
    
    nd_narrator_brown "Dia menatapku dengan sangat tajam, membuatku merinding melihatnya. Dia sepertinya sudah sangat curiga padaku, tapi tiba-tiba saja dia tertawa."
    
    show aergia at speaking
    voice voice_2_12_186_aergia
    nd_aergia_brown "Hahaha... Bercanda kok, Yuur. Gua tahu pasti lu lagi capek banget. Lu ga mungkin lupa sama gua kan ? {nw=0.5}"
    show aergia angry at shake
    extend "KAN !?"
    show aergia at idle
            
    show aergia at speaking
    voice voice_2_12_187_aergia
    nd_aergia_brown "Ini gua loh Yuur... Aergia !"
    show aergia at idle
        
    show yuura at speaking
    nd_yuura_brown "Ah... Aergia ! Inget-inget hehe."
    show yuura at idle

    show aergia at speaking
    voice voice_2_12_189_aergia
    nd_aergia_brown "Ohhh lu inget toh, Yuur ? Tapi...gua rasa nih...lu tuh bukan Yuura !"
        
    show yuura at speaking
    nd_yuura_brown "!!!"
    
    nd_yuura_brown "A-apa maksudmu ? A-aku Yuura, kok !"
    show yuura at idle
        
    show aergia at speaking
    voice voice_2_12_192_aergia
    nd_aergia_brown "Kenapa, Yuur ? Kenapa lu marah begitu ?"
    
    voice voice_2_12_193_aergia
    nd_aergia_brown "Apa emang gua ga pantes nanya itu sama lu ?"
    show aergia at idle
        
    show aergia at speaking
    nd_yuura_brown "B-bukan begitu, cuma terlalu mendadak jadinya aku kaget."
    show yuura at idle

    show aergia at speaking
    voice voice_2_12_195_aergia
    nd_aergia_brown "Oh... Gitu ya..."
    
    voice voice_2_12_196_aergia
    nd_aergia_brown "Maaf ya... Kalo gua terlalu aneh buat lu... Maaf ya."
    show aergia at idle

    nd_narrator_brown "Aergia langsung pergi dari sana, membuatku semakin bertanya-tanya dengan apa yang terjadi dan mengapa Yuura yang dulu sangat disayang oleh mereka."
    hide aergia with dissolve
    
    nd_narrator_brown "Aku sudah tidak peduli, aku lelah dan hanya ingin beristirahat sejenak. Pada akhirnya aku duduk di teras dan menikmati waktuku berdiam diri."

    jump scene_13
    
    return