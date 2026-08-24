# label start:

label _scene_3:
    # scene hutan # sementara
    scene hutan with Dissolve(2.0)
    $ quick_menu = True
    "Aku berlari, terus berlari. Tanpa sekalipun melihat ke belakangku, aku berlari tanpa henti berharap mereka semua tidak mengejar diriku lagi."
    show yuura normal animated at center
    with Dissolve(2.0)
    y "*huft huft..."
    # play music "audio/bgm/hutan.ogg" fadein 1.0
    y "Argghhh... Ini gila ! Bisa-bisanya aku terbangun di tempat kayak gini ?! Huah..."
    "Nafasku tersengal-sengal karena berlarian terus sepannjang waktu."
    "Aku melanjutkan perjalananku dengan rasa lelah yang luar biasa, sebelum akhirnya aku memutuskan untuk duduk di dekat sebuah pohon besar."
    "Aku berusaha menenangkan diriku, menarik nafas secara perlahan dan mulai memikirkan segalanya."
    y "(Bagaimana aku tiba-tiba berada di tempat ini ? APa yang telah terjadi ? Mengapa ini semua terjadi ? Dan kenapa hanya aku saja yang muncul di sini ?)"
    hide yuura normal animated
    with fade
    show yuura normal animated at left # harusnya cuma geser, tapi ga ngerti maenin x y nya
    with Dissolve(1.0)
    show Unknown at right # karakter terlalu kanan dan terlalu kiri
    with Dissolve(1.0)
    u "Capek kan lari-lari ?"
    "Aku terkejut mendengar suara yang entah dari mana asalnya. Aku melihat sekitar dan merasakan adanya seseoarng di balik pohon yang kusandari."
    u "Jangan takut, aku tidak menggigit."
    "Aku merasa terkejut, bingung, sekaligus bertanya-tanya dari mana orang ini berasal. Aku tidak tahu apapun tentangnya, yang aku tahu suara ini adalah suara laki-laki."
    u "Kamu... bukan berasal dari dunia ini kan ?"
    y "S-siapa kamu ??? CEPAT JAWAB DARI MANA KAMU TAHU TENTANGKU !"
    u "Hanya intuisiku saja."
    y "Aku sudah tidak mengerti lagi dengan tempat ini, tadi orang-orang mengejarku. Sekarang ada orang aneh yang berbicara denganku di balik pohon ! Lalu apa ? Aku akan melihat orang-orang masuk penjara ?"
    u "..."
    y "Aku capek... Aku mau pulang... Tidak seharusnya diriku di sini..."
    u "Hey... jangan menangis, aku tidak sanggup melihat wanita menangis tepat di hadapanku."
    "Aku mengangkat kepalaku dan melihat bahwa berdiri seseoarng di hadapanku, dengan jubah panjang dan topi fedora yang menutupi wajah."
    "Melihat sosoknya yang tinggi itu, membuatku tanpa sadar memeluknya dan langsung menangis."
    "Aku menceritakan semuanya tanpa kusadari, orang itu hanya diam membiarkanku mengeluarkan semuanya."
    "Setelah cukup puas bercerita, aku menyadari sesuatu yang janggal."
    "Aku mengeluarkan botol yang sama dengan di kamar sebelumnya, membuatku bertanya-tanya bagaimana bisa dia terbawa bersamaku."
    "Aku melihat sebuah ukiran bertuliskan dengan huruf jepang, Yozakura yuura normal animated."
    "Aku terkejut bukan main."
    y "(Kenapa namaku ada di sini ? Bahkan cara menulisnya sama persis seperti diriku)"
    "Aku semakin bingung dengan apa yang terjadi. Baru beberapa saat yang lalu aku dikejar oleh ratusan orang dan sekarang aku malah membawa benda berharga atas namaku sendiri."
    "Aku benar-benar tidak mengerti sekaligus bingung setelah melihat ukiran nama pada botol ini."
    "Tapi mana mungkin aku mampu membeli botol semahal ini, makan saja sudah sangat sulit. Mana mungkin aku punya botol semewah ini."
    u "Oh ? Kamu membawa benda yang menarik~"
    y "Apa maksudmu ? Lagipula aku ingat dengan jelas bahwa botol ini tidak bersamaku ?"
    u "Lalu bagaimana benda itu bisa bersamamu ?"
    y "Entahlah... Jika botol ini kubawa di dalam bajuku, sudah pasti akan sangat sulit membawanya sambil dikejar oleh banyak orang."
    u "Mungkin saja itu adalah takdir."
    y "Takdir ? Apa maksmudmu semua hal bodoh ini adalah takdir bagiku ?"
    u "Mungkin saja~"
    y "Ga, ga masuk akal. Mustahil, lebih baik aku pergi keluar dan menjual botol ini."
    "Aku berjalan melewati pria misterius itu"
    u "Coba saja, jika kamu memang bisa keluar."
    hide Unknown
    with fade
    y "Apa maksud...mu ??? Kemana orang itu pergi ?"
    "Aku menoleh ke belakang dan terdiam sejenak, bertanya-tanya kemana pria itu pergi, tapi aku langsung mengalihkan perhatianku saat ini, aku sudah tidak peduli lagi, dan langsung pergi mencari jalan keluar dari sini."
    $ quick_menu = False


    # play music "audio/bgm/hutan.ogg" fadeout 1.0

    return
