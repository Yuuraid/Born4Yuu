# label start:

label scene_4:
    scene black #sementara
    $ quick_menu = True
    # scene Kuil kecil with Dissolve(2.0)
    # play music "audio/bgm/kuil.ogg" fadein 1.0
    show Yuura at center
    with Dissolve(1.0)
    "Aku terus berjalan, melewati pepohonan yang entah kenapa sangat familiar bagiku. Sepertinya aku sudah berputar-putar di tempat ini selama berjam-jam tanpa menemukan jalan keluar."
    "Kaki ku lemas, rasanya sangat sakit sekali. Aku benar-benar berjalan-jalan sepanjang hari tapi tetap saja berakhir di tempat yang sama."
    "Sampai akhirnya aku mendengar suara dari sebuah gitar yang menuntunku menuju sebuah kuil kecil di dalam hutan."
    "Aku melihat sekitar, seraya mencari siapa yang memainkan gitar di hutan ini."
    "Aku berjalan dengan tubuh yang terhuyung-huyung, rasanya sangat tubuhku seperti dipukul palu besar."
    "Aku mencari disekitar dengan harapan bahwa aku akan bertemu seseorang. Tanpa ku sadari seseorang datang menghampiriku dari belakang, membuatku berteriak kencang"
    y "AHH !!" # buat gimmick biar karakternya loncat
    hide Yuura # harusnya geser aja ke kiri
    show Yuura at left
    show Haruto at right
    with Dissolve(0.5)
    u "Aneeki ?? Kenapa kamu bisa ada di sini ?"
    y "(Sepertinya dia mengenaliku, sebaiknya aku berpura-pura mengenalnya saja)"
    y "AH... em aku sedang jalan-jalan saja kok."
    u "Oh begitukah ? Bukannya jam segini harusnya kamu masih di penginapan ?"
    y "Ah... Em... Aku hanya bosan saja hahaha."
    u "Kenapa kamu terlihat sangat berantakan ? Apa kamu baik-baik saja ?"
    y "I-itu tidak penting sekarang, b-bisakah kamu menemani ku menuju jalan keluar dari hutan ini ?"
    u "Tentu ? Tapi tumben banget kamu ingin ditemani seperti ini. Biasanya juga kamu pergi sendiri."
    y "K-karena aku sudah terlalu lelah berkeliling hutan ini, makanya aku minta ditemani."
    "Dia tampak bingung dengan alibiku, tapi dia tetap percaya padaku dengan sepenuh hatinya."
    u "Baiklah biar aku antarkan kamu kembali ke penginapan."
    y "Penginapan? Bangunan besar yang bergaya jepang itu ? K-kenapa kita harus kesana ?"
    u "Loh ? Bukannya jalan keluar dari hutan ini memang di penginapan ? Anee kamu yakin baik-baik saja ?"
    y "Y-ya… aku baik-baik saja, um…"
    h "Haruto anee, namaku Haruto."
    "Haruto hanya bisa terdiam dan tertawa kecil melihat diriku yang seperti orang linglung."
    y "Haruto, mengapa kamu mau membantuku ?"
    "Aku menatapnya dengan keheranan, karena sepanjang tadi pagi aku terus saja mengalami kesialan membuatku curiga padanya."
    h "Hahaha... Pertanyaan macam apa itu Anee ? Tentu saja aku membantumu karena kamu selalu membantuku."
    "Aku bingung dengan maksudnya, tapi aku seperti merasakan sesuatu yang nostalgia dalam dirinya."
    "Haruto pun mengantarkan diriku sampai di depan gerbang penginapan, dia pun pamit karena masih ada banyak hal yang harus dia lakukan."
    "Aku berterimakasih banyak pada Haruto atas kebaikannya. Dia hanya tersenyum sembari berjalan menjauh menuju hutan, dan menghilang dari pandanganku."
    $ quick_menu = False

    return