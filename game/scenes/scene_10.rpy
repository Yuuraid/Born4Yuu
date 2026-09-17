# label start:


label scene_10:

    # show ruang tamu with Dissolve(1.0)
    # # play music jade bottle fadein
    
    scene transition_screen orange concentrationline02_w with fade
    show yuura scared at ease_custom(offscreenright, center, 0.5), speaking

    nd_narrator_brown "Aku berlari tanpa melihat ke belakang, tak peduli dengan pertengkaran mereka berdua. Saat ini yang paling penting adalah keselamatanku."

    hide yuura with easeoutleft
    scene inn ruang_tamu_2
    show dityo netra netral at left, silhouette
    with fade

    show yuura scared at ease_custom(offscreenright, left, 0.5), idle
    pause 0.5
    show yuura at ease_custom(left, center, 0.2), idle
    nd_narrator_brown "Meskipun aku sudah lolos dari mereka berdua. Nyatanya, dunia tidak seindah itu. Aku menabrak om-om yang tadi mengejarku. Ternyata dia sudah memperhitungkan jalur pelarianku dengan alatnya."
    
    show dityo at speaking, silhouette
    voice voice_2_10_101_dityo
    nd_unknown_brown "Mau ke mana kamu Anee ?"
    
    voice voice_2_10_102_dityo
    nd_unknown_brown "Aku kan udah bilang kamu ga bakal bisa pergi dariku..."
    
    show yuura angry at speaking
    show dityo at idle, silhouette
    nd_yuura_brown "Apasih ! Minggir ! Aku sudah muak banget ya sama kalian semua ! Dari pagi dikejar-kejar mulu"
    
    show dityo at speaking, silhouette
    show yuura at idle
    voice voice_2_10_104_dityo
    nd_unknown_brown "T-tapi Anee, bukannya--"
        # show yuura shake ??
    
    show yuura angry at speaking
    show dityo at idle, silhouette
    show layer master at shake
    nd_yuura_brown "DIEM !"
    
    show yuura at idle
    nd_narrator_brown "Aku memukul tangan Dityo dan bikin mahakaryanya jatuh."
        # nd_yuura_brown "DIEM ! (Aku memukul tangan Dityo dan bikin mahakaryanya jatuh.)"
    
    show yuura netral at speaking
    nd_yuura_brown "Ah..."
    
    show dityo at speaking, silhouette
    show yuura at idle
    nd_unknown_brown "..."
    
    voice voice_2_10_107_dityo
    nd_unknown_brown "Kenapa ne ?Kenapa kamu jadi seperti ini ?Ini bukan seperti Anee yang kukenal..."
    
    voice voice_2_10_108_dityo
    nd_unknown_brown "Yuura yang kukenal tidak akan langsung merusak barang orang lain ! Dia orang yang baik, penyayang."
        # show dityo marah with shake ??

    $ renpy.run(QuickSave())

    voice voice_2_10_109_dityo
    nd_unknown_brown "BUKAN ORANG YANG KASAR KAYAK GINI !"
        # show yuura with shake ??
        # stop music
        # play music foto mantan fadein(1.0)
    menu:
        "APA SIH ! ORANG DARI AWAL JUGA KAMU YANG NGEJAR-NGEJAR AKU ! KENAPA SEMUA MALAH JADI AKU YANG SALAH !":
            $ dityo_route = "Bad end"
            
            show yuura angry at speaking
            show dityo at idle, silhouette
            nd_yuura_brown "APA SIH ! ORANG DARI AWAL JUGA KAMU YANG NGEJAR-NGEJAR AKU ! KENAPA SEMUA MALAH JADI AKU YANG SALAH !"
                # show yuura panik
                # show dityo serius
            
            show dityo at speaking, silhouette
            show yuura at idle
            voice voice_2_10_111_dityo
            nd_unknown_brown "Jadi menurut kamu ini salah aku ? SALAHKU ? APA ANEE KIRA BIKIN KAYAK GINI GAMPANG ?"
                # show dityo marah with shake
            
            voice voice_2_10_112_dityo
            nd_unknown_brown "KAMU DENGAN MUDAHNYA NGANCURIN MAHAKARYAKU ??"
            
            voice voice_2_10_113_dityo
            nd_unknown_brown "Kalo bukan kamu yang minta juga aku ga mungkin bikin alat ini !"
            
            # show dityo at idle, silhouette
            # nd_narrator_brown "Orang itu pergi tanpa berkata-kata. Dia meninggalkan semua barangnya dan tidak pernah kembali lagi ke penginapan."

            # Disable the quick menu for this specific scene/cutscene
            $ quick_menu = False

            $ renpy.call_screen("game_over_screen", reason_text="Orang itu pergi tanpa berkata-kata. Dia meninggalkan semua barangnya dan tidak pernah kembali lagi ke penginapan.")
            
            return

        "A-aku beneran ga sengaja… sumpah, aku tadi niatnya cuma mau bikin kamu ngejauh bukan buat ngancurin karya yang kamu buat.":
            $ dityo_route = "Good end"
            
            show yuura at speaking
            show dityo at idle, silhouette
            nd_yuura_brown "A-aku beneran ga sengaja... Sumpah, aku tadi  niatnya cuma mau bikin kamu ngejauh bukan buat ngancurin karya yang kamu buat."
            
            show dityo at speaking, silhouette
            show yuura at idle
            nd_unknown_brown "..."
            
            show yuura at speaking
            show dityo at idle, silhouette
            nd_yuura_brown "Sumpah aku ga sengaja... A-aku beneran minta maaf..."
            
            show dityo sad at idle, silhouette
            show yuura at idle
            nd_narrator_brown "Aku ingat sebelumnya orang ini ada di buku tamu, namanya Dityo."
            
            show yuura at speaking
            show dityo at idle with dissolve
            nd_yuura_brown "Maaf, Dityo..."

            show dityo at speaking
            show yuura at idle
            voice voice_2_10_118_dityo
            nd_dityo_brown "Entahlah Anee... Aku capek banget... Bisakah kamu biarkan aku sendiri ?"
            
            show yuura at speaking
            show dityo at idle
            nd_yuura_brown "Iya... Sekali lagi aku minta maaf, Dityo..."
            
            show dityo sad at idle
            show yuura at ease_custom(center, offscreenleft, 3.0)
            nd_narrator_brown "Dityo berdiam diri, dia terdiam mematung tanpa berkata-kata lagi."
                # hide dityo with fade
                # stop music 
                # play music rock fadein
            
            scene inn rooftop_2 with fade
            show yuura netral at ease_custom(offscreenright, center, 1.0), idle, zorder 1
            nd_narrator_brown "Aku melanjutkan perjalananku di lantai ke-2, sepanjang lorong itu aku selalu melihat hal-hal janggal."
            
            nd_narrator_brown "Aku melihat sebuah foto kebakaran dari gedung ini, yang entah mengapa aku merasakan kemarahan melihat foto ini."
            
            show axia netral at custom_sprite_pos(x=0.6), silhouette with easeinright
            nd_narrator_brown "Entah apa yang terjadi tiba-tiba ada seseorang menepuk pundakku, orang itu mirip perempuan namun suaranya laki-laki."
            
            nd_narrator_brown "Mendengar suaranya saja membuat bulu kudukku langsung berdiri, dia dengan sangat percaya diri memelukku erat."
            
                # Axiaregis section 
            
            show axia at speaking, silhouette
            voice voice_2_10_120_axiaregis
            nd_unknown_brown "HAWOOOO ANYEEE, KAMU LAGI APAAA ? IHHH SENENG BANGET DEH RASANYA KETEMU ANYEE DI SINI."
            
            show axia at idle, silhouette
            show yuura at ease_custom(center, left, 0.3)
            show axia at right with ease
            pause 0.3
            show yuura at face_flip
            nd_yuura_brown "(Orang ini kayaknya Axiaregis deh, sesuai deskripsi di buku tamu.)"
            
            show axia at speaking with dissolve
            voice voice_2_10_122_axiaregis
            nd_axiaregis_brown "Kok kamu diam ajaaah anyee ??? Kamu terpaku yah sama diriku yang imut ini ? Iya kan ? KAAANNN ???"
            
            show yuura scared at offscreenleft with ease
            voice voice_2_10_123_axiaregis
            nd_axiaregis_brown "KYAAAH ANYEEE"
            
            show axia at offscreenleft with ease
            scene transition_screen orange concentrationline02_w with fade
            show yuura scared at ease_custom(offscreenright, center, 0.5), idle, zorder 2
            nd_narrator_brown "Mendengar itu, membuat merasa jijik sekaligus kesal melihat tingkah orang ini. Aku segera mempercepat langkah kaki ku untuk pergi menghindarinya. Tapi entah mengapa, dia bergerak lebih cepat."
            
            show axia netral at ease_custom(offscreenright, right, 0.5), speaking
            voice voice_2_10_124_axiaregis
            nd_axiaregis_brown "ANYEEE, KAMU TAU GA ??? PASTI GA TAU KAN ? SAMAAA AKU JUGA GA TAUUUU, TAPI YANG PASTI AKUU IMUTTTT"
            
            voice voice_2_10_125_axiaregis
            nd_axiaregis_brown "ANYEE KAMU KOK DIEM AJA SIH ??? PASTI TERPAKU KAN SAMA AKU ? IYA KAN? KANNN ? AKU IMUT KAN ???"
            
            show yuura at custom_sprite_pos(x=-0.2) with ease
            voice voice_2_10_126_axiaregis
            nd_axiaregis_brown "IHH KOK KAMU MAKIN CEPET SIHHHH ? AKU KAN JADI MAKIN SUKA ANYEEEEEE GEMESINN BANGET SIHHH MUAHH"
                # show yuura panik
            
            show axia at idle
            show yuura at face_flip
            pause 0.2
            nd_yuura_brown "DIEM !"
            
            show yuura at custom_sprite_pos(x=0.6) with ease
            show axia at custom_sprite_pos(x=1.3) with ease
            nd_narrator_brown "Aku mendorongnya jatuh dan dengan lebaynya Axiaregis terjatuh."
            
            scene inn rooftop_2
            show yuura netral at face_flip
            show yuura at custom_sprite_pos(x=0.6), idle
            show axia netral at custom_sprite_pos(x=1.3)
            with fade

            show axia at speaking
            voice voice_2_10_128_axiaregis
            nd_axiaregis_brown "Kyaahhh, anyee kamu kok jahat banget sihhh sama akyuuu ??"
            
            voice voice_2_10_129_axiaregis
            nd_axiaregis_brown "Kamu tega banget ihhh padahal aku udah syantik, imut, dan manish giniii. Masa dengan teganya kamu dorong akuuuu ahhh~ hidoiii."
            
            show yuura at speaking
            show axia at idle
            nd_yuura_brown "DIEM ANJENG KUPUKUL-PUKULIN JUGA YA KAMU !"
            
            show axia at speaking
            show yuura at idle
            voice voice_2_10_131_axiaregis
            nd_axiaregis_brown "Kyaahhh anyeee kasarrr, tolonggg ah~ anyeeki mau mukul akyuhhh"

            voice voice_2_10_129_axiaregis
            nd_axiaregis_brown "Kamuuu tega banget ihhh padahal aku udah syantik, imut dan manish giniiii. Masa dengan teganya kamu dorong akuuuu ahhh~ hidoiii"

            show yuura at speaking
            show axia at idle
            nd_yuura_brown "DIEM ANJENG KU PUKUL-PUKULIN JUGA YA KAMU!"
            
            show axia at speaking
            show yuura at idle
            voice voice_2_10_131_axiaregis
            nd_axiaregis_brown "Kyaahhhh anyeeee kasarrrr, tolonggg ah~ anyeeki mau mukul akyuhhhh"

            show yuura at left
            show axia at right, idle
            with ease
            nd_narrator_brown "Semua orang menatapku, membuatku panik dengan orang yang sangat banyak, aku berusaha untuk lari, tapi sayangnya aku terkepung oleh banyak orang."
            
            # TODO: This part suppose to have CG

            nd_narrator_brown "Aku yang sudah terpojok dan tidak bisa melakukan apa pun hanya bisa pasrah, sebelum akhirnya aku melihat ekor ikan hiu muncul. Dia menerobos banyak orang dengan kecepatan yang cukup tinggi."
            
            # show shark beast at ease_custom(offscreenleft, left, 0.5), face_flip
            voice voice_2_10_132_shark
            nd_unknown_brown "Aneee !!!"
            
            voice voice_2_10_133_shark
            nd_unknown_brown "Pegangan yang erat !"

            show shark beast at ease_custom(offscreenright, offscreenleft, 0.5), silhouette
            pause 0.2
            show yuura at ease_custom(left, offscreenleft, 0.5)
            
            nd_yuura_brown "Oi !!! Pelan-pelan !!"

            nd_narrator_brown "Aku melesat dengan hiu itu pergi dari lorong itu."
            
            show axia at speaking
            voice voice_2_10_135_axiaregis
            nd_axiaregis_brown "Hmph ! Beraninya hiu kecil ituh mengganggu rencanakuh ! Awas kamu yah ! IHHH KECOAKKKK !!! EWWWW."

            scene black with fade

            nd_narrator_black "Dari kejauhan aku mendengar suara teriakan menjijikan itu, tapi aku sudah tidak peduli lagi. Aku sudah lelah dengan semua hal aneh di tempat ini."
            
            scene inn lorong lantai_1 with fade
            show yuura netral at ease_custom(offscreenright, left, 1.0)
            show shark beast at ease_custom(offscreenright, right, 0.5)
            pause 1.5

            hide shark beast
            call evolve_sequence from _evolve_sequence

            pause 0.5

            voice voice_2_10_136_shark
            nd_shark_brown "A-aneeki gapapa ?"
            
            show yuura at speaking
            hide shark_n_sequence
            show shark netral at right, idle
            nd_yuura_brown "APAAN SIH INI TEMPAT ?! KENAPA COBA BANYAK BANGET KEANEHAN DI SINI ??! TADI OM-OM LAH, TERUS PEREMPUAN AYNG SUARANYA LAKI-LAKI LAH"
            
            nd_yuura_brown "SEKARANG APA LAGI ? SEEKOR HIU ?? BISAKAH TEMPAT INI NORMAL DIKIT GITU ?!"
            
            show shark at speaking
            show yuura at idle
            voice voice_2_10_139_shark
            nd_shark_brown "T-tapi anee, i-inikan tempatmu sendiri."
            
            show shark at idle
            show yuura at face_flip
            show yuura angry at speaking
            nd_yuura_brown "DIEM !"
            
            $ renpy.run(QuickSave())
            show yuura at idle
            nd_narrator_brown "Shark terdiam."
            
            nd_unknown_brown "..."
                # play music foto-foto kenangan
            menu:
                "Pergi":
                    $ shark_route = "Bad end"
                    
                    show yuura at speaking
                    nd_yuura_brown "Pergi"
                    
                    show yuura at idle
                    show shark at speaking
                    voice voice_2_10_142_shark
                    nd_shark_brown "T-tapi anee..."
                    
                    show yuura at speaking
                    show shark at idle
                    nd_yuura_brown "PERGI !! AKU UDAH CAPEK DENGAN SEMUA INI !"
                    
                    nd_shark_brown "..."
                    
                    
                    # nd_narrator_brown "Shark pergi meninggalkanku dan tidak pernah muncul lagi dalam kehidupanku."

                    # Game over?
                    $ quick_menu = False

                    $ renpy.call_screen("game_over_screen", reason_text="Shark pergi meninggalkanku dan tidak pernah muncul lagi dalam kehidupanku.")
                    
                    return

                "Sebenarnya... Aku ini siapa sih... Kenapa semua orang seperti ini...":
                    $ shark_route = "Good end"
                    
                    show yuura sad at speaking
                    show shark at idle
                    nd_yuura_brown "Sebenarnya... Aku ini siapa sih... Kenapa semua orang seperti ini..."
                    
                    show yuura at idle
                    show shark at speaking
                    voice voice_2_10_146_shark
                    nd_shark_brown "A-anee... Jangan nangis, a-aku tau i-ini sangat berat untuk anee, t-tapi a-aku yakin anee bisa kok ngelewatin semuanya."
                        # show yuura nangis
                        # play sound hiks
                    
                    show yuura at speaking
                    show shark at idle
                    nd_yuura_brown "*hiks"
                    
                    show yuura at idle
                    show shark at speaking
                    voice voice_2_10_147_shark
                    nd_shark_brown "Sini anee ikut aku sebentar."
                    
                    scene mading with fade

                    show shark netral at ease_custom(offscreenright, right, 0.5)
                    show yuura netral at ease_custom(offscreenright, center, 1.0)

                    nd_narrator_brown "Aku ditarik menuju sebuah papan besar di lantai 2. Shark dengan hati-hati mengeluarkan sebuah foto dari papan besar itu."
                    
                    show yuura at idle
                    show shark at speaking
                    voice voice_2_10_148_shark
                    nd_shark_brown "I-ini anee, kamu inget ini ga ?"
                    
                    show yuura at idle
                    show shark at idle
                    nd_narrator_brown "Aku menggelengkan kepalaku pelan."
                    
                    show yuura at speaking
                    show shark at idle
                    nd_yuura_brown "A-aku ga terlalu inget"
                        # scene black with dissolve(1.0)
                        # show yuura at center with dissolve(1.0)
                    
                    nd_yuura_brown "(AHHH BODOH BANGET HARUSNYA AKU PURA PURA TAU)"
                    
                    show yuura at idle
                    show shark at idle
                    nd_narrator_brown "Aku melihat sebuah foto di taman gedung ini dengan beberapa orang yang tidak aku kenali."
                    
                    show yuura at idle
                    show shark at speaking
                    voice voice_2_10_150_shark
                    nd_shark_brown "Anee... Kamu tau ga...?"
                    
                    voice voice_2_10_151_shark
                    nd_shark_brown "Aku memang anak baru di sini, tapi tiap kali ada acara pasti kamu ngajak aku untuk ikut."
                    
                    voice voice_2_10_152_shark
                    nd_shark_brown "Entah itu karaoke sampai mabuk, atau ya sekadar pesta aja."
                    
                    voice voice_2_10_153_shark
                    nd_shark_brown "T-tapi bukannya gimana-gimana ya...em...cuma suaranya anee itu bagus banget..."
                    
                    voice voice_2_10_154_shark
                    nd_shark_brown "Dan anee juga imut...terus em...ahh banyak deh Yuura."
                    
                    show yuura at speaking
                    show shark at idle
                    nd_yuura_brown "Hm ? Ahahaha... Kamu lucu deh."
                    
                    show yuura at idle
                    show shark at speaking
                    voice voice_2_10_156_shark
                    nd_shark_brown "A-apasih ! Diem deh lu, Yuur."
                    
                    show yuura at speaking
                    show shark at idle
                    nd_yuura_brown "Tch tsundere."
                    
                    show yuura at idle
                    show shark at speaking
                    voice voice_2_10_158_shark
                    nd_shark_brown "A-apaan sih ! Udah deh, yang penting sekarang udah tenangkan ?"
                    
                    show yuura at speaking
                    show shark at idle
                    nd_yuura_brown "Ya... Terima kasih Shark... Kusudah lebih baik sekarang."
                    
                    nd_yuura_brown "Tapi sepertinya aku masih butuh udara segar, Shark."
                    
                    show yuura at idle
                    show shark at speaking
                    voice voice_2_10_161_shark
                    nd_shark_brown "K-kalo gitu boleh ga aku antar kamu ?"
                    
                    show yuura at speaking
                    show shark at idle
                    nd_yuura_brown "Gapapa, aku bisa sendiri, sekali lagi terima kasih."
                    
                    show yuura at ease_custom(center, offscreenleft, 2.0), idle
                    show shark at idle
                    nd_narrator_brown "Aku berjalan pergi meninggalkan lorong-lorong menuju pintu teras."

            jump scene_11