# label start:

label scene_15:

    scene inn ruang_kerja with Dissolve(1.0)

    show yuura scared at left, speaking
    nd_yuura_brown "Ah... Ah..."
    show yuura at idle
     
    nd_narrator_brown "Aku sudah berlari lumayan jauh dari lorong tempat mereka bertarung satu sama lain, aku sedikit heran, mengapa mereka berani untuk bertarung satu sama lain... Karena aku ?"
    
    nd_narrator_brown "Tapi sebelum sempat berpikir lebih jauh, aku merasa ada seorang yang mendekat ke arahku."
    
    show yuura scared at speaking
    nd_yuura_brown "Ahh... Aku capek..."
    show yuura at idle

    nd_narrator_brown "Tiba-tiba aku merasakan ada seseorang yang memelukku dari belakang, dia berbisik pelan di telingaku, suaranya membuat bulu kudukku merinding ketakutan."

    show axia sassy at right, silhouette
    nd_unknown_brown "Anyeeeee kamu ngapain disini sendirian ??"
    
    show yuura at speaking
    nd_yuura_brown "KYAHHHH !"
    show yuura at idle
    
    # play sound perempuan teriak
    nd_narrator_brown "Aku melayangkan tanganku ke arahnya, berharap ia per-"
    
    show yuura at speaking
    nd_yuura_brown "WHAT THE FAHHH ?!"
    
    nd_yuura_brown "(T-TUBUHNYA.. TERBELAH !?)"
    show yuura at idle
    
    nd_narrator_brown "Dia tersenyum kecil sebelum tubuhnya menghilang seperti tertiup angin. Suasana di sekitar menjadi suram hingga entah darimana, dia tiba-tiba muncul kembali di hadapanku."
    
    show axia at right, speaking 
    with dissolve
    nd_axiaregis_brown "Arere ? Kenyapa kamu kaget begituh ?"
    
    nd_axiaregis_brown "Tidak usah takut anyee, ini aku, Axiaregis. Aku di sini untukmu."
    show axia at idle

    nd_narrator_brown "Dia mengulurkan tangannya, membuat diriku semakin takut padanya."
    
    show yuura at speaking
    nd_yuura_brown "Pergi ! PERGI !"
    show yuura at idle
    
    show axia at speaking
    nd_axiaregis_brown "Kenapa kamu selalu mengusirku sih ?"
    
    nd_axiaregis_brown "Apa aku memang tidak berhak ada di sekitarmu ?"
    show axia at idle

    show yuura at speaking
    nd_yuura_brown "M-menjauhlah dariku !"
    show yuura at idle
    
    nd_narrator_brown "Gadis dengan suara om-om itu pun mulai berjalan membelakangiku. Yang entah mengapa, semakin ia menjauh dariku, suasana di sini malah terasa sesak."
    
    show axia at speaking
    nd_axiaregis_brown "Kenapa sihhh harus selalu akuhhh yang pergi ?"
    show axia at idle

    show yuura at speaking
    nd_yuura_brown "Kamu aneh ! Aku sudah lelah dengan semua keanehan ini."
    show yuura at idle
    
    show axia at speaking
    nd_axiaregis_brown "Begitukah ?"
    show axia at idle

    show yuura at speaking
    nd_yuura_brown "Sial ! Keknya aku salah ngomong lagi."
    show yuura at idle
    
    nd_narrator_brown "Gadis itu tiba-tiba tersenyum dan mulai mendekatiku kembali. Dan ketika ia mendekat, suasana di sepanjang lorong ini makin terasa sesak."
    
    show axia at speaking
    nd_axiaregis_brown "Bagaimana nihhh, padahal aku pengen banget main sama kamu."
    
    nd_axiaregis_brown "Kalau bisa... AKU INGIN MEMILIKI MU SELAMANYA !"
    
    nd_axiaregis_brown "Seperti sebuah Standee yang ada di pojok ruangan !"
    
    nd_axiaregis_brown "Memandangiku dan selalu tersenyum padaku !"
    
    nd_axiaregis_brown "Are ? Kamu kenapa berkeringat anyee ? Aku hanya bercanda kok..."
    
    nd_axiaregis_brown "Or... am I ?" # im atau I'm nih?
    show axia at idle

    show yuura at speaking
    show yuura scared at shake
    # show yuura takut shake 
    nd_yuura_brown "*Tersentak"
    show yuura at idle
    
    # CG here
    nd_narrator_brown "Tubuhku tak dapat bergerak tepat setelah menatap mata Axiaregis yang menyala, aku mencoba menggerakkan seluruh anggota tubuh, namun hasilnya nihil. Aku tetap tak bisa bergerak, sementara nafasku perlahan mulai tersengal."
    
    show axia at speaking
    nd_axiaregis_brown "Oh... Anyeeki yang malang~ Aku sungguh kasihan padamu."
    
    nd_axiaregis_brown "Bagaimana jika kamu menyerah saja ?"
    
    nd_axiaregis_brown "Jika kamu menyerah semuanya akan menjadi lebih baik loh~"
    show axia at idle

    menu lawan:
        "Menyerah pada Axiaregis":
            show yuura at speaking
            nd_yuura_brown "A-aku... menyerah !"
            show yuura at idle
            
            show axia at speaking
            nd_axiaregis_brown "Begitukah ? Sayang sekali kamu harus mati kalau begitu..."
            show axia at idle

            show yuura at speaking
            nd_yuura_brown "Hah ? Kenapa begitu ?"
            show yuura at idle
            
            show axia at speaking
            nd_axiaregis_brown "Simple saja, Yuura yang ku kenal tak mungkin menyerah begitu saja"
            
            nd_axiaregis_brown "Selamat tinggal..."
            show axia at idle

            # show black with Dissolve(1.0)
            nd_narrator_brown "Axiaregis menjentikkan jarinya dan membuatku mematung tak bisa bergerak, mataku menjadi blur dan semuanya menjadi tak terlihat lagi. Aku mematung untuk selamanya."
            
            # end?
        "Berontak sekuat tenaga":
            show yuura at speaking
            nd_yuura_brown "ARGhhh Lepas !"
            show yuura at idle
            
            show axia at speaking
            nd_axiaregis_brown "Ihhh anyeee semakin imut deh kalau terus ngelawan kayak gitu."
            
            nd_axiaregis_brown "Tapi sayangnya semuanya akan sia-sia saja."
            show axia at idle

            hide yuura 
            show rian angry at left, silhouette
            nd_unknown_brown "Tidak jika aku membantu ! Aku keluarkan kartuku, {w}Fathanil !!!!"
            
            show axia at speaking
            nd_axiaregis_brown "Huh ?"
            show axia at idle

            # play sound kucing huh
            nd_narrator_brown "Tiba-tiba saja muncul sebuah kudanil besar menabrakkan dirinya yang membuat Axiaregis terpental ke dalam ruangan."
            
            show axia at speaking
            nd_axiaregis_brown "Ah…... Iya-iya si penjaga hewan rupanya..."
            show axia at idle

            show rian at left, speaking
            with dissolve
            nd_rian_brown "Aku bukan penjaga hewan, aku adalah sang petualang yang hanya numpang lewat. Ingat itu !"
            
            nd_rian_brown "Namaku, Rian !"
            show rian at idle

            show axia at speaking
            nd_axiaregis_brown "Ha... Sungguh menyebalkan sekali rasanya."
            
            nd_axiaregis_brown "Padahal aku ingin banget bersama Yuura ku !"
            
            nd_axiaregis_brown "Tapi kamu mengganggu semuanya !"
            show axia at idle

            show rian at speaking
            nd_rian_brown "Nenekku pernah berkata."
            
            nd_rian_brown "Jangan berani kamu lukai hati seorang wanita !"
            
            nd_rian_brown "Kalau kamu tetap melakukannya, maka aku akan menghajarmu !"
            show rian at idle

            show axia at speaking
            nd_axiaregis_brown "Ahhhh berisik berisik berisik!"
            
            nd_axiaregis_brown "Ayo kita bertarung."
            show axia at idle

            show rian at speaking
            nd_rian_brown "Oke, ayo kita duel !"
            show rian at idle

            nd_narrator_brown "Axiaregis menggunakan kekuatannya untuk merubah tempat ini jadi arena battle."
            
            # BG: show duel arena yugioh
            show axia at speaking
            nd_axiaregis_brown "Sekarang giliranku."
            
            nd_axiaregis_brown "Aku Summon Renge dengan attack 300 ke arena !"
            
            nd_axiaregis_brown "Aku aktifkan efeknya! Mengikat kuda nil mu ke posisi bertahan."
            show axia at idle

            show rian at speaking
            nd_rian_brown "Sial... Aku aktifkan efek Fatanil !"
            
            nd_rian_brown "Ketika dia bertahan, Fatanil akan menerima  kerusakan setengah dari musuh."
            show rian at idle

            show axia at speaking
            nd_axiaregis_brown "Tch, aku spesial summon,  Ultimate  Lolibaba, Kanna Kamui !!!!"
            
            nd_axiaregis_brown "Lalu aku akan korbankan Renge dengan menggunakan skill Kanna."
            
            nd_axiaregis_brown "Aku summon, Dragon Kanna ke battlefield !"
            
            nd_axiaregis_brown "Dengan Attack 2500 aku akan menghancurkan kuda nil sialan mu itu !"
            
            nd_axiaregis_brown "Kanna serang dia !"
            show axia at idle

            show rian at speaking
            nd_rian_brown "Sayang sekali... Aku aktifkan kartu ku !"
            
            nd_rian_brown "Panci Emak !"
            
            nd_rian_brown "Dengan panci itu aku menepis serangan naga mu !"
            show rian at idle

            show axia at speaking
            nd_axiaregis_brown "Sialan! Kau selamat kali ini."
            
            nd_axiaregis_brown "Tapi di giliran berikutnya adalah kemenangan ku !"
            show axia at idle

            show rian at speaking
            nd_rian_brown "Mari kita lihat saja, Edy."
            
            nd_rian_brown "Aku akan menyelesaikan ini tanpa kekalahan !"
            
            nd_rian_brown "Draw !"
            
            nd_rian_brown "Keluarlah ! Hiu Jawa !"
            
            nd_rian_brown "Hiu Jawa dengan attack 1000 memiliki efek yang menyeramkan."
            
            nd_rian_brown "Aku aktifkan, Gigi Hiu !"
            
            nd_rian_brown "Dengan menggunakan Gigi Hiu, aku mengurangi attack dari Kanna sebesar 2000."
            
            nd_rian_brown "Dengan begitu aku akan menggunakan kartu spell ku, aktiflah ! FBI !"
            
            nd_rian_brown "Dengan begitu para loli mu akan terkirim ke kuburan."
            
            nd_rian_brown "Lalu aku-"
            show rian at idle

            show axia at speaking
            nd_axiaregis_brown "Ckckck... Tidak secepat itu anak muda."
            
            nd_axiaregis_brown "Aku lakukan Chain Card, dan mengaktifkan{w} Zoo Hunter !"
            
            nd_axiaregis_brown "Dengan begitu semua tipe binatang milikmu akan hancur dan dikirim ke kuburan."
            
            nd_axiaregis_brown "Hahaha... Sekarang bagaimana Rian ? Apakah kamu mau menyerah saja ?"
            
            nd_axiaregis_brown "Karena nasib mu sudah ada di tanganku ! Maka kau sudah tamat."
            show axia at idle

            show rian at speaking
            nd_rian_brown "Jika nasib ku berada di tanganmu, aku akan merebutnya kembali !"
            
            nd_rian_brown "Aktifkan Fatanil dari kuburan !"
            
            nd_rian_brown "Aku akan menggabungkannya dengan Cyber Dragon !"
            
            nd_rian_brown "Datanglah ! Mecha Fatanil !"
            
            nd_rian_brown "Tidak hanya itu saja ! Munculah ! Ksatria Hitam !"
            
            nd_rian_brown "Manusia Kecoa Terbang !"
            
            nd_rian_brown "Dengan Attack 2500 ditambah oleh Mecha Fatanil serangan mereka menjadi 8000 !"
            
            nd_rian_brown "Dengan ini, berakhirlah sudah, Edy !"
            
            nd_rian_brown "Aku akan melawan takdir. Dan aku akan menang !"
            
            nd_rian_brown "Serang !"
            show rian at idle

            nd_narrator_brown "Axiaregis menerima serangan fatal, tapi sayangnya darahnya hanya berkurang setengah."
            
            show axia at speaking
            nd_axiaregis_brown "HAHAHAHA... Kau salah perhitungan bocah !"
            
            nd_axiaregis_brown "Aktifkan Kanna dari kuburan, mengurangi damage yang kuterima jadi setengah."
            
            nd_axiaregis_brown "Sekarang giliranku."
            show axia at idle

            show rian at speaking
            nd_rian_brown "Kata siapa ?"
            show rian at idle

            show axia at speaking
            nd_axiaregis_brown "Tidak mungkin ??"
            show axia at idle

            show rian at speaking
            nd_rian_brown "Aku aktifkan efek dari manusia kecoa terbang."
            
            nd_rian_brown "Menambahkan jumlah serangan yang kamu terima."
            
            nd_rian_brown "Sekarang nyawamu tersisa 2000."
            
            nd_rian_brown "Sebaiknya kamu hitung dosa-dosamu !"
            show rian at idle

            show axia at speaking
            nd_axiaregis_brown "Hahahaha... Dosa? Seharusnya kamu lihat kembali posisimu."
            
            nd_axiaregis_brown "Sekarang giliranku."
            
            nd_axiaregis_brown "Draw !"
            
            nd_axiaregis_brown "Hmmm, aku summon, Senko !"
            
            nd_axiaregis_brown "Dengan munculnya Senko, aku akan menghidupkan kembali..."
            
            nd_axiaregis_brown "Kanna Dragon !"
            
            nd_axiaregis_brown "Lalu serangannya akan menjadi 6000 dengan efek dari Kanna loli di kuburan."
            
            nd_axiaregis_brown "Sekarang kau tak akan bisa berbuat apa-apa... KAU KALAH RI-"
            show axia at idle

            nd_narrator_brown "Rian menarik tanganku dan langsung lari dari hadapan Axiaregis."
            
            show axia at speaking
            nd_axiaregis_brown "TUNGGU ! WOI !"
            
            nd_axiaregis_brown "ANYEEEE JANGAN TINGGALKAN AKU LAGIII !!!"
            
            nd_axiaregis_brown "ANYEEEEEEEEEE !!!"
            show axia at idle

            nd_narrator_brown "Rian terus berlari tanpa peduli dengan teriakan Axiaregis, aku yang masih tidak mengerti dengan mereka hanya bisa diam membisu."
            
            show rian at speaking
            nd_rian_brown "Yuur, aku harap kamu lari sekarang juga."
            show rian at idle

            show yuura at speaking
            nd_yuura_brown "Bagaimana denganmu ? Kenapa kita tidak lari bersama saja ?"
            show yuura at idle
            
            show rian at speaking
            nd_rian_brown "Tidak bisa... Aku harus menghentikan manusia NPD itu."
            
            nd_rian_brown "Tenang saja, aku akan baik-baik saja."
            
            nd_rian_brown "Selama dirimu bisa tersenyum, semuanya akan baik-baik saja."
            
            nd_rian_brown "Jadi... Tersenyumlah ! Dan pergi ke mana pun yang kamu mau."
            
            nd_rian_brown "Karena Yuura yang aku kenal selalu tersenyum."
            show rian at idle

            show yuura at speaking
            nd_yuura_brown "B-baiklah… Tapi kamu hati-hati, oke ? Dia terlalu berbahaya."
            show yuura at idle
            
            show rian at speaking
            nd_rian_brown "Tenang saja... Aku dan pasukan hewanku tak akan kalah !"
            show rian at idle

            nd_narrator_brown "Dia melempar banyak sekali bola dan mengeluarkan seluruh hewan yang ada di penginapan ini."
            
            show rian at speaking
            nd_rian_brown "Larilah ! Si NPD sudah datang !"
            show rian at idle

            nd_narrator_brown "Axiaregis datang dengan kecepatan penuh, dia membawa seluruh pasukan anak kecil yang jumlahnya ada ratusan. Membuatku tak punya pilihan lain selain lari lagi."
            
            nd_narrator_brown "Pada titik ini aku sudah sangat muak, mengapa diriku hanya berlari terus menerus. Apa aku tak bisa melakukan apapun seperti Yuura yang mereka kenal ?"
            
            nd_narrator_brown "Apa aku hanya akan terus seperti ini sampai aku menemukan jalan keluarnya ? Aku sudah sangat lelah dan ingin segera pergi dari tempat ini."

            jump scene_16


    return