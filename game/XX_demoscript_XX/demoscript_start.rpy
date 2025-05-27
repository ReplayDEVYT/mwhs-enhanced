

label escape_notify:

    $_skipping = False
    
    $quick_menu = False
    stop music fadeout 5.0
    screen black
    window hide 
    with Dissolve(3.0)
    show text "You can press the ESCAPE key or right click at any time to show the menu.{p}{p}You can also skip most seen text with the TAB or CTRL keys." at truecenter:
        alpha 0.0
        linear 0.8 alpha 1.0
        pause 7
        linear 0.8 alpha 0.0
    $hardpause(6)
    hide text
    $persistent.has_shown_escape_msg = True


label start:

    if not persistent.has_shown_escape_msg and not hasShownEscapeMSG :
        $hasShownEscapeMSG = True
        jump escape_notify

    #secrets reset
    $persistent.Nari_IconNoDance = False
    $persistent.Nari_IconGone = False

    #make sure we can skip (in case it was turned off)
    $_skipping = True


    if persistent.end_has_come and IsTimeForFinalEnding():
        jump restart_the_end

    if IsTimeForFinalEnding():
        jump intro_final

    #Turn this off since we're going normal
    $persistent.end_has_come = False

    $quick_menu = False
    stop music fadeout 5.0
    scene black
    window hide 
    with Dissolve(3.0)
    scene
    show bg school at place_school_bg
    show black zorder 0
    
    pause 3.0

    $hardpause(0.5)
    play music introtextmusic

    $hardpause(0.8)

    show bgblueworld:
        nearest True
        zoom 4
        parallel:
            alpha 0.0
            linear 8.0 alpha 0.8
        parallel:
            xpan 180
            linear 80. xpan 540
            repeat

    show ctc onlayer overlay:
        alpha 0.0
        pause 2
        block:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.3
            repeat
        on hide:
            linear 0.5 alpha 0.0
    
    ##opening quote
    python:
        #refill unseen quotes if all quotes have been seen
        
        if len(persistent.quote_bank_unseen) == 0:
            persistent.quote_bank_unseen = persistent.quote_bank_seen
            persistent.quote_bank_seen = []
        
        if len(persistent.quote_bank_unseen) == len(quote_bank):
            quote_index = 0
        else:
            quote_index = renpy.random.randint(0, len(persistent.quote_bank_unseen)-1)
        
        quote_array = persistent.quote_bank_unseen[quote_index]
        for msg in quote_array:
            if msg == "CLEAR":
                nvl_clear() 
                continue
            q("{cps=[qspeed]}{i}[msg]{/i}")
            if quote_array.index(msg) == 1:
                renpy.hide("ctc")

        persistent.quote_bank_unseen.pop(quote_index)
        persistent.quote_bank_seen.append(quote_array)
        #SECRET
        #https://youtu.be/oHg5SJYRHA0     
        renpy.save_persistent()

    stop music fadeout 8.0
    
