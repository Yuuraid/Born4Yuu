# label start:

label scene_7:
    
    scene black with fade

    nd_narrator_black "Setelah menyelesaikan makananku, aku berjalan-jalan di sekitar penginapan untuk mencari cara keluar dari sini."
    
    scene inn lorong with fade
    show yuura netral at ease_custom(offscreenleft, center, 1.8), face_flip

    nd_narrator_brown "Aku menyusuri tiap lorong penginapan yang tak kukenali, mencari informasi ke setiap sudut mengenai bangunan ini."

    play music bgm_scene1_rock volume 1.0 loop

    camera:
        zoom 2.0
        xalign 0.6
        yalign 0.3
    show yuura scared eff_exclamation_r at shake

    nd_narrator_brown "Tak selang berapa lama, aku bertemu dengan seseorang yang badannya besar, dengan perawakan layaknya om-om ganas di film cab*l yang kutonton."
    
    show yuura eff_tremble_w
    # nd_narrator_brown "Dia menatapku sebentar dan langsung lari ke arahku. Membuatku panik dan langsung kabur dari hadapannya."
    nd_narrator_brown "Setelah menatap ke arahku, ia langsung berlari ke arahku."
    
    # To use ease_custom if you need to flip the image, you put flip after the ease_custom function
    play sound sfx_action_whoosh_scene13_16
    show yuura none at face_flip, ease_custom(center, offscreenleft, 0.5)
    pause 0.5
    camera:
        zoom 1.0
        xalign 0.0
        yalign 0.0
    show dityo netral mahakarya at ease_custom(offscreenright, offscreenleft, 1.0), silhouette

    voice voice_2_7_74_dityo
    wd_unknown_brown "ANEE! TUNGGU! INI AKU BAWA SESUATU YANG BAKAL BIKIN KAMU SENANG!"

    scene transition_screen orange concentrationline02_b with fade    

    show yuura scared eff_sweat_w at ease_custom(offscreenright, center, 0.8), speaking

    nd_narrator_brown "Orang itu mengejarku dengan kecepatan yang tinggi, entah kenapa yang digunakannya sehingga membuatnya jadi sangat cepat."
        # cek lagi docs nya
    
    nd_narrator_brown "Sepertinya dia membawa sesuatu yang meningkatkan kecepatannya dalam bergerak."
    
    show yuura at ease_custom(center, left, 0.8), idle
    show dityo netral mahakarya at ease_custom(offscreenright, right, 0.8), speaking, silhouette
    
    voice voice_2_7_75_dityo
    wd_unknown_brown "Ane!!! Stop!!!"
    
    show dityo at idle, silhouette

    nd_narrator_brown "Dia tampak terus berlari mengejarku, membuat tiap orang yang melihatku menjadi salah paham, mengira bahwa aku sedang dalam masalah."
    
    show dityo at speaking, silhouette
    
    voice voice_2_7_76_dityo
    wd_unknown_brown "Anee!!! Berhenti disana!"
    
    show yuura at speaking
    show dityo at idle, silhouette
    
    nd_you_brown "Ga mau! Kalian aneh! Kenapa sih kalian terus mengejar aku dari pagi!"
    
    play sound sfx_action_whoosh_scene13_16
    show yuura at ease_custom(left, offscreenleft, 0.5)
    
    scene black with fade

    nd_narrator_black "Aku berlari semakin kencang, melupakan bahwa aku memiliki alat-alat canggih untuk lari di situasi ini."
    
    nd_narrator_black "Ketika aku sudah mulai kehabisan tenaga"
    
    play sound sfx_action_fall_down_scene5_14
    show layer master at shake
    nd_narrator_black "Tanganku tetiba ditarik ke dalam sebuah ruangan."
    
    nd_narrator_black "Membuatku terkejut bukan main dengan apa yang baru saja terjadi."

    stop music fadeout 1.0

    jump scene_8