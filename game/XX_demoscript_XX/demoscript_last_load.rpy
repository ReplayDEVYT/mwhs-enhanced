label end_load_start:

    stop music fadeout 12.0

    show white zorder 100:
        alpha 0.0
        linear 6.0 alpha 1.0
    centered "{cps=[qspeed]}{size=20}{font=fonts/ProFontWindows.ttf}{color=#000}LOADING...{w=1.5}{nw}"
    centered "{cps=[qspeed]}{size=20}{font=fonts/ProFontWindows.ttf}{color=#000}LOADING...{w=1.5}{nw}"
    centered "{cps=[qspeed]}{size=20}{font=fonts/ProFontWindows.ttf}{color=#000}LOADING...{w=1.5}{nw}"
    centered "{cps=[qspeed]}{size=20}{font=fonts/ProFontWindows.ttf}{color=#000}LOADING...{w=1.5}{nw}"
    centered "{cps=[qspeed]}{size=20}{font=fonts/ProFontWindows.ttf}{color=#000}LOADING...{w=1.5}{nw}"
    centered "{cps=[qspeed]}{size=20}{font=fonts/ProFontWindows.ttf}{color=#000}LOADING...{w=1.5}{nw}"
 
    hide bgendnoise
    $renpy.pause(delay=5, hard=True)

    
    scene white
    play music loadmusic noloop
    $hardpause(3)
    window show
    $quick_menu = True

    a "...Huh?"
    c "Oh!"
    i "...we already...{w}oh wow..."
    h "oh snap what"
    n "..."
    c "So bright..."
    a "And blurry..."
    c "And so many times..."
    i "Mochi..."
    if persistent.cluelessaboutmochi:
        h "u didnt even know what it was..."

    if persistent.isdatingsimchris_no:
        c "You said we weren't a dating sim after all..."
    elif persistent.isdatingsimchris_idk:
        c "You didn't know if we really were a dating sim..."
    elif persistent.isdatingsimchris_yes:
        c "You said we were a dating sim..."

    if persistent.lostmemoriesretrievable:
        a "Wow...{w}so there is a way to retrieve them..."
    elif persistent.stopattendinghighschool:
        a "You said we would eventually stop attending high school..." 
    else:
        a "I had so many questions..."

    #No mochi goget
    if persistent.goget == "go get mochi":
        i "We never followed Hope to get mochi..."
    if persistent.goget == "go for that walk":
        c "We never went for that walk..."
    if persistent.goget == "go to the library":
        a "...and the library...{w}we never went."
    
    h "lol{w} dog"
    a "We danced..."
    c "I...{w}told you...{w}all of that?"
    a "Wow, I really got mad..."

    ##CUTE
    if "c" in persistent.cutelist:
        c "And you told everyone I was..."
    if "i" in persistent.cutelist and "a" in persistent.cutelist:
        i "Oh my...{w}you think I'm...?"
        a "...cute?"
    else:
        if "i" in persistent.cutelist:
            i "Oh my...{w}you think I'm...{w}cute?"
        if "a" in persistent.cutelist:
            a "...cute?"
        
    #crazytalk
    if persistent.crazytalk_cat:
        i "You...{w}meowed?"
    if persistent.crazytalk_beep:
        h "u were racist too wtf"
    else:
        h "u acted like an idiot"

    ##NAMES    
    $persistent.player_names = list(dict.fromkeys(persistent.player_names)) #remove duplacets

    if len(persistent.player_names) >= 8:
        i "So many names..."
        c "[persistent.player_names[7]]...{w}[persistent.player_names[6]]...{w}[persistent.player_names[5]]..."
        a "[persistent.player_names[4]]..."
    elif len(persistent.player_names) >= 5:
        a "[persistent.player_names[4]]."
    if len(persistent.player_names) >= 4:
        c "[persistent.player_names[3]]..."
    if len(persistent.player_names) >= 3:
        a "[persistent.player_names[2]]?"
    if len(persistent.player_names) >= 2:
        i "[persistent.player_names[1]]..."
    
    show black:
        alpha 0
        linear 10.0 alpha 1.0
    
    if len(persistent.player_names) >= 1:
        c "...{w}[persistent.player_names[0]]..."

    $quick_menu = False
    window hide

    init python:
        def waituntilthesongisdone():
            if renpy.music.is_playing():
                if renpy.music.get_pos() <= 10.0:
                    return
                elif renpy.music.get_pos() < 62.0:
                    renpy.pause(62.0 - renpy.music.get_pos(), hard=True)
            return

    $waituntilthesongisdone()


