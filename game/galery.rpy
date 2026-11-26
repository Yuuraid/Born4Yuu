init python:
    # Example: if your CG is 1920x1080 and your screen is 1280x720,
    # 1280 / 1920 = 0.6667 to fit the full width inside the screen.
    CG_FIT_ZOOM = 0.6667
    CG_ZOOM_STEP = 0.15
    CG_MIN_ZOOM = 0.25
    CG_MAX_ZOOM = 2.0

transform cg_viewer_transform(z):
    anchor (0.5, 0.5)
    pos (0.5, 0.5)
    zoom z

screen cg_fullscreen_viewer(img_path):
    modal True
    tag menu

    # Start fitted to the screen
    default cg_zoom = CG_FIT_ZOOM

    # Optional keyboard shortcuts for zoom and close
    key "K_EQUALS" action SetScreenVariable("cg_zoom", min(CG_MAX_ZOOM, cg_zoom + CG_ZOOM_STEP))
    key "K_PLUS" action SetScreenVariable("cg_zoom", min(CG_MAX_ZOOM, cg_zoom + CG_ZOOM_STEP))
    key "K_KP_PLUS" action SetScreenVariable("cg_zoom", min(CG_MAX_ZOOM, cg_zoom + CG_ZOOM_STEP))
    key "K_MINUS" action SetScreenVariable("cg_zoom", max(CG_MIN_ZOOM, cg_zoom - CG_ZOOM_STEP))
    key "K_KP_MINUS" action SetScreenVariable("cg_zoom", max(CG_MIN_ZOOM, cg_zoom - CG_ZOOM_STEP))
    key "K_0" action SetScreenVariable("cg_zoom", CG_FIT_ZOOM)
    key "K_ESCAPE" action ShowMenu("cg_gallery")

    add "#000000ee"

    # Clicking the dark backdrop closes the viewer
    button:
        xfill True
        yfill True
        background None
        action ShowMenu("cg_gallery")

    # Image scaled by cg_zoom and centered
    add img_path at cg_viewer_transform(cg_zoom)

    # On-screen zoom & fit controls
    hbox:
        align (0.5, 0.96)
        spacing 12

        textbutton "Zoom Out (-)":
            action SetScreenVariable("cg_zoom", max(CG_MIN_ZOOM, round(cg_zoom - CG_ZOOM_STEP, 4)))

        textbutton "Fit Screen (0)":
            action SetScreenVariable("cg_zoom", CG_FIT_ZOOM)

        textbutton "100% Native":
            action SetScreenVariable("cg_zoom", 1.0)

        textbutton "Zoom In (+)":
            action SetScreenVariable("cg_zoom", min(CG_MAX_ZOOM, round(cg_zoom + CG_ZOOM_STEP, 4)))

        textbutton "Close":
            action ShowMenu("cg_gallery")

