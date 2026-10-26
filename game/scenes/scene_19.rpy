# label start:

label scene_19:
    scene inn resepsionis 
    # play sound barang ditaruh
    show yuura scared at face_flip, left, idle
    show haruto angry at right, idle
    with Dissolve(1.0)

    show yuura eff_sweat_w at face_flip, speaking
    nd_yuura_brown "Phiuu... Akhirnya beres juga bagian resepsionis."
    show yuura scared none at face_flip, idle
    voice voice_4_19_684_haruto
    show haruto at speaking
    nd_haruto_brown "Otsukare, sisanya biar aku yang lanjutkan."
    show haruto angry at idle
    show yuura happy at face_flip, speaking
    nd_yuura_brown "Tolong yah..."
    show yuura at face_flip, idle
    nd_narrator_brown "Tepat ketika baru duduk di kursi resepsionis untuk istirahat, aku melihat sebuah kotak yang tersempil di kolong meja, aku mengambil dan meletakkannya di meja."
    show yuura at face_flip, speaking
    nd_yuura_brown "Kotak apa ini ?"
    show yuura at face_flip, idle
    show haruto happy at speaking
    voice voice_4_19_687_haruto
    nd_haruto_brown "Oh... Itu Time Capsule milikmu, Aneeki."
    show haruto at idle
    show yuura at face_flip, speaking
    nd_yuura_brown "Time Capsule milikku ?"
    show yuura at face_flip, idle
    nd_narrator_brown "Aku membukanya tanpa ragu dan melihatnya begitu banyak barang, foto, dan surat-surat di dalamnya. Aku mengambil satu per satu barang yang ada di dalamnya dan saat itu juga kenangan-kenangan hangat kembali mengalir di benakku."
    
    nd_narrator_brown "Aku hanya tersenyum, ternyata sudah banyak hal yang kulewati selama ini, tak terasa semua kenangan itu telah lama terjadi dan mungkin saja terlupakan jika aku tak pernah menyimpan mereka di suatu tempat."
    
    nd_narrator_brown "Aku melihat surat-surat yang nampaknya ditulis oleh para penghuni penginapan, aku membaca satu per satu hingga terdapat beberapa nama yang tak terdengar lagi sekarang."
    show yuura at face_flip, speaking
    nd_yuura_brown "Si ini kemana yah ? Kok gak pernah keliatan lagi."
    show yuura at face_flip, idle
    show haruto at speaking
    voice voice_4_19_690_haruto
    nd_haruto_brown "Bukannya sudah lama pindah yah..."
    show haruto at idle
    show yuura at face_flip, speaking
    nd_yuura_brown "Iyakah ?"
    
    nd_yuura_brown "Eh, buku tamuku dimana yah..."
    show yuura at face_flip, idle
    show haruto at speaking
    voice voice_4_19_693_haruto
    nd_haruto_brown "Itu kutaruh di atas meja."
    show haruto at idle
    show yuura at idle
    nd_narrator_brown "Aku segera mengambil buku tamu dan membalik-balik halaman untuk mencari tahu orang-orang yang pernah menulis surat untukku, ada yang pindah bahkan ada yang tak terdaftar di sini."
    show yuura at face_flip, speaking
    nd_yuura_brown "Kenapa dia pindah yah ?"
    show yuura at face_flip, idle
    show haruto exhausted at speaking
    voice voice_4_19_695_haruto
    nd_haruto_brown "Kamu kelamaan menjarainnya dulu, Anee..."
    show yuura scared at shake, face_flip, idle
    show haruto at idle
    nd_narrator_brown "Tiba-tiba suasana berubah menjadi canggung..."
    show haruto at speaking
    voice voice_4_19_696_haruto
    nd_haruto_brown "Hehe, bercanda kok."
    show haruto netral at idle
    show yuura happy at face_flip, idle
    show haruto:
        ease 1.0 xalign 0.5
    
    nd_narrator_brown "Haruto mendekat ke meja."
    show haruto at speaking
    voice voice_4_19_697_haruto
    nd_haruto_brown "Kalau Aneeki kesusahan, sini kubantu untuk merekap buku tamunya."
    show haruto at idle
    show yuura at face_flip, speaking
    nd_yuura_brown "Biar aku sendiri aja."
    
    nd_yuura_brown "Lagian aku juga masih punya banyak utang."
    show yuura at face_flip, idle
    show haruto at speaking
    voice voice_4_19_700_haruto
    nd_haruto_brown "Dasar penghutang handal."
    show haruto at idle
    show layer master at shake
    nd_narrator_brown "Tiba-tiba saja terdengar sebuah ledakan besar di taman, membuatku langsung berlari dengan sangat kencang."

    hide yuura with easeoutright

    scene taman_penginapan_1
    show dawam netral at custom_sprite_pos(x=-0.2), idle
    show dityo netral at custom_sprite_pos(x=1.2), idle
    show seiya netral at face_flip, custom_sprite_pos(x=-0.5), idle
    show aergia netral at face_flip, custom_sprite_pos(x=0.5), idle
    show axia netral at custom_sprite_pos(x=0.8), idle
    show shark netral at face_flip, custom_sprite_pos(x=0.25), idle
    show rian netral at custom_sprite_pos(x=0.1), idle
    show akasyah netral at custom_sprite_pos(x=-0.55), idle
    
    with fade
    show yuura netral at custom_sprite_pos(x=1.4), idle with easeinright

    pause 0.2

    show yuura eff_surprise_y at speaking
    nd_yuura_brown "Apa sih yang kalian lakukan ?"
    show yuura none at idle
    show aergia psycho at speaking
    voice voice_4_19_702_aergia
    nd_aergia_brown "Hehe"
    show aergia at idle
    show axia netral at speaking
    voice voice_4_19_703_axiaregis
    nd_axiaregis_brown "Eh Aneee..."
    show axia at idle
    show rian happy at speaking
    voice voice_4_19_704_rian
    nd_rian_brown "Loh Anee ?"
    show rian at idle
    show shark scared at face_flip,  speaking
    voice voice_4_19_705_shark
    nd_shark_brown "A-aduh Anee."
    show shark at face_flip, idle
    show dityo netral at speaking
    voice voice_4_19_706_dityo
    nd_dityo_brown "Waduh..."
    show dityo at idle
    show dawam sad at speaking
    voice voice_4_19_707_dawam
    nd_dawam_brown "Mazui."
    show dawam at idle
    show akasyah netral at speaking
    voice voice_4_19_708_akasyah
    nd_akasyah_brown "Waduh..."
    show akasyah at idle
    show seiya netral at face_flip,  speaking
    voice voice_4_19_709_seiya
    nd_seiya_brown "..."
    show seiya at face_flip, idle
    show yuura at speaking
    nd_yuura_brown "Oi ! Apa yang kalian lakukan ? Kenapa ada ledakan tadi ?"
    show yuura at idle
    nd_narrator_brown "Aku berusaha mendekat, tapi tiba-tiba saja muncul sebuah kembang api di langit. Membuatku terkejut dengan semua ini."

    scene black

    show yuura netral at center, idle
    with Dissolve(1.0)
    voice voice_4_19_711_semua_orang
    show layer master at shake
    nd_narrator_brown "{size=+30}SELAMAT ULANG TAHUN YUURA !!!{/size}"
    show yuura at speaking
    nd_yuura_brown "..."
    show yuura angry eff_angry
    nd_yuura_brown "Kalian ini..."
    show yuura at shake
    nd_yuura_brown "TAPI TADI SUARA LEDAKAN APA OI !"
    hide seiya
    show yuura at idle
    # show aergia netral at right, shake, speaking
    voice voice_4_19_715_aergia
    nd_aergia_brown "Lari !!!"
    hide aergia 
    nd_narrator_brown "Mereka semua lari dengan sangat cepat, membuatku harus mengejar mereka satu per satu. Begitulah setiap hari di penginapan. Tak ada hari yang damai seperti di anime slice of life, isinya hanyalah aksi-aksi yang melelahkan."
    
    nd_narrator_brown "Kami adalah keluarga, keluarga Yuuraid yang akan selalu melindungi penginapan dan pemiliknya dengan sepenuh hati. Meskipun banyak orang yang sudah pergi, tapi orang baru datang dan mengisi kekosongan dalam penginapan."
    
    nd_narrator_brown "Meskipun begitu, kami tetap menjadi diri kami. Menjadi Yuuraid yang selalu mencintai Yuura sepenuh hati."

    return