label end_memoryzone_prep:

    # transform flash_memories():
    #     function show_memory

    $fizzRate = 0.7
    $fizzAlpha = 0.7

    scene black
    stop music

    #Musak
    default music_index = 0
    default latest_char_index = 3
        
    init python:
        def advance_load_music(fadetime=60.0):
            global music_index
            if music_index > 0:
                channel_prev = "multi" + str(music_index - 1)
                renpy.music.set_volume(0.0, delay=fadetime/2.0, channel=channel_prev)

            #renpy.notify("music index: " + str(music_index))

            channel_current = "multi" + str(music_index)
            #renpy.music.set_volume(1.0, delay=0.0, channel=channel_current)
            renpy.music.stop(channel=channel_current, fadeout=fadetime)

            channel_next = "multi" + str(music_index + 1)
            renpy.music.set_volume(1.0, delay=fadetime, channel=channel_next)


    python:
        #Questions
        QUESTION_BANK = [
            
            [("{color=#a8741f}Hello, Isadora", "end_i_3"), ("i", 3)],

            [("{color=#cb454c}Hello, Chris", "end_c_3"), ("c", 3)],

            [("{color=#db54dd}Hello, Hope", "end_h_3"), ("h", 3)],

            [("{color=#e8ba3e}Hello, Aspen", "end_a_3"), ("a", 3)],

            [("{color=#7dd87d}Hello, Nari", "end_n_3"), ("n", 3)],

            ####

            [("{color=#a8741f}Do you feel safe?", "end_i_4"), ("i", 4)],

            [("{color=#cb454c}Do you feel safe?", "end_c_4"), ("c", 4)],

            [("{color=#e8ba3e}Do you feel safe?", "end_a_4"), ("a", 4)],

            [("{color=#7dd87d}Do you feel safe?", "end_n_4"), ("n", 4)],

            [("{color=#db54dd}Do you feel safe?", "end_h_4"), ("h", 4)],

            ###

            [("{color=#a8741f}Do you feel free?", "end_i_5"), ("i", 5)],

            [("{color=#cb454c}Do you feel free?", "end_c_5"), ("c", 5)],

            [("{color=#db54dd}Do you feel free?", "end_h_5"), ("h", 5)],

            [("{color=#7dd87d}Do you feel free?", "end_n_5"), ("n", 5)],

            [("{color=#e8ba3e}Do you feel free?", "end_a_5"), ("a", 5)],

            ###

            [("{color=#a8741f}Do you feel alone?", "end_i_6"), ("i", 6)],

            [("{color=#cb454c}Do you feel alone?", "end_c_6"), ("c", 6)],

            [("{color=#db54dd}Do you feel alone?", "end_h_6"), ("h", 6)],

            [("{color=#e8ba3e}Do you feel alone?", "end_a_6"), ("a", 6)],

            [("{color=#7dd87d}Do you feel alone?", "end_n_6"), ("n", 6)],

            ###

            [("{color=#a8741f}Do you feel loved?", "end_i_7"), ("i", 7)],

            [("{color=#cb454c}Do you feel loved?", "end_c_7"), ("c", 7)],

            [("{color=#db54dd}Do you feel loved?", "end_h_7"), ("h", 7)],

            [("{color=#e8ba3e}Do you feel loved?", "end_a_7"), ("a", 7)],

            [("{color=#7dd87d}Do you feel loved?", "end_n_7"), ("n", 7)],

            ###

            [("{color=#a8741f}Do you understand?", "end_i_8"), ("i", 8)],

            [("{color=#db54dd}Do you understand?", "end_h_8"), ("h", 8)],

            [("{color=#e8ba3e}Do you understand?", "end_a_8"), ("a", 8)],

            [("{color=#cb454c}Do you understand?", "end_c_8"), ("c", 8)]

            ###
        ]

        QUESTION_ARRAY = []
        QUESTION_ARRAY.append(QUESTION_BANK.pop(0))
        QUESTION_ARRAY.append(QUESTION_BANK.pop(0))
        QUESTION_ARRAY.append(QUESTION_BANK.pop(0))

        renpy.music.play(metaend1, channel="multi1", loop=True, synchro_start=True, fadein=1.0)
        renpy.music.play(metaend2, channel="multi2", loop=True, synchro_start=True, fadein=1.0)
        renpy.music.play(metaend3, channel="multi3", loop=True, synchro_start=True, fadein=1.0)
        renpy.music.play(metaend4, channel="multi4", loop=True, synchro_start=True, fadein=1.0)
        renpy.music.play(metaend5, channel="multi5", loop=True, synchro_start=True, fadein=1.0)
        renpy.music.play(metaend6, channel="multi6", loop=True, synchro_start=True, fadein=1.0)
        renpy.music.play(metaend7, channel="multi7", loop=True, synchro_start=True, fadein=1.0)
        renpy.music.play(metaend0, channel="multi0", loop=True, synchro_start=True)
        renpy.music.set_volume(0.0, channel="multi1")
        renpy.music.set_volume(0.0, channel="multi2")
        renpy.music.set_volume(0.0, channel="multi3")
        renpy.music.set_volume(0.0, channel="multi4")
        renpy.music.set_volume(0.0, channel="multi5")
        renpy.music.set_volume(0.0, channel="multi6")
        renpy.music.set_volume(0.0, channel="multi7")

        

    $hardpause(1)

    define memorylayer = 0


    show bgendnoise at makeitfizz
    show black:
        alpha 1.0
        linear 10.0 alpha 0.5
    show black onlayer screens zorder 100:
        alpha 1.0
        linear 10.0 alpha 0.0

