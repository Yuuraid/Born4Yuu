# label start:

label scene_8:

    # BG: Ruangan di bawah tangga
        # show ruangan di bawah tangga with Dissolve(1.0)
        # play music  awkward with fadein 1.0 -> define dulu
    scene inn lorong lantai_1 with fade
    show yuura netral at ease_custom(offscreenright, right, 0.8), idle
    show shark netral at ease_custom(offscreenright, left, 1.5), idle
    nd_narrator_brown "Aku mendengar gemuruh orang berlarian mencariku, entah apa yang mereka lakukan sehingga mengejarku. Tapi aku selamat berkat seseorang yang menarik tanganku."
    
    show shark eff_sweat_w
    nd_narrator_brown "Dia terlihat sangat pemalu, dengan rambut putih dan mata berwarna biru. Membuatku merasa bersyukur masih ada yang mau menyelamatkanku."
    
    show yuura at speaking
    show shark none at face_flip, idle
    nd_yuura_brown "Terimakasih banyak... {w} Aku selamat berkat... {w} \n(Ah sial aku tidak tahu namanya)"
    
    show yuura at idle
    show shark at face_flip, speaking
    wd_unknown_brown "A-anee lupa sama kami ?"
    
    show yuura at speaking
    show shark at face_flip, idle
    nd_yuura_brown "B-bukan begitu, aku hanya lagi cape aja. Makanya a-aku lupa sama namamu."
    
    show yuura at idle
    show shark at face_flip, speaking
    wd_unknown_brown "O-oh begitu, i-ini anee waktu pertama kali gabung, kamu ngasih aku buku yang isinya nama-nama anak penginapan di sini."
        # play sound memberi barang ??
    
    show dark_overlay
    show guest_book at pos(y=0.3, r=45), speaking with dissolve

    show yuura at idle
    show shark at face_flip, idle

    pause

    hide guest_book 
    hide dark_overlay
    with dissolve

    show yuura at speaking
    show shark at face_flip, idle
    nd_yuura_brown "Oh, oke sekarang aku ingat. Shark!"

    nd_yuura_brown "Tapi kok bukunya kayak ga lengkap ?"
    
    show yuura at idle
    show shark at face_flip, speaking
    wd_shark_brown "Y-ya kan buku tamunya emang ga pernah kamu selesaiin anee..."
    
    show yuura at speaking
    show shark at face_flip, idle
    nd_yuura_brown "O-oh..."
    
    show yuura at idle
    show shark at face_flip, idle
    nd_narrator_brown "Suasana menjadi sangat canggung dan awkward"
        # cek lagi docs nya
    
    show yuura at speaking
    show shark at face_flip, idle
    nd_yuura_brown "Ya udah makasih ya udah bantuin  aku, aku udah ga denger suara apa pun dari luar. Jadi, sampai jumpa, Shark !"
    
    show yuura at ease_custom(right, offscreenleft, 1.5), speaking
    show shark at face_flip, idle
    pause 1.0
    show shark at speaking
    wd_shark_brown "T-tunggu anee a-aku..."
    
    show shark at idle
    nd_narrator_brown "Aku langsung lari tanpa memikirkan orang itu. Dia tampak ingin memanggilku, tapi aku sudah menghilang dari sudut pandangnya."
        # stop music 

    jump scene_9