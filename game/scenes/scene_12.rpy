# label start:

label scene_12:

    scene inn entrance_2 
    camera:
        zoom 1.0
        xalign 0.0
        yalign 0.0
    with Dissolve(2.0) 
    play music bgm_scene8_awkward volume 1.0 loop
    # show yuura netral at center, idle
    show yuura netral at face_flip, ease_custom(offscreenleft, left, 7.0)
    nd_narrator_brown "Tepat ketika aku tiba di dekat pintu depan, aku melihat seorang laki-laki berwajah masam.{w=1.0}{nw}"

    show aergia netral at ease_custom(offscreenright, right, 5.0), idle

    nd_narrator_brown "Kantung matanya sangat tebal, wajahnya terlihat sudah sangat lelah dan tidak karuan. Dia menghampiriku dan mencoba menyapaku."

    # show yuura at right
    # with move
        # Aergia
    show yuura eff_exclamation_y
    show aergia psycho at right, speaking
    with dissolve
    voice voice_2_12_181_aergia_1
    # nd_unknown_brown "Halo anee... Tidak. {w=0.5}Yuura... Apa kabar?"
    nd_unknown_brown "ehh halo~{nw}"
    show aergia smile_cool
    voice voice_2_12_181_aergia_2
    extend " eh.. uuhh ma-maksudnya Yuura, apa kabar yuur? hehe"
    show aergia at idle

    show yuura eff_sweat_w
    nd_narrator_brown "Aku terdiam sejenak, mencoba mencari tahu orang ini dari buku tamu yang kubawa."
    
    nd_narrator_brown "Sayangnya, di dalamnya tidak ada informasi apa pun mengenai orang ini."
        
    show yuura scared at face_flip, speaking
    nd_you_brown "Ah... H-halo... {w}eh...mh..."
    show yuura none at face_flip, idle

    # show aergia eff_question_mark_r at speaking
    # voice voice_2_12_183_aergia
    # nd_unknown_brown "Loh? Kamu cari aku di buku tamu? Padahal gua gapernah ditulis di sana sama lu loh... Lu tahukan gua siapa, Yuur?"
        # Ga konsisten gua gua, aku aku

    show aergia smile_normal eff_question_mark_r at speaking
    voice voice_2_12_183_aergia_1
    nd_unknown_brown "Lololololoh? Kamu cari aku dibuku tamu?{nw}"
    
    show aergia sad eff_sweat_b
    voice voice_2_12_183_aergia_2
    extend " Padahal gua ga pernah ditulis disana sama lu...{nw}"
    
    show aergia netral eff_question_mark_r
    voice voice_2_12_183_aergia_3
    extend " loh, bentar, lu tahukan gua siapa Yur?"
    show aergia none at idle
        
    show yuura at face_flip, speaking
    nd_you_brown "A-ah g-ga dong, tentu saja aku tahu."
    
    show yuura eff_sweat_w at face_flip, speak_in_mind
    camera:
        zoom 2.0
        xalign 0.2
        yalign 0.25
    nd_you_brown "(Sial, apakah aku akan ketahuan?)"
    show yuura none at face_flip, idle

    camera:
        zoom 1.0
        xalign 0.0
        yalign 0.0

    show aergia at speaking
    voice voice_2_12_185_aergia
    nd_unknown_brown "Ehh... beneran??? Yuura, inget kan sama gua iya kan? KAN? kan~?"
    show aergia at idle
    
    nd_narrator_brown "Dia menatapku dengan sangat tajam. Aku mulai merasa sedikit merinding."
    nd_narrator_brown "Nampaknya, orang ini sudah sangat curiga denganku. Tapi, dia tiba-tiba mulai tertawa tanpa alasan yang jelas."
    
    show aergia at speaking
    voice voice_2_12_186_aergia_1
    nd_unknown_brown "Hahaha... Bercanda kok, Yuur. Gua pasti tahu lu tuh lagi capek banget. Lu ga mungkin kan lupa sama gua, iya kan? {nw=0.5}"
    show aergia psycho at shake
    play music bgm_scene15_judgment volume 1.0 loop fadein 1.0
    $ renpy.music.set_volume(0.4, channel="music")
    voice voice_2_12_186_aergia_2
    extend "KAN!?"
    show aergia at idle
            
    show aergia at speaking
    voice voice_2_12_187_aergia
    nd_aergia_brown "Ehh, ini gua loh Yuur... gua Aergia, ingat kan?"
    show aergia at idle
        
    show yuura at face_flip, speaking
    nd_you_brown "Ah... Aergia! Inget-inget hehe."
    show yuura at face_flip, idle

    show aergia sad at speaking
    voice voice_2_12_189_aergia
    nd_aergia_brown "Nahhhh kan inget, eh tapi kok... hmm... kok rasanya ada yang aneh ya..lu...lu beneran yuura kan?"
    show aergia at idle

    show yuura at face_flip, speaking
    nd_you_brown "!!!"
    
    nd_you_brown "A-apa maksudmu? A-aku Yuura, kok!"
    show yuura at face_flip, idle
        
    show aergia angry eff_angry at speaking
    voice voice_2_12_192_aergia
    nd_aergia_brown "Lah lah, lah ko marah??" 

    voice voice_2_12_193_aergia
    nd_aergia_brown "Emangnya gua salah kah? Kok marah gitu sih?"
    show aergia at idle
        
    show yuura at face_flip, speaking
    nd_you_brown "B-bukan begitu, cuma terlalu mendadak jadinya aku kaget."
    show aergia at idle
    show yuura at face_flip, idle

    show aergia netral none at speaking
    voice voice_2_12_195_aergia
    nd_aergia_brown "Ohh gitu~"
    
    show aergia sad eff_sweat_b at speaking
    voice voice_2_12_196_aergia
    nd_aergia_brown "Maaf ya… kalo gua agak terlalu aneh buat lu haha… maaf ya Yuur, haha."
    show aergia at idle

    show aergia none at ease_custom(right, offscreenleft, 10.0)

    nd_narrator_brown "Aergia langsung pergi tanpa lanjut bertanya-tanya."

    show yuura none at center with ease
    # scene black with dissolve
    nd_narrator_brown "Aku terdiam sejenak."
    show yuura at speaking
    nd_you_brown "...lagi-lagi begini."
    show yuura at idle

    # ====

    # nd_narrator_brown "Kemanapun aku pergi,{w=0.5} selalu ada orang-orang yang menyapa dan bertanya."

    # ====

    nd_narrator_brown "Kemanapun aku pergi,{w=0.5} selalu ada orang-orang yang menyapa dan bertanya."

    nd_narrator_brown "Di tengah lamunanku, aku kembali mengeluarkan botol jade hijau yang selama ini tersimpan di dalam saku."

    play sound sfx_glass_bottle
    # show screen show_item("assets/props/jade_bottle.png", "Botol misterius") with Dissolve(0.2)
    show dark_overlay
    show jade_bottle at pos(y=0.5, z=2.0, r=45), speak_in_mind with dissolve

    # nd_narrator_brown "Meski tidak semuanya bersikap ramah,{w=0.5} ditambah kelakuan mereka yang kadang aneh dan menjengkelkan...{w=0.5} tidak bisa dipungkiri bahwa mereka sangat peduli dengan 'Yuura.'"
    # show yuura at speaking

    nd_narrator_brown "Di sana, masih terlihat jelas ukiran nama yang hari ini terus menerus disebut, Yozakura Yuura."

    nd_you_brown "Siapa.. siapa kamu sebenarnya?"
    # show yuura at idle
    nd_narrator_brown "Kenapa kamu bisa begitu dicari?"
    nd_narrator_brown "Kenapa banyak yang begitu peduli?"
    nd_narrator_brown "Kenapa...{w=0.5} siapa kamu?"
    # show yuura at speaking
    # nd_you_brown "..."
    # show yuura at idle
    
    hide dark_overlay
    hide jade_bottle
    with dissolve

    show yuura netral at face_flip with dissolve

    nd_narrator_brown "Di depan ku kini berdiri pintu keluar yang ku cari. Sekarang, aku hanya perlu mengambil langkah terakhir untuk keluar."

    nd_you_brown "..."

    nd_narrator_brown "Sekali lagi aku meraba botol yang ada di dalam saku ku. "

    nd_you_brown "... apa sebaiknya aku kembalikan saja ya?"

    nd_narrator_brown "Barang ini pasti juga berharga bagi mereka. Khususnya dengan Yuura yang tidak ada di sini."

    nd_you_brown "... aku juga sudah tahu jalan keluarnya."

    nd_narrator_brown "Aku rasa mengembalikan barang ini pada tempatnya takkan jadi masalah."

    hide yuura
    show yuura netral at idle, center
    with dissolve
    pause 0.3
    hide yuura with easeoutleft

    nd_narrator_brown "Pada akhirnya aku mengurungkan niatku untuk pergi untuk mengembalikan botol ini."
    
    stop music

    jump scene_13
    
    return