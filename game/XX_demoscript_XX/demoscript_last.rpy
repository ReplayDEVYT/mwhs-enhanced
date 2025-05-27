## Welcome to the end.


label intro_final:
    $_skipping = False

    $quick_menu = False
    stop music
    # scene black
    window hide 
    scene bg school
    show black zorder 0
    

    $renpy.pause(delay=4, hard=True)
    $qspeed = 7
    centered "{cps=[qspeed]}{size=+90}{font=fonts/ProFontWindows.ttf}CONGRATULATIONS"
    show bgblueworld: 
        nearest True
        zoom 4
        parallel:
            alpha 0.0
            linear 8.0 alpha 0.8
        # parallel:
        #     xpan 180
        #     linear 200. xpan 540
        #     repeat
        parallel:
            ypan 0
            linear 50 ypan -1080
            repeat


    queue music intromusicfinal_first noloop
    queue music intromusicfinal_loop

    show ctc onlayer overlay:
        alpha 0.0
        pause 2
        block:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.3
            repeat
        on hide:
            linear 0.5 alpha 0.0

    extend ""
    centered "{cps=[qspeed]}{size=+100}{font=fonts/ProFontWindows.ttf}THE FINAL ROUTE AWAITS"
    centered "{cps=[qspeed]}{size=+100}{font=fonts/ProFontWindows.ttf}ONCE YOU PROCEED"
    centered "{cps=[qspeed]}{size=+100}{font=fonts/ProFontWindows.ttf}YOU CANNOT RETURN"
    centered "{cps=[qspeed]}{size=+100}{font=fonts/ProFontWindows.ttf}WHEN THIS ROUTE IS COMPLETE"
    centered "{cps=[qspeed]}{size=+100}{font=fonts/ProFontWindows.ttf}ALL GAME DATA WILL BE \nERASED"
    centered "{cps=[qspeed]}{size=+100}{font=fonts/ProFontWindows.ttf}AND DELETED FROM YOUR COMPUTER"
    centered "{cps=[qspeed]}{size=+100}{font=fonts/ProFontWindows.ttf}PROCEED?"
    menu:
        "Yes":
            jump start_the_end
        "No":
            $_skipping = True
            jump nope_not_today

label nope_not_today:
    stop music fadeout 8.0
    hide bgblueworld with Dissolve(3.0)
    centered "{cps=[qspeed]}{size=+90}{font=fonts/ProFontWindows.ttf}THEN ALL SHALL REMAIN UNCHANGED"
    jump whitefade

label start_the_end:
    stop music
    hide bgblueworld
    $persistent.end_has_come = True
    $delete_all_saves() ###bye bye saves
    $hardpause(1)
    centered "{cps=5}{size=+90}{font=fonts/ProFontWindows.ttf}THEN IT BEGINS{w=2}{nw}"
    $hardpause(3)
    jump setup_the_end

label restart_the_end:
    stop music
    $quick_menu = False
    $hardpause(1)
    centered "{cps=5}{size=+90}{font=fonts/ProFontWindows.ttf}IT BEGINS AGAIN{w=2}{nw}"
    $hardpause(3)
    jump setup_the_end  
    



label setup_the_end:
    ##Setup Question Arrays
    $_skipping = True
    scene black

    python:
        QUESTION_BANK = [
            
            [("{color=#a8741f}Hello, Isadora", "end_i_hello"), ("i", 1)],

            [("{color=#cb454c}Hello, Chris", "end_c_hello"), ("c", 1)],

            [("{color=#db54dd}Hello, Hope", "end_h_hello"), ("h", 1)],

            [("{color=#e8ba3e}Hello, Aspen", "end_a_hello"), ("a", 1)],

            [("{color=#7dd87d}Hello, Nari", "end_n_hello"), ("n", 1)],

            ####

            [("{color=#a8741f}It's okay. You are not alone.", "end_i_okay"), ("i", 2)],

            [("{color=#cb454c}It's okay. You are loved.", "end_c_okay"), ("c", 2)],

            [("{color=#db54dd}It's okay. You are safe.", "end_h_okay"), ("h", 2)],

            [("{color=#e8ba3e}It's okay. You are free.", "end_a_okay"), ("a", 2)],

            [("{color=#7dd87d}It's okay. You will understand soon.", "end_n_okay"), ("n", 2)]

            ###

        ]

        QUESTION_ARRAY = []
        QUESTION_ARRAY.append(QUESTION_BANK.pop(0))
        QUESTION_ARRAY.append(QUESTION_BANK.pop(0))
        QUESTION_ARRAY.append(QUESTION_BANK.pop(0))

        QUESTION_TRACKER_DICT = {
            "c": 0,
            "i": 0,
            "a": 0,
            "h": 0,
            "n": 0
        }

    show bgendnoise at makeitfizz
    show black zorder 10:
        alpha 0.5

    $_skipping = True

    $quick_menu = False
    play music noise