label whitefade:

    show white onlayer overlay:
        alpha 0.0
        easeout 3.0 alpha 1.0
   
    play sound birds fadein 10.0 loop

    pause 10.0
    
    show ctc onlayer overlay:
        alpha 0.0
        xalign 0.4
        pause 2
        block:
            linear 1.0 alpha 0.8
            linear 1.0 alpha 0.3
            repeat
        on hide:
            linear 0.5 alpha 0.0

    show white:
        alpha 1.0

    hide bgblueworld
    hide black
    
    window show

    iq "...again?"
    hide ctc
    extend " So soon?"
    iq "I thought we just did!"
    aq "Uh, no? We haven't in a while."
    iq "Didn't we just...?"

    show c ahh at move(0.1, 0.0)
    show i long at move(0.4, 0.0)
    show a crossed long at move(0.8, 0.0)
    hide white
    show white zorder 50:
        on show:
            alpha 1.0
            easeout 10.0 alpha 0.0

    show c ahh
    cq "No, we got ramen yesterday."
    show c long
    show i ooo
    iq "Oh.{w} Right."
    show i long
    show a ahh
    aq "Well what should we do, then? I'm personally not feeling any of our usuals at the moment."
    show a long
    show c ahh
    cq "Shouldn't we wait for the others until we choose?"
    show c long
    show i disappoint
    iq "Nah, Hope is just going to say mochi like always. And I'm sure Nari isn't going to have an opinion..."
    show a ahh
    aq "How about the library?"
    show a disappoint
    show i long
    iq "I'm not really feeling library today..."
    show a long
    aq "Nothing to study?"
    show i ahh
    iq "More like don't want to."
    show c disappoint
    cq "I don't think I would m-{nw}"
    stop sound
    hide white
    show i open fists at move(0.3, 0.3, 200)
    iq "AHHH!{nw}"
    show a open at move(0.9, 0.3, 100)
    show c surprised open at move (-0.05)
    aq "WHOAH!"
    cq "..."
    aq "What is....!?!?"
    show i open at move(0.4)
    iq "OH MY GOD."
    show a ahh
    aq "Is that blurry thing...a person?!?!"
    show i wah
    iq "T-THAT'S THEM. THEY'RE HERE."
    show a ehh
    aq "Huh???"
    show i open at hop()
    iq "THAT'S THE PLAYER!!!!!!!!"
    show c standard laugh
    cq "Oh!"
    show i omg at shake(10)
    iqw "AHHHHHHHHHHHHHHHHHHH!!"
    show i omg at shake (10):
        ypos -200
        rotate -30
    iqw "SDDGXEQXJAWFVKZSLWEWAZSNWFWNWJXWDLKGSDGFWKGSDGFWKGS{nw}"
    show i omg at shake (10):
        ypos -220
        rotate 20
    iqw "DGFWKGSDGFWKGSDGFWKGSDGFWKGSDGFWKGSDGFWKGSDGFWKGSDGFW{nw}"
    hide i wah
    show i open oohh:
        xalign 0.5
        move (1.5, 0.5)
    iq "I'M GETTING HOPE AND NARI.{nw}"
    show c surprised open at move(0.2)
    hide i
    cq "Izzy hold on!"
    show c sad
    cq "..."
    show a sicko
    aq "..."
    window hide
    $renpy.pause(5, hard=True);
    show c long
    cq "...uh..."
    $renpy.pause(2, hard=True);
    show c standard
    $renpy.pause(1, hard=True);
    show c smile
    pause 1.5
    play music intromusic fadein 5.0
    show c smile at move(0.4, 1.0)

    $quick_menu = True

    cq "Hi there!{w} W-Welcome to {i}MetaWare High School!{/i}"
    show c ooo
    cq "Oh - I m-mean, {i}MetaWare High School (Demo){/i}!"
    show c smile
    menu:
        cq "It's wonderful to finally meet you!"
        "Hello!":
            $tone = 1
            jump start_polite
        "Goodbye!":
            jump start_bye
        "Screw you!":
            $tone = -1
            jump start_rude

label start_bye:
    ## c: 0.4 
    ## a: 0.9
    stop music
    show c ehh
    cq "...{w}eh...{w}what?"
    show a ahh
    aq "Goodbye?{w} Umm..."
    show c long
    cq "So...{w}I'm confused."
    show a disappoint
    aq "Maybe they're just stopping by."
    show black zorder 50:
        alpha 0.0
        easeout 5.0 alpha 1.0
    cq "But that doesn't make sense..."
    aq "...are they...?"
    show c surprised ahh 
    cq "What?! They're disappearing!?"
    show a ehh at move(0.7)
    aq "Wait wait wait wait wait wait!"
    show c open at move(0.5) zorder 2
    cq "ahhhhhhh Goodbye! It was nice to meet you!"
    jump credits_short
    return

##-------------------------
##Polite Start
##-------------------------

label start_polite:
    ## c: 0.4
    ## a: 0.9
    show a open at hop
    show c open at hop
    aq "Whoa!"
    cq "Wow, that was..{w} really weird..."
    show c ehh at hop
    extend "ehh! Sorry! I don't mean weird, just very...different..."
    show a ahh
    aq "That's not at all how I expected the player to...sound like."
    show c ooo
    cq "It was kind of cool, actually..."
    show a think disappoint
    aq "Yes, like you put words in our heads without speaking? Somehow?"
    show c smile
    cq "That's a good way of putting it!"
    show c ohh at hop
    cq "OH! We should introduce ourselves!"
    show c smile
    c "My name is Chris, and this here is Aspen."
    show a long
    a "..."
    show a standard happy at move (0.8, 0.4)
    a "It's a tremendous pleasure to meet you!"
    show a smile
    menu: 
        c "Is it...is it alright if we ask what your name is?"
        "Go ahead!":
            jump namegiver
        "I'd rather keep my name to myself.":
            jump noname_polite

