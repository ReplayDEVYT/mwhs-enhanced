
transform credits_scroll:
    ypos 1080
    xalign 0.5
    linear 40.0 ypos -500
        


transform logo_scroll:
    ypos 920
    xalign 0.5
    linear 40.0 ypos -1000




label credits:

    scene black
    $renpy.pause(delay=(10), hard=True)
    $_skipping = False
    play music goodbye noloop

    $ _game_menu_screen = None #keep that music in-Sync babyyyyyyyy

    # image   
    # image noisemask = AlpahMask("backgrounds/noisemask.png")

    #background





    $renpy.pause(delay=(99), hard=True)

    $renpy.pause(delay=(34), hard=True)

label logo_time:

    show logosolo at logo_scroll

    style credits_style:
        xalign 0.5
        text_align 0.5

    image creditsText1 = ParameterizedText(style="credits_style")
    image creditsText2 = ParameterizedText(style="credits_style")
    image creditsText3 = ParameterizedText(style="credits_style")
    image creditsText4 = ParameterizedText(style="credits_style")
    image creditsText5 = ParameterizedText(style="credits_style")
    image creditsText6 = ParameterizedText(style="credits_style")
    image creditsText7 = ParameterizedText(style="credits_style")
    image creditsText8 = ParameterizedText(style="credits_style")
    image creditsText9 = ParameterizedText(style="credits_style")
    image creditsText10 = ParameterizedText(style="credits_style")

    define credits_spacing = 6 #don't fuck with this

    $renpy.pause(delay=24, hard=True)
    show creditsText1 "{b}Concept and Design{/b}\nMarc Laroussini" at credits_scroll

    $renpy.pause(delay=credits_spacing, hard=True)
    show creditsText2 "{b}Character Art{/b}\nSparkBag" at credits_scroll #Can draw like a beast

    $renpy.pause(delay=credits_spacing, hard=True)
    show creditsText3 "{b}Background Art{/b}\nKeeby" at credits_scroll #Funny and talented fuck

    $renpy.pause(delay=credits_spacing, hard=True)
    show creditsText4 "{b}Logo Art{/b}\nAlexander A. McDonald" at credits_scroll #Always wanting to get it exactly right

    $renpy.pause(delay=credits_spacing, hard=True)
    show creditsText5 "{b}Writing{/b}\nMarc Laroussini" at credits_scroll #me

    $renpy.pause(delay=credits_spacing, hard=True)
    show creditsText6 "{b}Coding{/b}\nMarc Laroussini" at credits_scroll #me

    $renpy.pause(delay=credits_spacing, hard=True)
    show creditsText7 "{b}Music{/b}\nAhmaykmewsik" at credits_scroll #me - this is my online pseudonym

    $renpy.pause(delay=credits_spacing, hard=True)
    show creditsText9 "{b}Special Thanks{/b}\nHillary Kapan\nLaura Steenbridge\nTom Lesser\nrenpytom" at credits_scroll # <3
    # show creditsText8 "{b}Beta Testers{/b}\nJoe M.\nThis other dude\nBob\nSammy Freddy Smith" at credits_scroll

    $renpy.pause(delay=credits_spacing + 2, hard=True)


    $renpy.pause(delay=32, hard=True)

    image thanks1 = ParameterizedText(xalign=0.5, yalign=0.5, slow=True, size=72, slow_cps=10, font="fonts/MarcFont.ttf")
    image thanks2 = ParameterizedText(xalign=0.7, yalign=0.6, slow=True, size=72, slow_cps=10, font="fonts/MarcFont.ttf")
    image thanks3 = ParameterizedText(xalign=0.7, yalign=0.7, slow=True, size=72, slow_cps=10, font="fonts/MarcFont.ttf")
    
    show thanks1 "Thank you for playing my game." at fadestoblack(10) #And thank "you"? The person reading the code? Nerd.
    $renpy.pause(delay=8, hard=True)
    show thanks2 "Until next time," at fadestoblack(10)
    $renpy.pause(delay=4, hard=True)
    show thanks3 "-The Creator" at fadestoblack(10) 

    $renpy.pause(delay=5, hard=True)

    hide thanks1 
    hide thanks2
    hide thanks3 

    $renpy.pause(delay=8, hard=True)

    jump the_end

