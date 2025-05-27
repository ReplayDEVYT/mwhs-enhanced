
define introlength = 11.03448
define beat = 0.3448

define iconsize = 0.15

define grid = 1980/7
define icon_xoffset = 0
define toprow_y = 160
define bottomrow_y = 900

define menupos_ax = grid*6 + icon_xoffset
define menupos_ay = toprow_y
define menustartpos_ax = 10
define menustartpos_ay = 2000

define menupos_cx = grid*4 + icon_xoffset
define menupos_cy = toprow_y
define menustartpos_cx = -400
define menustartpos_cy = -400

define menupos_ix = grid*2 + icon_xoffset
define menupos_iy = toprow_y
define menustartpos_ix = grid*2
define menustartpos_iy = -300

define menupos_hx = grid*3 + icon_xoffset
define menupos_hy = bottomrow_y
define menustartpos_hx = 600
define menustartpos_hy = 1500

define menupos_nx = grid*5 + icon_xoffset
define menupos_ny = bottomrow_y
define menustartpos_nx = grid*2
define menustartpos_ny = 3000

transform icon_enter(x=0, y=0, xstart=0, ystart=0):
    anchor (0.5, 0.5)
    zoom iconsize
    xpos xstart 
    ypos ystart
    parallel:
        easein introlength-0.8 xpos x
    parallel:
        easein introlength-0.8 ypos y

transform scroll(speed=4.0):
    xpan 0.0
    linear introlength/2 xpan 360
    repeat

transform logo_pos:
    zoom 0.8
    xalign 1.0
    yalign 0.5

transform floatlogo:
    logo_pos

transform flyinright_demotext:
    logo_pos
    xoffset 600
    easeout 1.0 xoffset 0
    block:
        ease 3.0 yoffset 15
        ease 3.0 yoffset -15
        repeat

transform flyinleft_overlay:
    xpos -300
    easeout 1.0 xpos 0

transform flyinleft_menutext:
    xoffset -300
    easeout 1.0 xoffset 0

#416e696d 6174696f 6e732066 6f722061 206d656e 75207363 7265656e 3f

transform zoomin:
    logo_pos
    zoom 0.0
    easeout 0.2 zoom 0.8

transform glitchlogo:
    parallel:
        floatlogo()
    parallel:
        alpha 1.0
        choice:
            pause 0.01
        choice:
            pause 4.0
        choice:
            pause 0.02
        choice:
            pause 2.0
        choice:
            pause 1.0
        alpha 0.0
        choice:
            pause 0.01
        choice:
            pause 0.05
        choice:
            pause 0.03
        repeat

transform whitetrans:
        alpha 1.0
        easeout 1 alpha 0.0

#57687920 676c6974 63683f

transform dance_rotate(x, y, dancing=True):
    zoom iconsize
    anchor (0.5, 0.5)
    xpos x
    ypos y
    easein beat*2 rotate -10 * dancing
    easein beat*2 rotate 10 * dancing
    repeat

#3f3f3f3f 3f3f3f3f

transform show_logo:
    xalign 0.5
    yalign 0.5
    alpha 0
    linear 1.0 alpha 1.0
    pause 2.0
    linear 1.0 alpha 0.0  


label splashscreen:

    #volume set on first startup
    python:
        if not persistent.set_volumes:
            persistent.set_volumes = True
            _preferences.volumes['music'] = 0.8
            _preferences.volumes['sfx'] = 1.0

    if IsTimeForFinalEnding():
        return

    #NotFunGames Logo
    show notfungameslogo at show_logo
    pause 4.0
    show logo_miz at show_logo
    pause 2.0

    #4e6f7446 756e4761 6d657320 3d204372 6561746f 72277320 47616d65 20436f6d 70616e79 0a285768 61742074 68652061 63747561 6c206675 636b3f3f 3f3f29

    play music menumusic
    play sound bootsfx
    show menu_stripes_bw at scroll with Dissolve(1.0)
    show menu_stripes_color at scroll:
        alpha 0.0
    show menuicons_Aspen at icon_enter(menupos_ax, menupos_ay, menustartpos_ax, menustartpos_ay)
    show menuicons_Chris at icon_enter(menupos_cx, menupos_cy, menustartpos_cx, menustartpos_cy)
    show menuicons_Isadora at icon_enter(menupos_ix, menupos_iy, menustartpos_ix, menustartpos_iy)
    show menuicons_Hope at icon_enter(menupos_hx, menupos_hy, menustartpos_hx, menustartpos_hy)
    if not persistent.Nari_IconGone:
        show menuicons_Nari at icon_enter(menupos_nx, menupos_ny, menustartpos_nx, menustartpos_ny)
    pause (introlength - 1.2)


    show logo_main at zoomin
    show menu_stripes_color:
        linear 0.2 alpha 1.0
    pause 0.2
    return