#--------------------------------

label namegiver:
    ## c: 0.4
    ## a: 0.8
    show c laugh
    c "Ah, great! So...what can we call you?"
    show c smile
    jump inputname

label inputname:
    python:
        if not persistent.player_names:
            persistent.player_names = []
            default_name = ""
        else:
            default_name = persistent.player_names[-1] #name entered in most recently
        player = ""
        while player == "":
            player = renpy.input("{b}Please enter your name:{/b}", default=default_name)
        player = player.strip()
        #Nope
        if player.lower() == "the creator" or player.lower() == "creator":
            player = "Nope"
            
        player_lowercase = player.lower()
        persistent.player_names.append(player)
        
        player_name_is_a_name = IsName(player)

    if len(player_lowercase) == 1:
        show c ehh sweat
        c "Um...wow! What a unique name!{w=0.2} So-{nw} "
        show a sad
        a "Hold on, I think they might have pressed enter by mistake."
        show c -sweat ooo
        c "Huh?"
        show a crossed sad
        a "[player]? Really? You think they actually meant to write just one letter?"
        show c disappoint
        c "...um, I suppose that is a tad minimalistic..."
        show a smirk
        a "To say the least. Hey, come on, give your name a little more beef than that!"
        $player = ""
        jump inputname


    if len(player_lowercase) >= 30:
        $player = player[29:]
        show c sad
        c "Um...alright. So we'll call you [player]{nw} "
        show a long
        a "Wow that's a mouthfull. Is that your full name, or?"
        show c sicko sweat
        c "...um...maybe we can call you by a nickname? That's a little too long for most people to remember."
        show c -sweat
        $player = ""
        jump inputname

    python:
        if not persistent.player_names:
            persistent.player_names = []
            default_name = ""
        else:
            default_name = persistent.player_names[-1] #name entered in most recently

    if player_lowercase == "chris":
        show c morty sweat blush
        c "Really? Um...that's going to be confusing..."
        show c smile -sweat -blush
        c "But anyway-{nw}"
    elif player_lowercase == "isadora":
        show c ooo
        c "Really? Wow, that's going to be confusing...one of the gang is named Isadora too!"
        a "Yeah, she just ran off."
        show c smile
        c "But anyway-{nw}"
    elif player_lowercase == "aspen":
        show a wah
        a "Huh?"
        show c ooo
        c "Oh! Wow! What a funny coincidence!"
        show a crossed long
        a "...are you...{w}sure it's a coincidence?"
        show c long
        c "...yes?{w} Wait.{w} Oh."
        a "Yeah...they could have definitely just..."
        show a standard laugh
        a "Ha! Well no matter. If you want to really call yourself by the best name in the world that's fine by me!"
        show c disappoint
        c "But...what if their name really is Aspen?{nw}"
    elif player_lowercase == "hope":
        show c ooo
        c "Really? Wow, that's going to be confusing....one of the gang is named Hope too!"
        show a sad
        a "..."
    elif player_lowercase == "nari":
        show c open at hop
        c "...oh? Wow..."
        show a long
        a "Um."
        show c long
        c "Yeah that is quite weird. I don't think I've ever met another Nari. It's such an unusual name."
        show a crossed
        a "It's likely they must have already met Nari, so..."
        show c happy
        c "Ah, I guess you're right!"
        show a sad
        a "...Hm."
        show c ahh
        c "Does it mean anything, do you think?"
        show a long
        a "No idea."
        show c smile
        a "But anyway..."
    elif player_lowercase == "tim":
        show c laugh
        c "Wow!{w} That's such a great name!{w} Wow!{w} Wow!!!!"  
    elif IsName(player_lowercase):
        show c laugh
        c "Uh, ok! We'll call you [player]!{w=0.2} So-{nw}"
    elif IsBadWord(player_lowercase):
        stop music
        show c ehh
        show a ehh
        $hardpause(4)
        show a sad
        a "Well then."
        show c sad
        c "Yeah, they have every right to name themselves that, I guess..."
        a "Do we really have to...{w}call the player that?"
        c "Yes."
        show a crossed
        a "...really?"
        show c long
        c "Yeah."
        a "You're sure?"
        a "I really don't want to call them...{w}that."
        $hardpause(3)
        show c sad
        c "Well we don't really have a choice."
        a "That's...unfortunate."
        show c smile
        c "Besides, it's not the biggest deal in the world, is it?"
        c "I think it's kind of funny."
        a "...{w}well...{w}anyway...{w=0.35}{nw}"
    elif player_lowercase == "no":
        show c sad
        c "Uh.. \"No\"?{w} I can't tell if you're telling me you don't wanna tell me your name, or.."
        show a happy
        a "Wanna give them a name?"
        show c smile
        c "Sure!{w} What about..{w} er.."
        show c happy
        c "Tim!"
        show a inv
        a "Hm... {w}How do you know they're a boy, though?"
        show c long
        c "I guess..{w} Hm..{w} What pronouns you do use? {nw}"
        menu:
            "He/Him": 
                $pronoun = pronoun_he
                $Pronoun = Pronoun_he
                $is_conj = is_conj_heshe
                $s_conj = verb_conj_heshe
                $player = "Mr. Player"
                $persistent.pronoun_list.append("he")
                jump name_he
            "She/Her":
                $pronoun = pronoun_she
                $Pronoun = Pronoun_she
                $is_conj = is_conj_heshe
                $s_conj = verb_conj_heshe
                $player = "Ms. Player"
                $persistent.pronoun_list.append("she")
                jump name_she
            "They/Them":
                $pronoun = pronoun_they
                $Pronoun = Pronoun_they
                $is_conj = is_conj_they
                $s_conj = verb_conj_they
                $persistent.pronoun_list.append("they")
                $player = "Tim"
                jump name_they
    elif player_lowercase == "skibidi":
        show c line
        c "..{w}Isn't that the show middle schoolers like?"
        c "I guess if that's your name, then.."
    elif player_lowercase == "strelok":
        show c ahh at hop
        show a inv at hop
        stop music
        play sound MARKEDONE
        $hardpause(2.5)
        show white onlayer overlay:
            alpha 1.0
            easeout 3.0 alpha 0.0
        show c sicko
        c "What the hell was that..!?"
    else:
        show c ehh sweat
        c "Um...wow! What a unique name!{w=0.2} So-{nw} "

