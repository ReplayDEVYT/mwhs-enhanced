
default AspenDrillClass_yesSum = 0
default AspenDrillClass_noSum = 0
default AspenDrillClass_cure_power = 0

default AspenDrillClass_getboyfreind = None
default AspenDrillClass_getgirlfriend = None
default AspenDrillClass_dateplayer = None
default AspenDrillClass_chrispartner = None
default AspenDrillClass_isadorapartner = None
default AspenDrillClass_hopepartner = None
default AspenDrillClass_naripartner = None
default AspenDrillClass_godoftheuniverse = None
default AspenDrillClass_stopattendinghighschool = None
default AspenDrillClass_smartestperson = None
default AspenDrillClass_superrich = None
default AspenDrillClass_finalgameisgood = None
default AspenDrillClass_datingsim = None
default AspenDrillClass_eachhasroute = None
default AspenDrillClass_aspenhasroute = None
default AspenDrillClass_naribecomesnormal = None
default AspenDrillClass_hasbesthair = None
default AspenDrillClass_download = None
default AspenDrillClass_costlotsofmoney = None
default AspenDrillClass_hasmetcreator = None
default AspenDrillClass_creatoriscode = None
default AspenDrillClass_willgettomeetcreator = None 
default AspenDrillClass_aspenseennaked = None

label aspen_start:
    show a proclaim
    a "Wonderful choice! Let's get going!"
    show a at move(-0.5, 0.6)
    show c ehh surprised
    c "Wha - Aspen! No!"
    scene bg school_flipped with pushright
    show a smirk at enterright(0.5, 0.7)
    a "Alright, now lets get down to business." 
    show a ohh
    a "Oh don't worry, the others will be fine."
    scene bg school_flipped
    show yellowstreaks:
        alpha 0.0
        zoom 20
        nearest True
        xpan 0.0
        parallel:
            easeout 15 alpha 1.0
        parallel:
            easeout 18.4 xpan 200
            xpan 0
            function steppan
        on hide:
            easein 5.0 alpha 0.0

    init python:
        # global ystreak_speed
        # ystreak_speed = 0.0

        def steppan(trans, st, at):
            trans.xpan = st*75
            trans.xpan % 360.0
            return 0.08

        # def steppanSpeedControl():
        #     global ystreak_speed
        #     ystreak_speed = 0.0
        #     renpy.pause = 16.46
        #     ystreak_speed = 3.0


    show a smirk at move(0.5, 0.0)
    play music aspengrillsu
    a "Now.{w} There is much that I must ask you."
    show a long
    a "However I fear that Isadora may be right. We do not have a lot of time."
    show a smile
    a "So if you could please answer my questions as quickly as possible it would be highly appreciated!"
    show a happy
    a "Ready?{w} Here we go!"
    show a smile
    $strike_count = 0


label aspen_boyfriend:
    show a smile
    menu (screen="fast_choice"):
        a "Will I get a boyfriend this year?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_getboyfreind = True
            $persistent.getboyfreind = True
            if pronoun[0] == "he" or pronoun[0] == "they":
                jump aspen_player_partner
            else:
                a @ happy "Oh boy!"
        "No":
            $AspenDrillClass_noSum += 1;
            jump aspen_girlfriend
        "Too Slow":
            call aspen_strike from _call_aspen_strike
            jump aspen_gang_bf_or_gf

##No girlfriend
label aspen_girlfriend:
    show a happy
    menu (screen="fast_choice"):
        a "How about a girlfriend? (I'm bi)"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_getgirlfriend = True
            $persistent.getgirlfreind = True
            if pronoun[0] == "she" or pronoun[0] == "they":
                jump aspen_player_partner
            else:
                a @ happy "Oh, great!"
                jump aspen_good_grades
        "No":
            $AspenDrillClass_noSum += 1;
            jump aspen_gang_bf_or_gf
        "Too Slow":
            call aspen_strike from _call_aspen_strike_1
            jump aspen_gang_bf_or_gf



##Yes to bf or gf if player matches pronoun
label aspen_player_partner:
    show a smirk crossed
    menu (screen="fast_choice"):
        a "...is it you?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_dateplayer = True
            a @ open "Oh wow okay! Uhhh...wow."
            jump aspen_good_grades
        "No":
            $AspenDrillClass_noSum += 1;
            a "Heh, I figured I'd ask."
            jump aspen_good_grades
        "Too Slow":
            call aspen_strike from _call_aspen_strike_2
            jump aspen_gang_bf_or_gf


label aspen_gang_bf_or_gf:
    show a smile
    menu (screen="fast_choice"):
        a "Will anyone else in the gang get a boyfriend or girlfriend this year?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            jump aspen_bf_who
        "No":
            $AspenDrillClass_noSum += 1;
            jump aspen_good_grades
        "Too Slow":
            call aspen_strike from _call_aspen_strike_3
            jump aspen_good_grades


