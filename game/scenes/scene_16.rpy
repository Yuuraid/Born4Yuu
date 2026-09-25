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
    init python:
        def wipe_bawah(time=0.15):
            return CropMove(time, mode="wipedown")

        def wipe_atas(time=0.15):
            return CropMove(time, mode="wipeup")

        def wipe_kanan(time=0.15):
            return CropMove(time, mode="wiperight")

        def wipe_kiri(time=0.15):
            return CropMove(time, mode="wipeleft")
    # define wipe_kiri = CropMove(0.15, mode="wipeleft")
    # define wipe_atas = CropMove(0.15, mode="wipeup")
    # define wipe_kanan = CropMove(0.15, mode="wiperight")
    # define wipe_bawah = CropMove(0.15, mode="wipedown")
    scene black with fade

    show pe punch purple transparent as p1:
        rotate 50
        yoffset -750
        xoffset -200
    with wipe_kiri(.15)
    hide p1
    with Fade(.1, .0, .0)

    show pe punch purple transparent as p2:
        rotate 215
        center
        yoffset 300
        xoffset 0
        zoom 0.7
        flip_image
    with wipe_atas(.15)
    hide p2
    with Fade(.1, .0, .0)

    show pe punch purple transparent as p3:
        rotate 105
        center
        yoffset 300
        xoffset 0
        zoom 0.7
        flip_image
    with wipe_bawah(.15)
    hide p3
    with Fade(.1, .0, .0)
    
    show pe punch purple transparent as p4:
        rotate 0
        center
        yoffset 250
        xoffset 100
        zoom 0.6
    with wipe_kiri(.15)

    show pe punch purple transparent as p5:
        rotate 10
        center
        yoffset 300
        xoffset -100
        zoom 0.75
        flip_image
    with wipe_kanan(.15)

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
    with wipe_kiri(.15)
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
    with wipe_bawah(.15)

    camera:
        easein 0.5 zoom 1.0 xoffset 0 yoffset 0

    pause 0.5

    show pe punch purple transparent as p8:
        rotate 150
        center
        yoffset 500
        xoffset -350
        zoom 1
    with wipe_atas(.15)
    
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
    with wipe_kiri(.15)

    show pe punch purple transparent as p10:
        rotate 0
        center
        yoffset 200
        xoffset -100
        zoom 0.6
        flip_image
    with wipe_kanan(.15)
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
    with wipe_kiri(.15)
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
        ease .3 right
    pause .3
    hide dawam 
    with wipe_kanan(.35)
    # pause

    scene black with Dissolve(.25)
    show pe swing dawam
    with wipe_kiri(.15)
    pause .5
    hide pe swing dawam
    with Dissolve(.1)
    # pause .5

    scene inn gudang outside
    with Dissolve(0.5)
    # pause .5
    show aergia hurt at right, flip_image
    pause .15
    show aergia:
        ease .15 left 
        shake
    pause 
    # There are CG here
    nd_narrator_brown "Dawam langsung berpindah dengan cepat dan segera melayangkan tendangan ke arah Aergia yang membuatnya terdorong beberapa meter meski tidak melukainya."

    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')

    scene pe dash negative_blue:
        zoom 1.0
        truecenter
        ease 1.0 zoom 1.5 rotate 15
    with flashbulb
    # camera:
    #     linear .5 rotate 45
    scene black with Fade(0.2, 0.0, 0.5)
    show pe punch yellow 0 transparent:
        center rotate 45 yoffset 500
    with wipe_kiri(.15)
    nd_narrator_brown "Tapi tak berhenti disana, Dawam sudah berada di depannya ketika kepulan debu memudar dan segera memberikan uppercut padanya yang membuatnya terpental."
    
    nd_narrator_brown "Meski begitu, serangan itu nampaknya malah jadi pemicu bagi Aergia, energi di sekitarnya makin menjadi-jadi, terlebih lagi ia melayang yang di mana hal itu mungkin dapat mempengaruhi Dawam."

    transform matrix_sketch:
        matrixcolor InvertMatrix(1.0) * SaturationMatrix(0.0) * TintMatrix("#d0d8d0") * ContrastMatrix(1.0)

    show inn gudang outside 
    with Dissolve(.5)

    pause 1.0

    define circleirisout = ImageDissolve("assets/effects/partial_effects/imagedissolve circleiris.png", 1.0, 8)

    show inn gudang outside at matrix_sketch 
    with circleirisout

    show aergia at speaking
    nd_aergia_brown "Kenapa... Kenapa !!! KENAPA !?"
    
    nd_aergia_brown "Gua tahu bahwa gua ga pantes disini ! TAPI KENAPA !"
    
    nd_aergia_brown "ARGHHH MATI LU SEMUA !!!"
    show aergia at idle

    # There are CG here

    scene pe red_projectile full_CG
    # camera:
    #     zoom 2 
    # with wipe_kiri(.05)
    # pause .1
    # camera:
    #     zoom 2 xpos -1920 ypos -1080
    # with wipe_kanan(.05)
    # pause .1
    # camera:
    #     zoom 2 xpos 0 ypos -1080
    # with wipe_kiri(.05)
    # pause .1
    # camera:
    #     zoom 2 xpos -1920 ypos 0
    # with wipe_kanan(.05)
    # pause .1 
    # camera:
    #     zoom 1 xpos 0 ypos 0
    # with wipe_kiri(.05)
    camera:
        zoom 2 
    with Dissolve(.15)
    pause .1
    camera:
        zoom 2 xpos -1920 ypos -1080
    with Dissolve(.15)
    pause .1
    camera:
        zoom 2 xpos 0 ypos -1080
    with Dissolve(.15)
    pause .1
    camera:
        zoom 2 xpos -1920 ypos 0
    with Dissolve(.15)
    pause .1 
    camera:
        zoom 1 xpos 0 ypos 0
    with Dissolve(.15)
    pause .5
    nd_narrator_brown "Serangan proyektil hitam mulai bertebaran mengarah langsung ke Dawam."
    scene pe dash negative_blue
    pause .5
    # zoom + rotate nya masih blm bisa
    camera:
        truecenter
        ease 1.0 zoom 1.34 rotate 12 
    pause
    
    scene black with dissolve
    camera:
        truecenter
        zoom 1.0 rotate 0
        # rotate 0 xoffset 125 yoffset 100

    show pe punch yellow transparent as p11:
        truecenter zoom 0.75 xoffset 150 
    with wipe_kiri(.15)
    # camera:
    #     easein 0.25 zoom 1.25 xoffset -480 yoffset -125

    show pe punch yellow 0 transparent as p12:
        truecenter zoom 1.25 rotate 260 xoffset -200 
    with wipe_bawah(.15)

    # camera:
    #     easein 0.5 zoom 1.0 xoffset 0 yoffset 0

    show pe punch yellow transparent as p13:
        truecenter zoom 1 rotate 150 xoffset -400 
    with wipe_atas(.15)
    pause

    nd_narrator_brown "Meski demikian, Dawam menerjang ke arah proyektil-proyektil tersebut sembari menepis beberapa dari proyektil itu..."
    scene inn gudang outside
    with Dissolve(.25)
    camera:
        zoom 1.5 xoffset 300
        ease 5.0 xoffset 400

    show aergia full_angry:
        zoom .45
        center 
        flip_image
        yanchor .79
        xoffset -200

    show aergia zorder 2:
        ease 5.0 xoffset -510
    pause 1.0

    show pe red_projectile ball_0 transparent zorder 1 as a1:
        xoffset -500
        zoom .5 yoffset 200
        linear .25 xoffset 4000
    pause .2

    show pe red_projectile ball_0 transparent zorder 3 as a2:
        xoffset -500
        zoom .5 yoffset 500
        linear .25 xoffset 4000
    pause .2

    show pe red_projectile ball_0 transparent zorder 3 as a3:
        xoffset -500
        zoom .5 yoffset 400
        linear .25 xoffset 4000
    pause .2

    show pe red_projectile ball_0 transparent zorder 1 as a4:
        xoffset -500
        zoom .5 yoffset 300
        linear .25 xoffset 4000
    pause .2

    show pe red_projectile ball_0 transparent zorder 3 as a5:
        xoffset -500
        zoom .5 yoffset 550
        linear .25 xoffset 4000
    pause .2

    show pe red_projectile ball_0 transparent zorder 1 as a6:
        xoffset -500
        zoom .5 yoffset 350
        linear .25 xoffset 4000
    pause .2

    show pe red_projectile ball_0 transparent zorder 3 as a7:
        xoffset -500
        zoom .5 yoffset 250
        linear .25 xoffset 4000
    pause .2
    
    show pe red_projectile ball_0 transparent zorder 3 as a8:
        xoffset -500
        zoom .5 yoffset 450
        linear .25 xoffset 4000
    pause .2

    show pe red_projectile ball_0 transparent zorder 3 as a9:
        xoffset -500
        zoom .5 yoffset 550
        linear .25 xoffset 4000
    pause .2

    show pe red_projectile ball_0 transparent zorder 1 as a10:
        xoffset -500
        zoom .5 yoffset 350
        linear .25 xoffset 4000
    pause .2

    show pe red_projectile ball_0 transparent zorder 3 as a11:
        xoffset -500
        zoom .5 yoffset 250
        linear .25 xoffset 4000
    pause .2
    
    show pe red_projectile ball_0 transparent zorder 3 as a12:
        xoffset -500
        zoom .5 yoffset 450
        linear .25 xoffset 4000
    pause .2

    show pe red_projectile ball_0 transparent zorder 1 as a13:
        xoffset -500
        zoom .5 yoffset 200
        linear .25 xoffset 4000
    pause .2

    show pe red_projectile ball_0 transparent zorder 3 as a14:
        xoffset -500
        zoom .5 yoffset 500
        linear .25 xoffset 4000
    pause .2

    show pe red_projectile ball_0 transparent zorder 3 as a15:
        xoffset -500
        zoom .5 yoffset 400
        linear .25 xoffset 4000
    pause .2

    show pe red_projectile ball_0 transparent zorder 1 as a16:
        xoffset -500
        zoom .5 yoffset 300
        linear .25 xoffset 4000
    pause .2

    pause 1.0
    hide aergia
    
    show dawam full_angry:
        zoom .45
        center 
        yanchor .79
        xoffset 200
        ease .5 xoffset 600

    camera:
        zoom 1.5 xoffset -400
    with wipe_kiri(.5)

    hide dawam
    with wipe_kanan(.5)
    pause .5
    
    transform cin_atas:
        xpos 0 ypos -360
        size (1920, 360)
        easein 1.0 ypos 0
    
    transform cin_bawah:
        xpos 0 ypos 1080
        size (1920, 360)
        easein 1.0 ypos 720

    transform cin_out_atas:
        xpos 0 ypos 0
        size (1920, 360)
        easein .5 ypos -360

    transform cin_out_bawah:
        xpos 0 ypos 720
        size (1920, 360)
        easein .5 ypos 1080
        
    camera:
        ease .5 xoffset 0

    scene inn gudang outside:
        xoffset 230
        matrix_sketch
    
    show black as atas at cin_atas
    show black as bawah at cin_bawah

    show aergia full_angry:
        zoom .45
        center 
        flip_image
        yanchor .8
        xoffset -80
    with moveinleft


    pause .5
    
    show inn gudang outside:
        ease .5 xoffset 320

    show aergia:
        ease .5 xoffset -80

    nd_narrator_brown "Ketika ingin memusatkan serangan ke arah Dawam, Aergia terkejut ketika Dawam menghilang begitu saja dari pandangan nya."

    show inn gudang outside:
        ease .5 zoom 1.25 xoffset -220 yoffset -175

    show aergia zorder 1:
        ease .35 yoffset 550 zoom .8 xoffset -280

    pause .5
    show dawam full_angry zorder 2:
        xoffset -1000 zoom .8 yanchor .01
        silhouette
        ease .25 xoffset -210
     
    nd_narrator_brown "Tepat ketika dia sedang kebingungan, Aergia merasakan ada seseorang yang tepat berada di belakangnya, tapi ia tak sempat untuk membalikkan badannya saat itu juga."
    scene black
    camera:
        truecenter zoom 1.0
    nd_dawam_brown "Dasar lalat pengganggu !"
    
    nd_aergia_brown "Hahaha, iya lalat ya... TERUS KENAPA KALAU GW LALAT."

    # CG here
    show pe punch yellow 0 transparent as b1:
        truecenter
        rotate 20
    with wipe_bawah(.15)

    show pe punch yellow 0 transparent as b2:
        truecenter
        yoffset -200
        rotate 20
        flip_image
    with wipe_bawah(.15)

    nd_narrator_brown "Dawam menghantamkan kedua tangannya ke arah Aergia"
    scene pe dash blue:
        zoom 1.0
        truecenter 
        ease 1.0 zoom 1.5 rotate 15
    pause 1.0

    scene inn gudang outside:
        truecenter
        zoom 1.65 xoffset 270
    
    pause .1
    show inn gudang outside:
        ease .5 xoffset 320
    pause .1
    show aergia full_angry:
        flip_image
        truecenter zoom .675 xoffset 200
        ease .5 xoffset -600 yoffset 300
        linear 0.05 xoffset -615
        linear 0.05 xoffset -585
        linear 0.05 xoffset -610
        linear 0.05 xoffset -590
        linear 0.05 xoffset -600
    with dissolve

    nd_narrator_brown "Aergia melindungi dirinya dengan menyelimuti tubuhnya dengan energi di sekitarnya, ia membuat pelindung tepat sebelum menghantam tanah akibat hantaman dari Dawam yang begitu cepat."

    scene inn gudang outside:
        truecenter
        zoom 1.65 xoffset -270
    
    pause .1
    show inn gudang outside:
        ease .5 xoffset -600
    pause .1
    show dawam full_angry:
        truecenter zoom .675 xoffset 200
        ease .5 xoffset 550 yoffset 300
        linear 0.05 xoffset 565
        linear 0.05 xoffset 545
        linear 0.05 xoffset 560
        linear 0.05 xoffset 540
        linear 0.05 xoffset 550
    with wipe_kanan(.5)


    nd_narrator_brown "Dawam mendarat dengan selamat setelah melancarkan serangan serangan udara yang bukan keahliannya." 
    define irisoutdawam = ImageDissolve("assets/effects/fade.png", 1.0, 8)

    show inn gudang outside:
        ease 1.0 zoom 2.0 xoffset -600
    show inn gudang outside at matrix_sketch 
    # ----------------------- PERLU DI FIXX------------------
    with irisoutdawam
    show dawam:
        matrixcolor TintMatrix("#ffffff")
        ease 1.0 zoom 1.0 yoffset 700 xoffset 200 matrixcolor TintMatrix("#000000")

    nd_narrator_brown "Meski begitu, ia tetap waspada sambil memperhatikan jelas kabut debu yang kian memudar."
    
    hide dawam full_angry
    with dissolve
    
    show black as atas at cin_atas
    show black as bawah at cin_bawah
    
    pause 1.5
    
    show dawam full_angry:
        truecenter
        xoffset 1920 
        yoffset 700
        ease .35 xoffset 500
    # with moveinright
    pause .5
    nd_narrator_brown "------!!!!"
    
    # play sound tanah retak
    show black as atas at cin_out_atas
    # pause
    show black as bawah at cin_out_bawah
    pause 1.0
    hide atas
    hide bawah
    
    show dawam:
        ease .5 yoffset 700 
    show inn gudang outside:
        linear .5 matrixcolor TintMatrix("#ffffff")
    with circleirisout
    pause 1.0

    show dawam:
        linear .05 yoffset 710
        linear .05 yoffset 700
        linear .05 yoffset 710
        linear .05 yoffset 700
        linear .05 yoffset 620
    show inn gudang outside:
        linear .05 yoffset 20
        linear .05 yoffset 0
        linear .05 yoffset 20
        linear .05 yoffset 0
        linear .05 yoffset 180
        linear .5 yoffset 0
    pause .1
    hide dawam with dissolve
    pause .5
    show pe purple_flame flame_front as f1:
        zoom .75 yoffset 160 xoffset 1000
    show pe purple_flame flame_behind as f2:
        zoom .75 yoffset 160 xoffset 750
    show pe purple_flame flame_front as f3:
        zoom .75 yoffset 160 xoffset 500
    show pe purple_flame flame_full as f4:
        zoom .75 yoffset 160 xoffset 250
    show pe purple_flame flame_front as f5:
        zoom .75 yoffset 160 xoffset 0
    show pe purple_flame flame_behind as f6:
        zoom .75 yoffset 160 xoffset -1000
    show pe purple_flame flame_front as f7:
        zoom .75 yoffset 160 xoffset -750
    show pe purple_flame flame_full as f8:
        zoom .75 yoffset 160 xoffset -500
    show pe purple_flame flame_behind as f9:
        zoom .75 yoffset 160 xoffset -250
    with Dissolve(.5)
    nd_narrator_brown "Semburan api ungu yang keluar dari tanah dengan kuatnya diikuti semburan-semburan api lainnya, memaksa Dawam untuk berpindah."
    
    scene pe dash blue:
        truecenter
        zoom 1.0
        ease .5 zoom 1.6 rotate -20

    pause 1.5
    scene black:
        truecenter
        zoom 1.0
    pause
    show pe punch purple transparent as d1:
        truecenter zoom .65 rotate 270 xoffset -200 yoffset -100
    show pe punch purple transparent as d2:
        truecenter zoom .65 xoffset -200 yoffset -100
        flip_image
    with wipe_kanan(.25)

    hide d1 
    hide d2 
    with Fade(.25, .0, .0)

    show pe punch swipe transparent as d3:
        truecenter
    with wipe_kiri(.25)

    nd_narrator_brown "Belum sempat menyentuh tanah, Aergia muncul dari kepulan debu, memberikan pukulan telak yang segera ditahan oleh Dawam dengan kedua lengannya sebelum terpental beberapa kaki dari tempat ia pertama kali mendarat."
    
    show aergia at speaking
    nd_aergia_brown "BAJINGAN ! Berhenti ganggu gw sat !"
    show aergia at idle

    scene inn gudang outside:
        truecenter
        zoom 1.65 xoffset -270
    
    pause .1
    show inn gudang outside:
        ease .5 xoffset -600
    pause .1
    show dawam full_angry:
        truecenter zoom .675 xoffset 200
        ease .5 xoffset 600 yoffset 300
        linear 0.05 xoffset 615
        linear 0.05 xoffset 585
        linear 0.05 xoffset 610
        linear 0.05 xoffset 590
        linear 0.05 xoffset 600
    with wipe_kanan(.5)
    
    nd_narrator_brown "Dawam segera membalikkan badan sembari melancarkan serangan pada Aergia. Tetapi diluar dugaan, lengan dan kaki Dawam terikat oleh energi hitam itu dengan kuatnya, sedangkan Aergia masih jauh beberapa meter dari tempat Dawam terikat."

    scene inn gudang outside:
        truecenter
        zoom 1.65 xoffset 250
        # ease 5.0 xoffset 400
    with Dissolve(.25)

    show aergia full_psycho:
        zoom .75
        center 
        flip_image
        yoffset 400
        truecenter

    pause 

    init python:
        renpy.add_layer("effects", above="master")


    label gokil:
        show pe particle ring transparent as z1 onlayer effects:
            truecenter
            zoom .5 
            rotate 270
            yoffset 100 xoffset 400
            ease 5.0 xoffset -200 

        show pe particle ring transparent as z2 onlayer effects:
            truecenter
            zoom .4 
            rotate 270
            yoffset 100 xoffset 500
            ease 5.0 xoffset -150

        show pe particle ring transparent as z3 onlayer effects:
            truecenter
            zoom .3 
            rotate 270
            yoffset 100 xoffset 600
            ease 5.0 xoffset -100
        
        show aergia:
            ease 5.0 xoffset -510
        
        show inn gudang outside:
            ease 5.0 xoffset 450

        with { "effects": wipe_atas(5.0) }
        pause 5.0

    pause 
    hide z1
    hide z2
    hide z3
    scene pe red_blast full_CG:
        truecenter 
        flip_image
        zoom 1.75 xoffset -720 yoffset -405
    with wipe_kanan(1.0)

    pause 1.0

    show pe red_blast full_CG:
        linear .75 zoom 1.0 xoffset 0 yoffset 0

    nd_narrator_brown "Tepat ketika mendarat, sebuah pusaran energi melesat mengarah tepat padanya."

    scene black with fade

    show pe punch yellow 0 transparent as s1 with wipe_kiri(.15):
        truecenter rotate 12 yoffset -200
    show pe punch yellow 0 transparent as s2 with wipe_kanan(.15):
        truecenter
        flip_image rotate 22 yoffset -200

    pause

    scene pe red_blast full_CG at flip_image
    with Dissolve(1.0)

    pause 

    scene inn gudang outside:
        truecenter zoom 1.75 xoffset -650 yoffset 175
    show dawam angry at right
    
    show inn gudang outside:
        linear .5 xoffset -600 yoffset 150
        linear .5 xoffset -600 yoffset 150
        linear .5 xoffset -600 yoffset 150
        linear .5 xoffset -600 yoffset 150

    nd_narrator_brown "Sebelum sempat mengenai tubuhnya, Dawam menepuk kedua tangannya, menghasilkan gelombang angin yang sanggup memecah pusaran energi."
    
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