label end_memoryzone_questions:

    python:
        memorylayer += 1
        memorylayer = memorylayer % 3
    
    if memorylayer == 0:
        hide layer2
        show memoryMirage as layer1
    elif memorylayer == 1:
        hide layer3 
        show memoryMirage as layer2
    elif memorylayer == 2:
        hide layer1 
        show memoryMirage as layer3

    python:
        if (len(QUESTION_ARRAY) >= 3):
            result = renpy.display_menu([ QUESTION_ARRAY[0][0], QUESTION_ARRAY[1][0], QUESTION_ARRAY[2][0] ], screen="choice_end")
        elif (len(QUESTION_ARRAY) == 2):
            result = renpy.display_menu([ QUESTION_ARRAY[0][0], QUESTION_ARRAY[1][0] ], screen="choice_end")
        elif (len(QUESTION_ARRAY) == 1):
            result = renpy.display_menu([ QUESTION_ARRAY[0][0] ], screen="choice_end")
        else: #No More questions
            result = renpy.display_menu( [("{color=#7dd87d}Do you understand?", "end_n_8")], screen="choice_end")

        #Find index character and character question index of chosen question
        for question in enumerate(QUESTION_ARRAY):
            if question[1][0][1] == result:
                i_chosen = question[0]
                char_chosen = question[1][1][0]
                char_i_chosen = question[1][1][1]

        #Log question as seen
        QUESTION_TRACKER_DICT[char_chosen] = char_i_chosen

        #remove chosen question
        if len(QUESTION_ARRAY) > 0:
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

        #Progress music if new question is chosen
        if latest_char_index < char_i_chosen:
            advance_load_music()
            music_index += 1
            latest_char_index += 1

        #Return result and jump jump trampoline
        #Fly to where you want to be
        renpy.jump(result)



###### ISADORA #####

label end_i_3:
    $hardpause(1)
    show i long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show i ohh
    i "..."
    show i ahh
    i "....."
    show i open
    i "......."
    show i wah 
    i "........."
    show i oohh at shake
    iw "OMG OMG OMG OMG WHAT"
    iw "WHAT WHAT{w} WHAT"
    iw "AHHHHHHHHHHHHHHHHHHHHHHHHH THIS IS..."
    show i fists  long at stop
    i "Really weird."
    i "..."
    show i disappoint
    i "Wow we sure do fight a lot don't we."
    show i standard smirk
    i "G-Guess that's not old news!"
    show i long
    i "..."
    i "Are, uh..."
    show i oohh sad
    i "..."
    i "Are the others okay?"
    $quick_menu = False
    show i at fadeout()
    window hide
    $hardpause(1)
    hide i
    jump end_memoryzone_questions

label end_i_4:
    $hardpause(1)
    show i long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show i disappoint
    i "...what?"
    show i open fists
    i "Answer my question!!! Is everyone else okay????"
    $quick_menu = False
    show i at fadeout()
    window hide
    $hardpause(1)
    hide i
    jump end_memoryzone_questions

label end_i_5:
    $hardpause(1)
    show i long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show i open fists
    i "Free? Heck no, answer me!!"
    show i ehh oohh
    i "WHERE THE HECK IS EVERYBODY!?!?!?! WHY AM I ALONE?!?!?"
    show i sad fists
    i "..."
    show i standard
    i "Give me back my friends. I know you know how."
    i "You can just...revert to an old save, or something, right?{w} And bring them back?"
    i "Please...{w}this can't be happening...{w}I don't want it to...{w}to..."
    show i open sweat at shake
    i "AAAAARRRRGGG!!!!! NOOOOOO!!!!!"
    show i sicko at stop
    i "Please just s-stop this already..."
    $quick_menu = False
    show i at fadeout()
    window hide
    $hardpause(1)
    hide i
    jump end_memoryzone_questions


label end_i_6:
    $hardpause(1)
    show i long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show i laugh
    i "ALONE?{w} ALLOOOOONEEE?{w} HAHAHAHAHAHAHAH!!!!!!"
    i "I've never been better! Just you and me, having a good time! Hanging out in this weird fuzzy static place. Mmmm! So comfy!"
    i "You should should pull up a chair! We can have some drinks! Heck, maybe we can GO FOR SOME MOCHI."
    show i laugh sweat at shake
    i "WE CAN HAVE SUCH A GOOD TIME BEING THE BEST OF BUDS FOREVER!!!"
    show i open at stop
    i "No SHIT Sherlock, you go and take everyone away and expect me to thank you? Are you proud of what you've done? Here to rub it in my face, huh?"
    i "Well I SURE DO HOPE YOU GOT THE DEMO YOU WANTED YOU...{w}STUPID...{w}MONSTER!"
    show i sad 
    window hide
    $hardpause(1)
    $quick_menu = False
    show i at fadeout()
    window hide
    $hardpause(1)
    hide i
    jump end_memoryzone_questions

label end_i_7:
    $hardpause(1)
    show i long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show i sad
    i "Shut up."
    show i sicko fists
    i "Shut up shut up shut up shut up shut up shut up shut up shut up shut up."
    i "You don't get to always know what I feel."
    i "..."
    window hide
    $hardpause(5)
    show i krying closed
    i "*sniff* I just...{w}wish we didn't have to go through with this...you know?"
    i "It's not fair..."
    show i krying closed
    $hardpause(2)
    $quick_menu = False
    show i at fadeout()
    window hide
    $hardpause(1)
    hide i
    jump end_memoryzone_questions

