# label start:

label scene_8:
    # play sound crowd rushing against wooden floor

    scene inn lorong lantai_1 with fade
    show yuura netral at ease_custom(offscreenright, right, 0.8)
    show shark netral at ease_custom(offscreenright, left, 1.5)
    nd_narrator_brown "Aku mendengar gemuruh orang itu berlari mencariku, entah apa yang dia lakukan sehingga mengejarku. Tapi aku selamat berkat seseorang yang menarik tanganku."
    
    show shark eff_sweat_w
    nd_narrator_brown "Dia terlihat sangat pemalu, dengan rambut putih dan mata berwarna biru."
    
    nd_narrator_brown "Paling tidak aku harus berterimakasih, berkat dia aku bisa lolos dari kejaran orang tadi."

    play music bgm_scene8_awkward volume 1.0 loop
    
    show yuura at speaking
    show shark none at face_flip, idle
    # nd_you_brown "Terimakasih banyak... {w} Aku selamat berkat... {w} \n(Ah sial aku tidak tahu namanya)"
    nd_you_brown "Haloo...{w} Terimakasih...{w}ermm...{w}. Kamu udah bantuin aku dari kejaran {w}aduh siapa yah tadi──"
    
    show yuura at idle
    show shark at face_flip, speaking
    voice voice_2_8_79_shark
    wd_unknown_brown "A-anee lupa sama kami?"

    camera:
        zoom 2.0
        xalign 0.7
        yalign 0.3
    show yuura scared eff_sweat_w at speak_in_mind
    show shark none at face_flip, idle
    # nd_you_brown "Terimakasih banyak... {w} Aku selamat berkat... {w} \n(Ah sial aku tidak tahu namanya)"
    nd_narrator_brown "(Ah sial aku tidak tahu namanya)"
    
    camera:
        zoom 1.0
        xalign 0.0
        yalign 0.0
    show yuura at speaking
    show shark at face_flip, idle
    nd_you_brown "B-bukan begitu, aku hanya lagi cape aja. Makanya a-aku lupa sama namamu."
    
    show yuura none at idle
    show shark at face_flip, speaking
    voice voice_2_8_81_shark
    wd_unknown_brown "O-oh begitu, i-ini anee waktu pertama kali gabung, kamu ngasih aku buku yang isinya nama-nama anak penginapan disini"

        # play sound memberi barang??
    
    play sound sfx_paper
    show dark_overlay
    show guest_book at pos(y=0.3, r=45), speaking with dissolve

    show yuura at idle
    show shark at face_flip, idle

    nd_narrator_brown "Aku membuka buku yang dia berikan kepada ku."
    
    nd_narrator_brown "Di situ aku menemukan banyak nama orang yang menjadi penghuni penginapan ini."
    
    nd_narrator_brown "Termasuk orang yang tadi mengejarku dan Shark, orang yang membantu ku."

    # pause

    play sound sfx_paper
    hide guest_book 
    hide dark_overlay
    with dissolve

    show yuura netral at speaking
    show shark at face_flip, idle
    nd_you_brown "Oh, oke sekarang aku ingat. Shark!"

    show yuura eff_question_mark_y
    nd_you_brown "Tapi kok bukunya kayak ga lengkap?"
    
    show yuura none at idle
    show shark happy at face_flip, speaking
    voice voice_2_8_83_shark
    wd_shark_brown "Y-ya kan buku tamunya emang ga pernah kamu selesaiin Ane.." 
    
    show yuura eff_sweat_w at speaking
    show shark at face_flip, idle
    nd_you_brown "O-oh..."
    
    show yuura at idle
    show shark at face_flip, idle
    nd_narrator_brown "Suasana menjadi sangat canggung dan awkward"
        # cek lagi docs nya
    
    show yuura happy at speaking
    show shark at face_flip, idle
    nd_you_brown "Ya udah makasih ya udah bantuin aku, aku udah ga denger suara orang tadi. Jadi, sampai jumpa, Shark!"
    
    show yuura at ease_custom(right, offscreenleft, 1.5), speaking
    show shark at face_flip, idle
    pause 1.0
    show shark netral eff_sweat_w at speaking
    voice voice_2_8_86_shark
    wd_shark_brown "T-tunggu anee a-aku.."
    
    # show shark at idle
    scene black with dissolve
    nd_narrator_black "Aku langsung lari meninggalkan orang itu. Dia tampak ingin memanggilku, tapi aku sudah menghilang dari sudut pandangnya."

    # stop music 

    jump scene_9