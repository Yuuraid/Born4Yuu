# label start:

label scene_16:

    scene inn halaman with Dissolve(1.0)
        # show halaman belakang penginapan 
    nd_narrator_brown "Setelah keluar dari pintu dan berjalan beberapa langkah, langkahku terhenti. Tepat berada di hadapanku, Aergia berdiri dengan raut wajah yang tak dapat kumengerti."
    
        # play music judgment.mp3

    show aergia netral at right, speaking
    nd_aergia_brown "Ahahaha kebetulan banget ketemu lu disini, Yuur... ah... eh.... Sorry gua tau lu tuh ga nyaman kan sama gua sorry ya."
    
    show yuura scared at left, speaking
    nd_yuura_brown "Apa maksu-"
    show yuura at idle

    show aergia furious at speaking
    show aergia at shake
    nd_aergia_brown "DIAM !"
    show aergia sad
    nd_aergia_brown "Ah... Maaf maksudnya bukan... {nw=0.5}"
    show aergia angry
    extend "ARGGGH !"
    show aergia at idle

    nd_narrator_brown "Bentakan nya berhasil membuatku diam seribu bahasa, seperti saat pertama kami bertemu, ia marah karena hal yang tidak kuketahui."
    
        # stop music
        
    show aergia at speaking
    nd_aergia_brown "Cukup ! LU SIAPA !? GUA TAU LU BUKAN YUURA !"
    show aergia at idle

    nd_narrator_brown "Aergia mulai berjalan perlahan ke arahku. Aku ingin membantah pernyataan tersebut, tapi mulutku terbungkam ketika melihat energi-energi hitam mulai muncul di sekitarnya."
    
        # play sound angin
        
    show aergia at speaking
    nd_aergia_brown "Gua tau lu itu bukan Yuura !"
    
    nd_aergia_brown "Yuura yang asli bakal inget sama gua !"
    
    nd_aergia_brown "Yuura bakal peduli sama semua orang yang ada !"
    show aergia at idle
    
    show yuura at speaking
    nd_yuura_brown "Aku buka-"
    show yuura at idle

        # play music elegant boss.m4a
        
    show aergia at speaking
    nd_aergia_brown "BACOT !"
    
    nd_aergia_brown "LU TUH BUKAN SIAPA-SIAPA ! LU BUKAN YUURA !"
    show aergia at idle

    nd_narrator_brown "Gelombang angin berhembus kencang akibat gertakannya, berhasil membuat benda-benda di sekitar berterbangan dari tempatnya."
    
        # play sound barang-barang pecah dan hancur
            
    show yuura at speaking
    nd_yuura_brown "(Sial ! kalau terus begini, aku akan terjebak bersama orang aneh ini...)"
    
    nd_yuura_brown "(Aku harus kabur !)"
    show yuura at idle

        # play sound berpindah
        
    show aergia at speaking
    nd_aergia_brown "Mau ke mana lu ha ??"
    show aergia at idle

    nd_narrator_brown "Aergia mengarahkan tangan dan mencengkram."
    
    nd_narrator_brown "Yuura tersentak akibat tercekik."
    
        # There CG here
    nd_narrator_brown "Tubuhku melayang di udara dengan leherku yang tercekik oleh sesuatu yang tak terlihat, rasanya sangat menyakitkan membuat air mataku keluar. Dia berjalan menghampiriku dengan tatapan anehnya."
    
    show aergia at speaking
    nd_aergia_brown "JAWAB ! DIMANA YUURA !?"
    show aergia at idle
    
    show yuura hurt at speaking
    nd_yuura_brown "Aku... Yuura..."
    show yuura at idle

    show aergia at speaking
    nd_aergia_brown "BANGSAT !"
    
    nd_aergia_brown "DIMANA YUURA !?"
    show aergia at idle

    nd_narrator_brown "Aergia mencengkram leherku lebih kuat, membuat nafasku terputus saat itu juga. Kakiku menendang-nendang di udara, berusaha untuk lari. Namun itu sia-sia,"
    
    nd_narrator_brown "pandanganku mulai kabur..."
    
        # fx blur
        
    show aergia at speaking
    nd_aergia_brown "Tch"
    
    nd_aergia_brown "Ehhh sorry, ngapain gua gtu ke lu, gua tau lu salah tapi kan..."
    
    nd_aergia_brown "Tapi ini kan demi si Yuura ahhhh Yuura--aaaa..."
    show aergia at idle

    nd_narrator_brown "Aergia mengangkat sedikit dan membanting Yuura ke gudang."
    
        # fx stop blur
    # show gudang with shake
        # play sound kayu patah
    nd_narrator_brown "Setelah mencekikku dengan kuat, kini ia menghantamkan diriku ke tanah secara biadab. Sekujur tubuhku kesakitan, belum lagi debu-debu yang berterbangan di sekitarku."
    
    nd_narrator_brown "Tapi ini belum berakhir, Aergia perlahan berjalan ke arahku, aura di sekitarnya semakin menguat. Aku ingin lari... Tapi tubuhku sudah terlalu lemah untuk itu..."
    
    show aergia at speaking
    nd_aergia_brown "BALIKIN YUURA YG GUA KENAL SEKARANG !"
    show aergia at idle

        # aergia memukul Yuura
            
    show yuura at speaking
    show yuura at shake
    nd_yuura_brown "KHAKK..."
    show yuura at idle

    # scene black with fade

    define wipe_kiri = CropMove(0.15, mode="wipeleft")
    define wipe_atas = CropMove(0.15, mode="wipeup")
    define wipe_kanan = CropMove(0.15, mode="wiperight")
    define wipe_bawah = CropMove(0.15, mode="wipedown")
    scene black with fade

    show pe punch purple transparent as p1:
        rotate 50
        yoffset -750
        xoffset -200
    with wipe_kiri
    hide p1
    with Fade(.1, .0, .0)

    show pe punch purple transparent as p2:
        rotate 215
        center
        yoffset 300
        xoffset 0
        zoom 0.7
        flip_image
    with wipe_atas 
    hide p2
    with Fade(.1, .0, .0)

    show pe punch purple transparent as p3:
        rotate 105
        center
        yoffset 300
        xoffset 0
        zoom 0.7
        flip_image
    with wipe_bawah
    hide p3
    with Fade(.1, .0, .0)
    
    show pe punch purple transparent as p4:
        rotate 0
        center
        yoffset 250
        xoffset 100
        zoom 0.6
    with wipe_kiri

    show pe punch purple transparent as p5:
        rotate 10
        center
        yoffset 300
        xoffset -100
        zoom 0.75
        flip_image
    with wipe_kanan

    pause

    nd_narrator_brown "Aergia mulai melancarkan pukulan ke arahku, dengan tenaga yang tersisa, aku mengangkat kedua lenganku, menjadikan mereka sebagai bentuk pertahanan terakhir."

    scene black with fade

    # named
    camera:
        zoom 1.5
        xoffset -960
        yoffset -250
        
    # camera at cam_move

    show pe punch purple transparent as p6:
        rotate 0
        center
        yoffset 150
        xoffset 400
        zoom 0.6
    with wipe_kiri
    camera:
        easein 0.25 zoom 1.25 xoffset -480 yoffset -125

    pause 0.25
    
    show pe punch purple transparent as p7:
        rotate 25
        center
        yoffset 300
        xoffset 0
        zoom 0.8
        flip_image
    with wipe_bawah

    camera:
        easein 0.5 zoom 1.0 xoffset 0 yoffset 0

    pause 0.5

    show pe punch purple transparent as p8:
        rotate 150
        center
        yoffset 500
        xoffset -350
        zoom 1
    with wipe_atas
    
    nd_narrator_brown "Pukulan demi pukulan dilancarkan olehnya, makin lama pukulannya makin cepat dan lebih menyakitkan, aku hanya bisa menerima pukulan, aku sudah tidak ada kekuatan untuk melawan balik..."
    
    # stop music
    scene black with fade

    nd_aergia_brown "Balikin ga ? BALIKIN !"

    show pe punch purple transparent as p9:
        rotate 0
        center
        yoffset 150
        xoffset 100
        zoom 0.6
    with wipe_kiri

    show pe punch purple transparent as p10:
        rotate 0
        center
        yoffset 200
        xoffset -100
        zoom 0.6
        flip_image
    with wipe_kanan
    # play sound sweeping blow

    nd_narrator_brown "Tinju itu, nampaknya akan segera menghantam wajah ku..."

    scene black with fade

    nd_narrator_brown "Seberharga itukah Yuura di mata mereka... Sialan... Kenapa ini selalu terjadi padaku..."
    
    # play music trigger
    # show dawam angry at silhouette
    # with dissolve
    nd_unknown_brown "Hal yang kau perbuat itu sungguh menjijikan."
    
    nd_narrator_brown "Tiba-tiba seseorang melayangkan tendangan ke arah Aergia."
    
    nd_narrator_brown "Aergia dengan sigap mundur menghindari tendangan Dawam."
    
    show aergia hurt at center, zorder 2
    with dissolve
    show pe swing dawam
    with wipe_kiri
    show aergia at shake
    hide pe swing dawam
    with dissolve
    pause .5
    nd_aergia_brown "Bacot emangnya lu tau apa ?"
    show aergia at idle

    image white = Solid("#ffffff")

    transform swipe_kiri:
        xpos 0 ypos 0
        size (960, 1080)
        easein 1.0 xpos -960

    transform swipe_kanan:
        xpos 960 ypos 0
        size (960, 1080)
        easein 1.0 xpos 1920

    scene white
    
    show black as kiri at swipe_kiri
    show black as kanan at swipe_kanan
    pause 1.0
    hide kiri
    hide kanan

    show dawam angry at center, silhouette
    with dissolve
    nd_narrator_brown "Ketika mataku kembali terbuka, samar-samar aku melihat sosok tinggi dan besar sedang membelakangiku, dia... melindungiku ?"
    
    show dawam at silhouette
    nd_unknown_brown "Maaf atas keterlambatanku, nyonya Yuura"
        
    show yuura at speaking
    nd_yuura_brown "Kau..."
    show yuura at idle
            
    show dawam at speaking
    with dissolve
    nd_dawam_brown "Aku kesini atas perintah langsung Tuan Muda Maharaja Risol FRB."
    show dawam at idle
    
    show yuura at speaking
    nd_yuura_brown "Risol..."
    show yuura at idle

    nd_narrator_brown "Meski ingin tahu siapa sosok yang ingin membantuku, tubuhku terlalu lemah untuk menanyakan hal tersebut. Penglihatanku mulai menghitam dan akhirnya kesadaranku pun mulai menghilang."
    
    scene black with eye_close

    # should we make a black scene or transition for Yuura POV or what??
    
    show aergia at speaking
    nd_aergia_brown "Kenapa kalian lagi, kalian lagi."
    
    nd_aergia_brown "Udah sering lupain gua sekarang kalian lindungun ni orang ?"
    show aergia at idle
            
    show dawam at speaking
    nd_dawam_brown "Itu bukan urusanku, misi ku di sini hanya karena Tuan Muda Maharaja Risol FRB."
    
    nd_dawam_brown "Yang terpenting adalah... Selesaikan perintah... Tanpa adanya kesalahan."
    show dawam at idle
    
    scene inn gudang outside 
    with Dissolve(1.0)

    show dawam angry at left
    with dissolve
    show dawam:
        ease .5 right
    pause .5
    hide dawam 
    with wiperight

    scene black with dissolve
    show pe swing dawam
    with wipe_kiri
    pause .5
    hide pe swing dawam
    with dissolve
    # pause .5

    scene inn gudang outside
    with Dissolve(0.5)
    # pause .5
    show aergia hurt at right, flip_image
    pause .5
    show aergia:
        ease .5 left 
        shake
    pause 
    # There are CG here
    nd_narrator_brown "Dawam langsung berpindah dengan cepat dan segera melayangkan tendangan ke arah Aergia yang membuatnya terdorong beberapa meter meski tidak melukainya."

    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

    scene pe dash negative_blue
    with flashbulb
    # camera:
    #     linear .5 rotate 45
    scene black with Fade(0.2, 0.0, 0.5)
    show pe punch yellow 0 transparent:
        center rotate 45 yoffset 500
    with wipe_kiri
    nd_narrator_brown "Tapi tak berhenti disana, Dawam sudah berada di depannya ketika kepulan debu memudar dan segera memberikan uppercut padanya yang membuatnya terpental."
    
    nd_narrator_brown "Meski begitu, serangan itu nampaknya malah jadi pemicu bagi Aergia, energi di sekitarnya makin menjadi-jadi, terlebih lagi ia melayang yang di mana hal itu mungkin dapat mempengaruhi Dawam."
    
    transform matrix_sketch:
        matrixcolor InvertMatrix(1.0) * SaturationMatrix(0.0) * TintMatrix("#d0d8d0") * ContrastMatrix(1.0)

    scene inn halaman
    with matrix_sketch
    show aergia at speaking
    nd_aergia_brown "Kenapa... Kenapa !!! KENAPA !?"
    
    nd_aergia_brown "Gua tahu bahwa gua ga pantes disini ! TAPI KENAPA !"
    
    nd_aergia_brown "ARGHHH MATI LU SEMUA !!!"
    show aergia at idle

    # There are CG here
    nd_narrator_brown "Serangan proyektil hitam mulai bertebaran mengarah langsung ke Dawam. Meski demikian, Dawam menerjang ke arah proyektil-proyektil tersebut sembari menepis beberapa dari proyektil itu..."
    
    nd_narrator_brown "Ketika ingin memusatkan serangan ke arah Dawam, Aergia terkejut ketika Dawam menghilang begitu saja dari pandangan nya."
    
    nd_narrator_brown "Tepat ketika dia sedang kebingungan, Aergia merasakan ada seseorang yang tepat berada di belakangnya, tapi ia tak sempat untuk membalikkan badannya saat itu juga."
                
    show dawam at speaking
    nd_dawam_brown "Dasar lalat pengganggu !"
    show dawam at idle
    
    show aergia at speaking
    nd_aergia_brown "Hahaha, iya lalat ya... TERUS KENAPA KALAU GW LALAT."
    show aergia at idle

    # CG here
    nd_narrator_brown "Dawam menghantamkan kedua tangannya ke arah Aergia, Aergia melindungi dirinya dengan menyelimuti tubuhnya dengan energi di sekitarnya, ia membuat pelindung tepat sebelum menghantam tanah akibat hantaman dari Dawam yang begitu cepat."
    
    nd_narrator_brown "Dawam mendarat dengan selamat setelah melancarkan serangan serangan udara yang bukan keahliannya. Meski begitu, ia tetap waspada sambil memperhatikan jelas kabut debu yang kian memudar."
    
    # play sound tanah retak
    nd_narrator_brown "Dawam terkejut dan melompat dari tempat ia berdiri."
    
    nd_narrator_brown "Semburan api ungu yang keluar dari tanah dengan kuatnya diikuti semburan-semburan api lainnya, memaksa Dawam untuk berpindah."
    
    nd_narrator_brown "Belum sempat menyentuh tanah, Aergia muncul dari kepulan debu, memberikan pukulan telak yang segera ditahan oleh Dawam dengan kedua lengannya sebelum terpental beberapa kaki dari tempat ia pertama kali mendarat."
    
    nd_narrator_brown "Tepat ketika mendarat, sebuah pusaran energi melesat mengarah tepat padanya. Sebelum sempat mengenai tubuhnya, Dawam menepuk kedua tangannya, menghasilkan gelombang angin yang sanggup memecah pusaran energi."
    
    show aergia at speaking
    nd_aergia_brown "BAJINGAN ! Berhenti ganggu gw sat !"
    show aergia at idle

    # aku ga ngerti line ini mksdnya gmn
    # SFX dan kamera ??
    nd_narrator_brown "Dawam segera membalikkan badan sembari melancarkan serangan pada Aergia. Tetapi diluar dugaan, lengan dan kaki Dawam terikat oleh energi hitam itu dengan kuatnya, sedangkan Aergia masih jauh beberapa meter dari tempat Dawam terikat."
                
    show dawam at speaking
    nd_dawam_brown "Keuugh..."
    show dawam at idle
    
    show aergia at speaking
    nd_aergia_brown "Bahkan pas lu lawan orang bodo kaya gua aja lu kalah ?"
    
    nd_aergia_brown "Atau lu nya aja yg lebih bodo ?"
    show aergia at idle

    nd_narrator_brown "Aergia menghentakkan kakinya, energi hitam mulai mengalir seperti air ke arah Dawam. Tepat ketika sudah berada di dekatnya, gundukan tanah yang sudah dialiri oleh energi melesat tepat ke ulu hati Dawam yang membuatnya sontak terkejut akibat serangan tersebut."
    
    nd_narrator_brown "Tak berhenti di sana, gundukan tanah kedua melesat tepat ke arah dagu Dawam yang membuat dia terpental jauh saking kuatnya."
    
    nd_narrator_brown "Aergia berjalan dengan sebuah bola energi yang berputar di telapak tangannya,"
    
    nd_narrator_brown "ketika debu-debu di tempat jatuhnya Dawam memudar, tampak Dawam terduduk sembari tersenyum dengan darah segar yang mengalir dari mulutnya."
    
    show aergia at speaking
    nd_aergia_brown "Tch"
    
    nd_aergia_brown "Haa... Udahlah, nyerah aja. Buat apa sih bangkit lagi kalau endingnya sama aja."
    show aergia at idle

    nd_narrator_brown "Dawam berdiri sembari menyeka luka di wajah."
                
    show dawam at speaking
    nd_dawam_brown "Maaf saja... Tapi kupastikan kali ini akan jauh lebih menyenangkan !"
    show dawam at idle
    
    # play sound kretek tangan
    # stop music
    jump scene_17
    
    return