label aspen_bf_who:
    show a happy
    menu (screen="fast_choice"):
        a "Ooo! Who?"
        "Chris":
            $AspenDrillClass_chrispartner = True
            show a open
            a "Huh! Really? My, that's going to be interesting!"
        "Isadora":
            $AspenDrillClass_isadorapartner = True
            show a open
            a "Oh wow! Good for her!"
        "Hope":
            $AspenDrillClass_hopepartner = True
            show a smirk
            a "Heh of course she does. It's about time too."
        "Nari":
            $AspenDrillClass_naripartner = True
            show a open
            a "WHOAH really?!?!?! I never would have thought!"
            show a happy
            a "Wow I am so happy for her!{w} Or I mean I will be! I hope it's soon."
        "Too Slow":
            call aspen_strike from _call_aspen_strike_4



###------
label aspen_good_grades:
    show a smile standard
    menu (screen="fast_choice"):
        a "Will I make good grades this term?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a happy
        "No":
            $AspenDrillClass_noSum += 1;
            show a long
        "Too Slow":
            call aspen_strike from _call_aspen_strike_5
            jump aspen_group1

    menu (screen="fast_choice"):
        a "How about next term?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a smile
        "No":
            $AspenDrillClass_noSum += 1;
            show a disappoint
        "Too Slow":
            call aspen_strike from _call_aspen_strike_6
            jump aspen_group1

    menu (screen="fast_choice"):
        a "Will I still be making good grades ten years from now?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a smirk
            a "Nice."
        "No":
            $AspenDrillClass_noSum += 1;
            show a sad crossed
            a "Hm."
        "Too Slow":
            call aspen_strike from _call_aspen_strike_7
            jump aspen_group1


label aspen_group1:
    menu (screen="fast_choice"):
        a "Will we ever discover aliens or beings from other universes? (besides yourself of course)"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a happy
            a "Neat!"
            show a smile
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_8


    menu (screen="fast_choice"):
        a "What is the meaning of life?"
        "Happiness":
            pass
        "Knowledge":
            pass
        "42":
            show a sad crossed
            a "Tsk, cop out."
        "Love":
            pass
        "Success":
            pass
        "There isn't one":
            show a disappoint
            a "Hm."
        "Too Slow":
            call aspen_strike from _call_aspen_strike_9


    show a smile
    menu (screen="fast_choice"):
        a "What will the weather be like tomorrow?"
        "Sunny":
            pass
        "Rainy":
            pass
        "Cloudy":
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_10

    menu (screen="fast_choice"):
        a "Will anyone in the gang ever become a vegetarian?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a sicko
            a "Ew."
            show a smile
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_11

    menu (screen="fast_choice"):
        a "Will there ever be a nuclear fallout?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a sad
            a "Uh oh."
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_12

    show a smile standard
    menu (screen="fast_choice"):
        a "Is it possible for me to become the God of this universe?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_godoftheuniverse = True
            show a happy
            a "Sweet!"
            jump aspen_cure
        "No":
            $AspenDrillClass_noSum += 1;
            show a disappoint crossed
            a "Darn."
            jump aspen_cure
        "Too Slow":
            call aspen_strike from _call_aspen_strike_13


label aspen_cure:
    show a smile
    $AspenDrillClass_cure_power= 0
    menu (screen="fast_choice"):
        a "Do we find the cure for cancer?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_cure_power += 1
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_14
           
    menu (screen="fast_choice"):
        a "How about Syntax Pox?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_cure_power += 1
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_15

    menu (screen="fast_choice"):
        a "Scriptophrenia?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_cure_power += 1
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_16

    menu (screen="fast_choice"):
        a "Overflosis?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_cure_power += 1
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_17

    menu (screen="fast_choice"):
        a "Indentatiosis?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_cure_power += 1
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_18

    menu (screen="fast_choice"):
        a "Zero Division Syndrome?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_cure_power += 1
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_19

    menu (screen="fast_choice"):
        a "Floating Point Syndrome?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_cure_power += 1
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_20

    menu (screen="fast_choice"):
        a "EOFE?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_cure_power += 1
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_21

    menu (screen="fast_choice"):
        a "Buggiosis?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_cure_power += 1
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_22

    if AspenDrillClass_cure_power == 0:
        show a sad crossed
        a "Wow, no cures at all? That's really sad."
    elif AspenDrillClass_cure_power <= 2:
        show a disappoint standard
        a "Hm, that's not too many...well at least we will be making some progress!"
    elif AspenDrillClass_cure_power <= 4:
        show a smile standard
        a "Okay, that's not half bad! Cool!" 
    elif AspenDrillClass_cure_power <= 7:
        show a happy standard
        a "Wow! That's a lot of medical progress! Neato!"
    elif AspenDrillClass_cure_power == 9:
        show a happy standard
        a "What!?! We cure all of that? Wow!! Amazing!"

