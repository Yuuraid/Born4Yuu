# label start:

label scene_2:
    # scene lorong #sementara
    scene lorong with Dissolve(2.0)
    $ quick_menu = True
    # play sound "audio/sfx/grappling.ogg"
    show layer master at shake_custom
    "*sfx grappling"
    show yuura normal animated at center
    with Dissolve(2.0)
    y "*huft huft..."
    "Aku berlari, melompat, dan melesat sambil menyusuri lorong ini. Terlihat dari dinding dan lantainya, jelas ini menggunakan kayu yang berkualitas."
    "Meski begitu, tetap akan kujadikan dinding-dinding di lorong ini sebagai target dari grappling ku."
    y "(Peduli apa aku dengan kerusakan di tempat ini)"
    hide yuura normal animated
    with Dissolve(2.0)
    # play sound "audio/sfx/grappling.ogg 2/3 kali"
    show layer master at shake_custom
    "Pelarian tidak lah mulus, aku harus menghindari orang-orang yang berlalu lalang di lorong ini, belum lagi aku sempat menimpuk wajah seseorang yang berpakaian serba cokelat dengan lututku."
    "Melesat di tempat sempit nan ramai ini membuatku kesulitan dalam melaju. Akhirnya setelah cukup panjang menyusuri lorong ini, aku menemukan titik terang di ujung sana."
    
    show yuura normal animated at center
    with Dissolve(2.0)
    y "Akhirnya..."
    "Tapi aku salah kira, bukannya jalan keluar, aku malah mendarat di tempat yang penuh dengan banyak orang di sini."
    "Aku langsung panik, bisa-bisa aku malah pergi ke ruangan utama di tempat ini. Segera aku tembak grappling ku."
    "Tapi karena panik, arah tembaknya jadi tak karuan. Tertembak menyamping, tidak mengenai target yang menyebabkan harus melompat secara manual, dan membuatku menabrak beberapa orang yang tentu itu menyakitkan."
    "Akhirnya setelah 2 menit berlalu, aku berhasil mencapai atap dari tempat terbuka nan luas itu."
    "Orang-orang di bawah menatapku dengan tatapan bingung, seperti melihat orang gila yang sehabis berbuat kericuhan, tapi peduli apa aku."
    "Setelah melihat sekitar untuk mencari jalan keluar, aku melihat sebbuah gerbang kayu merah besar (Torii) tang terlihat mencolok, tidak salah lagi... karena lorong yang ada gerbangnya berbeda dengan lorong lainnya."
    y "Finally !"
    "Kutembakkan segera grappling ku dan melesat menuju jalan keluar. Mendarat dan berlari sekencang-kencangnya."
    y "(Semoga tak ada yang mengejarku, pagi ku sudah cukup sial untuk membuatku menggerutu.)"
    $ quick_menu = False

    return
