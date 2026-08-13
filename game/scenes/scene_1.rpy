# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Yuura")
define u = Character("???")
define h = Character("Haruto")
define taro = Character("Taro")
define shark = Character("Shark")
define seiya = Character("seiya")
define akasyah = Character("Akasyah")
define dityo = Character("Dityo")
define axia = Character("Axiaregis")
define josua = Character("Josua")
define ibe = Character("Ibe")
define nicholas = Character("Nicholas")
define lark = Character("Lark")
define yc = Character("Yc")
define aergia = Character("Aergia")

label scene_1:
    scene black

    $ quick_menu = True
    # play music start with fadein 1.0 -> define dulu
    # play sound "audio/sfx/knock_door.ogg"
    "Terdengar seperti ketukan pintu" 
    $ quick_menu = False
    show kamar pagi at panorama_kiri_ke_kanan with Dissolve(1.0)
    pause 4.0
    scene kamar pagi with Dissolve(2.0) 
    pause 1.0
    $ quick_menu = True
    show yuura normal animated at center
    with moveinbottom
    # with nongol_dari_bawah # <-- blm jadi :""
    y "Iya iya... Hooam..." 
    "Aku terbangun dari tidurku,{w} duduk sebentar sebelum benar-benar beranjak dari kasurku."
    "Rasanya benar-benar malas untuk beranjak dari kas-"
    "..."
    show layer master at shake_custom
    y "(MANA DASARNYA ?!)"
    "Aku langsung sadar ketika menyadari ada yang janggal,{w} dan mendapati bahwa aku tidur di kasur yang dibentangkan di lantai?..."
    "Aku segera melihat sekitar." 
    "Dan benar saja." 
    "Ini bukan kamarku."
    y "Kemarin aku salah masuk kamar apa gimana dah?{w} Kok bisa-bisanya kebangun di sini?"
    "Aku meminggirkan selimut yang selama ini menutupi setengah badanku dan berdiri melihat sekitar."
    "Aku melihat cermin, cermin itu memantulkan rupaku yang sama persis sebelum aku tertidur karena kelelahan."
    y "Nggak ada yang aneh sih..."
    "Aku berjalan kecil, mengelilingi kamar nan asing ini yang entah kenapa... terasa familiar bagiku."
    "Lukisan-lukisan aneh yang tergantung di dinding kamar, juga topeng-topeng yang bergantung di dinding agak membuat suasana agak seram"
    "belum lagi kamar yang redup yang sepertinya di desain untuk membuat pemilik kamar ini susah untuk bangun."
    # play sound "audio/sfx/cubit_pipi.ogg"
    "*Sfx cubit pipi"
    y "Aduh..."
    "(Aku benar-benar udah kebangun nih... Tapi kok bisa yah aku tidur di sini !?...)"
    "Aku terus keliling melihat sekitar, mana tau menemukan hal yang menarik."
    "Aku mendekati sebuah zirah yang terpajang gagah beserta pedang dengan sarungnya yang berwarna merah muda."
    y "Uh... Kayaknya pemilik kamar ini adalah orang yang menakutkan..."
    "Didekat zirah itu, terdapat meja kecil yang di atasnya terdapat alat penghisap tembakau dan topeng berbentuk hewan."
    y "Beneran kriminal ini mah..."
    "Tak jauh dari sana, aku melihat sebuah meja yang di atasnya terdapat banyak sekali foto."
    "Ketika kudekati, terlihat jelas foto-foto itu adalah momen kebersamaan si pemilik kamar dengan teman maupun keluarganya."
    "Aku mengambil sebuah foto dan mengamati lebih jelas."
    y "ANJIR!!"
    y "NIH ORANG MIRIP BANGET SAMA GUE COK !"
    #y "NIH ORANG MIRIP BANGET SAMA AKU!!" <-- Kok lebih terdengar seperti ane ya :"v imo lebih enak kalo konsisten, aku ya aku, gua gue ya gua gue
    "Aku mengammati beberapa foto lainnya. Benar saja, perempuan yang mirip denganku itu nampaknya merupakan pemilik kamar ini."
    "Aku meletakkan kembali foto-foto itu ke tempatnya semula."
    y "Kok bisa yah, ada orang yang beneran mirip sama aku...?"
    "Ditengah kebingungan itu, aku melihat sebuah benda yang bersinar.Pandanganku langsung tertuju pada benda itu dan melesat mendekatinya."
    "Sebuah botol berwarna hijau zamrud yang sejuk dan cerah, tidak salah lagi kalau botol ini terbuat dari batu jade yang berharga !"
    "Aku mengambil botol zamrud itu dan memandangi keindahannya. Hingga..."
    u "Anee, waktunya bangun."
    y "(ANJIR, TERNYATA ADA ORANG LAIN JUGA DI SINI)"
    "Aku segera memutar otakku, dan menemukan jawaban..."
    "LARI SEBELUM KETAHUAN !!"
    "Tepat ketika pintu kamar terbuka sempurna, aku menerjang keluar dan melesat bagai kilat."
    "Tak menyadari bahwa orang yang membukakan pintu terjatuh karenaku, tapi peduli apa aku."
    y "Argh dimana sih... Ah ini dia !"
    "Setelah kutembakan grappling gun ku dan melesat tanpa melihat ke belakang."
    $ quick_menu = False

    return