# label start:

label scene_6:
    # scene kamar Yuura with Dissolve(2.0)
    # play music softjazz fadein 1.0 -> define music dulu
    $ quick_menu = True
    show yuura normal animated at center
    with Dissolve(1.0)
    y "Ughhh... Kepalaku sakit banget..."
    "Aku terbangun dari pingsanku, entah sudah berapa lama tapi aku masih merasakan sakit disekujur tubuhku."
    y "Di mana ini? Kenapa rasanya sangat familiar..."
    "Aku memperhatikan sekitarku dengan seksama, menyadari bahwa aku kembali ke tempat aku bangun pertama kali."
    y "K-kenapa aku di sini !? {w}Tunggu... Apa jangan-jangan tadi aku mimpi ya ?"
    y "Ga, ga mungkin..."
    "Aku benar-benar merasa deja vu dengan kondisi diriku saat ini."
    y "Arghhhh... Aku sudah sangat lelah... Sebaiknya aku mandi, bauku sudah sangat buruk"
    "Aku mengambil handuk dan segera pergi ke onsen."
    # stop music softjazz fadeout 1.0
    # play audio byur -> define audio dulu
    "sfx *byuurrr"
    show layer master at shake_custom
    # scene onsen with Dissolve(2.0) ???
    "Suara percikan air yang membasahi tubuhku, aku mengelap seluruh bagian tubuhku. Bahkan bagian kaki yang paling bisa aku banggakan. Aku mengelap sela-sela jari kaki dengan sabun."
    # koreksi lagi docsnya
    "Baunya harum seperti bunga sakura yang mungkin bisa membuat laki-laki tergoda padaku."
    "Aku membersihkan bagian punggungku dengan sabun yang sama, membilas tiap keringat yang aku keluarkan sepanjang perjalanan."
    y "Ah~ enaknya..."
    y "Rasanya benar-benar puas dengan pemandian di gedung ini."
    "Aku mengambil air dan membilas sisa-sisa sabun dari tubuhku, dan mengeringkan sela-sela jari kakiku"
    "Setelah mandi, aku terkejut karena mendengar ketukan di pintu. Membuatku sedikit panik karena melupakan bahwa aku masih di tempat antah berantah."
    # play music fotokenangan fadein 1.0 -> define music dulu
    taro "Ane... Ini aku Tarochips, aku bawa makanan buat ane..."
    "Aku diam saja, tak membalas satu pun ucapannya."
    taro "Ane ? Kamu masih tidur ? Aku taruh di depan aja ya... Maaf sudah mengganggu istirahat ane."
    "Dia berjalan untuk pergi, tapi sebelum terlalu jauh dia menatap ke kamarku sekali lagi."
    taro "Ane... Apa pun yang terjadi, tolong... {w} jaga kesehatanmu, aku ga mau ngeliat ane pingsan lagi."
    taro "Apa ane kira aku tidak sedih melihatnya ? Aku sedih ane, melihat orang yang selalu menemaniku di penginapan ini tak berdaya di hadapanku."
    taro "(Suaranya sedikit gemetar, menahan perasaan sedih dalam batinnya.)" 
    # aku bingung nulisnya gmn yg atas ini
    taro "Aku emang yang paling tidak menonjol, aku emang yang paling ga mau diliat sama orang..."
    taro "Tapi yang ane harus tau, aku senang melihat ane bahagia... Jadi jangan sampai dirimu terluka lagi."
    "Dia berjalan pergi meninggalkan lorong. Suara langkah kakinya tidak terdedngar lagi."
    "Aku keluar dari kamar, mengambil makanan yang dia buat dan tersenyum tipis."
    "Merasakan sebuah ketulusan dari orang itu..."

    $ quick_menu = False

    return