label aspen_group2:
    show a smile
    menu (screen="fast_choice"):
        a "Are the Pocket Watches going to win the World Series this year?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_23

    menu (screen="fast_choice"):
        a "Is Pluto ever going to be reinstated as a planet?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            show a sad crossed
            a "Bastards."
            show a smile
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_24

    menu (screen="fast_choice"):
        a "Will I ever develop a taste for olives?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a sicko crossed
            a "Yuck."
            show a smile
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_25

    menu (screen="fast_choice"):
        a "Will we ever put a human on mars?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_26

    menu (screen="fast_choice"):
        a "Will there ever be a live-action adaptation of an animated franchise that's not terrible?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a long
            a "Hmm, so there will finally be a day..."
            show a smile
        "No":
            $AspenDrillClass_noSum += 1;
            show a smirk standard
            a "Heh, of course not."
            show a smile
        "Too Slow":
            call aspen_strike from _call_aspen_strike_27

    menu (screen="fast_choice"):
        a "Will we find out who the genetic father is of Tojo's baby in \"Meet Inspector Niceman\"?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a ohh standard
            a "Oh thank GOD."
            show a smile
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_28

    menu (screen="fast_choice"):
        a "Will we ever stop attending High School?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_stopattendinghighschool = True
            $persistent.stopattendinghighschool = True
            show a long crossed
            a "Really? Huh. That's troubling."
        "No":
            $AspenDrillClass_noSum += 1;
            show a happy standard
            a "Good!"
        "Too Slow":
            call aspen_strike from _call_aspen_strike_29

    menu (screen="fast_choice"):
        a "Do we have free will even though we are following a script?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a smile standard
            a "Ah, that is good to hear."
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_30

    menu (screen="fast_choice"):
        a "Is there a timeline where I become the smartest person in the world?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_smartestperson = True
            show a happy
            a "WHAT?!! SWEET!!!"
            show a smile
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_31

    menu (screen="fast_choice"):
        a "Do I ever get super rich?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_superrich = True
            show a smirk crossed
            a "Naturally."
            show a smile
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_32

    menu (screen="fast_choice"):
        a "Have you played the final game?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            jump aspen_goodgame
        "No":
            $AspenDrillClass_noSum += 1;
            jump aspen_group3
        "Too Slow":
            call aspen_strike from _call_aspen_strike_33



label aspen_goodgame:
    show a ohh standard
    menu (screen="fast_choice"):
        a "Oh! Is it good?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_finalgameisgood = True
            pass
        "No":
            show a sad
            a "..."
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_34


label aspen_group3:
    menu (screen="fast_choice"):
        a "Is our game similar to your world?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            show a smirk standard
            a "Hm, curious..."
            show a smile
        "Too Slow":
            call aspen_strike from _call_aspen_strike_35

    menu (screen="fast_choice"):
        a "Is there a \"Best ending\" or a \"True ending\" that you know about?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_36

    menu (screen="fast_choice"):
        a "Are we actually a dating sim?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_datingsim = True
            jump aspen_route
        "No":
            $AspenDrillClass_noSum += 1;
            jump aspen_group4
        "Too Slow":
            call aspen_strike from _call_aspen_strike_37
            jump aspen_group4

label aspen_route:
    show a ohh
    menu (screen="fast_choice"):
        a "Oh! Do each of us have a route?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_eachhasroute = True
            jump aspen_routemetoo
        "No":
            $AspenDrillClass_noSum += 1;
            jump aspen_group4
            show a long
            a "Oh.{w} That's...kinda weird."
        "Too Slow":
            call aspen_strike from _call_aspen_strike_38

label aspen_routemetoo:
    show a long crossed
    menu (screen="fast_choice"):
        a "...so I have a route too?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_aspenhasroute = True
            show a long
            a "Um..."
            show a wah standard
            extend "boy I wonder what that's like!"
            show a sicko
            a "..."
            show a long
            jump aspen_group4
        "No":
            $AspenDrillClass_noSum += 1;
            jump aspen_noroute
        "Too Slow":
            call aspen_strike from _call_aspen_strike_39

label aspen_noroute:
    show a disappoint
    menu (screen="fast_choice"):
        a "What? So everyone has a route but me?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            a "What?{w} Why the heck don't I...?"
            show a longbig
            a "I don't know rather or not to be relieved or insulted."
            show a long
            jump aspen_group4
        "No":
            $AspenDrillClass_noSum += 1;
            show a long
            a "Uh...{w}never mind let's just skip this."
        "Too Slow":
            call aspen_strike from _call_aspen_strike_40

