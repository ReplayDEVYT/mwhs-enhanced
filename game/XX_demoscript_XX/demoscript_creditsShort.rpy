label credits_short:
    $EndingComplete("GoodbyeShort")
    $quick_menu = False
    $_skipping = False
    hide black
    scene black
    play music goodbyemini noloop
    show logosolo at truecenter:
        on show:
            alpha 0.0
            linear 5.0 alpha 1.0
        on hide:
            linear 5.0 alpha 0.0
    $renpy.pause(delay=10, hard=True)
    hide logosolo
    $renpy.pause(delay=6, hard=True)
    $totalsofar = len(persistent.completed_endings)
    show text "{color=#FFF}[totalsofar]/[num_of_endings]{/color}":
        alpha 0.0
        linear 1.0 alpha 1.0
        pause 5.0
        linear 1.0 alpha 0.0
    $renpy.pause(delay=10, hard=True)
    return