label end_questions:

    python:
        if (len(QUESTION_ARRAY) >= 3):
            result = renpy.display_menu([ QUESTION_ARRAY[0][0], QUESTION_ARRAY[1][0], QUESTION_ARRAY[2][0] ], screen="choice_end")
        elif (len(QUESTION_ARRAY) == 2):
            result = renpy.display_menu([ QUESTION_ARRAY[0][0], QUESTION_ARRAY[1][0] ], screen="choice_end")
        elif (len(QUESTION_ARRAY) == 1):
            result = renpy.display_menu([ QUESTION_ARRAY[0][0] ], screen="choice_end")
        else: #No More questions
            renpy.jump("loadexe")

        #Find index character and character question index of chosen question
        for question in enumerate(QUESTION_ARRAY):
            if question[1][0][1] == result:
                i_chosen = question[0]
                char_chosen = question[1][1][0]
                char_i_chosen = question[1][1][1]

        #Log question as seen
        QUESTION_TRACKER_DICT[char_chosen] = char_i_chosen

        #remove chosen question
        QUESTION_ARRAY.pop(i_chosen)

        #Add question from Bank

        for itr in range(len(QUESTION_BANK)):
            #check if next question is ready to display
            bank_char = QUESTION_BANK[itr][1][0]
            bank_char_i = QUESTION_BANK[itr][1][1]
            char_i_next = QUESTION_TRACKER_DICT.get(bank_char) + 1
            if bank_char_i == char_i_next:
                QUESTION_ARRAY.insert(i_chosen, QUESTION_BANK.pop(itr))
                break
            #iterate if it don't work

        #Return result and jump jump trampoline
        #Fly to where you want to be
        renpy.jump(result)


# init python:
#     def start_end_dialouge(char):
#         renpy.pause(1)
#         renpy.show(char, at_list=[fadein])
#         renpy.pause(2)
#         _window_show = True
#         _windo_auto_hide = True
#         show_quick_menu = True

label end_i_hello:
    $hardpause(1)
    show i long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    i "..."
    i "......"
    show i ahh at hop()
    extend "wha-!"
    show i wah fists
    iw "OH MY GOD WHAT"
    show i oohh at shake(30)
    iw "WHERE AM I?"
    iw "WHAT'S GOING ON?"
    window hide
    $hardpause(3)
    show i ohh at stop
    i "Wait a minute...{w}is that...?"
    show i wah at shake(60)
    iw "OH MY GOD YOU'RE THE PLAYER WHAT THE HECK WHY ARE YOU COMING TO US LIKE THIS THIS IS REALLY WEIRD"
    iw "OR ARE YOU THE CREATOR OR SOMETHING?"
    iw "WHY DO YOU FEEL LIKE YOU'RE MADE OF LIGHT?"
    show i wah at stop
    i "..."
    show i ahh
    i "What did you do with Chrissy and Aspen?"
    show i open
    i "You better not have hurt them!{w} You hear me?!?!?!"
    $quick_menu = False
    show i at fadeout()
    window hide
    $hardpause(1)
    hide i
    jump end_questions


label end_h_hello:
    $hardpause(1)
    show h long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    h "..."
    show h ahh
    h "huh"
    show h long
    h "..."
    window hide
    $hardpause(3)
    show h ehh
    h "OH GOD"
    show h ehh sweat at shake()
    h "NO NO NO NO NO NO THIS ISNT HAPPENING NOW OH GOD"
    h "DONT FUCKING TOUCH ME"
    h "I WILL PUNCH YOU IN THE NUTS STAY THE FUCK AWAY FROM ME"
    h "DONT{w} COME{w} ANY{w} CLOSER"
    show h ahh
    h "..."
    h "......"
    show h at stop
    $hardpause(6)
    $quick_menu = False
    show h at fadeout()
    window hide
    $hardpause(1)
    hide h
    jump end_questions
    

label end_c_hello:
    $hardpause(1)
    show c long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    c "..."
    show c ohh at hop()
    c "Ohh!{w} Is that..."
    window hide
    $hardpause(3)
    show c ehh
    c "I-{w}I-{w}I-{w}uh..."
    show c sicko blush
    $hardpause(3)
    c "It's really happening..."
    c "It really is happening...{w}you're finally here..."
    show c ahh sweat at shake(4)
    c "{cps=10}Ahhhhhhhhhhhahahhhhhh..."
    show c ahh at stop
    c "..."
    show c sicko
    c "Um."
    $hardpause(5)
    c "H-hi there, Mr. Player."
    c "I-Is there...{w}is there anything you would like me to...{w}do for you?"
    $quick_menu = False
    show c at fadeout()
    window hide
    $hardpause(1)
    hide c
    jump end_questions
    

