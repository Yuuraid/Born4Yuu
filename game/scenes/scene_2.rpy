label scene_2:
    scene inn lorong pagi with dissolve
    play sound sfx_grappling
    b_narrator "Aku berlari, melompat, dan melesat sambil menyusuri lorong ini. Terlihat dari dinding dan lantainya, jelas ini menggunakan kayu yang berkualitas."
    b_narrator "Meski begitu, tetap akan kujadikan dinding-dinding di lorong ini sebagai target dari grappling ku."
    
    show sprite yuura_scared at center, idle with easeinright
    
    b_yuura "(Peduli apa aku dengan kerusakan di tempat ini)"

    show sprite yuura_scared at center, idle

    b_narrator "Pelarian tidak lah mulus, aku harus menghindari orang-orang yang berlalu lalang di lorong ini, belum lagi aku sempat menimpuk wajah seseorang yang berpakaian serba cokelat dengan lututku."
    b_narrator "Melesat di tempat sempit nan ramai ini membuatku kesulitan dalam melaju. Akhirnya setelah cukup panjang menyusuri lorong ini, aku menemukan titik terang di ujung sana."
    
    # hid inn ruang_tamu_1
    play sound sfx_grappling
    hide sprite yuura_scared with easeoutleft
    scene inn ruang_tamu_1 with dissolve

    show sprite yuura_scared at center, idle with easeinright
    pause 0.5
    show sprite yuura_happy at center, speaking
    
    b_yuura "Akhirnya..."

    show sprite yuura_scared at center, idle
    b_narrator "Tapi aku salah kira, bukannya jalan keluar, aku malah mendarat di tempat yang penuh dengan banyak orang di sini."
    b_narrator "Aku langsung panik, bisa-bisa aku malah pergi ke ruangan utama di tempat ini. Segera aku tembak grappling ku."
    b_narrator "Tapi karena panik, arah tembaknya jadi tak karuan. Tertembak menyamping, tidak mengenai target yang menyebabkan harus melompat secara manual, dan membuatku menabrak beberapa orang yang tentu itu menyakitkan."
    b_narrator "Akhirnya setelah 2 menit berlalu, aku berhasil mencapai atap dari tempat terbuka nan luas itu."
    b_narrator "Orang-orang di bawah menatapku dengan tatapan bingung, seperti melihat orang gila yang sehabis berbuat kericuhan, tapi peduli apa aku."

    play sound sfx_grappling
    hide sprite yuura_scared with easeoutleft

    b_narrator "Setelah melihat sekitar untuk mencari jalan keluar, aku melihat sebbuah gerbang kayu merah besar (Torii) tang terlihat mencolok, tidak salah lagi... karena lorong yang ada gerbangnya berbeda dengan lorong lainnya."

    scene hutan kuil entrance with dissolve

    play sound sfx_grappling
    show sprite yuura_happy at center, speaking with easeinright
    b_yuura "Finally !"
    show sprite yuura_happy at center, idle
    b_narrator "Kutembakkan segera grappling ku dan melesat menuju jalan keluar. Mendarat dan berlari sekencang-kencangnya."
    show sprite yuura_happy at center, speaking
    b_yuura "(Semoga tak ada yang mengejarku, pagi ku sudah cukup sial untuk membuatku menggerutu.)"
    show sprite yuura_scared at center, speaking

    stop music fadeout 3.0

    return