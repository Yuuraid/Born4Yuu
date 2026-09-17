# label start:

label scene_7:
    scene inn lorong with fade
    show yuura netral at ease_custom(offscreenleft, center, 1.8), face_flip, idle
    # BG: lorong penginapan
    # show lorong penginapan with dissolve(2.0)
    nd_narrator_brown "Setelah menyelesaikan makananku, aku berjalan-jalan di sekitar penginapan untuk mencari cara keluar dari sini. Aku menyusuri tiap lorong penginapan yang tak kukenali, mencari informasi ke setiap sudut mengenai bangunan ini."
        # play music rock with fadein 1.0 -> define music dulu
    
    nd_narrator_brown "Tak selang berapa lama, aku bertemu dengan seseorang yang badannya besar, dengan perawakan layaknya om-om ganas di film cab*l yang kutonton."
    
    nd_narrator_brown "Dia menatapku sebentar dan langsung lari ke arahku. Membuatku panik dan langsung kabur dari hadapannya."
    
    # To use ease_custom if you need to flip the image, you put flip after the ease_custom function
    show yuura at face_flip, ease_custom(center, offscreenleft, 0.5), idle
    pause 0.5
    show dityo netral at ease_custom(offscreenright, offscreenleft, 1.0), silhouette

    voice voice_2_7_74_dityo
    nd_unknown_brown "ANEE ! TUNGGU ! INI AKU BAWA SESUATU YANG BAKAL BIKIN KAMU SENANG !"

    scene transition_screen orange concentrationline02_b with fade    

    show yuura scared at ease_custom(offscreenright, center, 0.8), speaking

    nd_narrator_brown "Orang itu mengejarku dengan kecepatan tinggi, entah kenapa yang digunakannya sehingga membuatnya jadi sangat cepat."
        # cek lagi docs nya
    
    nd_narrator_brown "Sepertinya dia membawa sesuatu yang meningkatkan kecepatannya dalam bergerak."
    
    show yuura at ease_custom(center, left, 0.8), idle
    show dityo netral at ease_custom(offscreenright, right, 0.8), speaking, silhouette
    
    voice voice_2_7_75_dityo
    nd_unknown_brown "Ane !!! Stop !!!"
    
    show dityo at idle, silhouette

    nd_narrator_brown "Dia tampak terus berlari mengejarku, membuat tiap orang yang melihatku menjadi salah paham, mengira bahwa aku sedang dalam masalah. Mereka membantu om-om itu untuk mengejarku."
    
    show dityo at speaking, silhouette
    
    voice voice_2_7_76_dityo
    nd_unknown_brown "Ane !!! Berhenti di sana !"
    
    show yuura at speaking
    show dityo at idle, silhouette
    
    nd_yuura_brown "Ga mau ! Kalian aneh ! Kenapa sih kalian terus mengejar aku dari pagi !"
    
    show yuura at ease_custom(left, offscreenleft, 0.5)
    
    nd_narrator_brown "Aku berlari semakin kencang, melupakan bahwa aku memiliki alat-alat canggih untuk lari di situasi ini."
    
    nd_narrator_brown "Ketika aku sudah mulai kehabisan tenaga, tanganku tetiba ditarik ke dalam sebuah ruangan."
    
    nd_narrator_brown "Membuatku terkejut bukan main dengan apa yang baru saja terjadi."
        # stop music fadeout 1.0

    jump scene_8