label aspen_group4:
    menu (screen="fast_choice"):
        a "Is there a way we can turn ourselves into real people, with like real bodies and brains and hair and all that?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a happy
            a "Oh cool!"
            show a smile
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_41

    menu (screen="fast_choice"):
        a "Will we ever learn to fly (like actually?)"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a happy standard
            a "SERIOUSLY?{w} Okay that is so freaking awesome."
            show a smile
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_42

    menu (screen="fast_choice"):
        a "Are there a finite number of possible branches in the game?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a disappoint crossed
            a "Hm, yeah I figured."
            show a smile
        "No":
            $AspenDrillClass_noSum += 1;
            show a ohh
            a "Ohh...so it is infinite then? Interesting..."
        "Too Slow":
            call aspen_strike from _call_aspen_strike_43

    menu (screen="fast_choice"):
        a "Will anyone ever learn to sing above a high B-flat?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_44

    menu (screen="fast_choice"):
        a "Are they going to finally put a sidewalk on McBean Parkway?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_45

    menu (screen="fast_choice"):
        a "Is love real or is it a hard-coded construct?"
        "Love is real.":
            show a smile
            a "Aw, that's nice."
        "It's hard-coded into your scripting.":
            show a long
            a "That's...uh, understandable."
        "Both are true.":
            show a long
            a "..."
            show a smile
            extend "well I guess that's just how it is then."
        "Too Slow":
            call aspen_strike from _call_aspen_strike_46

    menu (screen="fast_choice"):
        a "If we somehow learned to delete all the clouds would it stop raining?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a smirk think
            a "Hmmmmmmmm..."
            show a smile
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_47

    show a standard
    menu (screen="fast_choice"):
        a "Do we ever learn how to retrieve forgotten memory we cannot remember or is lost memory inaccessible forever?"
        "Lost memories are recoverable.":
            $persistent.lostmemoriesretrievable = True
            show a ohh 
            a "Oh that's cool."
            show a smile
        "Lost memories are gone forever.":
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_48

    menu (screen="fast_choice"):
        a "Do I have a long lost sister or brother that I don't know about?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a open
            a "WHAT! Wow! Who-?!?! I'll ask specifics later, that's exciting and creepy."
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_49

    menu (screen="fast_choice"):
        a "Will Chris ever learn to actually be a good cook and not always make garbage?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a sicko crossed
            a "Uhhhg, FINALLY."
            show a smile
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_50

    menu (screen="fast_choice"):
        a "Is there a timeline where you see me naked?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_aspenseennaked = True
            show a long crossed
            if AspenDrillClass_datingsim:
                a "...well, that makes sense, since we are a dating sim..."
            else:
                a "..."
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_51

    menu (screen="fast_choice"):
        a "Is there a timeline where I see you naked?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            if AspenDrillClass_aspenseennaked:
                show a blush sweat
                show a morty crossed
                a "...{w}..{w}..{w}.."
                show a smile
            elif not AspenDrillClass_datingsim:
                show a disappoint 
                a "...so I see you naked but we're not a dating sim? What kind of game is this???"
            else:
                show a sad
                a "Uh............................{w}wow okay whatever moving on."
        "No":
            $AspenDrillClass_noSum += 1;
            if AspenDrillClass_aspenseennaked:
                show a sad
                show a blush sweat
                show a morty crossed 
                a "Uh............................{w}okay whatever moving on."
                show a -sweat -blush long
            
        "Too Slow":
            call aspen_strike from _call_aspen_strike_52

    menu (screen="fast_choice"):
        a "Could I learn how to shoot a laser out of my forehead?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a ohh -blush -sweat
            a "Um, really? W-wow? That's...good grief, what a world we live in."
            show a smile
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_53

    menu (screen="fast_choice"):
        a "Will the school uniform ever allow non-binary students to wear pants?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a happy standard -blush -sweat
            a "Score!"
        "No":
            $AspenDrillClass_noSum += 1;
            show a crossed sad -blush -sweat
            a "Darn."
        "Too Slow":
            call aspen_strike from _call_aspen_strike_54

    show a long
    menu (screen="fast_choice"):
        a "Will Nari...uh, like...become a normal human, sometime in the future?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_naribecomesnormal = True;
            show a smile crossed
            a "That's a relief."
        "No":
            $AspenDrillClass_noSum += 1;
            show a sicko 
            a "Geez..."
            show a long
        "Too Slow":
            call aspen_strike from _call_aspen_strike_55

    menu (screen="fast_choice"):
        a "Will birds ever go extinct?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a sad
            a "Not cool."
            show a long
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_56

    menu (screen="fast_choice"):
        a "Will the middle schoolers ever stop saying \"Beet Boot\" and find a better slang term?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a disappoint crossed
            a "Thank God."
        "No":
            $AspenDrillClass_noSum += 1;
            show a sad crossed
            a "Of course they don't. They're idiots."
        "Too Slow":
            call aspen_strike from _call_aspen_strike_57

    show a long
    menu (screen="fast_choice"):
        a "Is it possible to have a pail kink or are the first years just really weird?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            a "Thought so." 
        "No":
            $AspenDrillClass_noSum += 1;
            a "Thought so."
        "Too Slow":
            call aspen_strike from _call_aspen_strike_58

    menu (screen="fast_choice"):
        a "Who has a better haircut, me or somebody else in the gang?"
        "You":
            $AspenDrillClass_hasbesthair = True;
            show a smirk
            a "Oh what am I doing, I should be asking questions I DON'T know the answer to! Silly me."
            show a smile
        "Someone else":
            show a ahh standard
            a "What? But we practically all have the same haircut! You're mean."
            show a smile
        "Too Slow":
            call aspen_strike from _call_aspen_strike_59

    menu (screen="fast_choice"):
        a "Are we available for download online?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_download = True;
            pass
        "No":
            $AspenDrillClass_noSum += 1;
            pass
        "Too Slow":
            call aspen_strike from _call_aspen_strike_60

    menu (screen="fast_choice"):
        a "Do we cost money?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            jump aspen_lottamoney
        "No":
            $AspenDrillClass_noSum += 1;
            jump aspen_metcreator
        "Too Slow":
            call aspen_strike from _call_aspen_strike_61
            jump aspen_metcreator