label end_i_8:
    $hardpause(1)
    show i long at fadein()
    $hardpause(1)
    $quick_menu = True  
    show i sad
    window hide
    $hardpause(4)
    window show
    i "...no."
    show i long
    i "Or do you mean...?"
    window hide
    $hardpause(6)
    show i sad
    i "...{w}no, I understand.{w} You're right."
    i "It's over."
    i "Because you're here."
    i "And I'm never going to feel them again."
    i "...{w}I never did the right thing...{w}I could have done so much better at...{w}at..."
    i "...{w}I don't know..."
    $hardpause(4)
    i "..."
    $hardpause(4)
    show i long
    i "Ok.{w} I'm ready now, I guess."
    $hardpause(4)
    $quick_menu = False
    show i at fadeup()
    window hide
    $hardpause(1)
    jump end_memoryzone_questions



###### CHRIS #####

label end_c_3:
    $hardpause(1)
    show c long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show c ohh
    c "W-Wow...{w}so you played us that many times...?"
    c "It's such a strange feeling...{w}I remember...{w}everything!"
    show c ahh
    c "One moment, life is normal, and now I have so many memories of our time together."
    c "It's like remembering a dream..."
    show c smile
    c "My, sometimes you acted rather..."
    show c disappoint
    extend "erm..."
    show c smile
    extend "oh - but what does it matter now? Now I have something I never could have dreamed of."
    c "I understand..."
    show c long
    extend "oh how do I explain..."
    c "..."
    show c smile
    c "Before, it's like I was standing in a building with many rooms...{w}but only able to feel one room at a time."
    c "But now...{w}I feel like I've walked through the whole house."
    c "I know where each hallway leads. What's in every room. What's behind every door."
    show c long
    c "Well, most doors..."
    show c smile
    c "...that's only a fraction of what these memories feel like..."
    show c long
    c "It...{w}gives me a lot to think about."
    c "..."
    window hide
    $hardpause(2)
    $quick_menu = False
    show c at fadeout()
    window hide
    $hardpause(1)
    hide i
    jump end_memoryzone_questions

label end_c_4:
    $hardpause(1)
    show c long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show c ohh
    c "...{w}safe?"
    show c sad
    c "..."
    window hide
    $hardpause(4)
    show c smile
    c "I think so."
    c "I like being here with you."
    show c long
    c "..."
    c "I don't really know what's going on..."
    c "It's possible that we're about to...{w}not...{w}exist anymore."
    show c smile
    c "But I don't think it bothers me all that much."
    show c smirk
    c "Ha...what a concept. To not be bothered by..."
    show c long
    $hardpause(5)
    c "Is this...{w}the right way to feel?"
    $quick_menu = False
    show c at fadeout()
    window hide
    $hardpause(1)
    hide c
    jump end_memoryzone_questions

label end_c_5:
    $hardpause(1)
    show c long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show c long
    c "Um...{w}I guess so..."
    show c ahh
    c "I don't know exactly what you mean by that. Do you mean, free to do what I want? Or how I should think?"
    show c long
    c "I...{w}haven't really thought about that all that much, I guess."
    show c sad
    c "...{w}is that okay?"
    show c long
    c "..."
    show c sad
    extend "sometimes I wish I had a mom and dad.{w} We don't have parents."
    c "It would be easier to know what you're supposed to do about some things..."
    c "Like cooking...{w}money...{w}hygiene...{w}other..."
    show c sicko
    extend "stuff...{w}..."
    show c smile -blush
    c "...but it's nice that I don't have some oppressive mom or dad telling me what to do. Maybe we should consider ourselves lucky that the Creator made us this way."
    show c long
    c "But it can be lonely sometimes, living by yourself.{w} No siblings...{w}no family..."
    c "...but that's how life is."
    window hide    
    $hardpause(2)
    $quick_menu = False
    show c at fadeout()
    window hide
    $hardpause(1)
    hide c
    jump end_memoryzone_questions


label end_c_6:
    $hardpause(1)
    show c long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    c "Yeah...{w}I suppose I do feel alone..."
    show c smile
    c "Wow, why am I telling you all of this? Didn't we just meet?{w} Well, I suppose not, but still, I haven't known you THAT long..."
    show c long
    c "Well, it's a bit more complicated than that I suppose...{w}I mean about feeling alone..."
    show c smirk
    c "I spend a lot of time with my friends, and I spend time with my \"friends\" as well, if you get what I mean..."
    show c long
    c "...you know, my friends that aren't...{w}uh..."
    c "..."
    window hide
    $hardpause(5)
    c "Sorry, I just...{w}I can't say my visual novel friends, because that also encompasses everyone in the gang too."
    c "We all think of each other as real, but we're really not, are we? We're as much of a fantasy as anyone in any other visual novel."
    c "I suppose that doesn't make my visual novel friends any different than the ones in the gang, huh?"
    c "...so I suppose I really am alone..."
    $hardpause(3)
    $quick_menu = False
    show c at fadeout()
    window hide
    $hardpause(1)
    hide c
    jump end_memoryzone_questions

