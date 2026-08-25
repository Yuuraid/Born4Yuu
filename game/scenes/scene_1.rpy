label scene_1:
    
    scene inn kamar_yuura morning

    play music bgm_scene_1_start loop
    play sound sfx_ketukan_sozu

    b_narrator "Aku mendengar suara berisik dari luar, membuatku terbangun dari mimpi indahku."

    show yuura happy at center, speaking

    b_yuura "Iya iya.. Hooam.." 

    show yuura at center, idle

    b_narrator "Aku terbangun dari tidurku, duduk sebentar sebelum benar-benar beranjak dari dari kasurku. Rasanya benar-benar malas untuk beranjak dari kas-"

    b_narrator "..."
    
    # show angry_emotes at yuura_height
    show yuura angry angry_aura at center, shake_custom, speaking


    b_yuura "(MANA DASARNYA !?)"

    hide angry_emotes

    show yuura at center, idle

    show dawam angry angry_aura at left, speaking

    b_narrator "Aku langsung sadar ketika menyadari ada yang janggal,{w} dan mendapati bahwa aku tidur di kasur yang dibentangkan di lantai?..."
    b_narrator "Aku segera melihat sekitar." 
    b_narrator "Dan benar saja." 
    show yuura scared at center, idle
    b_narrator "Ini bukan kamarku."

    show yuura at center, speaking

    b_yuura "Kemarin aku salah masuk kamar apa gimana dah?{w} Kok bisa-bisanya kebangun di sini?"

    show yuura at center, idle

    b_narrator "Aku meminggirkan selimut yang selama ini menutupi setengah badanku dan berdiri melihat sekitar."
    b_narrator "Aku melihat cermin, cermin itu memantulkan rupaku yang sama persis sebelum aku tertidur karena kelelahan."

    show yuura at center, speaking

    b_yuura "Nggak ada yang aneh sih..."

    show yuura at center, idle

    b_narrator "Aku berjalan kecil, mengelilingi kamar nan asing ini yang entah kenapa... terasa familiar bagiku."
    b_narrator "Lukisan-lukisan aneh yang tergantung di dinding kamar, juga topeng-topeng yang bergantung di dinding agak membuat suasana agak seram"
    b_narrator "belum lagi kamar yang redup yang sepertinya di desain untuk membuat pemilik kamar ini susah untuk bangun."

    # play sound sfx_cubit_pipi
    b_narrator "*Sfx cubit pipi"

    show yuura sad at center, shake_custom, speaking

    b_yuura "Aduh..."

    show yuura at center, idle

    b_narrator "(Aku benar-benar udah kebangun nih... Tapi kok bisa yah aku tidur di sini !?...)"
    b_narrator "Aku terus keliling melihat sekitar, mana tau menemukan hal yang menarik."
    b_narrator "Aku mendekati sebuah zirah yang terpajang gagah beserta pedang dengan sarungnya yang berwarna merah muda."

    show yuura scared at center, speaking

    b_yuura "Uh... Kayaknya pemilik kamar ini adalah orang yang menakutkan..."
    
    show yuura scared at center, idle
    
    b_narrator "Didekat zirah itu, terdapat meja kecil yang di atasnya terdapat alat penghisap tembakau dan topeng berbentuk hewan."
    
    show yuura scared at center, speaking
    
    b_yuura "Beneran kriminal ini mah..."
    
    show yuura scared at center, idle
    
    stop music fadeout 3.0
    play music bgm_foto_kenangan fadein 3.0 loop

    b_narrator "Tak jauh dari sana, aku melihat sebuah meja yang di atasnya terdapat banyak sekali foto."
    b_narrator "Ketika kudekati, terlihat jelas foto-foto itu adalah momen kebersamaan si pemilik kamar dengan teman maupun keluarganya."
    b_narrator "Aku mengambil sebuah foto dan mengamati lebih jelas."

    show yuura scared at center, shake_custom, speaking

    b_yuura "ANJIR!!"
    b_yuura "NIH ORANG MIRIP BANGET SAMA GUE COK !"

    show yuura scared at center, idle

    b_narrator "Aku mengamati beberapa foto lainnya. Benar saja, perempuan yang mirip denganku itu nampaknya merupakan pemilik kamar ini."
    b_narrator "Aku meletakkan kembali foto-foto itu ke tempatnya semula."

    show yuura at center, speaking

    b_yuura "Kok bisa yah, ada orang yang beneran mirip sama aku...?"

    show yuura at center, idle

    # stop music fadeout 3.0
    play music bgm_jade_bottle fadein 3.0 loop

    b_narrator "Ditengah kebingungan itu, aku melihat sebuah benda yang bersinar. Pandanganku langsung tertuju pada benda itu dan melesat mendekatinya."
    b_narrator "Sebuah botol berwarna hijau zamrud yang sejuk dan cerah, tidak salah lagi kalau botol ini terbuat dari batu jade yang berharga!"
    b_narrator "Aku mengambil botol zamrud itu dan memandangi keindahannya. Hingga..."

    stop music fadeout 3.0
    play sound sfx_ketuk_pintu

    b_unknown "Anee, waktunya bangun."

    show yuura scared at center, shake_custom, speaking

    play music bgm_scene_2_rock loop

    b_yuura "(ANJIR, TERNYATA ADA ORANG LAIN JUGA DI SINI)"

    show yuura scared at center, idle

    b_narrator "Aku segera memutar otakku, dan menemukan jawaban..."
    b_narrator "LARI SEBELUM KETAHUAN !!"
    b_narrator "Tepat ketika pintu kamar terbuka sempurna, aku menerjang keluar dan melesat bagai kilat."
    b_narrator "Tak menyadari bahwa orang yang membukakan pintu terjatuh karenaku, tapi peduli apa aku."

    show yuura scared at center, speaking

    b_yuura "Argh dimana sih... Ah ini dia !"

    show yuura scared at center, idle

    b_narrator "Setelah kutembakan grappling gun ku dan melesat tanpa melihat ke belakang."
    
    hide yuura scared with easeoutleft

    return