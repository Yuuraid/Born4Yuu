# label start:

label scene_6:
    # # scene kamar Yuura with Dissolve(2.0)
    # # play music softjazz fadein 1.0 -> define music dulu
    # $ quick_menu = True
    # show yuura normal animated at center
    # with Dissolve(1.0)
    scene inn kamar_yuura morning with eye_open
    pause 1.0
    show layer master at shake
    
    nd_yuura_brown "Ughhh... Kepalaku sakit banget..."
    
    nd_narrator_brown "Aku terbangun dari pingsanku, entah sudah berapa lama tapi aku masih merasakan sakit disekujur tubuhku."
    
    show yuura netral at jump_in_bottom(duration=2.0), speaking
    nd_yuura_brown "Di mana ini? Kenapa rasanya sangat familiar..."
    
    show yuura at idle
    nd_narrator_brown "Aku memperhatikan sekitarku dengan seksama, menyadari bahwa aku kembali ke tempat aku bangun pertama kali."
    
    show yuura at speaking
    nd_yuura_brown "K-kenapa aku di sini !? {w}Tunggu... Apa jangan-jangan tadi aku mimpi ya ?"
    
    nd_yuura_brown "Ga, ga mungkin..."
    
    show yuura at idle
    nd_narrator_brown "Aku benar-benar merasa deja vu dengan kondisi diriku saat ini."
    
    show yuura at speaking
    nd_yuura_brown "Arghhhh... Aku sudah sangat lelah... Sebaiknya aku mandi, bauku sudah sangat buruk"
    
    show yuura at idle
    nd_narrator_brown "Aku mengambil handuk dan segera pergi ke onsen."
        # stop music softjazz fadeout 1.0
        # play audio byur -> define audio dulu
    
    scene black
    # Start CG here
    nd_narrator_brown "sfx *byuurrr"
        # show layer master at shake_custom
        # # scene onsen with Dissolve(2.0) ???
    
    nd_narrator_brown "Suara percikan air yang membasahi tubuhku, aku mengelap seluruh bagian tubuhku. Bahkan bagian kaki yang paling bisa aku banggakan. Aku mengelap sela-sela jari kaki dengan sabun."
        # koreksi lagi docsnya
    
    nd_narrator_brown "Baunya harum seperti bunga sakura yang mungkin bisa membuat laki-laki tergoda padaku."
    
    nd_narrator_brown "Aku membersihkan bagian punggungku dengan sabun yang sama, membilas tiap keringat yang aku keluarkan sepanjang perjalanan."
    
    nd_yuura_brown "Ah~ enaknya..."
    
    nd_yuura_brown "Rasanya benar-benar puas dengan pemandian di gedung ini."
    
    nd_narrator_brown "Aku mengambil air dan membilas sisa-sisa sabun dari tubuhku, dan mengeringkan sela-sela jari kakiku"
    
    scene inn kamar_yuura morning with fade
    show yuura happy at ease_custom(offscreenright, center, 1.8)
    pause 1.8
    show yuura netral 

    nd_narrator_brown "Setelah mandi, aku terkejut karena mendengar ketukan di pintu. Membuatku sedikit panik karena melupakan bahwa aku masih di tempat antah berantah."
        # play music fotokenangan fadein 1.0 -> define music dulu
    
    show yuura at face_flip with dissolve
    
    voice voice_2_6_68_taro
    wd_unknown_brown "Ane... Ini aku Tarochips, aku bawa makanan buat ane..."
    
    nd_narrator_brown "Aku diam saja, tak membalas satu pun ucapannya."
    
    show yuura at idle
    voice voice_2_6_69_taro
    wd_taro_brown "Ane ? Kamu masih tidur ? Aku taruh di depan aja ya... Maaf sudah mengganggu istirahat ane."
    
    nd_narrator_brown "Dia berjalan untuk pergi, tapi sebelum terlalu jauh dia menatap ke kamarku sekali lagi."
    
    voice voice_2_6_70_taro
    wd_taro_brown "Ane... Apa pun yang terjadi, tolong... jaga kesehatanmu, aku ga mau ngeliat ane pingsan lagi."
    
    voice voice_2_6_71_taro
    wd_taro_brown "Apa ane kira aku tidak sedih melihatnya ? Aku sedih ane, melihat orang yang selalu menemaniku di penginapan ini tak berdaya di hadapanku."
    
    nd_narrator_brown "(Suaranya sedikit gemetar, menahan perasaan sedih dalam batinnya.)" 
        # aku bingung nulisnya gmn yg atas ini
    
    voice voice_2_6_72_taro
    wd_taro_brown "Aku emang yang paling tidak menonjol, aku emang yang paling ga mau diliat sama orang..."
    
    voice voice_2_6_73_taro
    wd_taro_brown "Tapi yang ane harus tau, aku senang melihat ane bahagia... Jadi jangan sampai dirimu terluka lagi."
    
    nd_narrator_brown "Dia berjalan pergi meninggalkan lorong. Suara langkah kakinya tidak terdedngar lagi."
    
    show yuura at ease_custom(center, offscreenright, 1.8)
    nd_narrator_brown "Aku keluar dari kamar, mengambil makanan yang dia buat."
    show yuura happy at face_flip, ease_custom(offscreenright, center, 1.8)
    
    nd_narrator_brown "dan tersenyum tipis, merasakan sebuah ketulusan dari orang itu..."

        # $ quick_menu = False

    jump scene_7