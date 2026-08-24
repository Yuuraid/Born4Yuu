
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
image sprite aergia_netral = "images/sprite/Aergia/aergia_main_netral.png"

image sprite akasyah_happy = "images/sprite/Akasyah/akasyah_main_happy.png"
image sprite akasyah_arrogant = "images/sprite/Akasyah/akasyah_main_sombong.png"
image sprite akasyah_hurt = "images/sprite/Akasyah/akasyah_main_terluka.png"

image sprite axia_angry = "images/sprite/Axia/axia_main_marah.png"
image sprite axia_happy = "images/sprite/Axia/axia_main_senang.png"
image sprite axia_cute = "images/sprite/Axia/axia_main_sok-imut.png"
image sprite axia_summon = "images/sprite/Axia/axia_main_summon.png"
image sprite axia_summon_action = "images/sprite/Axia/axia_main_action-summon.png"
image sprite axia_sassy = "images/sprite/Axia/axia_main_tengil.png"
image sprite axia_hurt = "images/sprite/Axia/axia_main_terluka.png"

image sprite dawam_sad = "images/sprite/Dawam/dawam_main_murung.png"
image sprite dawam_happy = "images/sprite/Dawam/dawam_main_senang.png"
image sprite dawam_laugh = "images/sprite/Dawam/dawam_main_tertawa.png"
image sprite dawam_serious = "images/sprite/Dawam/dawam_main_serius.png"
image sprite dawam_hurt = "images/sprite/Dawam/dawam_main_terluka.png"

image sprite dityo_serious = "images/sprite/Dityo/dityo_main_serius.png"

image sprite haruto_confused = "images/sprite/Haruto/haruto_main_bingung.png"
image sprite haruto_tired = "images/sprite/Haruto/haruto_main_kewalahan.png"
image sprite haruto_serious = "images/sprite/Haruto/haruto_main_ngomong.png"
image sprite haruto_smile = "images/sprite/Haruto/haruto_main_senyum.png"
image sprite haruto_netral = "images/sprite/Haruto/haruto_main_tenang.png"

image sprite pria_netral = "images/sprite/Pria Misterius/pria_main_netral.png"

image sprite rian_netral = "images/sprite/Rian/rian_main_binar-binar.png"
image sprite rian_happy = "images/sprite/Rian/rian_main_senyum.png"
image sprite rian_angry = "images/sprite/Rian/rian_main_serius.png"
image sprite rian_hurt = "images/sprite/Rian/rian_main_terluka.png"

image sprite seiya_netral = "images/sprite/Seiya/seiya_main_netral.png"
image sprite seiya_happy = "images/sprite/Seiya/seiya_main_senyum.png"
image sprite seiya_angry = "images/sprite/Seiya/seiya_main_serius.png"
image sprite seiya_hurt = "images/sprite/Seiya/seiya_main_terluka.png"
image sprite seiya_sassy = "images/sprite/Seiya/seiya_main_tengil.png"

image sprite shark_happy = "images/sprite/Seiya/shark_main_senang.png"
image sprite shark_scared = "images/sprite/Seiya/shark_main_takut.png"
image sprite shark_worried = "images/sprite/Seiya/shark_main_khawatir.png"
image sprite shark_hurt = "images/sprite/Seiya/shark_main_terluka.png"
image sprite shark_sassy = "images/sprite/Seiya/shark_main_tengil.png"

# TODO: Add Tarochips

image sprite yuura_netral = "images/sprite/Yuura/yuura_main_netral.png"
image sprite yuura_happy = "images/sprite/Yuura/yuura_main_senyum.png"
image sprite yuura_scared = "images/sprite/Yuura/yuura_main_takut.png"
image sprite yuura_hurt = "images/sprite/Yuura/yuura_main_terluka.png"
image sprite yuura_sad = "images/sprite/Yuura/yuura_main_sedih.png"
image sprite yuura_angry = "images/sprite/Yuura/yuura_main_marah.png"