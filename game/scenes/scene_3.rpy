# label start:

label scene_3:
        # # scene hutan # sementara
        # scene hutan with Dissolve(2.0)
        # $ quick_menu = True
    
    # BG hutan taman

    nd_narrator_brown "Aku berlari, terus berlari. Tanpa sekalipun melihat ke belakangku, aku berlari tanpa henti berharap mereka semua tidak mengejar diriku lagi."
        # show yuura normal animated at center
        # with Dissolve(2.0)
    
    nd_yuura_brown "*huft huft..."
    # play music "audio/bgm/hutan.ogg" fadein 1.0
    
    nd_yuura_brown "Argghhh... Ini gila ! Bisa-bisanya aku terbangun di tempat kayak gini ?! Huah..."
    
    nd_narrator_brown "Nafasku tersengal-sengal karena berlarian terus sepannjang waktu."
    
    nd_narrator_brown "Aku melanjutkan perjalananku dengan rasa lelah yang luar biasa, sebelum akhirnya aku memutuskan untuk duduk di dekat sebuah pohon besar."
    
    nd_narrator_brown "Aku berusaha menenangkan diriku, menarik nafas secara perlahan dan mulai memikirkan segalanya."
    
    nd_yuura_brown "(Bagaimana aku tiba-tiba berada di tempat ini ? APa yang telah terjadi ? Mengapa ini semua terjadi ? Dan kenapa hanya aku saja yang muncul di sini ?)"

        # hide yuura normal animated
        # with fade
        # show yuura normal animated at left # harusnya cuma geser, tapi ga ngerti maenin x y nya
        # with Dissolve(1.0)
        # show Unknown at right # karakter terlalu kanan dan terlalu kiri
        # with Dissolve(1.0)
    nd_unknown_brown "Capek kan lari-lari ?"
    
    nd_narrator_brown "Aku terkejut mendengar suara yang entah dari mana asalnya. Aku melihat sekitar dan merasakan adanya seseoarng di balik pohon yang kusandari."
    
    wd_pria_brown "Jangan takut, aku tidak menggigit."
    
    nd_narrator_brown "Aku merasa terkejut, bingung, sekaligus bertanya-tanya dari mana orang ini berasal. Aku tidak tahu apapun tentangnya, yang aku tahu suara ini adalah suara laki-laki."

    wd_pria_brown "Kamu... bukan berasal dari dunia ini kan ?"

    nd_yuura_brown "S-siapa kamu ??? CEPAT JAWAB DARI MANA KAMU TAHU TENTANGKU !"
    
    wd_pria_brown "Hanya intuisiku saja."
    
    nd_yuura_brown "Aku sudah tidak mengerti lagi dengan tempat ini, tadi orang-orang mengejarku." 
    
    nd_yuura_brown "Sekarang ada orang aneh yang berbicara denganku di balik pohon ! Lalu apa ? Aku akan melihat orang-orang masuk penjara ?"
    
    wd_pria_brown "..."

    nd_yuura_brown "Aku capek... Aku mau pulang... Tidak seharusnya diriku di sini..."
    
    wd_pria_brown "Hey... jangan menangis, aku tidak sanggup melihat wanita menangis tepat di hadapanku."
    
    nd_narrator_brown "Aku mengangkat kepalaku dan melihat bahwa berdiri seseoarng di hadapanku, dengan jubah panjang dan topi fedora yang menutupi wajah."
    
    nd_narrator_brown "Melihat sosoknya yang tinggi itu, membuatku tanpa sadar memeluknya dan langsung menangis."
    
    nd_narrator_brown "Aku menceritakan semuanya tanpa kusadari, orang itu hanya diam membiarkanku mengeluarkan semuanya."
    
    # Start BGM Jade

    nd_narrator_brown "Setelah cukup puas bercerita, aku menyadari sesuatu yang janggal."
    
    nd_narrator_brown "Aku mengeluarkan botol yang sama dengan di kamar sebelumnya, membuatku bertanya-tanya bagaimana bisa dia terbawa bersamaku."
    
    nd_narrator_brown "Aku melihat sebuah ukiran bertuliskan dengan huruf jepang, Yozakura Yuura."

    nd_narrator_brown "Aku terkejut bukan main."

    nd_yuura_brown "(Kenapa namaku ada di sini ? Bahkan cara menulisnya sama persis seperti diriku)"

    nd_narrator_brown "Aku semakin bingung dengan apa yang terjadi. Baru beberapa saat yang lalu aku dikejar oleh ratusan orang dan sekarang aku malah membawa benda berharga atas namaku sendiri."

    nd_narrator_brown "Aku benar-benar tidak mengerti sekaligus bingung setelah melihat ukiran nama pada botol ini."

    nd_narrator_brown "Tapi mana mungkin aku mampu membeli botol semahal ini, makan saja sudah sangat sulit. Mana mungkin aku punya botol semewah ini."


    wd_pria_brown "Oh ? Kamu membawa benda yang menarik~"
    
    nd_yuura_brown "Apa maksudmu ? Lagipula aku ingat dengan jelas bahwa botol ini tidak bersamaku ?"
    
    wd_pria_brown "Lalu bagaimana benda itu bisa bersamamu ?"
    
    nd_yuura_brown "Entahlah... Jika botol ini kubawa di dalam bajuku, sudah pasti akan sangat sulit membawanya sambil dikejar oleh banyak orang."
    
    wd_pria_brown "Mungkin saja itu adalah takdir."
    
    nd_yuura_brown "Takdir ? Apa maksmudmu semua hal bodoh ini adalah takdir bagiku ?"
    
    wd_pria_brown "Mungkin saja~"
    
    nd_yuura_brown "Ga, ga masuk akal. Mustahil, lebih baik aku pergi keluar dan menjual botol ini."
    
    nd_narrator_brown "Aku berjalan melewati pria misterius itu"
    
    wd_pria_brown "Coba saja, jika kamu memang bisa keluar."
        # hide Unknown
        # with fade
    
    nd_yuura_brown "Apa maksud...mu ??? Ke mana orang itu pergi ?"
    
    nd_narrator_brown "Aku menoleh ke belakang dan terdiam sejenak, bertanya-tanya ke mana pria itu pergi, tapi aku langsung mengalihkan perhatianku saat ini, aku sudah tidak peduli lagi, dan langsung pergi mencari jalan keluar dari sini."
        # $ quick_menu = False


    # play music "audio/bgm/hutan.ogg" fadeout 1.0

    return
