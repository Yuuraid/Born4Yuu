# label start:

label scene_15:
    play music bgm_scene15_feint volume 0.9 loop
    scene inn ruang_kerja with Dissolve(1.0)

    show yuura scared at center, speaking with easeinright
    nd_yuura_brown "Ah... Ah..."
    show yuura at idle
     
    nd_narrator_brown "Aku sudah berlari lumayan jauh dari lorong tempat mereka bertarung satu sama lain, aku sedikit heran, mengapa mereka berani untuk bertarung satu sama lain.. Karena aku ?"
    
    nd_narrator_brown "Tapi sebelum sempat berpikir lebih jauh, aku merasa ada seorang yang mendekat ke arahku."
    
    show yuura scared at speaking
    nd_yuura_brown "Ahh... Aku capek..."
    show yuura at idle

    nd_narrator_brown "Tiba-tiba aku merasakan ada seseorang yang memelukku dari belakang, dia berbisik pelan di telingaku, suaranya membuat bulu kudukku merinding ketakutan."

    show axia sassy behind yuura at center, speaking with dissolve
    voice voice_3_15_251_axiaregis
    nd_unknown_brown "Anyeeeee kamu ngapain disini sendirian ??"
    show axia at idle

    show yuura at left 
    show axia at right
    with ease
    show yuura at face_flip, speaking
    nd_yuura_brown "KYAHHHH !"
    show yuura at face_flip, idle

    show yuura at face_flip, custom_sprite_pos(x=0.6) with ease

    show axia at custom_sprite_pos(x=0.6):
        crop (0, 0, 540, 1080)
    with Flash

    # play sound perempuan teriak
    nd_narrator_brown "Aku melayangkan tanganku ke arahnya, berharap ia per-"

    # show yuura at left with ease

    show yuura at left, speaking with ease
    nd_yuura_brown "WHAT THE FAHHH ?!"
    
    nd_yuura_brown "(T-TUBUHNYA.. TERBELAH !?)"
    show yuura at face_flip, idle
    
    show axia at consumed_by_darkness
    pause 0.5
    hide axia

    show yuura at face_flip, center with ease
    show yuura at idle

    nd_narrator_brown "Dia tersenyum kecil sebelum tubuhnya menghilang seperti tertiup angin."

    show axia loli behind yuura at center, idle with dissolve
    
    pause 0.2

    show yuura at left 
    show axia at right
    with ease
    
    show yuura at face_flip 

    nd_narrator_brown "Suasana di sekitar menjadi suram hingga entah darimana, dia tiba-tiba muncul kembali di belakangku."
    
    show axia at right, speaking 
    with dissolve
    voice voice_3_15_255_axiaregis
    nd_axiaregis_brown "Arere ? Kenyapa kamu kaget begituh ?"
    
    hide axia loli
    call axia_transform_sequence from _axia_transform_sequence
    show axia cute at speaking, right

    # show axia cute at right
    # with dissolve

    voice voice_3_15_256_axiaregis
    nd_axiaregis_brown "Tidak usah takut anyee, ini aku, Axiaregis. Aku di sini untukmu."
    show axia at center, idle with ease
    show yuura at custom_sprite_pos(x=-0.2) with ease

    nd_narrator_brown "Dia mengulurkan tangannya, membuat diriku semakin takut padanya."
    
    show yuura at speaking
    nd_yuura_brown "Pergi ! PERGI !"
    show yuura at idle
    
    show axia at speaking
    voice voice_3_15_258_axiaregis
    nd_axiaregis_brown "Kenapa kamu selalu mengusirku sih ?"
    
    voice voice_3_15_259_axiaregis
    nd_axiaregis_brown "Apa aku memang tidak berhak ada di sekitarmu ?"
    show axia at idle

    show yuura at speaking
    show axia at right with ease
    nd_yuura_brown "M-menjauhlah dariku !"
    show yuura at idle
    
    # nd_narrator_brown "Gadis dengan suara om-om itu pun mulai berjalan membelakangiku. Yang entah mengapa, semakin ia menjauh dariku, suasana di sini malah terasa sesak."
    
    show axia at speaking
    voice voice_3_15_261_axiaregis
    nd_axiaregis_brown "Kenapa sihhh harus selalu akuhhh yang pergi ?"
    show axia at idle

    show yuura at speaking
    nd_yuura_brown "Kamu aneh ! Aku sudah lelah dengan semua keanehan ini."
    show yuura at idle
    
    show axia at speaking
    voice voice_3_15_263_axiaregis
    nd_axiaregis_brown "Begitukah ?"
    show axia at idle

    show yuura at speaking
    nd_yuura_brown "(Sial ! Keknya aku salah ngomong lagi.)"
    show yuura at idle
    
    show axia at custom_sprite_pos(x=0.7) with ease
    nd_narrator_brown "Gadis itu tiba-tiba tersenyum dan mulai mendekatiku kembali. Dan ketika ia mendekat, suasana di sepanjang lorong ini makin terasa sesak."
    
    show axia at speaking
    voice voice_3_15_265_axiaregis
    nd_axiaregis_brown "Bagaimana nihhh, padahal aku pengen banget main sama kamu."
    
    voice voice_3_15_266_axiaregis
    nd_axiaregis_brown "Kalau bisa... AKU INGIN MEMILIKI MU SELAMANYA !"
    
    voice voice_3_15_267_axiaregis
    nd_axiaregis_brown "Seperti sebuah Standee yang ada di pojok ruangan !"
    
    voice voice_3_15_268_axiaregis
    nd_axiaregis_brown "Memandangiku dan selalu tersenyum padaku !"
    
    voice voice_3_15_269_axiaregis
    nd_axiaregis_brown "Are ? Kamu kenapa berkeringat anyee ? Aku hanya bercanda kok..."
    
    voice voice_3_15_270_axiaregis
    nd_axiaregis_brown "Or... am I ?" # im atau I'm nih?
    show axia at idle

    show yuura at speaking
    show yuura scared at shake
    # show yuura takut shake 
    nd_yuura_brown "!!"
    show yuura at idle
    
    # CG here
    nd_narrator_brown "Tubuhku tak dapat bergerak tepat setelah menatap mata Axiaregis yang menyala, aku mencoba menggerakkan seluruh anggota tubuh, namun hasilnya nihil. Aku tetap tak bisa bergerak, sementara nafasku perlahan mulai tersengal."
    
    show axia at speaking
    voice voice_3_15_271_axiaregis
    nd_axiaregis_brown "Oh... Anyeeki yang malang~ Aku sungguh kasihan padamu."
    
    voice voice_3_15_272_axiaregis
    nd_axiaregis_brown "Bagaimana jika kamu menyerah saja ?"
    
    $ renpy.run(QuickSave())

    voice voice_3_15_273_axiaregis
    nd_axiaregis_brown "Jika kamu menyerah semuanya akan menjadi lebih baik loh~"
    show axia at idle
    stop music
    menu lawan:
        "Menyerah pada Axiaregis":
            play music bgm_scene1_foto_foto_kenangan volume .9 loop
            show yuura at speaking
            nd_yuura_brown "A-aku... menyerah !"
            show yuura at idle
            
            show axia at speaking
            voice voice_3_15_275_axiaregis
            nd_axiaregis_brown "Begitukah ? Sayang sekali kamu harus mati kalau begitu..."
            show axia at idle

            show yuura at speaking
            nd_yuura_brown "Hah ? Kenapa begitu ?"
            show yuura at idle
            
            show axia at speaking
            voice voice_3_15_277_axiaregis
            nd_axiaregis_brown "Simple saja, Yuura yang ku kenal tak mungkin menyerah begitu saja"
            
            voice voice_3_15_278_axiaregis
            nd_axiaregis_brown "Selamat tinggal... hehehe"
            show axia at idle
            
            scene black with eye_close

            # show black with Dissolve(1.0)
            nd_narrator_black "Axiaregis menjentikkan jarinya dan membuatku mematung tak bisa bergerak, mataku menjadi blur dan semuanya menjadi tak terlihat lagi. Aku mematung untuk selamanya."
            
            $ quick_menu = False

            $ renpy.call_screen("game_over_screen", reason_text="Yuura berubah menjadi standee, menambahkan koleksi my bini Axiaregis.")
            stop music
            return

            # end?
        "Berontak sekuat tenaga":
            play music bgm_scene15_feint volume 0.9 loop
            show axia at custom_sprite_pos(x=0.4) with ease
            show yuura at speaking
            nd_yuura_brown "ARGhhh Lepas !"
            show yuura at idle
            
            show axia at speaking
            voice voice_3_15_280_axiaregis
            nd_axiaregis_brown "Ihhh anyeee semakin imut deh kalau terus ngelawan kayak gitu."
            
            voice voice_3_15_281_axiaregis
            nd_axiaregis_brown "Tapi sayangnya semuanya akan sia-sia saja."
            show axia at idle

            # hide yuura 
            # show rian angry at left, silhouette
            voice voice_3_15_282_rian
            nd_unknown_brown "Tidak jika aku membantu ! Aku mengeluarkan kartuku. Fathanil !!!!"
            
            show axia at speaking
            voice voice_3_15_283_axiaregis
            nd_axiaregis_brown "Huh ?"
            show axia at idle

            scene cg_arc_3_scene_15_shoot_01 with Flash
            pause 0.0
            scene cg_arc_3_scene_15_shoot_02 with Flash
            pause 0.0
            scene cg_arc_3_scene_15_shoot_03 with Flash
            pause 0.0
            scene cg_arc_3_scene_15_shoot_04 with Flash
            pause 0.0
            scene cg_arc_3_scene_15_shoot_05 with Flash
            # pause 0.1

            # play sound kucing huh
            nd_narrator_brown "Tiba-tiba saja muncul sebuah kudanil besar menabrakkan dirinya yang membuat Axiaregis terpental ke dalam ruangan."

            stop music
            play audio bgm_scene15_pursuit volume 0.9 loop
            
            scene inn ruang_kerja
            show axia netral at right, idle
            show yuura netral at custom_sprite_pos(x=-0.2), idle
            show rian angry at left, idle
            with fade

            show axia at speaking
            voice voice_3_15_284_axiaregis
            nd_axiaregis_brown "Ah…... Iya-iya si penjaga hewan rupanya..."
            show axia at idle

            show rian at speaking
            with dissolve
            voice voice_3_15_285_rian
            nd_unknown_brown "Aku bukan penjaga hewan, aku adalah sang petualang yang hanya numpang lewat. Ingat itu !"
            
            voice voice_3_15_286_rian
            nd_rian_brown "Namaku, Rian !"
            show rian at idle

            show axia at speaking
            voice voice_3_15_287_axiaregis
            nd_axiaregis_brown "Ha... Sungguh menyebalkan sekali rasanya."
            
            voice voice_3_15_288_axiaregis
            nd_axiaregis_brown "Padahal aku ingin banget bersama Yuura ku !"
            
            voice voice_3_15_289_axiaregis
            nd_axiaregis_brown "Tapi KAU MENGGANGU SEMUANYA !"
            show axia at idle

            show rian at speaking
            voice voice_3_15_290_rian
            nd_rian_brown "Nenekku pernah berkata."
            
            voice voice_3_15_291_rian
            nd_rian_brown "Jangan berani kamu lukai hati seorang wanita !"
            
            voice voice_3_15_292_rian
            nd_rian_brown "Kalau kamu tetap melakukannya, maka aku akan menghajarmu !"
            show rian at idle

            show axia at speaking
            voice voice_3_15_293_axiaregis
            nd_axiaregis_brown "Ahhhh berisik berisik berisik!"
            
            voice voice_3_15_294_axiaregis
            nd_axiaregis_brown "Ayo kita bertarung."
            show axia at idle

            show rian at speaking
            voice voice_3_15_295_rian
            nd_rian_brown "Oke, ayo kita duel !"
            show rian at idle

            # ARENA START

            init python:
                import time

                class LPTicker(object):
                    def __init__(self, name, current=8000, text_color="#ffbf00"):
                        self.name = name
                        self.current_lp = current
                        self.target_lp = current
                        self.start_lp = current
                        self.start_time = 0
                        self.duration = 1.9
                        self.text_color = text_color
                        self.text_font = "fonts/FOT-SlumpStd-DB.ttf"

                    def change_lp(self, amount):
                        self.start_lp = self.current_lp
                        self.target_lp = max(0, self.target_lp + amount)
                        self.start_time = time.time()
                        renpy.restart_interaction()

                    def display_func(self, st, at):
                        if self.current_lp != self.target_lp:
                            elapsed = time.time() - self.start_time
                            if elapsed < self.duration:
                                progress = elapsed / self.duration
                                self.current_lp = int(self.start_lp + (self.target_lp - self.start_lp) * progress)
                                renpy.redraw(self, 0)
                            else:
                                self.current_lp = self.target_lp
                        
                        txt = Text(f"{self.current_lp}", size=50, color=self.text_color, font=self.text_font, bold=True)
                        return txt, 0.05
                
                rian_lp = LPTicker("Rian", 8000)
                axia_lp = LPTicker("Axia", 8000)

            $ rian_lp.current_lp = 8000
            $ rian_lp.target_lp = 8000
            
            $ axia_lp.current_lp = 8000
            $ axia_lp.target_lp = 8000

            show white at white_flicker
            pause 1.0
            hide white
            scene white with Flash
            scene arena with slashht
            stop music
            play music bgm_scene15_pursuit volume 0.9 loop
            show axia netral at right, idle with easeinleft
            show rian angry at left, idle with easeinright

            show screen lp_display(player = rian_lp, x_align = 0.1) as rian_hp
            show screen lp_display(player = axia_lp, x_align = 0.9) as axia_hp
            with dissolve

            nd_narrator_brown "Axiaregis menggunakan kekuatannya untuk merubah tempat ini jadi arena battle."
            
            hide screen rian_hp 
            hide screen axia_hp 
            with dissolve
            stop music
            play music bgm_scene15_catastrophe volume .9 loop

            show axia netral at right, speaking
            voice voice_3_15_296_axiaregis
            nd_axiaregis_brown "Sekarang giliranku."

            # ======= 
            # Effects bg
            image card_bg_axia_h = Movie(play="assets/effects/video effects/card/axia_h.webm", loop = True)
            image card_bg_axia_v = Movie(play="assets/effects/video effects/card/axia_v.webm", loop = True)
            image card_bg_rian_h = Movie(play="assets/effects/video effects/card/rian_h.webm", loop = True)
            image card_bg_rian_v = Movie(play="assets/effects/video effects/card/rian_v.webm", loop = True)
            # Card sequence

            # =======

            show card_bg_axia_v with dissolve

            show card_back:
                xalign 0.5 
                yalign 5.0
                linear 0.5 yalign 0.5
                pause 0.5
                linear 0.2 xzoom 0.0
                # Flip back to 0 width
            pause 1.2
            play sound sfx_action_summon_1_scene15
            show card_ilya_von_eizbern:
                # Expand front face
                xalign 0.5
                yalign 0.5
                xzoom 0.0
                linear 0.2 xzoom 1.0
                # linear 0.5 zoom 5.0
            
            voice voice_3_15_297_axiaregis
            nd_axiaregis_brown "Aku Summon Ilya dengan attack 300 ke arena !"
            
            show card_ilya_von_eizbern:
                xalign 0.8
            with ease

            show card_fatanil:
                zoom 5.0
                xalign 0.5 
                yalign 0.5
                linear 0.2 zoom 1.0 xalign 0.2 yalign 0.5

            pause 1.0

            play sound sfx_action_summon_2_scene15
            show card_fatanil:
                ease 0.2 rotate 90

            show axia netral at left
            voice voice_3_15_298_axiaregis
            nd_axiaregis_brown "Aku aktifkan efeknya! Mengikat kuda nil mu ke posisi bertahan."
            show axia at idle

            # reset again
            scene arena
            show axia netral at right, idle
            show rian angry at left, idle 
            with dissolve

            show rian at speaking
            voice voice_3_15_299_rian
            nd_rian_brown "Sial... Aku aktifkan efek Fatanil !"
            
            show card_bg_rian_h
            show card_fatanil:
                rotate 90
                xalign 0.5 
                yalign 0.5
                linear 0.5 zoom 1.3 alpha 0.7
                linear 0.5 zoom 1.0 alpha 1.0
            with dissolve

            voice voice_3_15_300_rian
            nd_rian_brown "Ketika dia bertahan, Fatanil akan menerima  kerusakan setengah dari musuh."
            # show rian at idle

            scene arena
            show axia netral at right, idle
            show rian angry at left, idle 
            with dissolve

            show axia at speaking
            voice voice_3_15_301_axiaregis            
            nd_axiaregis_brown "Tch, aku spesial summon,  Ultimate  Lolibaba, Kanna Kamui !!!!{nw}"

            show card_bg_axia_v with dissolve

            show card_back:
                xalign 0.5 
                yalign 5.0
                linear 0.5 yalign 0.5
                pause 0.5
                linear 0.2 xzoom 0.0
                # Flip back to 0 width
            pause 1.2
            play sound sfx_action_summon_1_scene15
            show card_kanna_Kamui_human:
                # Expand front face
                xalign 0.5
                yalign 0.5
                xzoom 0.0
                linear 0.2 xzoom 1.0
                # linear 0.5 zoom 5.0

            pause 1.0

            voice voice_3_15_302_axiaregis
            nd_axiaregis_brown "Lalu aku akan korbankan Ilya dengan menggunakan skill Kanna."

            show card_kanna_Kamui_human:
                xalign 0.2
            with ease

            show card_ilya_von_eizbern:
                zoom 5.0
                xalign 0.5 
                yalign 0.5
                linear 0.2 zoom 1.0 xalign 0.8 yalign 0.5
            
            pause 1.0
            hide card_ilya_von_eizbern with dusted
            show card_kanna_Kamui_human:
                xalign 0.5
            with ease

            voice voice_3_15_303_axiaregis
            nd_axiaregis_brown "Aku summon, Dragon Kanna ke battlefield !"
            
            hide card_kanna_Kamui_human 
            show card_dragon_kanna:
                zoom 5.0
                xalign 0.5 
                yalign 0.5
                linear 0.2 zoom 1.0 xalign 0.5 yalign 0.5
            with Flash
            pause 0.3

            show card_dragon_kanna:
                xalign 0.8
            with ease
            show card_fatanil:
                zoom 5.0
                xalign 0.5 
                yalign 0.5
                rotate 90
                linear 0.2 zoom 1.0 xalign 0.2 yalign 0.5
            
            voice voice_3_15_304_axiaregis
            nd_axiaregis_brown "Dengan Attack 2500 aku akan menghancurkan kuda nil sialan mu itu !"

            voice voice_3_15_305_axiaregis
            nd_axiaregis_brown "Kanna serang dia !"
            show axia netral at left, idle

            show card_dragon_kanna:
                xalign 0.7 
            with ease

            pause 0.2

            scene arena
            show axia netral at right, idle
            show rian angry at left, idle 
            with dissolve

            show rian at speaking
            voice voice_3_15_306_rian
            nd_rian_brown "Sayang sekali... Aku aktifkan kartu ku !"
            
            show card_bg_rian_v
            show card_dragon_kanna:
                xalign 0.7
                yalign 0.5
            show card_fatanil:
                zoom 1.0
                xalign 0.2 
                yalign 0.5
                rotate 90
            with dissolve
            
            show card_mother_pot:
                zoom 5.0
                xalign 0.5 
                yalign 0.5
                linear 0.2 zoom 1.0 xalign 0.5 yalign 0.5
            pause 0.2
            show card_dragon_kanna:
                xalign 0.9
            with ease

            voice voice_3_15_307_rian
            nd_rian_brown "Panci Emak !"
            
            hide card_mother_pot with dusted

            voice voice_3_15_308_rian
            nd_rian_brown "Dengan panci itu aku menepis serangan naga mu !"
            # show rian at idle

            scene arena
            show axia netral at right, idle
            show rian angry at left, idle 
            with dissolve

            show axia at speaking
            voice voice_3_15_309_axiaregis
            nd_axiaregis_brown "Sialan! Kau selamat kali ini ya."
            
            voice voice_3_15_310_axiaregis
            nd_axiaregis_brown "Tapi di giliran berikutnya adalah kemenangan ku !"
            show axia at idle

            show rian at speaking
            voice voice_3_15_311_rian
            nd_rian_brown "Mari kita lihat saja, Edy."
            
            voice voice_3_15_312_rian
            nd_rian_brown "Aku akan menyelesaikan ini tanpa kekalahan !"
            
            show card_bg_rian_v
            with dissolve

            voice voice_3_15_313_rian
            nd_rian_brown "Draw !"
            
            show card_back:
                xalign 0.5 
                yalign 5.0
                linear 0.5 yalign 0.5
                pause 0.5
                linear 0.2 xzoom 0.0
                # Flip back to 0 width
            pause 1.2
            play sound sfx_action_summon_1_scene15
            show card_javanese_shark:
                # Expand front face
                xalign 0.5
                yalign 0.5
                xzoom 0.0
                linear 0.2 xzoom 1.0
                # linear 0.5 zoom 5.0

            # pause 1.0

            voice voice_3_15_314_rian
            nd_rian_brown "Keluarlah ! Hiu Jawa !"
            
            voice voice_3_15_315_rian
            nd_rian_brown "Hiu Jawa dengan attack 1000 memiliki efek yang menyeramkan."
            
            show card_javanese_shark:
                # rotate 90
                xalign 0.5 
                yalign 0.5
                linear 0.5 zoom 1.2 alpha 0.7
                linear 0.5 zoom 1.0 alpha 1.0

            voice voice_3_15_316_rian
            nd_rian_brown "Aku aktifkan, Gigi Hiu !"
            
            show card_javanese_shark:
                xalign 0.2
            with ease
            show card_dragon_kanna:
                xalign 1.5
                yalign 0.5
                linear 0.2 xalign 0.8
            pause 0.2
            show card_javanese_shark:
                xalign 0.7
            with ease
            show card_dragon_kanna at shake
            pause 0.4
            show card_javanese_shark:
                xalign 0.2
            with ease

            voice voice_3_15_317_rian
            nd_rian_brown "Dengan menggunakan Gigi Hiu, aku mengurangi attack dari Kanna sebesar 2000."
            
            show card_fbi:
                zoom 5.0
                xalign 0.5 
                yalign 0.5
                alpha 0.0
                pause 5.0
                linear 0.2 zoom 1.3 xalign 0.5 yalign 0.5 alpha 1.0

            voice voice_3_15_318_rian
            nd_rian_brown "Dengan begitu aku akan menggunakan kartu spell ku, aktiflah ! FBI !"
            
            hide card_dragon_kanna with dusted

            voice voice_3_15_319_rian
            nd_rian_brown "Dengan begitu para loli mu akan terkirim ke kuburan."

            scene arena
            show axia netral at right, idle
            show rian angry at left, idle 
            with dissolve

            show rian at speaking            
            voice voice_3_15_320_rian
            nd_rian_brown "Lalu aku-"
            show rian at idle

            show axia at speaking
            voice voice_3_15_321_axiaregis
            nd_axiaregis_brown "Ckckck... Tidak secepat itu anak muda."
            
            show card_bg_axia_v
            with dissolve

            show card_back:
                xalign 0.5 
                yalign 5.0
                linear 0.5 yalign 0.5
                pause 0.5
                linear 0.2 xzoom 0.0
                # Flip back to 0 width
            pause 1.2
            play sound sfx_action_summon_1_scene15
            show card_zoo_hunter:
                # Expand front face
                xalign 0.5
                yalign 0.5
                xzoom 0.0
                linear 0.2 xzoom 1.0

            voice voice_3_15_322_axiaregis
            nd_axiaregis_brown "Aku lakukan Chain Card, dan mengaktifkan Zoo Hunter !"
            
            show card_zoo_hunter:
                xalign 0.8
            with ease

            show card_fatanil:
                zoom 5.0
                xalign 0.5 
                yalign 0.5
                linear 0.2 zoom 1.0 xalign 0.1 yalign 0.5
            show card_javanese_shark:
                zoom 5.0
                xalign 0.5 
                yalign 0.5
                linear 0.2 zoom 1.0 xalign 0.45 yalign 0.5

            voice voice_3_15_323_axiaregis
            nd_axiaregis_brown "Dengan begitu semua tipe binatang milikmu akan hancur dan dikirim ke kuburan."

            hide card_javanese_shark with dusted
            hide card_fatanil with dusted
            
            scene arena
            show axia netral at right, idle
            show rian angry at left, idle 
            with dissolve

            show axia at speaking
            voice voice_3_15_324_axiaregis
            nd_axiaregis_brown "Hahaha... Sekarang bagaimana Rian ? Apakah kamu mau menyerah saja ?"
            
            voice voice_3_15_325_axiaregis
            nd_axiaregis_brown "Karena nasib mu sudah ada di tanganku ! Maka kau sudah tamat."
            show axia at idle

            show rian at speaking
            voice voice_3_15_326_rian
            nd_rian_brown "Jika nasib ku berada di tanganmu, aku akan merebutnya kembali !"
            
            show card_bg_rian_v
            with dissolve

            voice voice_3_15_327_rian
            nd_rian_brown "Aktifkan Fatanil dari kuburan !"
            
            show card_fatanil:
                zoom 1.0
                xalign 0.5 
                yalign 0.5
            with dusted

            pause 1.0

            show card_fatanil:
                xalign 0.2
            with ease
            show card_cyber_dragon:
                zoom 5.0
                xalign 0.5 
                yalign 0.5
                linear 0.2 zoom 1.0 xalign 0.8 yalign 0.5

            voice voice_3_15_328_rian
            nd_rian_brown "Aku akan menggabungkannya dengan Cyber Dragon !"
            
            show card_fatanil:
                xalign 0.5
            show card_cyber_dragon:
                xalign 0.5
            with ease

            # show card_bg_rian_v 
            hide card_fatanil
            hide card_cyber_dragon            
            with Flash

            show card_mecha_fatanil:
                zoom 5.0
                xalign 0.5 
                yalign 0.5
                linear 0.5 zoom 1.0 xalign 0.5 yalign 0.5

            voice voice_3_15_329_rian
            nd_rian_brown "Datanglah ! Mecha Fatanil !"

            voice voice_3_15_330_rian
            nd_rian_brown "Tidak hanya itu saja ! Munculah ! Ksatria Hitam !{nw}"
            
            show card_mecha_fatanil:
                xalign 0.2
            with ease
            show card_manusia_kecoa:
                zoom 5.0
                xalign 0.5 
                yalign 0.5
                linear 0.5 zoom 1.0 xalign 0.8 yalign 0.5

            voice voice_3_15_331_rian
            nd_rian_brown "Manusia Kecoa Terbang !"
            
            voice voice_3_15_332_rian
            nd_rian_brown "Dengan Attack 2500 ditambah oleh Mecha Fatanil serangan mereka menjadi 8000 !"
            
            scene arena
            show axia netral at right, idle
            show rian angry at left, idle 
            with dissolve

            show rian at speaking
            voice voice_3_15_333_rian
            nd_rian_brown "Dengan ini, berakhirlah sudah, Edy !"
            
            voice voice_3_15_334_rian
            nd_rian_brown "Aku akan melawan takdir. Dan aku akan menang !"
            
            show card_bg_rian_v
            show card_mecha_fatanil:
                xalign 0.2
                yalign 0.5
            show card_manusia_kecoa:
                xalign 0.8 
                yalign 0.5
            with dissolve

            pause 0.2

            show card_mecha_fatanil:
                yalign -2.0
            show card_manusia_kecoa:
                yalign -2.0
            with ease

            voice voice_3_15_335_rian
            nd_rian_brown "Serang !"
            show rian at idle

            scene arena
            show axia netral at right, idle
            show rian angry at left, idle 
            with dissolve

            show axia at shake
            show screen lp_display(player = axia_lp)
            $ axia_lp.change_lp(-4000)
            play sound sfx_action_life_point_scene15
            nd_narrator_brown "Axiaregis menerima serangan fatal, tapi sayangnya darahnya hanya berkurang setengah."
            
            hide screen lp_display

            show axia at speaking
            voice voice_3_15_336_axiaregis
            nd_axiaregis_brown "HAHAHAHA... Kau salah perhitungan bocah !"
            
            show card_bg_axia_h
            show card_dragon_kanna:
                xalign 0.5
                yalign 1.5
                zoom 2.0
            with dissolve

            voice voice_3_15_337_axiaregis
            nd_axiaregis_brown "Aktifkan Kanna dari kuburan, mengurangi damage yang kuterima jadi setengah."
            
            scene arena
            show axia netral at right, idle
            show rian angry at left, idle 
            with dissolve

            show axia at speaking
            voice voice_3_15_338_axiaregis
            nd_axiaregis_brown "Sekarang giliranku."
            show axia at idle

            show rian at speaking
            voice voice_3_15_339_rian
            nd_rian_brown "Humu humu kata siapa ?"
            show rian at idle

            show axia at speaking
            voice voice_3_15_340_axiaregis
            nd_axiaregis_brown "Tidak mungkin ??"
            show axia at idle

            show rian at speaking
            voice voice_3_15_341_rian
            nd_rian_brown "Aku aktifkan efek dari manusia kecoa terbang."
            
            show card_bg_rian_v
            show card_manusia_kecoa:
                xalign 0.5
                yalign 1.5
                zoom 2.0
            with dissolve

            voice voice_3_15_342_rian
            nd_rian_brown "Menambahkan jumlah serangan yang kamu terima."
            
            scene arena
            show axia netral at right, idle
            show rian angry at left, idle 
            with dissolve

            show screen lp_display(player = axia_lp)
            $ axia_lp.change_lp(-2000)
            play sound sfx_action_life_point_scene15
            
            show rian at speaking
            voice voice_3_15_343_rian
            nd_rian_brown "Sekarang nyawamu tersisa 2000."

            hide screen lp_display
            
            voice voice_3_15_344_rian
            nd_rian_brown "Sebaiknya kamu hitung dosa-dosamu !"
            show rian at idle

            show axia at speaking
            voice voice_3_15_345_axiaregis
            nd_axiaregis_brown "Hahahaha... Dosa? Seharusnya kamu lihat kembali posisimu."
            
            voice voice_3_15_346_axiaregis
            nd_axiaregis_brown "Sekarang giliranku."
            
            show card_bg_axia_v with dissolve

            voice voice_3_15_347_axiaregis
            nd_axiaregis_brown "Draw !"
            
            show card_back:
                xalign 0.5 
                yalign 5.0
                linear 0.5 yalign 0.5
                pause 0.5
                linear 0.2 xzoom 0.0
                # Flip back to 0 width
            pause 1.2
            play sound sfx_action_summon_1_scene15
            show card_senko:
                # Expand front face
                xalign 0.5
                yalign 0.5
                xzoom 0.0
                linear 0.2 xzoom 1.0
                # linear 0.5 zoom 5.0

            voice voice_3_15_348_axiaregis
            nd_axiaregis_brown "Aku summon, Senko !"
            
            voice voice_3_15_349_axiaregis
            nd_axiaregis_brown "Dengan munculnya Senko, aku akan menghidupkan kembali..."
            
            show card_senko:
                xalign 0.2
            with ease
            show card_dragon_kanna:
                zoom 5.0
                xalign 0.5 
                yalign 0.5
                linear 0.5 zoom 1.0 xalign 0.8 yalign 0.5

            voice voice_3_15_350_axiaregis
            nd_axiaregis_brown "Kanna Dragon !"
            
            voice voice_3_15_351_axiaregis
            nd_axiaregis_brown "Lalu serangannya akan menjadi 6000 dengan efek dari Kanna loli di kuburan."
            
            voice voice_3_15_352_axiaregis
            nd_axiaregis_brown "Sekarang kau tak akan bisa berbuat apa-apa... KAU KALAH RI-"
            show axia at idle

            scene arena
            show axia netral at right, idle
            # show rian angry at left, idle 
            with dissolve

            nd_narrator_brown "Rian menarik tanganku dan langsung lari dari hadapan Axiaregis."

            stop music
            play music bgm_scene1_rock volume 0.9 loop
            
            show axia at speaking
            voice voice_3_15_353_axiaregis
            nd_axiaregis_brown "TUNGGU ! WOI !"
            
            voice voice_3_15_354_axiaregis
            nd_axiaregis_brown "ANYEEEE JANGAN TINGGALKAN AKU LAGIII !!!"
            
            voice voice_3_15_355_axiaregis
            nd_axiaregis_brown "ANYEEEEEEEEEE !!!"
            # show axia at idle

            stop music
            scene inn ruang_tamu_2 with fade

            show yuura sad at center
            show rian netral at right
            with easeinright

            nd_narrator_brown "Rian terus berlari tanpa peduli dengan teriakan Axiaregis, aku yang masih tidak mengerti dengan mereka hanya bisa diam membisu."
            
            show rian at speaking
            voice voice_3_15_356_rian
            nd_rian_brown "Yuur, aku harap kamu lari sekarang juga."
            show rian at idle

            show yuura at face_flip, speaking
            nd_yuura_brown "Bagaimana denganmu ? Kenapa kita tidak lari bersama saja ?"
            show yuura at face_flip, idle
            
            show rian at speaking
            voice voice_3_15_358_rian
            nd_rian_brown "Tidak bisa... Aku harus menghentikan manusia NPD itu."
            
            voice voice_3_15_359_rian
            nd_rian_brown "Tenang saja, aku akan baik-baik saja."
            
            voice voice_3_15_360_rian
            nd_rian_brown "Selama dirimu bisa tersenyum, semuanya akan baik-baik saja."
            
            voice voice_3_15_361_rian
            nd_rian_brown "Jadi... Tersenyumlah ! Dan pergi ke mana pun yang kamu mau."
            
            voice voice_3_15_362_rian
            nd_rian_brown "Karena Yuura yang aku kenal selalu tersenyum."
            show rian at idle

            show yuura at face_flip, speaking
            nd_yuura_brown "B-baiklah… Tapi kamu hati-hati, oke ? Dia terlalu berbahaya."
            show yuura at face_flip, idle
            
            show rian at speaking
            voice voice_3_15_364_rian
            nd_rian_brown "Tenang saja... Aku dan pasukan hewanku tak akan kalah !"
            show rian at idle

            # nd_narrator_brown "Dia melempar banyak sekali bola dan mengeluarkan seluruh hewan yang ada di penginapan ini."
            
            show rian at speaking
            voice voice_3_15_365_rian
            nd_rian_brown "Larilah ! Si NPD sudah datang !"
            show rian at idle

            hide yuura at idle with easeoutleft
            scene black with fade

            nd_narrator_black "Axiaregis datang dengan kecepatan penuh, dia membawa seluruh pasukan anak kecil yang jumlahnya ada ratusan. Membuatku tak punya pilihan lain selain lari lagi."
            
            nd_narrator_black "Pada titik ini aku sudah sangat muak, mengapa diriku hanya berlari terus menerus. Apa aku tak bisa melakukan apapun seperti Yuura yang mereka kenal ?"
            
            nd_narrator_black "Apa aku hanya akan terus seperti ini sampai aku menemukan jalan keluarnya ? Aku sudah sangat lelah dan ingin segera pergi dari tempat ini."

            jump scene_16


    return