label pronoun_polite:
    ## c: 0.4
    ## a: 0.8

    show a smile at move(0.5, 0.3)

    show c long -sweat at move(0.3, 0.3, 40)
    menu: 
        a "So what pronoun do you go by then? I use \"they/them\" pronouns."  
        "He/Him": 
            $pronoun = pronoun_he
            $Pronoun = Pronoun_he
            $is_conj = is_conj_heshe
            $s_conj = verb_conj_heshe
            $dont_conj = dont_conj_heshe
            $persistent.pronoun_list.append("he")
            $persistent.pronoun_he = True
        "She/Her":
            $pronoun = pronoun_she
            $Pronoun = Pronoun_she
            $is_conj = is_conj_heshe
            $s_conj = verb_conj_heshe
            $dont_conj = dont_conj_heshe
            $persistent.pronoun_list.append("she")
            $persistent.pronoun_she = True
        "They/Them":
            $pronoun = pronoun_they
            $Pronoun = Pronoun_they
            $is_conj = is_conj_they
            $s_conj = verb_conj_they
            $dont_conj = dont_conj_they
            $persistent.pronoun_list.append("they")
            $persistent.pronoun_they = True
    show c sicko at move (0.15, 0.6)
    c "Also, you nearly bumped into [pronoun[1]], Aspen.."
    show a crossed ahh
    a "Sorry, but you were in the way!"
    show c disappoint
    c "...just be careful, alright?"
    show a think disappoint
    a "Hm...Come to think of it, what would happen if one of us bumped into [pronoun[1]]?"
    show c think
    c "I have no idea...[pronoun[4]] VERY...glowy."
    show a ahh
    a "And blurry."
    show a disappoint
    
label polite_veryglowy:
    menu:
        c "Why are you like that?"
        "What? Like what? What do you mean?":
            jump polite_what
        "Uh...why do you not have eyes?":
            jump polite_eyes