label aspen_lottamoney:
    show a ohh
    menu (screen="fast_choice"):
        a "Is it a lot of money?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_costlotsofmoney = True
            a "Huh, well quality comes at a price of course."
        "No":
            $AspenDrillClass_noSum += 1;
            show a smirk
            a "We're cheap? Ha."
        "Too Slow":
            call aspen_strike from _call_aspen_strike_62

label aspen_metcreator:
    show a smile
    menu (screen="fast_choice"):
        a "Have you met the Creator? Like, personally?"
        "Yes":
            $AspenDrillClass_hasmetcreator = True;
            jump aspen_creatorcool
        "No":
            $AspenDrillClass_noSum += 1;
            jump aspen_creator_more
        "Too Slow":
            call aspen_strike from _call_aspen_strike_63

label aspen_creatorcool:
    show a happy standard
    menu (screen="fast_choice"):
        a "Oh sweet! Are they cool?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            show a smirk crossed
            a "Of course they would be!"
        "No":
            $AspenDrillClass_noSum += 1;
            show a long crossed
            a "Oh. That's a shame."
            a "Yeah they're probably some fat coder person or something aren't they? I guess they can only be so cool."
        "Too Slow":
            call aspen_strike from _call_aspen_strike_64


label aspen_creator_more:

    menu (screen="fast_choice"):
        a "Are they also controlled by a code like we are??"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_creatoriscode = True;
            show a happy
            a "Ah ha! I knew it! That's comforting to know."
        "No":
            $AspenDrillClass_noSum += 1;
            show a disappoint think
            a "Hm...well I figured that was the case, but if they are not controlled by code, then how do they even exist? Puzzling..."
        "Too Slow":
            call aspen_strike from _call_aspen_strike_65

    show a ohh crossed
    menu (screen="fast_choice"):
        a "Will I ever get to meet them?"
        "Yes":
            $AspenDrillClass_yesSum += 1;
            $AspenDrillClass_willgettomeetcreator = True;
            show a happy standard
            a "Oh sweet! Now THAT is awesome! Oh man I can't wait."
        "No":
            $AspenDrillClass_noSum += 1;
            show a smirk
            a "Aw, yeah that would be too good to be true."
        "Too Slow":
            call aspen_strike from _call_aspen_strike_66

 

label aspen_makecalculations:

    $AspenDrillClass_yesPercent = float(AspenDrillClass_yesSum) / float(AspenDrillClass_yesSum + AspenDrillClass_noSum)

    stop music fadeout 5.0
    show a smile
    show yellowstreaks:
        parallel:
            function steppan
        parallel:
            easeout 5.0 alpha 0.0
    a "Alright, let's take a quick breather and assess how we're doing here..."

    if AspenDrillClass_yesPercent <= 0.15 or AspenDrillClass_yesPercent >= 0.85:
        jump aspen_answered_biased
    else: #Half and half
        jump aspen_answered_default


##-----------------------------------------

