# label start:

label scene_17:

    play music bgm_scene3_pria_asing volume 1.0 loop

    scene inn ruang_tamu_1 
    camera:
        zoom 1.0
        # xalign 0.0
        # yalign 0.0
        truecenter
        xoffset 0
        yoffset 0
    show yuura hurt at left, idle
    show pria netral at right, idle
    with eye_open
    # play music pria asing

    nd_narrator_brown "Sementara itu di tempat yang tidak diketahui, aku terbangun tepat di hadapan seseorang yang pernah kutemui di dalam hutan."
    show yuura hurt at left, speaking
    nd_you_brown "Di mana aku? Kenapa aku di sini?"
    show yuura at idle
    
    show pria happy at right, speaking
    voice voice_3_17_411_pria_misterius
    wd_unknown_brown "Ah.. sang putri tidur sudah bangun"
    
    voice voice_3_17_412_pria_misterius
    wd_unknown_brown "Selamat datang kembali di rumah."
    show pria at idle

    show yuura at face_flip
    pause 0.2
    show yuura at custom_sprite_pos(x=-0.2) with ease

    nd_narrator_brown "Aku mundur beberapa langkah setelah mendengar suara itu."

    show pria at speaking
    voice voice_3_17_413_pria_misterius
    wd_unknown_brown "Kenapa? Kaget banget lihat aku"
    
    voice voice_3_17_414_pria_misterius
    wd_unknown_brown "Bukannya kamu yang ngajak? Untuk minum teh bersama?"
    show pria at idle

    show yuura netral at speaking
    nd_you_brown "Minum teh?"
    show yuura at idle
    nd_narrator_brown "Aku melihat sekeliling dan mendapati diriku berada di kamar tempat pertama kali aku bangun, tapi suasananya jauh berbeda dari sebelumnya."
    
    nd_narrator_brown "Belum lagi peralatan minum serta pria asing yang tiba-tiba ada di kamar ini membuatnya jadi lebih membingungkan."
    
    show yuura at speaking
    nd_you_brown "(Tunggu... Bukannya aku sebelumnya berada di halaman belakang tempat ini...)"
    
    nd_you_brown "Bagaimana aku bisa di sini?"
    
    nd_you_brown "Apa yang terjadi? Bukankah tadi ada pertarungan?"
    show yuura at idle

    show pria eff_laugh_y
    nd_narrator_brown "Pria itu tertawa kecil."

    show pria happy none at speaking
    voice voice_3_17_419_pria_misterius
    wd_unknown_brown "Pertarungan? Yang mana?" 
    
    voice voice_3_17_420_pria_misterius
    wd_unknown_brown "Bukankah kita disini untuk membicarakan dirimu?"
    show pria at idle

    show yuura at speaking
    nd_you_brown "Diri...ku???"
    show yuura at idle
    
    show pria at speaking
    voice voice_3_17_422_pria_misterius
    wd_unknown_brown "Iya… aku ingin membicarakan soal dirimu."
    show pria at idle

    show yuura at speaking
    nd_you_brown "Hah?"
    show yuura at idle

    nd_narrator_brown "Yuura menggelengkan kepala ke samping."
    
    nd_narrator_brown "Aku sedikit bingung melihat tingkah pria asing itu, membuatku semakin mempertanyakan apa maksud dari semua ini."
    
    show pria at speaking
    voice voice_3_17_424_pria_misterius
    wd_unknown_brown "Langit benar-benar sudah menentukan takdirnya sendiri."
    
    voice voice_3_17_425_pria_misterius
    wd_unknown_brown "Sudah banyak sekali takdir yang tertulis, namun hanya satu yang benar."
    
    voice voice_3_17_426_pria_misterius
    wd_unknown_brown "Sekarang giliranmu, Aneki."
    show pria at idle

    play sound sfx_spit_water
    show layer master at shake

    show pria netral_wet
    show yuura scared
    nd_narrator_brown "Yuura menyemburkan teh yang baru ia teguk."
    
    nd_narrator_brown "..."

    show yuura eff_sweat_w
    show yuura at speaking
    nd_you_brown "Ah maaf..."
    show yuura none at idle

    show pria at speaking
    voice voice_3_17_428_pria_misterius
    wd_unknown_brown "Hahahaha… tidak terduga bukan?"
    show pria at idle

    play sound sfx_finger_snap
    show white
    pause 0.2
    show pria happy
    hide white with dissolve

    nd_narrator_brown "Pria itu menjentikkan jari nya dan seketika sisa-sisa teh yang ada di tubuhnya lenyap seperti tak terjadi apa-apa."

    show yuura eff_sweat_w at speaking
    nd_you_brown "Bagaimana..."
    show yuura none at idle

    show pria at speaking
    voice voice_3_17_430_pria_misterius
    wd_unknown_brown "Kita tidak fokus kesana sekarang."
    
    voice voice_3_17_431_pria_misterius
    wd_unknown_brown "Takdirmu sudah ditentukan dari awal."
    
    $ renpy.run(QuickSave())

    voice voice_3_17_432_pria_misterius
    wd_unknown_brown "Sekarang ini adalah waktunya untuk kamu memilih."
    show pria at idle

    # stop music
    menu siap:
        "Apa maksudmu?":
            $ renpy.sound.set_volume(0.0, channel="memories")
            # play music bgm_scene3_pria_asing volume 1.0 loop
            show yuura at speaking
            nd_you_brown "Apa maksudmu?"
            show yuura at idle

            show pria at speaking
            voice voice_3_17_451_pria_misterius
            wd_unknown_brown "Tidak apa, biar aku tunjukkan sesuatu untukmu."
            show pria at idle
            
            play sound sfx_finger_snap
            scene whiteroom 
            show yuura scared at custom_sprite_pos(x=-0.2), idle, face_flip
            show pria happy at right, idle
            with Flash

            nd_narrator_brown "Pria itu menjentikkan jarinya dan membuat kami langsung berpindah menuju sebuah ruangan putih yang tak aku kenali sama sekali."
            # play sound zupp
            # show ruang putih
            show yuura eff_sweat_w at speaking
            nd_you_brown "D-di mana kita sekarang?"
            show yuura none at idle

            show pria eff_laugh_y at speaking
            voice voice_3_17_453_pria_misterius
            wd_unknown_brown "Kita ada di dalam pusat alam bawah sadarmu."
            show pria at idle

            show yuura at speak_in_mind
            nd_you_brown "!?"
            show yuura at idle
            
            nd_narrator_brown "Pria itu tertawa kecil."

            show pria none at speaking
            voice voice_3_17_455_pria_misterius
            wd_unknown_brown "Semakin aku lihat kamu semakin imut saja"
            show pria at idle

            show yuura at speaking
            nd_you_brown "Berhenti bercanda sekarang juga! Apa sih yang ingin kamu sampaikan?"
            show yuura at idle

            show pria at speaking
            voice voice_3_17_457_pria_misterius
            wd_unknown_brown "Kenapa terlalu terburu-buru seperti itu?"

            voice voice_3_17_458_pria_misterius
            wd_unknown_brown "Apa kamu tidak nyaman berbicara denganku?"
            show pria at idle

            show yuura angry eff_yelling at speaking
            nd_you_brown "DIEM!"
            show yuura none at idle

            show pria eff_laugh_y at speaking
            voice voice_3_17_460_pria_misterius
            wd_unknown_brown "Hahaha memang dirimu tidak pernah berubah ya, Aneeki."

            $ renpy.sound.set_volume(0.0, channel="memories")

            voice voice_3_17_461_pria_misterius
            wd_unknown_brown "Selalu saja terburu-buru, apalagi soal sake."

            show pria happy none
            show yuura netral
            
            show vid_memory_mabok behind yuura:
                blur 25
            with Dissolve(2.0)

            $ renpy.sound.set_volume(0.0, channel="memories")

            voice voice_3_17_462_pria_misterius
            wd_unknown_brown "Apa kamu ingat? Ketika hari itu kamu pulang dengan satu buah box berisi sake?"
            # show pria at idle
            
            # nd_narrator_brown "Tiba-tiba saja muncul penglihatan di ruangan putih itu mengenai kenangan ketika aku berpesta dengan mereka. Canda dan tawa terdengar jelas di telingaku, seakan-akan aku masuk ke dalamnya."

            hide vid_memory_mabok with Dissolve(2.0)
            show vid_memory_singging behind yuura:
                blur 25
            with Dissolve(2.0)

            $ renpy.sound.set_volume(0.0, channel="memories")

            show pria at speaking
            voice voice_3_17_463_pria_misterius
            wd_unknown_brown "Kita bernyanyi dari pagi, tanpa memikirkan apakah besok kita punya kegiatan atau tidak."
            
            hide vid_memory_singging with Dissolve(2.0)
            show vid_memory_sake behind yuura:
                blur 25
            with Dissolve(2.0)

            $ renpy.sound.set_volume(0.0, channel="memories")

            voice voice_3_17_464_pria_misterius
            wd_unknown_brown "Kamu bahkan yang paling lantang dalam mengajak kami semua minum."
            
            hide vid_memory_sake with Dissolve(2.0)
            show vid_memory_people_laugh behind yuura:
                blur 25
            with Dissolve(2.0)

            $ renpy.sound.set_volume(0.0, channel="memories")

            voice voice_3_17_465_pria_misterius
            wd_unknown_brown "Rasanya sangat menyenangkan bukan? Melihat mereka tertawa dan tersenyum."
            show pria at idle

            camera:
                zoom 2.0
                xalign 0.15
                yalign 0.45
            show yuura at speaking
            nd_you_brown "Aku... Tidak mengerti..."
            show yuura at idle

            camera:
                zoom 1.0
                xalign 0.5
                yalign 0.5

            hide vid_memory_people_laugh with Dissolve(0.5)
            
            show pria at speaking
            voice voice_3_17_467_pria_misterius
            wd_unknown_brown "Tidak apa, tidak semua hal harus dipahami."
            
            voice voice_3_17_468_pria_misterius
            wd_unknown_brown "Tapi rasakanlah kenangannya dalam benakmu."
            show pria at idle

            show yuura at speaking
            nd_you_brown "..."
            
            nd_you_brown "Aku..."
            show yuura at idle

            show pria at speaking
            voice voice_3_17_471_pria_misterius
            wd_unknown_brown "Tidak perlu memaksakan dirimu,{w=3.57} aku..{w=2} tidak— {w=1}KITA akan siap membantumu selalu."
            
            voice voice_3_17_472_pria_misterius
            wd_unknown_brown "Bagaimana jika kita lanjut saja?"
            show pria at idle

            show vid_memory_reading behind yuura:
                blur 25
            with Dissolve(2.0)

            $ renpy.sound.set_volume(0.0, channel="memories")
            # CG here
            nd_narrator_brown "Pria itu menampilkan sebuah momen ketika aku membacakan sebuah cerita pada mereka, pembawaanku yang tadinya kasar dan beringas menjadi sangat lembut."
            
            nd_narrator_brown "Mereka terlihat nyaman mendengar suaraku yang menenangkan hati, membuat mereka perlahan tertidur pulas."
            
            show pria at speaking
            voice voice_3_17_473_pria_misterius
            wd_unknown_brown "Suara yang indah dan menenangkan."
            
            voice voice_3_17_474_pria_misterius
            wd_unknown_brown "Bahkan dunia pun terlelap mendengar suaranya."
            
            voice voice_3_17_475_pria_misterius
            wd_unknown_brown "Dongeng yang selalu dibuat oleh teman-teman."
            
            voice voice_3_17_476_pria_misterius
            wd_unknown_brown "Dan dibacakan oleh panda merah yang mereka sayangi."
            
            voice voice_3_17_477_pria_misterius
            wd_unknown_brown "Sungguh perpaduan yang indah, bukan?"
            show pria at idle
            nd_narrator_brown "Aku semakin bingung, sejak kapan aku pernah membacakan mereka cerita. Aku tidak paham arah dari pembicaraan ini."
            
            camera:
                zoom 2.0
                xalign 0.15
                yalign 0.45
            show yuura at speaking
            nd_you_brown "Bisakah kita berhenti?"
            show yuura at idle

            camera:
                zoom 1.0
                xalign 0.5
                yalign 0.5

            hide vid_memory_reading with Dissolve(0.5)
            
            show pria netral at speaking
            voice voice_3_17_479_pria_misterius
            wd_unknown_brown "Mengapa demikian?"
            show pria at idle

            show yuura at speaking
            nd_you_brown "Aku... Aku tak pernah melakukan yang kamu sebutkan..."
            # show yuura at idle
            
            nd_you_brown "Aku bukan Yuura yang kalian kenal."
            show yuura at idle
            
            show pria happy
            nd_narrator_brown "Pria itu tersenyum, dia menatapku dengan penuh kasih. Rasanya sangat menenangkan melihatnya."

            show pria at speaking
            voice voice_3_17_482_pria_misterius
            wd_unknown_brown "Jadi... Kamu Yuura yang mana?"
            show pria at idle

            show yuura at speaking
            nd_you_brown "Apa maksudmu?"
            show yuura at idle

            show vid_memory_hutang behind yuura:
                blur 25
            with Dissolve(2.0)

            $ renpy.sound.set_volume(0.0, channel="memories")

            show pria at speaking
            voice voice_3_17_484_pria_misterius
            wd_unknown_brown "Yuura yang belum melunasi hutangnya?"
            
            hide vid_memory_hutang with Dissolve(2.0)
            show vid_memory_senyum behind yuura:
                blur 25
            with Dissolve(2.0)

            $ renpy.sound.set_volume(0.0, channel="memories")

            voice voice_3_17_485_pria_misterius
            wd_unknown_brown "Atau Yuura yang akan selalu tersenyum untuk kami?"
            
            hide vid_memory_senyum with Dissolve(2.0)
            show vid_memory_nyanyi behind yuura:
                blur 25
            with Dissolve(2.0)

            $ renpy.sound.set_volume(0.0, channel="memories")

            voice voice_3_17_486_pria_misterius
            wd_unknown_brown "Atau Yuura yang akan selalu bernyanyi bersama kami?"
            
            hide vid_memory_nyanyi with Dissolve(2.0)
            show vid_memory_tertawa behind yuura:
                blur 25
            with Dissolve(2.0)

            $ renpy.sound.set_volume(0.0, channel="memories")

            voice voice_3_17_487_pria_misterius
            wd_unknown_brown "Atau Yuura yang akan selalu tertawa bersama kami?"
            show pria at idle

            camera:
                zoom 2.0
                xalign 0.15
                yalign 0.45
            show yuura sad at speaking
            nd_you_brown "Aku tidak mengerti apa yang kamu ingin sampaikan?"
            
            hide vid_memory_tertawa with Dissolve(0.5)

            nd_you_brown "Aku bukanlah Yuura yang kamu kenal! Aku terlempar ke sini dan menjalani hari yang super berat."
            
            nd_you_brown "Apakah kita tidak bisa berhenti saja?"
            show yuura at idle
            
            camera:
                zoom 1.0
                xalign 0.5
                yalign 0.5

            show pria netral
            nd_narrator_brown "Mendengar kata itu, membuatnya terdiam sejenak."
            
            show pria happy
            extend " Dia menatap kearahku sembari tersenyum kecil."
            
            # Hiko improv

            # show pria at speaking
            # voice voice_
            # wd_unknown_brown "Apa kamu pernah terpikirkan perasaan mereka yang menyerangmu?"
            # show pria at idle

            # show yuura at speaking
            # nd_you_brown "Tidak! Mana mungkin aku mau memikirkan orang-orang aneh seperti mereka?"
            # show yuura at idle
            
            # show pria at speaking
            # voice voice_
            # wd_unknown_brown "Kenapa?"
            # show pria at idle

            # show yuura at speaking
            # nd_you_brown "Ya... Buat apa? Kenapa aku harus peduli sama kalian?"
            
            # nd_you_brown "Tempatku bukan di sini... Aku tak memiliki tempat di sini dan tak akan pernah."
            # show yuura at idle
            
            show pria at speaking
            voice voice_3_17_491_pria_misterius
            wd_unknown_brown "Apakah kamu yakin dengan itu?"
            show pria at idle

            show yuura at speaking
            nd_you_brown "Iyalah..."
            show yuura at idle
            
            show pria at speaking
            voice voice_3_17_493_pria_misterius
            wd_unknown_brown "Baiklah... Biar aku perlihatkan sesuatu untukmu."
            show pria at idle
            
            show dark_overlay
            play sound sfx_paper
            show foto_seratus_hal at pos(y=0.7, r=2):
                xalign 0.5
                yalign 5.0
                ease 0.5 yalign 0.5


            nd_narrator_brown "Pria itu memperliahtkan sebuah foto, di mana begitu banyak orang bersorak di depan panggung."

            nd_narrator_brown "Meski aku tahu jelas bahwa orang yang mereka soraki adalah aku, aku jelas-jelas tidak memiliki ingatan tentang itu."
            
            play sound sfx_paper
            hide foto_seratus_hal 
            hide dark_overlay
            with dissolve

            # nd_narrator_brown "Mereka terlihat dengan bersemangat membuat hal-hal diluar nalar, membuatku mempertanyakan mengapa mereka begitu peduli padaku?" # using question mark?
            
            camera:
                zoom 2.0
                xalign 0.7
                yalign 0.35

            show pria at speaking
            voice voice_3_17_494_pria_misterius
            wd_unknown_brown "Bagaimana? Apa ada sesuatu yang berbeda?"
            show pria at idle

            camera:
                zoom 2.0
                xalign 0.15
                yalign 0.45

            show yuura at speaking
            nd_you_brown "Aku... Aku tak bisa..."
            
            nd_you_brown "Aku hanya seorang pencuri biasa yang terjebak ditubuh orang yang kalian sebut YUURA"

            nd_you_brown "AKU BUKAN DIA, aku tak bisa... Sama sekali tidak bisa."
            
            nd_you_brown "Meski aku berusaha sekeras mungkin untuk menjadi Yuura sekarang, aku gak akan bisa jadi Yuura yang kalian kenal sejak lama!"

            show yuura at idle
            
            show pria at speaking
            voice voice_3_17_498_pria_misterius
            wd_unknown_brown "Siapa yang menyuruhmu menjadi seperti Yuura yang lama?"
            
            camera:
                zoom 2.0
                xalign 0.7
                yalign 0.35

            voice voice_3_17_499_pria_misterius
            wd_unknown_brown "Apakah kamu pikir Yuura yang dulu seperti gambar itu?"
            
            voice voice_3_17_500_pria_misterius
            wd_unknown_brown "Apa kamu kira dia sempurna sejak awal?"
            show pria at idle
            
            # show pria at custom_sprite_pos(x=0.2) with ease
            # show pria at ease_custom(right, 0.2, 2.0)

            play sound sfx_action_footstep_on_wooden_floor_scene10
            show pria:
                ease 3.0 xalign 0.2

            # pause 1.5
            $ renpy.pause(1.5, hard=True)

            camera:
                zoom 1.0
                xalign 0.5
                yalign 0.5

            $ renpy.pause(1.5, hard=True)

            camera:
                zoom 2.0
                xalign 0.15
                yalign 0.4

            # camera:
            #     zoom 1.5
            #     xpos 0.4

            nd_narrator_brown "Pria itu mendekatiku, tangannya yang lembut mengelus pipiku dan menyeka air mataku."
            
            show pria at speaking
            voice voice_3_17_501_pria_misterius
            wd_unknown_brown "Yuura perlu waktu yang lama untuk bisa mencapai tempatnya sekarang ini."
            
            voice voice_3_17_502_pria_misterius
            wd_unknown_brown "Dia tidak pernah menyerah, selalu berusaha yang terbaik."
            
            voice voice_3_17_503_pria_misterius
            wd_unknown_brown "Bahkan terkadang dia akan memaksakan dirinya sendiri."
            
            voice voice_3_17_504_pria_misterius
            wd_unknown_brown "Apakah kamu pikir dia berubah karena orang-orang ingin dia berubah?"
            
            voice voice_3_17_505_pria_misterius
            wd_unknown_brown "Tidak.. dia berubah karena dirinya mau, dia selalu berusaha menjadi dirinya sendiri."
        
            voice voice_3_17_506_pria_misterius
            wd_unknown_brown "Untuk apa dirimu berusaha menjadi Yuura yang dulu?"
            
            voice voice_3_17_507_pria_misterius
            wd_unknown_brown "Untuk siapa? Dan kenapa kamu harus?"
            
            show pria eff_laugh_y
            voice voice_3_17_508_pria_misterius
            wd_unknown_brown "Demi kita? PPFFTT HAHAHAHA! YAKALI PANDA TUA ITU MIRIKIRIN KITA." 
            
            show pria none
            voice voice_3_17_509_pria_misterius
            wd_unknown_brown "Melihatmu tersenyum saja sudah sangat membahagiakan bagi kami."
            
            voice voice_3_17_510_pria_misterius
            wd_unknown_brown "Jadi... Berhenti memaksakan dirimu."
            
            camera:
                zoom 1.0
                xalign 0.5
                yalign 0.5
            with dissolve

            voice voice_3_17_511_pria_misterius
            wd_unknown_brown "Jadilah dirimu sendiri dan temukan jati dirimu sendiri."
            
            voice voice_3_17_512_pria_misterius
            wd_unknown_brown "Karena Yuura yang kukenal adalah orang yang kuat." # kasih pause setelah kata "kenal"?
            
            voice voice_3_17_513_pria_misterius
            wd_unknown_brown "Jadi jangan menangis... Tersenyumlah dan berbahagialah!" # kasih pause setelah jeda titik-titik?
            show pria at idle

                     
            show pria at face_flip with dissolve
            pause 0.5
            play sound sfx_finger_snap
            scene whiteroom_door
            show yuura netral at custom_sprite_pos(x=-0.2), idle, face_flip
            show pria happy at face_flip, idle:
                xalign 0.2
            with Flash

            nd_narrator_brown "Pria itu menjentikkan jarinya, perlahan memperlihatkan dua buah pintu untukku."

            show pria at face_flip, center with ease
            # pause 0.2
            $ renpy.pause(0.2, hard=True)
            
            show pria at speaking
            voice voice_3_17_514_pria_misterius
            wd_unknown_brown "Takdir memanglah kejam, dia tak memberikan waktu untukmu."
            
            voice voice_3_17_515_pria_misterius
            wd_unknown_brown "Yang kau bisa lakukan adalah memilih."
            
            $ renpy.run(QuickSave())

            voice voice_3_17_516_pria_misterius
            wd_unknown_brown "Jadilah Yuura yang kamu inginkan atau pergi dan tak pernah kembali."
            show pria at idle
            # stop music
            menu keputusan:
                "Aku tidak bisa":
                    play music bgm_scene1_foto_foto_kenangan volume 1.0 loop
                    camera:
                        zoom 2.0
                        xalign 0.15
                        yalign 0.45
                    show yuura at speaking
                    nd_you_brown "Aku tidak bisa."
                    show yuura at idle
                    
                    camera:
                        zoom 1.0
                        xalign 0.5
                        yalign 0.5

                    show pria sad at speaking
                    voice voice_3_17_518_pria_misterius
                    wd_unknown_brown "Mengapa?"
                    show pria at idle

                    show yuura at speaking
                    nd_you_brown "Aku rasa... Aku bukan lah orang yang cocok."
                    show yuura at idle
                    
                    show pria at speaking
                    voice voice_3_17_520_pria_misterius
                    wd_unknown_brown "Apa maksudmu, anee?"
                    
                    voice voice_3_17_521_pria_misterius
                    wd_unknown_brown "Mengapa kamu berbicara seperti itu?"
                    show pria at idle

                    show yuura at speaking
                    nd_you_brown "Aku... Hanya tidak mengerti mengapa aku harus di sini..."
                    
                    show yuura happy
                    nd_you_brown "Memang benar banyak hal yang terjadi hari ini."
                    
                    nd_you_brown "Memang benar semua yang kamu beritahukan padaku sungguh indah."
                    
                    show yuura sad
                    nd_you_brown "Tapi itu bukanlah diriku..."
                    
                    nd_you_brown "Aku tak pernah melakukan semua itu..."
                    
                    nd_you_brown "Aku merasa tidak pantas untuk menggantikan Yuura kalian."
                    
                    nd_you_brown "Bahkan aku saja jauh dari Yuura yang kalian kenal."
                    
                    nd_you_brown "Aku... Hanya ingin pulang, ke tempat asalku..."
                    show yuura at idle
                    
                    # voice voice_3_17_530_pria_misterius
                    # wd_unknown_brown "..."
                    
                    # nd_you_brown "..."
                    
                    nd_narrator_brown "Aku benar-benar terdiam, tak tahu harus berbuat apa lagi. Aku hanya ingin beristirahat dan melupakan semua kejadian yang melelahkan ini."
                    
                    show pria happy at speaking
                    voice voice_3_17_532_pria_misterius
                    wd_unknown_brown "Baiklah..."
                    
                    show pria netral
                    voice voice_3_17_533_pria_misterius
                    wd_unknown_brown "Aku memang tak bisa memaksakan keputusan mu..."
                    
                    show pria sad eff_laugh_y
                    voice voice_3_17_534_pria_misterius
                    wd_unknown_brown "Hahaha... Rasanya sangat menyakitkan yah..."
                    show pria none at idle

                    show yuura at speaking
                    nd_you_brown "Maaf... Aku tidak punya pilihan lagi."
                    show yuura at idle
                    
                    show pria happy at speaking
                    voice voice_3_17_536_pria_misterius
                    wd_unknown_brown "Tak apa... Aku mengerti."
                    
                    voice voice_3_17_537_pria_misterius
                    wd_unknown_brown "Pada akhirnya sang pengembara pun harus berpisah dengan kota yang ia singgahi bukan?"
                    
                    voice voice_3_17_538_pria_misterius
                    wd_unknown_brown "Tapi, meskipun begitu aku harap kamu tetap kembali pada kami."
                    
                    voice voice_3_17_539_pria_misterius
                    wd_unknown_brown "Karena kami akan selalu ada di sini untukmu."
                    
                    voice voice_3_17_540_pria_misterius
                    wd_unknown_brown "Maaf jika selama ini kami selalu merepotkanmu."
                    
                    voice voice_3_17_541_pria_misterius
                    wd_unknown_brown "Maaf jika kami tidak bisa menjadi orang yang baik untukmu."
                    
                    voice voice_3_17_542_pria_misterius
                    wd_unknown_brown "Kalau begitu sampai jumpa."
                    
                    voice voice_3_17_543_pria_misterius
                    wd_unknown_brown "Semoga takdir dunia ini mempertemukan kami denganmu kembali."
                    show pria at idle

                    show yuura at speaking
                    nd_you_brown "Terimakasih..."
                    show yuura at idle

                    stop music
                    # $ renpy.movie_cutscene("assets/videos/intro-reversed-1.5-faded.webm")

                    scene vid_intro_reversed:
                        xalign 0.5
                        yalign 0.5
                    with Flash
                    pause 15
                    
                    scene workshop with eye_open
                    # with dissolve

                    nd_narrator_brown "Aku kembali terbangun dari tidur ku."
                    
                    nd_narrator_brown "Cahaya bulan menyisip masuk dari celah gerigi menara jam, menyinari meja dengan tumpukan kertas dan peralatan yang berserak di atasnya."
                    
                    nd_narrator_brown "Bekas luka yang ia terima dari mimpi panjangnya masih terasa. Mungkin mimpi itu memang nyata."

                    nd_narrator_brown "Tapi, seperti keinginannya, dia sudah kembali ke tempatnya. Tanpa tahu nasib tempat yang  sempat ia singgahi, ataupun nasib dari orang-orang yang ia tinggalkan."

                    scene black with dissolve

                    nd_narrator_black "Meski ingin tahu ataupun pergi, kini keduanya sudah tidak mungkin terjadi."

                    # ------------ END ------------

                    $ quick_menu = False

                    $ renpy.call_screen("game_over_screen", reason_text="Yuura kembali ke dunianya, \ntapi bagaimana nasib dunia yang dia tinggalkan?")
                    
                    return
                "Aku tidak mengerti...":
                    # play music two chords
                    play music bgm_scene17_chord volume 1.0 loop
                    show yuura at speaking
                    nd_you_brown "Aku..."
                    
                    show yuura sad
                    nd_you_brown "Aku tidak mengerti... Sama sekali tidak mengerti dengan ini semua..."
                    
                    nd_you_brown "Kenapa kalian melakukannya sejauh itu?"
                    
                    nd_you_brown "Maksudku... Ah! Apasih..."
                    # show yuura at idle
                    
                    scene cg_arc_3_scene_17_shoot_01 with Flash
                    pause 0.5
                    scene cg_arc_3_scene_17_shoot_02 with Flash
                    pause 0.5
                    $ unlock_cg("cg_arc_3_scene_17_shoot_03")
                    scene cg_arc_3_scene_17_shoot_03 with Flash
                    pause 0.5

                    # This have CG
                    nd_narrator_brown "Air mata ku turun perlahan. Masih dilanda bingung. Mengapa mereka mengejarku? Mengapa mereka melindungiku? Mengapa mereka mencariku? Aku benar-benar tidak tahu apa-apa."
                    
                    $ unlock_cg("cg_arc_3_scene_17_shoot_04")
                    scene cg_arc_3_scene_17_shoot_04 with dissolve

                    nd_narrator_brown "Sampai sekarang pun aku hanya melarikan diri, tanpa memahami apapun."

                    scene cg_arc_3_scene_17_shoot_03 with dissolve
                    # show yuura at speaking
                    nd_you_brown "Apa sih yang kalian inginkan dariku..."
                    
                    nd_you_brown "Apa kalian tidak takut ketika Yuura berubah menjadi seseorang yang kalian tidak kenali?"

                    nd_you_brown "Gimana kalau Yuura yang kalian lindungi itu palsu?"
                    
                    with hpunch

                    nd_you_brown "KENAPA KALIAN TETAP BEGINI PADAHAL KALIAN SEBENARNYA PUN CURIGA DAN RAGU PADAKU?"
                    
                    nd_you_brown "Kenapa kalian...{w} masih mau menerimaku?"
                    # show yuura at idle
                    
                    scene cg_arc_3_scene_17_shoot_04 with dissolve

                    # show pria at speaking
                    voice voice_3_17_554_pria_misterius
                    wd_unknown_brown "Jika kamu bertanya padaku."
                    
                    voice voice_3_17_555_pria_misterius
                    wd_unknown_brown "Alasannya Sederhana, karena kamu Yuura" # kasih pause setelah jeda koma?

                    scene whiteroom_door
                    show yuura sad at custom_sprite_pos(x=-0.2), idle, face_flip
                    show pria netral at center, speaking
                    with fade
                    
                    voice voice_3_17_556_pria_misterius
                    wd_unknown_brown "Karena mereka peduli padamu, pada Yuura." # kasih pause setelah jeda koma?
                    show pria at idle

                    show yuura at speaking
                    nd_you_brown "Tapi aku bukan Yuura yang kalian kenal!"
                    
                    nd_you_brown "Mengapa masih saja ada yang mau melindungiku, bahkan melukai dirinya sendiri demi diriku!"
                    show yuura at idle
                    
                    show pria at speaking
                    voice voice_3_17_559_pria_misterius
                    wd_unknown_brown "Karena kamu Yuura."
                    show pria at idle

                    show yuura at speaking
                    nd_you_brown "Bagaimana bisa? Hanya karena aku mirip dengan orang yang kalian kenal, kalian langsung melakukan apapun demi diriku!" # demiku atau demi aku?
                    
                    nd_you_brown "Apa kalian itu tolol atau gimana sih!"
                    show yuura at idle
                    
                    show pria happy at speaking
                    voice voice_3_17_562_pria_misterius
                    wd_unknown_brown "Pffttt!!"
                    
                    show pria eff_laugh_y
                    voice voice_3_17_563_pria_misterius
                    wd_unknown_brown "Hahaha"
                    show pria none at idle

                    show yuura angry at speaking
                    nd_you_brown "Apanya yang lucu dari itu?"
                    show yuura at idle
                    
                    show pria at speaking
                    voice voice_3_17_565_pria_misterius
                    wd_unknown_brown "Tidak... Hanya saja itu adalah hal yang paling sering kamu katakan."
                    show pria at idle
                    
                    show yuura netral at speaking
                    nd_you_brown "Maksudmu?"
                    show yuura at idle
                    
                    show pria at speaking
                    voice voice_3_17_567_pria_misterius
                    wd_unknown_brown "Iya... Kamu selalu bilang 'Yuuraid itu aneh banget, emang kalian ga cape apa?'" # italic buat kutipannya kah?
                    
                    voice voice_3_17_568_pria_misterius
                    wd_unknown_brown "Tapi kita selalu bilang 'ga, biasa aja sih'" # perlukah italic?
                    
                    voice voice_3_17_569_pria_misterius
                    wd_unknown_brown "Terus kita ketawa bareng-bareng."
                    
                    voice voice_3_17_570_pria_misterius
                    wd_unknown_brown "Lagian buat apa tanya begituan juga?"
                    
                    voice voice_3_17_571_pria_misterius
                    wd_unknown_brown "Kami ngelakuin semua ini, ya karena kamu!"
                    show pria at idle
                    
                    nd_narrator_brown "Aku semakin bingung dengan pernyataan yang pria ini lontarkan. Aku tak mengerti mengapa dia terlihat tidak peduli, padahal aku adalah orang asing."

                    show pria at speaking
                    voice voice_3_17_572_pria_misterius
                    wd_unknown_brown "Biar aku tunjukkan padamu."
                    # show pria at idle

                    stop music
                    play sound sfx_finger_snap
                    # play music bgm_credit_scene volume 1.0 loop
                    scene vid_memory_pleaseework:
                        xalign 0.5
                        yalign 0.5
                    with Flash
                    pause 250
                    
                    play sound sfx_finger_snap
                    # hide vid_memory_pleaseework
                    scene whiteroom_door
                    show yuura sad at custom_sprite_pos(x=-0.2), idle, face_flip
                    show pria netral at center, speaking
                    with Flash

                    # nd_narrator_brown "Pria itu menunjukkan sebuah video, di mana banyak hal yang terjadi."
                    
                    show pria at speaking
                    voice voice_3_17_573_pria_misterius
                    wd_unknown_brown "Bagaimana menurutmu?"
                    
                    voice voice_3_17_574_pria_misterius
                    wd_unknown_brown "Apa kamu masih ragu pada dirimu sendiri?"
                    show pria at idle
                    
                    nd_you_brown "..."
                    
                    show pria happy at speaking
                    play music bgm_scene4 volume 1.0 loop fadein 1.0
                    voice voice_3_17_576_pria_misterius
                    wd_unknown_brown "Tidak apa, untuk sekarang kembalilah dan temui mereka."
                    
                    voice voice_3_17_577_pria_misterius
                    wd_unknown_brown "Katakan bahwa kamu adalah Yuura."
                    
                    voice voice_3_17_578_pria_misterius
                    wd_unknown_brown "Baik Yuura yang manapun itu, kamu tetaplah Yuura."
                    
                    voice voice_3_17_579_pria_misterius
                    wd_unknown_brown "Selesaikan semuanya, dan jadilah dirimu sendiri."
                    
                    voice voice_3_17_580_pria_misterius
                    wd_unknown_brown "Jadilah Yuura yang kami sayangi, kami cintai, dan kami dukung."
                    show pria at idle

                    show yuura:
                        alpha 1.0
                        ease 10 alpha 0.5
                    
                    nd_narrator_brown "Perlahan aku mulai menghilang, melihat pria itu tersenyum bahagia membuatku merasa sangat bahagia. Apakah ini adalah jalan yang benar untukku? Entahlah, aku hanya perlu menjadi diriku sendiri."
                    show yuura at speaking
                    wd_yuura_brown "Terima kasih... {w}ermm..."
                    show yuura at idle
                    
                    show pria at speaking
                    voice voice_3_17_582_pria_misterius
                    nd_pria_brown "Panggil saja aku Yuuraid." # kasih pause setelah jeda titik-titik?

                    show pria at idle

                    show yuura:
                        ease 5 alpha 0.2
                    
                    show yuura at speaking
                    wd_yuura_brown "Ya! Terimakasih, Yuuraid."
                    # show yuura at idle

                    show yuura:
                        ease 2 alpha 0.0
                    
                    # hide yuura with dissolve

                    nd_narrator_brown "Aku menghilang sepenuhnya dan kembali ke dunia nyata."

                    stop music fadeout 1.0
                    jump scene_18
        "Aku ingin pergi dari sini":
            play music bgm_scene1_foto_foto_kenangan volume 1.0 loop
            show yuura at speaking
            camera:
                zoom 2.0
                xalign 0.15
                yalign 0.45
            nd_you_brown "Aku ingin pergi dari sini."
            show yuura at idle

            camera:
                zoom 2.0
                xalign 0.8
                yalign 0.35
    
            show pria netral at speaking
            voice voice_3_17_434_pria_misterius
            wd_unknown_brown "Apa kamu yakin dengan pilihan mu?"
            show pria at idle

            camera:
                zoom 1.0
                xalign 0.5
                yalign 0.5

            show yuura at speaking
            nd_you_brown "Maaf... Aku tidak bisa di sini..."
            show yuura at idle

            # show pria at speaking
            # voice voice_
            # wd_unknown_brown "kamu orang yang seperti itu ya."
            # show pria at idle

            show yuura at speaking
            nd_you_brown "Maaf..."
            show yuura at idle

    
            show pria at speaking
            voice voice_3_17_438_pria_misterius
            wd_unknown_brown "Hm, untuk apa minta maaf?"
    
            voice voice_3_17_439_pria_misterius
            wd_unknown_brown "Tidak ada yang salah dalam pilihan mu."
            show pria at idle

            show yuura at speaking
            nd_you_brown "Maaf… aku bukan orang yang baik."
            show yuura at idle
            
    
            show pria at speaking
            voice voice_3_17_441_pria_misterius
            wd_unknown_brown "Tidak apa, tidak semua orang berani mengambil pilihan."
    
            
            voice voice_3_17_442_pria_misterius
            wd_unknown_brown "Pada akhirnya sang pengembarapun harus berpisah dengan kota yang ia singgahi bukan?"
    
            
            voice voice_3_17_443_pria_misterius
            wd_unknown_brown "Tapi, meskipun begitu aku harap kamu tetap kembali pada kami."
    
            show pria happy
            voice voice_3_17_444_pria_misterius
            wd_unknown_brown "Karena kami akan selalu ada di sini untukmu."
    
            
            voice voice_3_17_445_pria_misterius
            wd_unknown_brown "Maaf jika selama ini kami selalu merepotkanmu."
    
            
            voice voice_3_17_446_pria_misterius
            wd_unknown_brown "Maaf jika kami tidak bisa menjadi orang yang baik untukmu."
    
            
            voice voice_3_17_447_pria_misterius
            wd_unknown_brown "Kalau begitu sampai jumpa."
    
            
            voice voice_3_17_448_pria_misterius
            wd_unknown_brown "Semoga takdir dunia ini mempertemukan kami denganmu kembali."
            show pria at idle
            
            show yuura at speaking
            nd_you_brown "Terimakasih..."
            show yuura at idle

            stop music
            # $ renpy.movie_cutscene("assets/videos/intro-reversed-1.5-faded.webm")
            
            play sound sfx_finger_snap
            show gerbang with Flash

            nd_narrator_black "Aku terbangun tepat luar gerbang tempat ini."
            
            play sound sfx_walkling_on_the_forest_scene_4
            show gerbang:
                zoom 1.0
                yalign 0.5
                linear 10 zoom 2.0 yalign 0.4

            pause 5

            # nd_narrator_black "Aku memutuskan pergi keluar penginapan ini."
            
            scene black with fade

            nd_narrator_black "Tanpa melihat ke belakang dan tanpa menyesali semuanya. Aku harap aku tak akan kembali ke sini, meskipun hatiku masih menginginkannya."
            # ------------ END ------------

            $ quick_menu = False

            $ renpy.call_screen("game_over_screen", reason_text="Yuura Pergi.")
            
            return
    return