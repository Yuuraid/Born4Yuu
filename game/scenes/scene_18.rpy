# label start:

label scene_18:
    scene inn backyard with Dissolve(1.0)
    # play music trigger
    nd_narrator_brown "Aku terbangun dan mendengar suara samar, ketika aku mencoba untuk duduk, aku melihat Dawam dan Aergia yang masing-masing diantara mereka telah menyiapkan kuda-kuda, sudah jelas itu merupakan serangan pengakhiran untuk mengakhiri pertempuran panjang mereka."
    show aergia angry at right, shake, speaking
    voice voice_3_18_584_aergia
    nd_aergia_brown "Mati aja lu."
    show aergia at idle
    show dawam angry at left, speaking
    voice voice_3_18_585_dawam
    nd_dawam_brown "Sesuai dengan permintaanmu !"
    show dawam at idle
    nd_narrator_brown "Tepat disaat itu, sebuah perasaan aneh mengalir kuat didalam tubuhku. Entah mengapa tubuhku yang sebelumnya dihajar habis-habisan dapat dengan mudahnya berdiri seperti tak terjadi apa-apa sebelumnya"
    
    nd_narrator_brown "Aku berlari ke tengah-tengah pertarungan, untuk menghentikan hal tak ada gunanya ini."
    # play sound melangkah
    show dawam at speaking
    show dawam at shake
    show aergia at speaking
    show aergia at shake
    voice voice_3_18_586_aergia
    voice voice_3_18_587_dawam
    nd_narrator_brown "ARRGGGHH !!!" #aergia and dawam scream
    # play sound lesatan cepat
    show aergia at idle
    show dawam at idle
    nd_narrator_brown "..."
    # play sound dentingan jam dinding
    show aergia at shake
    show dawam at shake
    nd_narrator_brown "Aergia dan Dawam terkejut."
    # stop music
    # play music jade bottle
    
    nd_narrator_brown "Aku menangkap tangan mereka masing-masing dengan tanganku, dalam sekejap menghentikan semua serangan pamungkas mereka tanpa sisa."
    show yuura angry at center, idle
    show dawam at speaking
    voice voice_3_18_588_dawam
    nd_dawam_brown "Y-yuura ?"
    show dawam at idle
    show yuura at speaking
    show yuura at shake
    nd_yuura_brown "{size=+20}CUKUP !{/size}"
    show yuura at idle
    show aergia at speaking
    voice voice_3_18_590_aergia
    nd_aergia_brown "Minggir, Yuur !"
    show aergia at idle
    show yuura at speaking
    nd_yuura_brown "{size=+20}Aku bilang CUKUP !{/size}"
    
    nd_yuura_brown "Kalian mau ngelanjutin ini sampai kapan sih ? Sampai penginapan ini hancur ?"
    show yuura at idle
    show aergia at speaking 
    voice voice_3_18_593_aergia
    nd_aergia_brown "Emang lu tau apa sih ? Lu itu kan bukan Yuura." 
    show aergia at idle
    show yuura at speaking
    show yuura at shake
    nd_yuura_brown "{size=+20}YA TERUS KENAPA ?{/size}"
    
    nd_yuura_brown "APA AKU BUKAN YUURA ? KARENA AKU DARI DUNIA YANG BERBEDA ?"
    show yuura at idle
    show aergia at speaking
    voice voice_3_18_596_aergia
    nd_aergia_brown "T-tapi Yuur..."
    show aergia at idle
    show yuura netral at speaking
    nd_yuura_brown "Aer..."
    
    nd_yuura_brown "Maaf yah, kalo aku selalu lupa akan dirimu."
    show yuura at idle
    show aergia at speaking
    voice voice_3_18_599_aergia
    nd_aergia_brown "A-apaan sih !"
    
    voice voice_3_18_600_aergia
    nd_aergia_brown "Lagian siapa gua sampe bisa diinget orang-orang."
    show aergia at idle
    show yuura at speaking
    nd_yuura_brown "Kata siapa ?"
    show yuura happy
    nd_yuura_brown "Aer, kita adalah keluarga. Jangan selalu merasa bahwa dirimu sendirian di dunia ini."
    
    nd_yuura_brown "Tak peduli seperti apapun dirimu, kamu sudah berusaha yang terbaik."
    show yuura at idle
    show aergia sad at speaking
    voice voice_3_18_604_aergia
    nd_aergia_brown "Yuura..."
    show aergia furious
    voice voice_3_18_605_aergia
    nd_aergia_brown "Alah nyocot doang, lu kira bakalan mem-"
    show aergia sad
    voice voice_3_18_606_aergia
    nd_aergia_brown "Eh iya makasih ya..."
    show aergia at idle
    nd_narrator_brown "Aergia menangis dan mulai menyadari bahwa dirinya tidak sendirian lagi."
    show yuura at speaking
    nd_yuura_brown "Dawam... Maaf ya aku bikin kamu terluka."
    show yuura at idle
    show dawam at speaking
    voice voice_3_18_608_dawam
    nd_dawam_brown "Gapapa Anee, ini semua adalah tugas yang diperintahkan oleh pak bos."
    show dawam at idle
    show yuura at speaking
    nd_yuura_brown "Ga... Itu adalah keinginanmu sendiri."
    
    nd_yuura_brown "Gausahlah nurutin si Risol-Risol itu, jadilah dirimu sendiri. Karena kamu adalah Yuuraid."
    show yuura at idle
    show dawam sad at speaking
    voice voice_3_18_611_dawam
    nd_dawam_brown "Anee..."
    show dawam at idle
    hide aergia with dissolve
    hide dawam with dissolve
    nd_narrator_brown "Aku mengelus kepalanya dengan lembut, sebelum meninggalkan mereka berdua. Aku berlari menuju tempat pertarungan lainnya."

    show yuura at speaking
    show yuura at shake
    nd_yuura_brown "EDY !"
    show yuura at idle
    nd_narrator_brown "Axiaregis yang sedang fokus bertarung terkejut karena mendengar nama panggilannya."
    voice voice_3_18_613_axiaregis
    nd_axiaregis_brown "A-anee ???"
    show layer master at shake
    nd_narrator_brown "Axiaregis sekali lagi ditabrak oleh kuda nil, membuatnya terjatuh tepat di hadapan diriku."
    show axia hurt at jump_in_right(duration=1.0), idle
    pause 2.0
    show rian angry at left, speaking
    voice voice_3_18_614_rian
    nd_rian_brown "Edy, maaf... Aku ga sengaja."
    
    voice voice_3_18_615_rian
    nd_rian_brown "Loh ? Anee ?"
    show rian at idle
    show yuura at speaking, zorder 5
    nd_yuura_brown "Rian, kerja bagus !"
    show yuura at idle
    nd_narrator_brown "Aku mengelus kepala Rian, membuatnya senang seperti anak kecil."
    show yuura at speaking
    nd_yuura_brown "Maaf ya, Edy... Aku berbuat jahat padamu."
    
    nd_yuura_brown "Tapi lain kali tolong jangan kayak gitu lagi."
    show yuura at idle
    nd_narrator_brown "Aku memeluk Axiaregis dan menenangkan dirinya. Membuat dia perlahan mulai menyadari kesalahannya."
    show axia at right, speaking
    voice voice_3_18_619_axiaregis
    nd_axiaregis_brown "Aneeeee... Maafiiin akuuuu."
    show axia at idle
    show yuura at speaking
    nd_yuura_brown "Iya, aku maafin kok."
    show yuura at idle
    show axia at speaking
    voice voice_3_18_621_axiaregis
    nd_axiaregis_brown "Huaaaaaa aku cinta kamu Aneee."
    show axia at idle
    nd_narrator_brown "Aku mengelus Axiaregis dan membuatnya menangis sangat kencang dalam pelukanku."
    
    nd_narrator_brown "Setelah puas mengeluarkan semua emosinya, Axiaregis dan Rian menawarkan dirinya untuk membantu dalam menyelesaikan masalah lainnya."
    show yuura at speaking
    nd_yuura_brown "Tidak, biar aku saja yang menyelesaikannya."
    
    nd_yuura_brown "Dimana Akasyah dan lainnya ?"
    show yuura at idle
    show axia at speaking
    voice voice_3_18_624_axiaregis
    nd_axiaregis_brown "Di sana Anee."
    
    voice voice_3_18_625_axiaregis
    nd_axiaregis_brown "Tapi kamu yakin, Anee ? Mereka berdua berbahaya."
    show axia at idle
    show rian at speaking
    voice voice_3_18_626_rian
    nd_rian_brown "Betul kata Edy, Anee. Sebaiknya kami membantu."
    show rian at idle
    show yuura at speaking
    nd_yuura_brown "Tidak apa, biar aku saja."
    
    nd_yuura_brown "Terima kasih banyak, tolong jaga diri kalian."
    show yuura at idle
    hide rian with dissolve
    hide axia with dissolve
    nd_narrator_brown "Aku pergi dengan grappling hook dan melesat ke arah pertempuran berikutnya."
    # stop music
    # play music pursuit ver 2
    hide yuura
    show akasyah hurt at left, speaking
    show seiya hurt at right, idle
    show akasyah at shake
    voice voice_3_18_629_akasyah
    nd_akasyah_brown "SEIYAAAAA !!"
    show akasyah at idle
    show seiya at speaking
    show seiya at shake
    voice voice_3_18_630_seiya
    nd_seiya_brown "AKASYAHHH !!"
    # play sound cartoonish punch
    show seiya at idle
    nd_narrator_brown "Sebelum mereka berhasil menyerang satu sama lain, aku langsung berdiri di antara keduanya. Menghentikan serangan mematikan yang mereka."
    show akasyah at speaking
    show akasyah at shake
    voice voice_3_18_631_akasyah
    nd_akasyah_brown "LU NGAPAIN SIH, YUUR !"
    
    voice voice_3_18_632_akasyah
    nd_akasyah_brown "GANGGU BANGET, LAGI SERU JUGA."
    
    voice voice_3_18_633_akasyah
    nd_akasyah_brown "MINGGIR GA? ATAU LU..."
    show akasyah at idle
    # stop music
    # play music awkward yoyu
    
    nd_narrator_brown "Aku melempar sebuah minuman berlabel Yoyu kepada Akasyah."
    show yuura happy at center, speaking
    nd_yuura_brown "Nih, kuganti yang sebelumnya."
    
    nd_yuura_brown "Maaf yah, aku malah bikin kamu marah."
    
    nd_yuura_brown "Sini-sini, aku peluk."
    show yuura at idle
    show akasyah angry at speaking
    voice voice_3_18_637_akasyah
    nd_akasyah_brown "Apaan sih, Yuur. Lu kira gua anak kecil ?"
    show akasyah netral at idle
    nd_narrator_brown "Akasyah meminum Yoyu yang diberikan dan mulai sedikit tenang."
    show seiya netral at speaking
    voice voice_3_18_638_seiya
    nd_seiya_brown "Apa yang terjadi padamu, Anee ?"
    
    voice voice_3_18_639_seiya
    nd_seiya_brown "Bukankah, kamu seperti orang yang berbeda sekarang ?"
    show seiya at idle
    show yuura at speaking
    nd_yuura_brown "Memang ya, Seiya ini."
    
    nd_yuura_brown "Mau yang tadi atau sekarang, aku tetaplah Yuura, bukan ?"
    show yuura at idle
    show seiya at speaking
    voice voice_3_18_642_seiya
    nd_seiya_brown "Hahaha...ya... Kamu benar."
    # stop music
    # play music pursuit ver 2
    # play sound angin berhembus sepoi sepoi
    show seiya at idle
    nd_narrator_brown "Sebuah roket meluncur ke arah kami yang sedang mengobrol."
    
    voice voice_3_18_643_akasyah
    nd_akasyah_brown "Yuur !!!"
    hide seiya 
    hide akasyah 
    hide yuura 
    # sink sprite ?
    nd_narrator_brown "Akasyah melompat untuk menyelamatkan diriku, dia menjadikan dirinya sebagai tameng hidup demi diriku. Beruntung Seiya berhasil memindahkan roket itu sebelum hal buruk terjadi."
    show dityo angry at left, speaking
    voice voice_3_18_644_dityo
    nd_dityo_brown "Aduh sorry, ga sengaja kelempar ke sini."
    
    voice voice_3_18_645_dityo
    nd_dityo_brown "Kalian gapapa kan ?"
    show dityo netral at idle
    show yuura happy at center, speaking, zorder 5
    nd_yuura_brown "Dityo !"
    show yuura at idle
    nd_narrator_brown "Aku menghampiri Dityo dan memberikannya sebuah alat yang aku rusak siang tadi."
    show yuura at speaking
    nd_yuura_brown "Ini, aku berhasil memperbaikinya."
    
    nd_yuura_brown "Maaf, aku mendorong dirimu dan tanpa sengaja dan bertindak kasar padamu."
    show yuura at idle
    show dityo at speaking
    voice voice_3_18_649_dityo
    nd_dityo_brown "Anee..."
    show dityo at idle
    show shark hurt at right, speaking
    voice voice_3_18_650_shark
    nd_shark_brown "Kalian gapapa kan ?"
    show shark at speaking
    voice voice_3_18_651_shark
    nd_shark_brown "L-loh Anee ?"
    show shark at idle
    show yuura at speaking
    nd_yuura_brown "Shark, kamu gapapa ?"
    show yuura at idle
    show shark at speaking
    voice voice_3_18_653_shark
    nd_shark_brown "A-aman aja Anee, luka begini doang mah kecil."
    show shark at idle
    nd_narrator_brown "Aku menarik tangannya dan melihat luka yang ada disana. Aku mengoleskan sebuah salep di luka tersebut, untuk membuatnya menjadi lebih baik."
    # stop music
    # play music awkward
    show shark at speaking
    voice voice_3_18_654_shark
    nd_shark_brown "A-ane ???"
    show shark at idle
    show yuura at speaking
    nd_yuura_brown "Lebih baik ?"
    show yuura at idle
    show shark at speaking
    voice voice_3_18_656_shark
    nd_shark_brown "I-iya..."
    show shark at idle
    show yuura at speaking
    nd_yuura_brown "Makasih ya, udah ngelindungin aku."
    
    nd_yuura_brown "Kamu imut deh."
    show yuura at idle
    show shark at speaking
    voice voice_3_18_659_shark
    nd_shark_brown "D-dihh...  Diem deh..."
    show shark at idle
    # stop music
    # play music scene 4
    
    nd_narrator_brown "Aku tertawa kecil karena merasa sangat senang menjahili dirinya. Semua orang yang tadi sedang beristirahat menghampiriku."
    hide dityo
    show aergia netral at left, speaking
    voice voice_3_18_660_aergia
    nd_aergia_brown "Yuur, lu gapapa ?"
    show aergia at idle
    hide shark
    show axia netral at right, speaking
    voice voice_3_18_661_axiaregis
    nd_axiaregis_brown "Anee gapapah ?"
    show axia at idle
    hide aergia
    show dawam netral at left, speaking
    voice voice_3_18_662_dawam
    nd_dawam_brown "Anee gapapa ?"
    show dawam at idle
    hide axia
    show rian netral at right, speaking
    voice voice_3_18_663_rian
    nd_rian_brown "Aneeki aman ?"
    hide rian
    hide dawam
    show yuura scared at speaking
    nd_yuura_brown "Maaf..."
    show yuura sad at idle
    nd_narrator_brown "Air mataku mulai turun seraya tubuhku mulai terduduk lemas."
    show yuura at speaking
    nd_yuura_brown "Maaf..."
    
    nd_yuura_brown "Maaf aku ga bisa jadi Yuura yang kalian kenal."    
    
    nd_yuura_brown "Maaf bahwa aku berubah."
    
    nd_yuura_brown "Maaf kalau aku selalu mengecewakan para Yuuraid."
    
    nd_yuura_brown "Maaf."
    
    nd_yuura_brown "Maaf..."
    hide yuura
    show aergia angry at left, speaking
    voice voice_3_18_671_aergia
    nd_aergia_brown "Apaan dah lu tuh ga salah, harusnya gua yang minta maaf."
    
    voice voice_3_18_672_aergia
    nd_aergia_brown "Coba aja kalau gua ga goblok maaf ya, Yuur."
    show aergia at idle
    show axia sassy at right, speaking
    voice voice_3_18_673_axiaregis
    nd_axiaregis_brown "Apaan, ini semua salahku, Anee."
    
    voice voice_3_18_674_axiaregis
    nd_axiaregis_brown "Karena aku semuanya jadi kayak gini."
    show axia at idle
    hide aergia
    show dityo sad at left, speaking
    voice voice_3_18_675_dityo
    nd_dityo_brown "Ga, ini semua salahku..."
    
    voice voice_3_18_676_dityo
    nd_dityo_brown "Seandainya aku lebih sabar mungkin ga bakal kayak gini."
    show dityo at idle
    show akasyah smug at center, speaking
    voice voice_3_18_677_akasyah
    nd_akasyah_brown "Au, lu pada ngapain coba kayak gitu ?"
    show akasyah at idle
    show dityo at speaking
    show dityo at shake
    voice voice_3_18_678_dityo
    show axia at speaking
    show axia at shake
    voice voice_3_18_679_axiaregis
    
    nd_narrator_brown "{size=+20}Kamu juga.{/size}" # dityo dan aergia
    hide dityo
    show axia at idle
    show aergia netral at left, speaking
    voice voice_3_18_680_aergia
    nd_aergia_brown "Lu juga."
    show aergia at idle
    nd_narrator_brown "Mereka mulai bertengkar lagi di hadapanku, membuatku yang menangis menjadi tertawa."
    hide akasyah
    show yuura happy at center, speaking, zorder 5
    nd_yuura_brown "Emang yah, Yuuraid itu aneh banget hahaha."
    show yuura at idle
    hide aergia
    show akasyah smug at left, speaking
    voice voice_3_18_682_akasyah
    nd_akasyah_brown "Nah gitu dong, Yuur ! Ketawa hehe."
    show akasyah at idle
    nd_narrator_brown "Mereka semua memelukku, mengingatkan kembali kehangatan yang selama ini aku inginkan."
    
    nd_narrator_brown "Memang benar, bahwa diriku bukanlah Yuura yang sebelumnya. Tapi aku tetaplah Yuura, dan mereka tetaplah Yuuraid."
    
    nd_narrator_brown "Yang perlu kami lakukan adalah memulai kembali semuanya dibalik kekacauan yang aneh ini."
    
    nd_narrator_brown "Kesalahpahaman sering terjadi, kecerobohan adalah hal yang biasa. Tapi yang pasti kami adalah keluarga, dan tak ada yang bisa melupakan fakta itu."
    jump scene_19

    return