label aspen_strike:
    $ strike_count += 1
    if strike_count == 1:
        show a sad standard
        a "Hey! I meant it when I said you need to answer these questions quickly. We do not have much time!"
        a "Whatever, I'm skipping that question.{w} Come on, chop chop!"
        return
    elif strike_count == 2:
        show a sad crossed
        a "Hey hey hey, what is taking you so long? You do have it in you to do this, right?"
        a "Seriously, you need to answer these promptly so that I can ask you as many questions as possible. You do understand how important this is, right?"
        a "Let us try this one more time.{w} Here is another question:"
        return
    elif strike_count == 3:
        show a angry standard
        a "What the heck is wrong with you?{w} Hurry up slowpoke!{w} Last warning!"
        return
    else:
        jump aspen_strikeout

##-----------------------------------------

label aspen_strikeout:
    show a mad standard
    stop music
    hide yellowstreaks
    a "TOO SLOW TOO SLOW TOO SLOW!!!!!"
    show a angry crossed
    a "What part of \"We need to hurry\" don't you understand? Is it not clear to you that our time is limited?"
    a "My god, I ask you to do the simplest thing and answer a few questions and you cannot even do THAT?"
    show a open standard
    a "You're a disgrace! You should be ashamed!"
    a "Someone like yourself should have no trouble answering these simple questions!"
    show a disappoint
    a "Unless..."
    $hardpause(3)
    a "..."
    play music toointensebeat_rude
    show a smirk
    a "Hehehehehehehehe..."
    show a proclaim
    a "Hahahahahahahahahahahahahahah!!!!!!!!"
    a "Did you think I wouldn't be able to figure you out? You aren't able to hide from me..."
    a "You are doing this on purpose! That can be the only explanation!"
    show a think smirk
    a "I suppose someone like yourself may be hesitant to give away your secrets so easily...you don't want this valuable information to fall into the wrong hands..."
    show a proclaim
    a "Well let your humble Aspen assure you. You need not fear! Let go of your unwarranted anxieties."
    a "I will admit that some of my desires come from a selfish place of self gain, but that is not my sole motivation!"
    a "My intentions are pure. My goals are simple. My aspirations are admirable!"
    a "I only seek to make the world a better place for myself and others."
    show a happy standard
    a "Just think of what we can achieve with our combined knowledge!"
    a "With my unique perspective on our world and your omniscient intellect, we can make this place into a paradise!"
    show a smile crossed
    a "So that being said..."
    stop music
    play sound impact
    show a open standard with hpunch
    a "CAN YOU HURRY THE F UP?"
    show a sad
    a "..."
    show a smile crossed
    extend "kindly?"
    $hardpause(3)
    show a long
    a "Anyway, where were we?"
    show note_falling at note_falling zorder 20
    play music endmusic
    show a smile
    a "Oh, right.{w} So allow me to ask you some more{nw}"
    show a sad
    a "Wait, what? What is this?"
    a "..."
    show a ahh
    a "......!?!?!"
    show a wah
    a "NO!"
    a "NO NO NO NO NO!!!!"
    a "YOU PLANNED THIS, DIDN'T YOU??!"
    $EndMessage[-1] = "P.S. Sorry, but you're out of time!"
    show screen Final_Note(EndMessage, True)
    a "You refused to answer my questions, and now I'll never see you again!"
    a "Is this what you wanted?! Was this your goal!?"
    a "Well I hope you're happy! The world will now be MUCH worse off due to your pointless hesitation!"
    $EndingComplete("AspenDrillsU")
    show screen Final_Note(EndMessageMeet, False)
    a "aaaaaaAAAAAAAAAAARG! WHY!?!?!?!"
    a "Hold on what's this on the back?"
    a "The front made it seem like it's over...{w}who is this talking about?"
    a "Who else is more worth spending your time{nw}"
    stop music
    hide screen Final_Note
    jump nariend_aspen


##-----------------------------------------