label end_a_hello:
    $hardpause(1)
    show a long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    a "..."
    show a ahh
    a "Huh?{w} Why is it-"
    a "..."
    show a ehh
    a "Y-You must be..."
    window hide
    $hardpause(3)
    show a laugh
    a "Hello!{w} Hi!{w} W-Welcome t-t-t-to MetaWare High School (Demo)!..."
    a "You are the player, right?{w} Right?"
    show a sweat
    a "I don't see what else you could be?"
    a "I don't know what path you're on right now but..."
    show a ehh
    extend " eheheheheh, it sure is kinda...unexpected, huh?"
    a "I h-hope you're having a good time? Doing the...whole make everything disappear thing??"
    a "Y-y-y-you didn't like...{w}um...{w}happen to just delete anything, did you?{w} Kinda had some friends back there..."
    $quick_menu = False
    show a at fadeout()
    window hide
    $hardpause(1)
    hide a
    jump end_questions
    

label end_n_hello:
    $hardpause(1)
    show n line at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    n "..."
    n "......"
    window hide
    $hardpause(8)
    n "Well then?"
    $quick_menu = False
    show n at fadeout()
    window hide
    $hardpause(1)
    hide n
    jump end_questions
    

###----------------------------------------------------------------2

label end_h_okay:
    $hardpause(1)
    show h long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show h mad sweat at shake()
    h "FUCK YOU FUCK YOU FUCK YOU FUCK YOU FUCK FUCK FUCK FUCK FUCK FUCK"
    h "AAAAAAAAAAAARRRRRRRRRRRRGGGGGGGGGGGGGG"
    show h blush
    h "STOP STOP STOP STOP STOP STOP STOP STOP STOP"
    show h ahh at stop
    h "{i}*pant* *pant* *pant* *pant*...{/i}"
    window hide
    $hardpause(6)
    show h long -blush
    h "..."
    h "......"
    h "........."
    $hardpause(6)
    show h ahh
    h "wheres nari"
    h "are you going to kill her too"
    $quick_menu = False
    show h at fadeout()
    window hide
    $hardpause(1)
    hide h
    jump end_questions
    

label end_c_okay:
    $hardpause(1)
    show c long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show c ohh blush surprised
    c "..."
    show c sicko standard sweat
    c "Oh...{w}that's...{w}n-n-ice..."
    c "Um..."
    window hide
    $hardpause(3)
    show c long -blush -sweat
    c "...{w}um...{w}if it's okay, I have a question..."
    show c ahh
    c "What did you do with everyone else?"
    c "Is there a reason why you and I are the only ones here?"
    show c sicko sweat
    c "I'm honored t-that...{w}um..."
    show c long blush
    extend "I-I mean - It's nice to finally meet you in person."
    c "But I'm worried that the others might have been...{w}well you know..."
    show c sad
    c "..."
    $quick_menu = False
    show c at fadeout()
    window hide
    $hardpause(1)
    hide c
    jump end_questions
    

label end_a_okay:
    $hardpause(1)
    show a long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show a ohh
    a "..."
    show a sad crossed
    a "Okay I don't know what you have planning here but whatever it is I demand you tell me what's going on.."
    a "Also um...{w}mind answering my question?{w} You didn't go and off everyone, did you?{w} Or like, delete the world?"
    show a disappoint
    a "I kind of had a life back there...with friends...and a high school career to take care of."
    show a standard
    a "Would rather not have to give that up because of you coming onto the scene, you know?"
    $quick_menu = False
    show a at fadeout()
    window hide
    $hardpause(1)
    hide a
    jump end_questions
    

label end_n_okay:
    $hardpause(1)
    show n line at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    n "..."
    n "I will, huh?"
    window hide
    $hardpause(4)
    n "So tell me then."
    $hardpause(6)
    $quick_menu = False
    show n at fadeout()
    window hide
    $hardpause(1)
    hide n
    jump end_questions
    

label end_i_okay:
    $hardpause(1)
    show i long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show i open
    i "What? Are they here too?"
    i "I don't feel them nearby?!?! Are you trying to trick me?"
    show i sweat at shake()
    i "CHRISSSSYYYY!!!! ASPEEEEEEEEENNNNNN!!"
    show i disappoint at stop
    i "..."
    i "......"
    show i ahh
    i "What do you mean I'm not alone? There's no one else here!"
    show i open
    i "You don't count!!!"
    $quick_menu = False
    show i at fadeout()
    window hide
    $hardpause(1)
    hide i
    jump end_questions

    

###----------------------------------------------------------------3


label loadexe:
    $result = renpy.display_menu([("{font=fonts/ProFontWindows.ttf}LOAD_ALL()", "end_load_start")], screen="choice_end")
    $renpy.jump(result)












