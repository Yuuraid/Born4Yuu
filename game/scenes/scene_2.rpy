# label start:

label scene_2:
    # scene lorong #sementara
    # scene lorong with Dissolve(2.0)
    # $ quick_menu = True
    # play sound "audio/sfx/grappling.ogg"
    # show layer master at shake_custom
    # "*sfx grappling"
    # show yuura normal animated at center
    # with Dissolve(2.0)
    
    # BG: inn lorong pagi

    scene transition_screen orange concentrationline02_w with dissolve
    show yuura scared eff_sweat_w at center, speaking with easeinright

    nd_yuura_black "*huft huft..."

    show yuura at idle

    nd_narrator_black "Aku berlari, melompat, dan melesat sambil menyusuri lorong ini. Terlihat dari dinding dan lantainya, jelas ini menggunakan kayu yang berkualitas."

    nd_narrator_black "Meski begitu, tetap akan kujadikan dinding-dinding di lorong ini sebagai target dari grappling ku."

    show yuura at speaking
    nd_yuura_black "(Peduli apa aku dengan kerusakan di tempat ini)"

        # hide yuura normal animated
        # with Dissolve(2.0)
        # # play sound "audio/sfx/grappling.ogg 2/3 kali"
        # show layer master at shake_custom

    hide yuura with easeoutleft

    nd_narrator_black "Pelarian tidak lah mulus, aku harus menghindari orang-orang yang berlalu lalang di lorong ini, belum lagi aku sempat menimpuk wajah seseorang yang berpakaian serba cokelat dengan lututku."

    nd_narrator_black "Melesat di tempat sempit nan ramai ini membuatku kesulitan dalam melaju. Akhirnya setelah cukup panjang menyusuri lorong ini, aku menemukan titik terang di ujung sana."
    
        # show yuura normal animated at center
        # with Dissolve(2.0)
    scene inn ruang_tamu_1 with fade
    show yuura netral at center, speaking with easeinright
    nd_yuura_brown "Akhirnya..."
    
    # BG inn ruang_tamu_1
    
    show yuura at idle
    nd_narrator_brown "Tapi aku salah kira, bukannya jalan keluar, aku malah mendarat di tempat yang penuh dengan banyak orang di sini."

    show yuura scared eff_sweat_w at pacing_left_right
    nd_narrator_brown "Aku langsung panik, bisa-bisa aku malah pergi ke ruangan utama di tempat ini. Segera aku tembak grappling ku."

    nd_narrator_brown "Tapi karena panik, arah tembaknya jadi tak karuan. Tertembak menyamping, tidak mengenai target yang menyebabkan harus melompat secara manual, dan membuatku menabrak beberapa orang yang tentu itu menyakitkan."

    hide yuura with easeoutleft
    
    scene inn rooftop with dissolve
    show yuura netral at center, idle with easeinright

    nd_narrator_brown "Akhirnya setelah 2 menit berlalu, aku berhasil mencapai atap dari tempat terbuka nan luas itu."

    nd_narrator_brown "Orang-orang di bawah menatapku dengan tatapan bingung, seperti melihat orang gila yang sehabis berbuat kericuhan, tapi peduli apa aku."
    
    show yuura at pacing_left_right

    nd_narrator_brown "Setelah melihat sekitar untuk mencari jalan keluar, aku melihat sebuah gerbang kayu merah besar (Torii) yang terlihat mencolok. Tidak salah lagi.. karena lorong yang ada gerbang di depannya berbeda dengan lorong lainnya.."
    
    scene hutan kuil entrance
    camera:
        # Initial position (zoomed out at the right side)
        zoom 2.0
        xalign 0.5
        yalign 0.0
        
        # Pan across to the left over 5 seconds
        ease 15.0 yalign 0.5
    with dissolve

    pause 5.0

    scene inn rooftop
    show yuura netral eff_exclamation at center, speaking
    camera:
        # Initial position (zoomed out at the right side)
        zoom 1.0
        xalign 0.0
        yalign 0.0
    with fade

    nd_yuura_brown "Finally !"
    
    # BG hutan kuil entrance

    show yuura at idle
    nd_narrator_brown "Kutembakkan segera grappling ku dan melesat menuju jalan keluar. Mendarat dan berlari sekencang-kencangnya."
    
    hide yuura with easeoutleft

    nd_yuura_brown "(Semoga tak ada yang mengejarku, pagi ku sudah cukup sial untuk membuatku menggerutu.)"
        # $ quick_menu = False

    return