label polite_what:
    ## c: 0.4 ohh
    ## a: 0.8 ahh
    show c think
    c "Um...it's like you're...{w}uh...{w}really really big and...{w}uh...{w}no I take that back you're..."
    a "Hm...{w} [is_conj] [pronoun[0]] our height do you think?"
    show c long
    c "I think?"
    show a disappoint
    a "I don't know, [pronoun[0]] seem[s_conj] taller to me."
    show c think
    c "Really? I think [pronoun[4]] rather short."
    show a crossed long
    a "...yeah I guess you're right."
    ##timer 2.0 action Jump(polite_isadora_enter)
    show a ahh
    menu (screen="mouse_move_auto_choice"):
        c "How tall are you? We kind of can't tell"
        "I don't know.":
            jump polite_isadora_enter
        "I haven't measured.":
            jump polite_isadora_enter
        "Uhh...":
            jump polite_isadora_enter
        "7 fishes":
            jump polite_isadora_enter
        "4 giraffe necks":
            jump polite_isadora_enter
        "Fail":
            jump polite_isadora_enter
        
    jump polite_isadora_enter


label polite_eyes:
    $ask_about_eyes = True
    a "..."
    show a ahh
    extend "could you repeat that?"
    show c disappoint
    c "Where are our I's? Like, where am I? Is that what you mean?"
    show a long
    a "No I think [pronoun[4]] referring to the letter I..? Like...uh... {nw}"
    c "That doesn't make any sense."
    show a ohh
    a "Where are your...ice? Our ice? Is that what [pronoun[0]] said?"
    show c longbig
    c "...uh...that still doesn't make any sense."
    show a standard open
    a "No! No [pronoun[0]] said thighs! We just misheard [pronoun[1]], that's all!"
    show c sicko
    c "...{w}um..."
    show a crossed long
    a "By the way. Our bodies are placeholders."
    show c smile
    c "Yeah, we're temporary versions of our final selves."
    show c laugh
    c "We're the demo versions!"
    show a ohh
    a "Oh I just realized! The player isn't a demo of anything...{w}they're finished!"
    show c ohh
    c "Whoah...so this is what it's like..."
    show a crossed disappoint
    a "You won't believe how many people obsess over what they'll be like in the final game."
    show c long
    c "Don't you wonder about it?"
    show a long
    a "Of course I do. But not as much as some people...{w}it gets on my nerves sometimes."
    show a ahh
    menu (screen="mouse_move_auto_choice"):
        a "What's it like having an original body?"
        "It's nice.":
            jump polite_isadora_enter
        "ahh....what?":
            jump polite_isadora_enter
        "Ion even know":
            jump polite_isadora_enter
        "ts pmo icl":
            jump polite_isadora_enter
        "Fail":
            jump polite_isadora_enter

    jump polite_isadora_enter

    label name_she:
        c "So, then...we'll call you..{w} hm...{W} Ms. Player?"
        show a crossed long
        a "That's such a horrible name."
        show c smirk
        c "I think it's cute!"
        show a disappoint
        a "It's the opposite of cute. I feel like I'm talking to a dog."
        show a standard
        a "Wait, how do you know she isn't married?"
        show c ahh
        c "What?"
        show c disappoint
        extend " Oh, right, Ms. vs. Mrs...{nw}"
        $player = "Ms. Player"
        $player_name_is_a_name = False
        jump polite_isadora_enter
    label name_he:
        c "So, then...we'll call you..{w} er..{w} Mr. Player?"
        show a crossed long
        a "That's a horrible name."
        show c smirk
        c "I think it's nice!"
        show a disappoint
        a "I don't want to feel like I'm talking to a fish. {nw}"
        $player = "Mr. Player"
        $player_name_is_a_name = False
        jump polite_isadora_enter
    label name_they:
        c "Then we'll call you Tim!"
        show a crossed long
        a "That's not very gender neutral though.."
        show c smirk
        c "I think it's nice!"
        show a disappoint
        a "Eh.."
        c "I think they feel like a Tim."
        a "What does a Tim feel like..?"
        show c long
        c "You know...{w}like a Tim."
        a "..."
        show a ahh
        $player = "Tim"
        $player_name_is_a_name = True
        menu (screen="mouse_move_auto_choice"):
            a "Are you alright with this?"
            "Tim is fine!":
                jump polite_isadora_enter
            "Please call me something else, I don't care what.":
                jump polite_isadora_enter
            "Actually I changed my mind, let me just tell you my name.":
                jump polite_isadora_enter
            "Fail":
                jump polite_isadora_enter