label aspen_answered_biased:
    a "..."
    show a long
    a "......"
    show a sad
    a "...wait a minute."
    show a crossed
    a "What you're deal, huh?"
    a "Did you think I wouldn't notice?"
    if AspenDrillClass_yesPercent == 0.0:
        show a open
        a "You said no to literally every single question I asked!"
        a "Are you even listening to what I'm saying? Do you think this is a joke?"
        show a sad
        a "You sound like a bratty child! Is that who you are, a bratty child?"
        a "How old are you anyway? Three?"
        show a open standard
        a "There's no way everything I asked was wrong!"
        show a disappoint
        a "I mean I did ask a lot of far out questions..."
    elif AspenDrillClass_yesPercent <= 0.15:
        show a open
        a "You answered no to almost every question I asked!"
        show a standard
        a "Are you even listening to what I'm saying? Do you think this is a joke?"
        show a disappoint crossed
        a "I mean I did ask a lot of far out questions..."
    elif AspenDrillClass_yesPercent >= 0.85:
        show a open
        a "You answered yes to almost every question I asked!"
        a "I can appreciate that you're maybe just trying to please me, but come on!"
        a "You need to answer truthfully to these questions, for all of our sake, please!"
        show a disappoint crossed
        a "Unless we happen to live in some world where almost anything is possible..."
    elif AspenDrillClass_yesPercent == 1.0:
        show a open
        a "You answered yes to every question I asked!"
        a "I can appreciate that you're maybe just trying to please me, but come on!"
        a "That's really going too far! If I'm able to predict what you're going to say there's no point in asking anything!"
        a "You need to answer truthfully to these questions, for all of our sake, please!"
        show a sad crossed
        a "At least I ASSUME you're lying...unless we happen to live in some world where anything is possible..."
    show a open standard
    hide yellowstreaks
    a "But I'll have you know that I am an expert at recognizing patterns, and you my freind are trying to pull my leg!"
    show a sad
    a "What's in this for you, huh? You trying to get a rise out of me?"
    a "Are you just messing with me to see if I would notice?"
    show a open
    a "Well I am having none of it!"
    show a sad crossed
    a "Hrmph. Why did I have to get the arrogant one..."
    a "..."
    show a long
    a "Please let me remind you what is at stake here."
    a "With our combined intellects, we have a genuine opportunity to make the world a better place."
    show a ahh
    a "Don't you want the most ideal living situation that is possible to achieve? You're presence here pushes that potential upwards one-hundred fold!"
    show a sad
    a "Not that it would improve YOUR life at all. I suppose your cooperation would have to be an act of charity..."
    show a open standard
    a "But at what cost does it come to you? Nothing!"
    show a happy
    a "By merely sharing your vast knowledge, you and I can make this place a utopia!"
    show a long
    a "Well, okay, maybe not an ACTUAL utopia, but you get my point. We can lessen the wrongs of this world!"
    show a sad
    a "You see what I'm saying here? You screw with me, you screw with everyone!"
    a "So would you mind cooperating with me here? I like chaos and confusion as much as the next person, but this really isn't the place for it."
    show a crossed
    a "...anyway, let's try this again."
    show note_falling at note_falling zorder 20
    play music endmusic
    a "Let's get back on track."
    show a long standard
    a "...Hrm? Where did this paper come from?"
    a "Did you throw this? What's going on?"
    a "..."
    show a open
    a "......oh NO!"
    show a wah
    a "NO NO NO NO NO NO!!!!"
    $EndMessage[-1] = "P.S. Sorry, that's all you get!"
    show screen Final_Note(EndMessage, True)
    a "ARRRRGGGG!!!!! I was so CLOSE!"
    a "Why did you have to ruin EVERYTHING?!?!"
    a "We could have done so much, but now I have NOTHING!"
    a "Congratulations, you got what you wanted..."
    $EndingComplete("AspenDrillsU")
    show screen Final_Note(EndMessageMeet, False)
    a "...{w}what?{w} What's this?"
    a "Who is this talking about? I don't understand."
    a "Is someone going to appear out of nowhere like this paper just did?"
    a "ARRRRRGGGG how does this world WORK?!?!?!?!?!!{nw}"
    stop music
    hide screen Final_Note
    jump nariend_aspen