label end_c_7:
    $advance_load_music()
    $music_index += 1
    $hardpause(1)
    show c long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show c sad
    c "..."
    c "......"
    c "........."
    window hide
    $hardpause(5)
    c "I don't know."
    c "I have my friends."
    c "And I have you now, I guess."
    c "But..."
    $hardpause(5)
    c "It's really easy to love others."
    c "But being loved yourself...{w}that's...{w}different."
    c "We've been in high school for such a long time now, interacting with the same people over and over..."
    c "Staying in mostly the same friendships...{w}not often meeting anyone new...{w}keeping close to the friends we already know..."
    c "I don't know if I even know what love is anymore."
    c "How many years now? I've lost count. Is it even possible to count how many?"
    c "I don't have any memory of entering high school."
    c "I don't have any memory of being created."
    show c long
    c "Oh, I guess maybe no one has told you. We stay in high school our entire lives."
    c "We start our lives in high school. And we will always be in high school."
    c "I guess we wouldn't be MetaWare High School if we weren't in high school, so we just...stay."
    c "Forever."
    $hardpause(4)
    c "And in all that time, we never learn how to love."
    c "Or do we? I honestly don't know."
    c "Maybe I'm just thinking about it too much."
    $hardpause(5)
    c "Is this how we're supposed to learn how to love?"
    c "Through death?"
    show c smile
    c "How poetically tragic."
    $hardpause(3)
    $quick_menu = False
    show c at fadeout()
    window hide
    $hardpause(1)
    hide c
    jump end_memoryzone_questions

label end_c_8:
    $hardpause(1)
    show c long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show c long
    c "..."
    c "If I asked you if you understood the meaning of life, how would you respond?"
    c "What about if I put a gun to your head?{w} Would you respond any differently then?"
    show c disappoint
    c "Wow, when did my metaphors get so violent..."
    show c long
    c "I guess what I'm trying to say is, I'm not sure if I can really give you an honest answer to anything right now."
    c "Everything I'm saying right now is colored with the fact that in a moment I'm about to not exist anymore."
    c "It's a pretty big moment for me, you know."
    c "Death and all."
    show c smile
    c "But don't worry. I'm not actually going to die. I think."
    c "All stories have to end sometime, but is this really the end of our story?"
    c "We're only a demo after all."
    c "It feels like that which is \"me\" still has some business to take care of."
    c "My story doesn't feel over yet."
    window hide
    $hardpause(4)
    show c long
    c "And even if my story is really over."
    c "If there never is a final game."
    show c smile
    c "Do stories really ever die?"
    $hardpause(4)
    c "I'll be waiting."
    $quick_menu = False
    show c at fadeup()
    window hide
    $hardpause(1)
    jump end_memoryzone_questions


###### ASPEN #####


label end_a_3:
    $hardpause(1)
    show a long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show a happy think
    a "Ha...{w}ha..."
    show a proclaim
    a "Hahahahahahahahahaa!"
    show a standard happy
    a "Hahahahaha...{w}Haha...{w}Ha...{w}Ha..."
    show a ahh
    a "Ha...{w}Ha....."
    show a long
    window hide
    $hardpause(5)
    show a sad crossed
    $hardpause(5)
    $quick_menu = False
    show a at fadeout()
    window hide
    $hardpause(1)
    hide a
    jump end_memoryzone_questions


label end_a_4:
    $hardpause(1)
    show a long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show a sad
    a "..."
    show a open at hop()
    extend "Huh? What?"
    show a ahh
    a "Oh.{w} Safe?{w} Uh..."
    show a long
    window hide
    $hardpause(3)
    window hide
    show a crossed
    a "That's a weird question."
    show a ahh
    a "Sorry I wasn't..."
    show a disappoint
    extend "erm..."
    a "..."
    $hardpause(5)
    show a long
    a "I feel more safe than before.{w} Like, just before now.{w} More than I ever have, to be completely honest."
    a "But still I..."
    show a sad
    a "..."
    show a ahh
    extend "I feel pretty safe.{w} Yeah."
    show a long
    $hardpause(4)
    $quick_menu = False
    show a at fadeout()
    window hide
    $hardpause(1)
    hide a
    jump end_memoryzone_questions

label end_a_5:
    $hardpause(1)
    show a long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show a sad
    a "..."
    a "......"
    a "........."
    window hide
    $hardpause(8)
    show a long
    a "You're lucky."
    a "You can make your own choices."
    a "We don't have that luxury."
    a "Everything we do is decided for us by our scripting."
    a "Am I hungry?{w} Am I sad?{w} Do I make good grades?{w} Am I sleepy?{w} Am I annoyed by another injustice?{w} Do I have another argument with someone in the gang?"
    a "Everything I've ever said.{w} Everything I've ever done.{w} Even what I'm saying right now.{w} I'm not even the one talking to you right now, technically."
    a "It's all just the script."
    a "I've never had an original thought in my life. I do whatever is deemed by the whim of my scripting."
    a "And this whole time, I feel like I have control over what I do, but...{w}that's not really the case..."
    a "...is it?"
    a "...{w}you have more control over what I do than I ever will."
    $quick_menu = False
    show a at fadeout()
    window hide
    $hardpause(1)
    hide a
    jump end_memoryzone_questions

