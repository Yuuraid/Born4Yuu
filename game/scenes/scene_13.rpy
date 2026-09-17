# label start:

label scene_13:

    nd_narrator_brown "Hari pun mulai gelap, rasanya kepalaku lebih baik dibanding sebelumnya. Aku berjalan menuju kamarku untuk berleha-leha."
    
    nd_narrator_brown "Tapi entah mengapa aku banyak sekali mendengar hal-hal aneh di sekitar, mereka tampak seperti sedang membicarakanku."
    
    nd_narrator_brown "Aku bingung bagaimana berita ini bisa sangat cepat menyebar dalam waktu beberapa jam saja ? Aku tidak mengerti lagi dengan tempat ini."
    
    nd_narrator_brown "Tepat ketika aku sedang melamun, aku mendengar suara langkah kaki yang cepat menghampiriku."
    
        # play sound pressure
        # Use CG here
    nd_narrator_brown "Untuk sekilas, aku melihat persis seseorang melancarkan tendangan yang mengarah tepat ke arahku." 
    
    nd_narrator_brown "Tapi sebelum sempat bereaksi, pijakanku tiba-tiba menghilang, membuat keseimbanganku tumbang dan terjatuh sebelum akhrinya tenggelam ke dalam kegelapan..."
    
        # play sound wind blow
    scene inn resepsionis
    with Dissolve(1.0) 

    show akasyah angry at left, speaking
    show dityo angry at right, idle
    voice voice_3_13_197_akasyah
    nd_akasyah_brown "BRENGSEK SEIYA !!!"
    show akasyah at idle
    
    show dityo at speaking
    voice voice_3_13_198_dityo
    nd_dityo_brown "Berhasil kabur lagi ?"
    show dityo at idle
            
    show akasyah at speaking
    voice voice_3_13_199_akasyah
    nd_akasyah_brown "Hah ? Kabur ? Dari hadapan gue ? Ga mungkin ! Ga bakal gua biarin si tua itu kabur dari gua."
    show akasyah at idle
    
    show akasyah at speaking
    voice voice_3_13_200_akasyah
    nd_akasyah_brown "Gimana Dit ? Lu udah nemu belum kelemahannya si Seiya ?"
    show akasyah at idle
    
    show dityo at speaking
    voice voice_3_13_201_dityo
    nd_dityo_brown "Udah. Menurut pengamatanku, Seiya hanya dapat berpindah dari radius 20 meter dari tempat ia terakhir berdiri."
    show dityo at idle
            
    show akasyah at speaking
    voice voice_3_13_202_akasyah
    nd_akasyah_brown "20 meter ? Segitu doang mah bisa gua kejar ! Beraninya si Seiya itu merusak semua rencana gua !"
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