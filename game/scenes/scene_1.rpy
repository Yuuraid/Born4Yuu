# The script of the game goes in this file.

label scene_1:
    # scene black

    # $ quick_menu = True
    # play music start with fadein 1.0 -> define dulu
    # play sound "audio/sfx/knock_door.ogg"
    scene black
    nd_narrator_black "Aku mendengar suara berisik dari luar"
    
    nd_narrator_black "membuatku terbangun dari mimpi indahku."
    
        # First half-blink
        # scene inn kamar_yuura morning with Dissolve(0.2)
        # scene black with Dissolve(0.2)
    
    scene inn kamar_yuura morning with eye_open
        # $ quick_menu = False
        # show kamar pagi at panorama_kiri_ke_kanan with Dissolve(1.0)
        # pause 4.0
        # scene kamar pagi with Dissolve(2.0) 
        # pause 1.0
        # $ quick_menu = True
        # show yuura normal animated at center
        # with moveinbottom
        # with nongol_dari_bawah # <-- blm jadi :""
    show yuura netral eff_sleepy at jump_in_bottom(duration=2.0), speaking
    nd_yuura_brown "Iya iya... Hooam..." 

    show yuura netral at idle
    nd_narrator_brown "Aku terbangun dari tidurku,{w} duduk sebentar sebelum benar-benar beranjak dari dari kasurku."
    
    nd_narrator_brown "Rasanya benar-benar malas untuk beranjak dari kas-"
    
    nd_narrator_brown "{w=0.5}.{w=0.5}.{w=0.5}.{nw}"
    
    show yuura scared eff_surprise_y at shake, speaking
    nd_yuura_brown "(LOH KENAPA AKU DI LANTAI !?)"
    
    show yuura scared none at idle
    
    nd_narrator_brown "Aku langsung sadar ketika menyadari ada yang janggal,{w} dan mendapati bahwa aku tidur di kasur yang dibentangkan di lantai?..."
    
    show yuura scared eff_sweat_w at pacing_left_right, idle
    nd_narrator_brown "Aku segera melihat sekitar"
    
    show yuura scared at center, idle
    nd_narrator_brown "Dan benar saja" 
    
    show yuura scared none at center, shake, speaking
    nd_yuura_brown "INI BUKAN KAMARKU!!"
    
    show yuura netral eff_question_mark at center, speaking
    nd_yuura_brown "Kemarin aku salah masuk kamar apa gimana dah?{w} Kok bisa-bisanya kebangun di sini?"
    
    show yuura netral none at center, idle
    nd_narrator_brown "Aku meminggirkan selimut yang selama ini menutupi setengah badanku dan berdiri melihat sekitar."
    
    nd_narrator_brown "Aku melihat cermin, cermin itu memantulkan rupaku yang sama persis sebelum aku tertidur karena kelelahan."
    
    show yuura netral at center, speaking
    nd_yuura_brown "Nggak ada yang aneh sih..."
    
    show yuura netral at center, idle
    nd_narrator_brown "Aku berjalan kecil, mengelilingi kamar nan asing ini yang entah kenapa.. terasa familiar bagiku."
    
    nd_narrator_brown "Lukisan-lukisan aneh yang tergantung di dinding kamar, juga topeng topeng yang digantung di dinding membuat suasana agak seram"
    
    nd_narrator_brown "belum lagi pencahayaan yang redup, Sepertinya kamar ini didesain untuk membuat sang pemilik susah untuk bangun."
        # play sound "audio/sfx/cubit_pipi.ogg"
    
    nd_narrator_brown "*Sfx cubit pipi"
    
    show yuura sad at center, shake, speaking
    nd_yuura_brown "Aduh..."
    
    show yuura netral at center, idle
    nd_narrator_brown "(Aku benar-benar udah kebangun nih.. Tapi kok bisa yah aku tidur disini !?...)"
    
    nd_narrator_brown "Aku terus keliling melihat sekitar, mana tau menemukan hal menarik."
    
    nd_narrator_brown "Aku mendekati sebuah zirah yang terpajang gagah beserta pedang dengan sarungnya yang berwarna merah muda"
    
    show yuura scared eff_sweat_w at center, speaking
    nd_yuura_brown "Uh.. Kayaknya pemilik kamar ini adalah orang yang menakutkan.."
    
    show yuura scared eff_sweat_w at center, idle
    nd_narrator_brown "Didekat zirah itu terdapat meja kecil yang diatasnya terdapat alat penghisap tembakau dan topeng berbentuk hewan"
    
    show yuura scared eff_surprise_y at center, shake, speaking
    nd_yuura_brown "Beneran kriminal ini mah.."

    # Start CG

    scene cg meja_kamar_yuura with dissolve
    hide yuura

    nd_narrator_brown "Tak jauh dari sana, aku melihat sebuah meja yang di atasnya terdapat banyak sekali foto."

    camera:
        # Initial position (zoomed out at the right side)
        zoom 1.5
        xalign 1.0
        yalign 0.2
        
        # Pan across to the left over 5 seconds
        ease 15.0 xalign 0.0
    with dissolve

    nd_narrator_brown "Ketika kudekati, terlihat jelas foto-foto itu adalah momen kebersamaan si pemilik kamar dengan teman maupun keluarga nya. "
    
    # Zoomed into picture frame
    camera:
        zoom 2.0
        xalign 1.0
        yalign 0.5
    with dissolve

    nd_narrator_brown "Aku mengambil sebuah foto dan mengamati lebih jelas."

    scene inn kamar_yuura morning 
    # Reset camera
    camera:
        zoom 1.0
        xalign 0.0
        yalign 0.0

    show yuura scared eff_exclamation at center, shake, speaking
    nd_yuura_brown "ANJIR!!"
    
    nd_yuura_brown "NIH ORANG MIRIP BANGET SAMA GUE COK !"
    
    show yuura netral none at center, idle
    nd_narrator_brown "Aku mengamati beberapa foto lainnya. Benar saja, perempuan yang mirip denganku itu nampaknya merupakan pemilik kamar ini."
    
    nd_narrator_brown "Aku meletakkan kembali foto-foto itu ke tempatnya semula"
    
    show yuura netral eff_question_mark at center, speaking
    nd_yuura_brown "Kok bisa yah, ada orang yang beneran mirip sama aku..?"

    # BGM jade bottle

    show yuura netral none at center, idle
    nd_narrator_brown "Di tengah kebingungan itu, aku melihat sebuah benda yang bersinar. Pandanganku langsung tertuju pada benda itu dan melesat mendekatinya."
    
    nd_narrator_brown "Sebuah botol berwarna Jade yang sejuk dan cerah, tidak salah lagi kalau botol ini terbuat dari batu Jade yang berharga!"

    nd_narrator_brown "Aku mengambil botol hijau zamrud itu dan memandangi keindahan nya. Hingga.."
    
    wd_unknown_brown "Anee, waktu nya bangun"

    # BGM rock

    show yuura scared eff_exclamation at center, shake, speaking
    nd_yuura_brown "ANJIR,TERNYATA ADA ORANG LAIN JUGA DISINI"
    
    show yuura scared eff_sweat_w at pacing_left_right, idle
    nd_narrator_brown "Aku segara memutar otakku, dan menemukan jawaban."
    
    show yuura scared eff_sweat_w at center, speaking
    nd_yuura_brown "AKU HARUS LARI SEBELUM KETAHUAN !!!"
    
    hide yuura with easeoutleft
    nd_narrator_brown "Tepat ketika pintu kamar terbuka sempurna, aku menerjang keluar dan melesat bagai kilat."
    
    show layer master at shake

    nd_narrator_brown "Tak menyadari bahwa orang yang membukakan pintu terjatuh karena ku, tapi peduli apa aku."
    
    nd_yuura_brown "Argh dimana sih.. Ah ini dia !"
    
    nd_narrator_brown "Segera kutembakkan Grappling Gun ku dan melesat tanpa melihat ke belakang."
        # $ quick_menu = False

    jump scene_2