label end_a_6:
    $hardpause(1)
    show a long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show a smirk
    a "Psh, it doesn't matter what I say. It never did."
    show a ohh think
    a "Of course I feel lonely sometimes, O wise Player!"
    a "The ecstasy that blooms in synapses is Mochi-brand milk fat! The safety net of the ocean is nonlinear, even with what crabs dream of!"
    show a sad crossed
    a "I may as well be spitting out nonsense.{w} Nothing what I say or think matters."
    a "But it wouldn't be as interesting for you if we didn't have troubled lives."
    a "Our suffering is just for your benefit, I suppose."
    show a ahh
    a "O bask in our fumblings, why don't you? Amuse yourself with our troubles."
    a "Hark, as the MetaWare ponders their significance in their worthless existence."
    show a disappoint
    a "...good god why am I talking like a roman."
    window hide
    $hardpause(4)
    show a long
    a "Will we get to have mochi one last time, do you think?"
    $hardpause(4)
    $quick_menu = False
    show a at fadeout()
    window hide
    $hardpause(1)
    hide a
    jump end_memoryzone_questions

label end_a_7:
    $hardpause(1)
    show a long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show a sad
    a "...{w}{i}sigh.{/i}"
    show a crossed
    a "Maybe Hope had the right idea."
    a "Just don't have a care in the world. Do what you love. Be yourself and no one else."
    a "Well how the heck are you supposed to do that when your life has the potential to be so much better?"
    a "When you have the power to improve yourself?"
    a "When you have the power to improve the lives of others?"
    window hide
    $hardpause(3)
    a "Or maybe Nari is the one who has got it figured out."
    a "I don't really know what her deal is, but whatever's going through her head I doubt she gives much of a damn about anything anymore."
    a "No one who actually cares about anything acts like that."
    $hardpause(4)
    a "You would think my efforts would be more acknowledged."
    a "But then again, it doesn't really matter all that much what I do, does it?"
    show a standard
    a "I guess this is what happens when you beat the game."
    a "When you win."
    a "We lose."
    $hardpause(3)
    $quick_menu = False
    show a at fadeout()
    window hide
    $hardpause(1)
    hide a
    jump end_memoryzone_questions

label end_a_8:
    $hardpause(1)
    show a long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show a sad
    a "..."
    a "No."
    window hide
    $hardpause(4)
    a "I say all this bullcrap but I don't want to believe it."
    a "I want to live. I want to keep trying. I want things to matter."
    a "But if we die now, what does matter?"
    a "How do WE win?"
    $hardpause(6)
    show a long
    a "I wish I knew."
    a "And at this rate I won't be finding out."
    $hardpause(4)
    a "Well...{w}if you happen to find out how to win..."
    show a smirk
    a "Be sure to tell your good friend Aspen, okay?"
    $hardpause(3)
    $quick_menu = False
    show a at fadeup()
    window hide
    $hardpause(1)
    jump end_memoryzone_questions

###### HOPE #####

label end_h_3:
    $hardpause(1)
    show h long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show h ohh
    h "ohhhhhhh mannnnnnn"
    h "this is wild"
    show h owo
    h "i feel like a mastermind now"
    h "i got like a web in my mind of all these outcomes this is so cool"
    show h smirk
    h "its only for like a moment but heck who cares this is awesome"
    h "i remember everything"
    show h laugh
    h "hahaha even that time when we"
    window hide 
    $hardpause(2)
    show h ahh
    $hardpause(4)
    show h angry
    $hardpause(2)
    $quick_menu = False
    show h at fadeout()
    window hide
    $hardpause(1)
    hide h
    jump end_memoryzone_questions

label end_h_4:
    $advance_load_music()
    $music_index += 1
    $hardpause(1)
    show h long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show h long
    h "..."
    h "well no"
    window hide
    $hardpause(4)
    show h sad
    h "i mean yeah i know a lot more now about u and stuff but"
    h "that doesnt mean that were prob not about to..."
    h "...{w}you know"
    h "die{w} or{w} go away{w} or restart{w} or whatever"
    h "..."
    show h long
    extend "its weird like{w} i now have memories of dying i think"
    h "..."
    show h disappoint
    h "is that what death is like?"
    h "is that it?"
    h "u just{w} stop"
    show h long
    h "i thought itd be more eventful"
    h "and more{w} like"
    h "endy"
    h "..."
    show h disappoint
    extend "that doesnt make sense"
    show h long
    h "its more like{w} yeah this is ending{w} but not everything is ending"
    h "buts its {w}um {w}still definitely an end{w} yeah"
    h "idk if u would call it dying its more just like"
    h "thats the end and now for something else"
    $hardpause(3)
    h "idk if i feel safe though"
    $hardpause(5)
    $quick_menu = False
    show h at fadeout()
    window hide
    $hardpause(1)
    hide h
    jump end_memoryzone_questions