init python:
    # Stores unlocked CG keys in persistent data (survives across saves/replays)
    if persistent.unlocked_cgs is None:
        persistent.unlocked_cgs = set()

    def unlock_cg(cg_id):
        persistent.unlocked_cgs.add(cg_id)

    def is_cg_unlocked(cg_id):
        return cg_id in persistent.unlocked_cgs
    # # Create the Gallery instance
    # g = Gallery()

    # # Transition used when switching images inside the gallery
    # g.transition = dissolve

    # # Optional: custom locked image (defaults to a blank/missing image if omitted)
    # g.locked_button = "assets/props/locked_thumb.png"

    # # --- CG 1: Beach Sunset ---
    # # g.button("cg meja_kamar_yuura")
    # # g.unlock_image("cg_meja_kamar_yuura")
    
    # # g.button("cg arc_1_scene_03_shoot_4")
    # # g.unlock_image("cg_arc_1_scene_03_shoot_4")

    # # g.button("cg arc_1_scene_03_shoot_5")
    # # g.unlock_image("cg_arc_1_scene_03_shoot_5")

    # # g.button("cg arc_2_scene_06_shoot_4")
    # # g.unlock_image("cg_arc_2_scene_06_shoot_4")

    # # g.button("cg arc_3_scene_14_shoot_3")
    # # g.unlock_image("cg_arc_3_scene_14_shoot_3")

    # # g.button("cg arc_3_scene_14_shark_shoot_04")
    # # g.unlock_image("cg_arc_3_scene_14_shark_shoot_04")

    # # g.button("cg arc_3_scene_15_shoot_05")
    # # g.unlock_image("cg_arc_3_scene_15_shoot_05")

    # # g.button("cg arc_3_scene_16_cekik_shoot_03")
    # # g.unlock_image("cg_arc_3_scene_16_cekik_shoot_03")

    # # g.button("cg arc_3_scene_16_cekik_shoot_04")
    # # g.unlock_image("cg_arc_3_scene_16_cekik_shoot_04")

    # # g.button("cg arc_3_scene_16_aer_cg")
    # # g.unlock_image("cg_arc_3_scene_16_aer_cg")

    # # g.button("cg arc_3_scene_16_aer_aura_01")
    # # g.unlock_image("cg_arc_3_scene_16_aer_aura_01")

    # # g.button("cg arc_3_scene_16_balikin_3")
    # # g.unlock_image("cg_arc_3_scene_16_balikin_3")

    # # g.button("cg arc_3_scene_17_shoot_04")
    # # g.unlock_image("cg_arc_3_scene_17_shoot_04")

    # # g.button("cg arc_3_scene_18_yuura_nahan_shoot_3")
    # # g.unlock_image("cg_arc_3_scene_18_yuura_nahan_shoot_3")

    # # g.button("cg arc_3_scene_18_lempar_yoyu_shoot_4")
    # # g.unlock_image("cg_arc_3_scene_18_lempar_yoyu_shoot_4")

    # # g.button("cg arc_3_scene_19_credit")
    # # g.unlock_image("cg_arc_3_scene_19_credit")

    cg_list = [
        ("cg arc_1_scene_01", "cg_arc_1_scene_01_primary_taro_foto-meja"),
        ("cg arc_1_scene_03_shoot_4", "cg_arc_1_scene_03_shoot_4"),
        ("cg arc_1_scene_03_shoot_5", "cg_arc_1_scene_03_shoot_5"),
        ("cg arc_2_scene_06_shoot_4", "cg_arc_2_scene_06_shoot_4"),
        ("cg arc_3_scene_14_shoot_3", "cg_arc_3_scene_14_shoot_3"),
        ("cg arc_3_scene_14_shark_shoot_04", "cg_arc_3_scene_14_shark_shoot_04"),
        ("cg arc_3_scene_15_shoot_05", "cg_arc_3_scene_15_shoot_05"),
        ("cg arc_3_scene_16_cekik_shoot_03", "cg_arc_3_scene_16_cekik_shoot_03"),
        ("cg arc_3_scene_16_cekik_shoot_04", "cg_arc_3_scene_16_cekik_shoot_04"),
        ("cg arc_3_scene_16_balikin_3", "cg_arc_3_scene_16_balikin_3"),
        ("cg arc_3_scene_16_aer_aura_01", "cg_arc_3_scene_16_aer_aura_01"),
        ("cg arc_3_scene_16_aer_aura_02", "cg_arc_3_scene_16_aer_aura_02"),
        ("cg arc_3_scene_16_aer_cg", "cg_arc_3_scene_16_aer_cg"),
        ("cg arc_3_scene_17_shoot_03", "cg_arc_3_scene_17_shoot_03"),
        ("cg arc_3_scene_17_shoot_04", "cg_arc_3_scene_17_shoot_04"),
        ("cg arc_3_scene_18_yuura_nahan_shoot_3", "cg_arc_3_scene_18_yuura_nahan_shoot_3"),
        ("cg arc_3_scene_18_lempar_yoyu_shoot_4", "cg_arc_3_scene_18_lempar_yoyu_shoot_4"),
        ("cg arc_3_scene_19_credit", "cg_arc_3_scene_19_credit"),
    ]

# screen cg_gallery():
#     tag menu

#     # Use game_menu so you get standard navigation/return behavior
#     use game_menu(_("CG Gallery"), scroll="viewport"):

#         grid 4 6:
#             spacing 20
#             xalign 0.5

#             # Add one thumbnail button per CG
#             # add g.make_button(
#             #     "cg meja_kamar_yuura",
#             #     Transform("assets/cg/cg_arc_1_scene_01_primary_taro_foto-meja.png", xysize=(320, 180)),
#             #     xalign=0.5,
#             #     yalign=0.5,
#             # )
#             for btn_name, img_name in cg_list:
#                 imagebutton:
#                     idle Transform("assets/cg/{}.png".format(img_name), xysize=(320, 180))
#                     hover Transform("assets/cg/{}.png".format(img_name), xysize=(320, 180))
#                     xalign 0.5
#                     yalign 0.5
#                     action Show("cg_fullscreen_viewer", img_path="assets/cg/{}.png".format(img_name))

screen cg_gallery():
    tag menu

    use game_menu(_("CG Gallery"), scroll="viewport"):

        grid 4 6:
            spacing 20
            xalign 0.5

            for btn_name, img_name in cg_list:
                $ unlocked = is_cg_unlocked(img_name)
                $ thumb_path = "assets/cg/{}.png".format(img_name) if unlocked else "assets/props/locked_thumb.png"

                if unlocked:
                    imagebutton:
                        idle Transform(thumb_path, xysize=(320, 180))
                        hover Transform(thumb_path, xysize=(320, 180))
                        xalign 0.5
                        yalign 0.5
                        action Show("cg_fullscreen_viewer", img_path="assets/cg/{}.png".format(img_name))
                else:
                    imagebutton:
                        idle Transform(thumb_path, xysize=(320, 180))
                        hover Transform(thumb_path, xysize=(320, 180))
                        xalign 0.5
                        yalign 0.5
                        action NullAction()