# label start:

label scene_13:

    scene inn resepsionis
    with Dissolve(1.0) 

    show yuura netral at face_flip, ease_custom(offscreenleft, center, 7.0)

    nd_narrator_brown "Hari pun mulai gelap, rasanya kepalaku lebih baik dibanding sebelumnya. Aku berjalan menuju kamarku untuk berleha-leha."
    
    nd_narrator_brown "Tapi entah mengapa aku banyak sekali mendengar hal-hal aneh di sekitar, mereka tampak seperti sedang membicarakanku."
    
    nd_narrator_brown "Aku bingung bagaimana berita ini bisa sangat cepat menyebar dalam waktu beberapa jam saja ? Aku tidak mengerti lagi dengan tempat ini."
    
    nd_narrator_brown "Tepat ketika aku sedang melamun, aku mendengar suara langkah kaki yang cepat menghampiriku."
    
    scene pe kick kick_set_alter:
        zoom 0.95
        xzoom -1
        xalign 0.5
        yalign 0.5
        linear 0.5 zoom 1.05
    with Flash

        # play sound pressure
        # Use CG here
    nd_narrator_brown "Seseorang melancarkan tendangan ke arahku.{w=0.5}{nw}" 
    
    scene inn resepsionis
    show yuura scared at face_flip, center
    pause 0.2
    show yuura at face_flip, ease_custom(center, left, 0.25)

    nd_narrator_brown "Tapi sebelum sempat bereaksi{w=0.5}{nw}"

    show pe purple_flame flame_full at custom_sprite_pos(x=3.0, y=0.5), silhouette
    show yuura at face_flip, consumed_by_darkness

    pause 0.2
    hide pe purple_flame flame_full with dissolve
    # scene inn resepsionis with fast_fade

    nd_narrator_brown "Pijakanku tiba-tiba menghilang dan aku tenggelam ke dalam kegelapan.."

    hide yuura
    
        # play sound wind blow

    show akasyah angry at left, idle with easeinleft
    show dityo angry at right, idle with easeinright
    
    pause 0.5
    show akasyah at speaking
    voice voice_3_13_197_akasyah
    nd_akasyah_brown "BRENGSEK SEIYA !!!"
    show akasyah at idle
    
    show dityo at speaking
    voice voice_3_13_198_dityo
    nd_dityo_brown "Berhasil kabur lagi ?"
    show dityo at idle
            
    show akasyah at speaking
    voice voice_3_13_199_akasyah
    nd_akasyah_brown "Hah ? Kabur ? Dari hadapan gue ? Ga mungkin ! Ga bakal gua biarin si tua itu kabur dari gua. Gimana Dit ? Lu udah nemu belum kelemahannya si Seiya ?"
    show akasyah at idle
    
    # show akasyah at speaking
    # voice voice_3_13_200_akasyah
    # nd_akasyah_brown "Gimana Dit ? Lu udah nemu belum kelemahannya si Seiya ?"
    # show akasyah at idle
    
    show dityo at speaking
    voice voice_3_13_201_dityo
    nd_dityo_brown "Udah. Menurut pengamatanku, Seiya hanya dapat berpindah dari radius 20 meter dari tempat ia terakhir berdiri."
    show dityo at idle
            
    show akasyah at speaking
    voice voice_3_13_202_akasyah
    nd_akasyah_brown "20 meter ? Ya elah segitu doang mah bisa gua kejar ! Beraninya si Seiya itu merusak semua rencana gua !"
    hide akasyah 
    with moveoutright
    
        # play sound whoosh
    
    nd_narrator_brown "Akasyah berlari meninggalkan Dityo sendirian."
    
        # play krik krik
    show dityo at speaking
    voice voice_3_13_203_dityo
    nd_dityo_brown "WOI ! TUNGGU, EMANGNYA LU TAU DIA LARI KE... {w=0.5}Ah sudahlah, tidak ada untungnya mengharapkan dia untuk bekerja sama."
    show dityo at idle

    jump scene_14

    return