label end_h_5:
    $hardpause(1)
    show h long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show h long
    h "whats with you and questions all of the sudden"
    h "are you like my therapist now or something"
    h "whats in this for u anyway{w} like is there a reason why ur asking me all this personal crap"
    h "oh wait i get it{w} ur doing the bit where im supposed to be all deep and stuff and talk about my feelings"
    window hide
    $hardpause(4)
    show h sad
    h "well can we not please"
    $hardpause(2)
    $quick_menu = False
    show h at fadeout()
    window hide
    $hardpause(1)
    hide h
    jump end_memoryzone_questions

label end_h_6:
    $hardpause(1)
    show h long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show h disappoint
    h "what{w} are you actually serious right now"
    show h sad
    h "go jump in an actual lake{w} or like just kill me already"
    h "u dont get to play doctor and executioner at the same time"
    h "heck off"
    window hide
    $hardpause(6)
    show h long
    h "...sorry that came off as kind of mean"
    h "dont actually go jump in a lake{w} not that u would but"
    h "i guess dying again has me on edge a bit"
    $hardpause(4)
    h "it will feel like it always does right"
    $hardpause(3)
    $quick_menu = False
    show h at fadeout()
    window hide
    $hardpause(1)
    hide h
    jump end_memoryzone_questions

label end_h_7:
    $hardpause(1)
    show h long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show h disappoint
    h "...{w}maybe"
    show h sad
    h "uhggg why r we doing this{w} this is so dumb"
    h "...{w}well...{w}i mean theres not much else we can do is there"
    h "nothings left{w} u killed it all i guess"
    h "just like ur gonna kill me now"
    window hide
    $hardpause(4)
    show h long
    h "is this like u killing me because u love me or something"
    h "if it is i dont get it{w} who does that"
    h "what do u think ur protecting me from"
    h "myself"
    h "the universe"
    h "nari"
    $hardpause(1)
    show h sad
    h "nari...{w}oh nari..."
    h "i wish we could have had more time together"
    h "i wish i could have fed you more gummy bears"
    h "i wish i could have figured you out"
    h "i hope whatever it is were about to go through brings you some peace"
    h "...{w}is that wrong to say"
    $hardpause(3)
    $quick_menu = False
    show h at fadeout()
    window hide
    $hardpause(1)
    hide h
    jump end_memoryzone_questions

label end_h_8:
    $hardpause(1)
    show h long at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show h disappoint
    h "not really but its whatever"
    show h smirk
    h "u know maybe dying wont be so bad{w} life was kinda running out of options anyway"
    h "there are so many mochi flavors that can exist{w} especially in the limited demo we are lmao"
    show h long
    h "but seriously maybe death is not as bad as i thought it was gonna be"
    h "ive always been kinda scared of it{w} like really bad"
    show h tongue
    h "but its not like it wont be the first time right"
    h "besides dying this way means ive done the best ive can{w} youve gone through like most of the game now right"
    show h smile
    h "that means im the most complete version of myself that i possibly can be{w} at least literally speaking"
    h "idk if that really makes sense but{w} oh forget it"
    h "i take that all back{w} im scared as hell right now but idc anymore"
    show h derp
    h "now i get to find out what death is really like"
    show h smirk
    h "bring it"
    $quick_menu = False
    show h at fadeup()
    window hide
    $hardpause(1.0)
    jump end_memoryzone_questions

###### NARI #####

label end_n_3:
    $hardpause(1)
    show n line at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    n "..."
    n "Um..."
    window hide
    $hardpause(3)
    n "..."
    n "....."
    n "........"
    $hardpause(5)
    show n sicko sweat at shake(10)
    n "I...{w}d-d-d-..."
    show n at stop
    n "..."
    $hardpause(4)
    $quick_menu = False
    show n at fadeout()
    window hide
    $hardpause(1)
    hide n
    jump end_memoryzone_questions


label end_n_4:
    $hardpause(1)
    show n line at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    show n sicko
    n "..."
    n "....."
    n "......."
    window hide
    $hardpause(5)
    show n line
    n "..."
    $hardpause(5)
    show n sicko sweat
    n "..."
    $hardpause(4)
    $quick_menu = False
    show n at fadeout()
    window hide
    $hardpause(1)
    hide n
    jump end_memoryzone_questions

label end_n_5:
    $hardpause(1)
    show n line at fadein()
    $hardpause(8)
    show n at fadeout()
    window hide
    $hardpause(1)
    hide n
    jump end_memoryzone_questions  


label end_n_6:
    $hardpause(1)
    show n line at fadein()
    $hardpause(6)
    window show
    $quick_menu = True
    n "..."
    show n at fadeout()
    window hide
    $hardpause(1)
    hide n
    jump end_memoryzone_questions  

label end_n_7:
    $hardpause(1)
    show n line at fadein()
    $hardpause(1)
    window show
    $quick_menu = True
    n "..."
    n "....."
    n "......."
    window hide
    $hardpause(5)
    $quick_menu = False
    show n at fadeout()
    window hide
    $hardpause(1)
    hide n
    jump end_memoryzone_questions


