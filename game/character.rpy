
# Define Character Yuura

define b_narrator = Character("", window_background = "gui/textbox/brown.png")
define b_yuura = Character("Yuura", who_color = "#FDE08B", window_background = "gui/textbox/no_decoration/Yuura.png")
define b_unknown = Character("???", who_color = "#FDE08B", window_background = "gui/textbox/no_decoration/???.png")
define b_pria_misterius = Character("Pria Misterius", who_color = "#FDE08B", window_background = "gui/textbox/with_decoration/Pria Misterius.png")

# Define Character Lainnya

# define unknown = Character("???")

# ============

transform speaking:
    matrixcolor None
    parallel:
        easein 1.5 yoffset 20
        easeout 1 yoffset 0
        repeat

transform idle:
    matrixcolor TintMatrix("#777777") # Hex color code to darken/tint the sprite


# ============

# TODO: Wait more from Aergia
image aergia_netral = "images/sprite/Aergia/aergia_main_netral.png"

image akasyah_happy = "images/sprite/Akasyah/akasyah_main_happy.png"
image akasyah_arrogant = "images/sprite/Akasyah/akasyah_main_sombong.png"
image akasyah_hurt = "images/sprite/Akasyah/akasyah_main_terluka.png"

image axia_angry = "images/sprite/Axia/axia_main_marah.png"
image axia_happy = "images/sprite/Axia/axia_main_senang.png"
image axia_cute = "images/sprite/Axia/axia_main_sok-imut.png"
image axia_summon = "images/sprite/Axia/axia_main_summon.png"
image axia_summon_action = "images/sprite/Axia/axia_main_action-summon.png"
image axia_sassy = "images/sprite/Axia/axia_main_tengil.png"
image axia_hurt = "images/sprite/Axia/axia_main_terluka.png"

image dawam sad = "images/sprite/Dawam/dawam_main_murung.png"
image dawam happy = "images/sprite/Dawam/dawam_main_senang.png"
image dawam laugh = "images/sprite/Dawam/dawam_main_tertawa.png"
image dawam serious = "images/sprite/Dawam/dawam_main_serius.png"
image dawam hurt = "images/sprite/Dawam/dawam_main_terluka.png"

image dityo_serious = "images/sprite/Dityo/dityo_main_serius.png"

image haruto_confused = "images/sprite/Haruto/haruto_main_bingung.png"
image haruto_tired = "images/sprite/Haruto/haruto_main_kewalahan.png"
image haruto_serious = "images/sprite/Haruto/haruto_main_ngomong.png"
image haruto_smile = "images/sprite/Haruto/haruto_main_senyum.png"
image haruto_netral = "images/sprite/Haruto/haruto_main_tenang.png"

image pria_netral = "images/sprite/Pria Misterius/pria_main_netral.png"

image rian_netral = "images/sprite/Rian/rian_main_binar-binar.png"
image rian_happy = "images/sprite/Rian/rian_main_senyum.png"
image rian_angry = "images/sprite/Rian/rian_main_serius.png"
image rian_hurt = "images/sprite/Rian/rian_main_terluka.png"

image seiya_netral = "images/sprite/Seiya/seiya_main_netral.png"
image seiya_happy = "images/sprite/Seiya/seiya_main_senyum.png"
image seiya_angry = "images/sprite/Seiya/seiya_main_serius.png"
image seiya_hurt = "images/sprite/Seiya/seiya_main_terluka.png"
image seiya_sassy = "images/sprite/Seiya/seiya_main_tengil.png"

image shark_happy = "images/sprite/Seiya/shark_main_senang.png"
image shark_scared = "images/sprite/Seiya/shark_main_takut.png"
image shark_worried = "images/sprite/Seiya/shark_main_khawatir.png"
image shark_hurt = "images/sprite/Seiya/shark_main_terluka.png"
image shark_sassy = "images/sprite/Seiya/shark_main_tengil.png"

# TODO: Add Tarochips

image yuura netral = "images/sprite/Yuura/yuura_main_netral.png"
image yuura happy = "images/sprite/Yuura/yuura_main_happy.png"
image yuura scared = "images/sprite/Yuura/yuura_main_scared.png"
image yuura hurt = "images/sprite/Yuura/yuura_main_hurt.png"
image yuura sad = "images/sprite/Yuura/yuura_main_sad.png"
# image yuura angry = "images/sprite/Yuura/yuura_main_angry.png"

image yuura angry:
    "images/sprite/Yuura/yuura_main_angry.png"
    parallel:
        Movie(play="images/effects/output.webm", mask="images/effects/output.webm")
        zoom 0.3
        xanchor 0 yanchor 0
        xpos 0.35 ypos 0.15

transform yuura_height:
    xanchor 0 yanchor 0
    xpos 0.35 ypos 0.15

image angry_emotes:
    Movie(play="images/effects/output.webm", mask="images/effects/output.webm")
    zoom 0.3

# image angry_emotes = Movie(play="images/effects/output.webm")