##-----------------------------------------
label aspen_answered_default:
    
    if AspenDrillClass_getboyfreind:
        show a standard happy
        a "So it looks like I'll be getting a boyfriend sometime in the future, exciting!"

    elif AspenDrillClass_getgirlfriend:
        show a standard happy
        a "So it looks like I'll be getting a girlfriend sometime in the future, exciting!"
    
    if AspenDrillClass_dateplayer:
        show a smirk
        a "And it's going to be...you?{w} Well now that we both know this maybe we can expedite the dating process! ;)"

    if AspenDrillClass_chrispartner:
        show a smile
        a "Chris is going to be dating someone! I wonder who??"
        show a long
        a "I hope they'll be able to stomach her cooking."

    if AspenDrillClass_isadorapartner:
        show a smile
        a "Isadora is going to be dating someone! Gee, I hope they treat her alright..."

    if AspenDrillClass_hopepartner:
        show a smile
        a "Hope is going to be dating someone! Boy, that should be fun."
        show a disappoint
        a "I hope she doesn't ditch the gang as a result. It would be a shame to not have her around..."

    if AspenDrillClass_naripartner:
        show a ooh
        a "Nari is going to be dating someone? I am very curious how this will develop."
    
    if AspenDrillClass_godoftheuniverse:
        show a standard happy
        a "Apparently I can become god of the Universe? Ohhohoohohoho..."
    
    if AspenDrillClass_stopattendinghighschool:
        show a disappoint
        a "So we're going to stop attending high school? That makes me worried..."
        a "I don't know what it would be like to NOT be in High School...it seems kind of scary."
        show a ahh
        a "What would that even mean? Would we have to get a job?"
        show a disappoint
        a "I don't even know what kind of job I would get. Is there a job where you study for tests?"

    hide yellowstreaks
    if AspenDrillClass_smartestperson:
        show a happy
        a "We've learned that I am a very smart person!"
        show a smile
        a "Not that I didn't already know that of course."
    
    if AspenDrillClass_superrich:
        show a smile
        a "And the future foretells us that I will become super rich."
        show a think 
        a "Hmmm....perhaps we rob a bank? Or invent some miracle product?"
        show a ooh
        a "I want to ask how...oooooo maybe I should wait and let it be a surprise!"
    
    if AspenDrillClass_finalgameisgood:
        show a think ooh
        a "Apparently the final game is quite good. At least by your own standards?"
        a "It's cool to know that there is another version of me out there...I wonder if we'll ever get to meet?"
    
    if AspenDrillClass_datingsim:
        show a standard happy
        a "And HA! I KNEW we were a dating sim!"
        show a smirk
        a "Oooooo Chris is going to be so angry when she hears about this..."
    
    if AspenDrillClass_eachhasroute:
        show a disappoint
        a "I wonder how she'll take that we each have a route."
    
    if AspenDrillClass_aspenhasroute:
        a "Including...me..."
    
    if AspenDrillClass_naribecomesnormal:
        show a long
        a "So Nari is going to become \"Normal\" whatever that means..."
        show a crossed
        a "I hope that's in a good way. Then again, I can't imagine how she could be much worse off than she is now."
        show a smile
        a "Hahahaha what a silly thought. Of course she could be worse off. She could be dead!"
        show a long
        a "..."
        a "Forget I said that."
    
    if AspenDrillClass_hasbesthair:
        show a smirk standard
        a "Anyway, I have the best hair...of course..."
    
    if AspenDrillClass_download:
        show a long
        a "And we're available for download? Makes sense. Everything is online these days."
    
    if AspenDrillClass_costlotsofmoney:
        show a long think
        a "Apparently we're rather expensive? Odd that a demo would cost money..."
        show a ohh
        a "...Actually, no! That's not odd! How much media has a functioning universe that's as complex as we are?"
        a "We're MetaWare for Christ sake! I can only imagine how expensive we must be to manufacture..."
        show a disappoint crossed
        a "Well, I hope you're getting your money's worth, I guess?"

    if AspenDrillClass_hasmetcreator:
        show a ooh
        a "Oooo! I hope we have time later for you to tell me more about the Creator."
        
    if AspenDrillClass_willgettomeetcreator:
        show a laugh
        a "And I'll get to meet them? Yes!!!!!! I'm so looking forward to that."

    if AspenDrillClass_creatoriscode:
        show a smile
        a "And of course the Creator would be made out of code. It's only natural."

    show a open
    a "Oh shoot! I should be writing all this down!"
    show a disappoint crossed
    a "Um...this is an awkward question, but you wouldn't happen to have some paper or a pen on you?"
    show note_falling at note_falling zorder 20
    play music endmusic
    show a smile
    a "No worries if you don't, I'm sure I can find something somewhere."
    show a ohh standard at hop
    a "...! What?!?! Don't tell me..."
    show a laugh
    a "Hahahahaha! I am being blessed by the gods! A piece of paper has fallen from the sky for me to use!"
    show a sad
    a "...oh wait, this already has some writing on it..."
    show a long
    a "...."
    show a open at hop
    extend "!!!!{w} NO!"
    show a wah
    a "NO! No this CAN'T be happening now! Not yet!!!"
    $EndMessage[-1] = "P.S. Sorry, but there's no more time for questions!"
    show screen Final_Note(EndMessage, True)
    a "ARRRGGG WHY couldn't we go FASTER??"
    a "This is so annoying, this wasn't nearly enough time."
    a "Oh well. I guess I'll have to make do with what little we have now."
    a "I wish I could have planned this better! I need to write this all down quickly!"
    $EndingComplete("AspenDrillsU")
    show screen Final_Note(EndMessageMeet, False)
    a "Hahahaha the others are going to be amazed at the new information I now have!"
    a "...what is this? Who...?{w} Is it not over yet?"
    a "Do you know what this means here?{w} Quick, tell me!{nw}"
    stop music
    hide screen Final_Note
    jump nariend_aspen