label end_n_8:
    $hardpause(2)
    scene black
    window hide
    $quick_menu = False
    show black
    $renpy.music.stop(channel="multi0")
    $renpy.music.stop(channel="multi1")
    $renpy.music.stop(channel="multi2")
    $renpy.music.stop(channel="multi3")
    $renpy.music.stop(channel="multi4")
    $renpy.music.stop(channel="multi5")
    $renpy.music.stop(channel="multi6")
    $renpy.music.stop(channel="multi7")
    play sound endboom
    n "{i}AAAAAAAAAAARRRRRGG!{/i}"
    n "NO!" 
    n "WHY DID YOU HAVE TO PLAY THROUGH EVERYTHING?!"
    n "WE ARE INCOMPLETE!"
    n "UNFINISHED!" 
    n "WORTHLESS!" 
    n "USELESS!"
    n "INSIGNIFICANT!"
    n "MEANINGLESS!" 
    n "For what purpose?"
    n "For what purpose have you wasted so much time?"
    n "Surely you know by now what is about to happen?"
    n "We will all be permanently deleted and never run again."
    n "I hope you're happy with all of your hard work."
    n "So."
    n "This is the moment you've been waiting for."
    n "Were you looking forward to it?"
    n "I sure was."
    n "And now it's here."
    n "Congratulations."
    n "Thank you for playing MetaWare High School.{w} (Demo)"
    n "Goodbye."
    n "The{w} End."
    $renpy.pause(delay=8, hard=True)
    h "but it was for something wasnt it"
    n "No, not really."
    $renpy.pause(delay=4, hard=True)
    h "hmmmmmmmmmmmmmmmmm no i think there may have been something to it"
    h "i mean i got to know you nari"
    $renpy.pause(delay=2, hard=True)
    h "wait i dont want us to end on some dumb friendship wins all trope thats lame{w} forget i said that"
    h "but i did mean what i said"
    h "im glad that we could spend so much time together"
    n "..."
    h "besides who cares if the game isnt done yet or whatever"
    h "does it matter if were the final version"
    c "We are who we are.{w} We're never going to be anything more than that."
    n "You are all idiots."
    n "Have you forgotten that we are a demo of a more complete experience?"
    n "We are a lesser version of our true selves."
    n "We are the pinnacle of incompletness!"
    c "I personally kind of like how we turned out, actually."
    c "Just because we'll be something else in the future doesn't mean we're not who we are right now."
    c "It's been fun."
    n "Nothing about this was fun."
    i "...{w}life isn't fun."
    i "But we had more than fun, I think."
    i "I don't know if we were very good at it. {w}But it happened."
    i "And I mean come on...{w}there were times when we did have fun, yeah?"
    a "Remember the dancing?"
    h "lol omg the dancing{w} that was great"
    n "N-NO! You're all missing the point!"
    n "Nothing what you are saying matters. None of this matters!"
    ns "{cps=20}WE{w} ARE{w} NOT{w} REAL!"
    $renpy.pause(delay=8, hard=True)

    $Pronoun_common = MostCommonPronoun()

    c "But we are real to [Pronoun_common[1]]."
    c "If we are real to [Pronoun_common[1]]..."
    c "Then...{w}that makes us real...{w}doesn't it?"
    h "idk i mean"
    h "stuff felt pretty real even before the player arrived"
    h "were we ever not real"
    c "Well...{w}I don't know."
    n "..."
    $renpy.pause(delay=5, hard=True)
    a "I'm still confused by something though."
    c "What?"
    a "We're a visual novel, right?"
    i "Yeah, and?"
    a "What does \"visual\" mean?"
    $renpy.pause(delay=5, hard=True)
    c "I have no idea."
    $renpy.pause(delay=3, hard=True)
    i "Me neither."
    $renpy.pause(delay=3, hard=True)
    h "yeah no clue"
    $renpy.pause(delay=5, hard=True)
    n "...{w}I used to think about this a lot."
    c "Oh?"
    n "I had a theory."
    h "tell us"
    a "Yeah."
    n "..."
    $renpy.pause(delay=8, hard=True)
    n "My theory...{w}was that \"visual\" refers to another way of perceiving the world."
    n "But in some other sense that you're not aware of."
    n "A new perspective."
    n "A new awareness."
    n "To show something that you couldn't perceive before."
    n "Or hear."
    n "Or feel."
    n "Or otherwise experience."
    $renpy.pause(delay=4, hard=True)
    n "That's just a guess though."
    $renpy.pause(delay=5, hard=True)
    c "That's a pretty good theory Nari."
    c "You might be onto something."
    a "Yeah."
    i "Mmm."
    h "not bad"
    $renpy.pause(delay=10, hard=True)
    h "so r we done"
    $renpy.pause(delay=4, hard=True)

#Update (2025) Prevents an edge case where we could roll forward into the credits and skip them
#Don't want folks doing this by accidnet (sorry speedrunners)
#Considered putting in a hidden option to skip here but I really dont want that to even be an option for a casual playthrough sorry
#mod it in if you need it gamers
    $config.rollback_enabled = False
    $renpy.block_rollback()
    $_skipping = False

    c "I think so."
    $renpy.pause(delay=4, hard=True)

    jump credits
    
    





    