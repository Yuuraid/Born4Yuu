# label start:


label scene_10:

    show ruang tamu with Dissolve(1.0)
    # play music jade bottle fadein
    "Aku berlari tanpa melihat ke belakang, tak peduli dengan pertengkaran mereka berdua. Saat ini yang paling penting adalah keselamatanku."
    "Meskipun aku sudah lolos dari mereka berdua. Nyatanya, dunia tidak seindah itu. Aku menabrak om-om yang tadi mengejarku. Ternyata dia sudah memperhitungkan jalur pelarianku dengan alatnya."
    u "Mau kemana kamu Anee ?"
    u "Aku kan udah bilang kamu ga bakal bisa pergi dariku..."
    y "Apasih ! Minggir ! Aku sudah muak banget ya sama kalian semua ! Dari pagi dikejar-kejar mulu"
    u "T-tapi Anee, bukannya--"
    # show yuura shake ??
    y "DIEM !"
    "Aku memukul tangan Dityo dan bikin mahakaryanya jatuh."
    # y "DIEM ! (Aku memukul tangan Dityo dan bikin mahakaryanya jatuh.)"
    y "Ah..."
    u "..."
    u "Kenapa ne ?{w} Kenapa kamu jadi seperti ini ?{w} Ini bukan seperti Anee yang kukenal..."
    u "Yuura yang kukenal tidak akan langsung merusak barang orang lain ! Dia orang yang baik, penyayang."
    # show dityo marah with shake ??
    u "BUKAN ORANG YANG KASAR KAYAK GINI !"
    # show yuura with shake ??
    # stop music
    # play music foto mantan fadein(1.0)
    menu:
        "A. Marahin":
            $ dityo_route = "Bad end"
            y "APA SIH ! ORANG DARI AWAL JUGA KAMU YANG NGEJAR-NGEJAR AKU ! KENAPA SEMUA MALAH JADI AKU YANG SALAH !"
            # show yuura panik
            # show dityo serius
            u "Jadi menurut kamu ini salah aku ? SALAHKU ? APA ANEE KIRA BIKIN KAYAK GINI GAMPANG ?"
            # show dityo marah with shake
            u "KAMU DENGAN MUDAHNYA NGANCURIN MAHAKARYAKU ??"
            u "Kalo bukan kamu yang minta juga aku ga mungkin bikin alat ini !"
            "Dityo pergi tanpa berkata-kata. Dia meninggalkan semua barangnya dan tidak pernah kembali lagi ke penginapan."

        "B. Minta maaf":
            $ dityo_route = "Good end"
            y "A-aku beneran ga sengaja... Sumpah, aku tadi  niatnya cuma mau bikin kamu ngejauh bukan buat ngancurin karya yang kamu buat."
            
            u "..."
            y "Sumpah aku ga sengaja... A-aku beneran minta maaf..."
            "Aku ingat sebelumnya orang ini ada di buku tamu, namanya Dityo."
            y "Maaf, Dityo..."
            dityo "Entahlah Anee... Aku capek banget... Bisakah kamu biarkan aku sendiri ?"
            y "Iya... Sekali lagi aku minta maaf, Dityo..."
            "Dityo berdiam diri, dia terdiam mematung tanpa berkata-kata lagi."
            # hide dityo with fade
    # stop music 
    # play music rock fadein
    "Aku melanjutkan perjalananku di lantai ke-2, sepanjang lorong itu aku selalu melihat hal-hal janggal."
    "Aku melihat sebuah foto kebakaran dari gedung ini, yang entah mengapa aku merasakan kemarahan melihat foto ini."
    "Entah apa yang terjadi tiba-tiba ada seseorang menepuk pundakku, orang itu mirip perempuan namun suaranya laki-laki."
    "Mendengar suaranya saja membuat bulu kudukku langsung berdiri, dia dengan sangat percaya diri memelukku erat."
    
    # Axiaregis section 
    axia "HAWOOOO ANYEEE, KAMU LAGI APAAA ? IHHH SENENG BANGET DEH RASANYA KETEMU ANYEE DI SINI."
    y "(Orang ini kayaknya Axiaregis deh, sesuai deskripsi di buku tamu.)"
    axia "Kok kamu diam ajaaah anyee ??? Kamu terpaku yah sama diriku yang imut ini ? Iya kan ? KAAANNN ???"
    axia "KYAAAH ANYEEE"
    "Mendengar itu, membuat merasa jijik sekaligus kesal melihat tingkah orang ini. Aku segera mempercepat langkah kaki ku untuk pergi menghindarinya. Tapi entah mengapa, dia bergerak lebih cepat."
    axia "ANYEEE, KAMU TAU GA ??? PASTI GA TAU KAN ? SAMAAA AKU JUGA GA TAUUUU, TAPI YANG PASTI AKUU IMUTTTT"
    axia "ANYEE KAMU KOK DIEM AJA SIH ??? PASTI TERPAKU KAN SAMA AKU ? IYA KAN? KANNN ? AKU IMUT KAN ???"
    axia "IHH KOK KAMU MAKIN CEPET SIHHHH ? AKU KAN JADI MAKIN SUKA ANYEEEEEE GEMESINN BANGET SIHHH MUAHH"
    # show yuura panik
    axia "DIEM !"
    "Aku mendorongnya jatuh dan dengan lebaynya Axiaregis terjatuh."
    axia "Kyaahhh, anyee kamu kok jahat banget sihhh sama akyuuu ??"
    axia "Kamu tega banget ihhh padahal aku udah syantik, imut, dan manish giniii. Masa dengan teganya kamu dorong akuuuu ahhh~ hidoiii."
    y "DIEM ANJENG KUPUKUL-PUKULIN JUGA YA KAMU !"
    axia "Kyaahhh anyeee kasarrr, tolonggg ah~ anyeeki mau mukul akyuhhh"
    "Semua orang menatapku, membuatku panik dengan orang yang sangat banyak, aku berusaha untuk lari, tapi sayangnya aku terkepung oleh banyak orang."
    "Aku yang sudah terpojok dan tidak bisa melakukan apapun hanya bisa pasrah, sebelum akhirnya aku melihat ekor ikan hiu muncul. Dia menerobos banyak orang dengan kecepatan yang cukup tinggi."
    shark "Aneee !!!"
    shark "Pegangan yang erat !"
    y "Oi !!! Pelan-pelan !!"
    "Aku melesat dengan Shark pergi dari lorong itu."
    axia "Hmph ! Beraninya hiu kecil ituh mengganggu rencanakuh ! Awas kamu yah ! IHHH KECOAKKKK !!! EWWWW."
    "Dari kejauhan aku mendengar suara teriakan menjijikan itu, tapi aku sudah tidak peduli lagi. Aku sudah lelah dengan semua hal aneh di tempat ini."
    shark "A-aneeki gapapa ?"
    y "APAAN SIH INI TEMPAT ?! KENAPA COBA BANYAK BANGET KEANEHAN DI SINI ??! TADI OM-OM LAH, TERUS PEREMPUAN AYNG SUARANYA LAKI-LAKI LAH"
    y "SEKARANG APA LAGI ? SEEKOR HIU ?? BISAKAH TEMPAT INI NORMAL DIKIT GITU ?!"
    shark "T-tapi anee, i-inikan tempatmu sendiri."
    y "DIEM !"
    "Shark terdiam."
    shark "..."
    # play music foto-foto kenangan
    menu:
        "A. Pergi":
            $ shark_route = "Bad end"
            y "Pergi"
            shark "T-tapi anee..."
            y "PERGI !! AKU UDAH CAPEK DENGAN SEMUA INI !"
            shark "..."
            "Shark pergi meninggalkanku dan tidak pernah muncul lagi dalam kehidupanku."

        "B. Sebenarnya... Aku ini siapa sih... Kenapa semua orang seperti ini...":
            $ shark_route = "Good end"
            y "Sebenarnya... Aku ini siapa sih... Kenapa semua orang seperti ini..."
            shark "A-anee... Jangan nangis, a-aku tau i-ini sangat berat untuk anee, t-tapi a-aku yakin anee bisa kok ngelewatin semuanya."
            # show yuura nangis
            # play sound hiks
            y "*hiks"
            shark "Sini anee ikut aku sebentar."
            "Aku ditarik menuju sebuah papan besar di lantai 2. Shark dengan hati-hati mengeluarkan sebuah foto dari papan besar itu."
            shark "I-ini anee, kamu inget ini ga ?"
            "Aku menggelengkan kepalaku pelan."
            y "A-aku ga terlalu inget"
            # scene black with dissolve(1.0)
            # show yuura at center with dissolve(1.0)
            y "(AHHH BODOH BANGET HARUSNYA AKU PURA PURA TAU)"
            "Aku melihat sebuah foto di taman gedung ini dengan beberapa orang yang tidak aku kenali."
            shark "Anee... Kamu tau ga...?"
            shark "Aku memang anak baru di sini, tapi tiap kali ada acara pasti kamu ngajak aku untuk ikut."
            shark "Entah itu karaoke sampai mabuk, atau ya sekadar pesta aja."
            shark "T-tapi bukannya gimana-gimana ya...em...cuma suaranya anee itu bagus banget..."
            shark "Dan anee juga imut...terus em...ahh banyak deh Yuura."
            y "Hm ? Ahahaha... Kamu lucu deh."
            shark "A-apasih ! Diem deh lu, Yuur."
            y "Tch tsundere."
            shark "A-apaan sih ! Udah deh, yang penting sekarang udah tenangkan ?"
            y "Ya... Terima kasih Shark... Kusudah lebih baik sekarang."
            y "Tapi sepertinya aku masih butuh udara segar, Shark."
            shark "K-kalo gitu boleh ga aku antar kamu ?"
            y "Gapapa, aku bisa sendiri, sekali lagi terima kasih."
            "Aku berjalan pergi meninggalkan lorong-lorong menuju pintu teras."

    return