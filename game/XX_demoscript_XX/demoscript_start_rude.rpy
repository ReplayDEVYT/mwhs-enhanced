##-------------------------
##Rude Start
##-------------------------

label start_rude:
    ## c: 0.4
    ## a: 0.9
    show a ahh
    show c ahh
    
    $renpy.music.set_pause(True)

    $hardpause(2)
    aq "..."
    cq "..."
    aq "Chris...{w}did you just hear...{w} \"Screw you\"?"
    show c long
    c "That's what I heard too...{w}I think?"
    show a long
    aq "Yeah it sounded like it was coming from inside my head or something."
    c "I'm assuming that came from...?"
    aq "..."
    show a laugh standard sweat
    $renpy.music.set_pause(False)
    extend "Wahahahaha!{w} Screw you too then!"
    show c laugh sweat
    c "Um...yeah! Hahaha..."
    aq "Go to hell!"
    show a longbig
    aq "..."
    show c disappoint
    c "..."
    aq "..."
    show c laugh
    c "Well...uh, this is {i}MetaWare High School (Demo){/i}. My name is Chris, and this is Aspen."
    a "You already said that."
    show c morty
    c "Oh, right.{w} Uh..."
    menu: 
        c "Is it alright if we ask your name?"
        "Go ahead!":
            show c -sweat
            jump namegiver
        "You're never going to know who I am! Muhahahahahaha!!!!!!":
            $player = "Player"
            jump rude_noname

label rude_noname:
    show a sad -sweat
    a "I think they're just messing with us."
    show c disappoint -sweat
    c "They sure do have a..."
    show c smile
    extend "good sense of humor!"
    show a long
    a "Hey Chris...are you hearing the player talk the same way I am?"
    show c disappoint
    c "Uh...I feel like I'm hearing them from the inside of my own head?"
    a "Yeah, it's a little disorienting."
    show c disappoint
    c "..."
    show c ahh
    menu: 
        c "W-w-well, if we won't ever get to know your name, can we at least know your pronoun?"
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
        "cnap#gnd&si/asdviwoekdjs?zl":
            $pronoun = pronoun_they
            $Pronoun = Pronoun_they
            $is_conj = is_conj_they
            $s_conj = verb_conj_they
            $dont_conj = dont_conj_they
            jump rude_postnoname_nopronoun
    


label rude_postnoname_pronoun:
    show c laugh
    c "Ok, got it!"
    if pronoun[0] == "he" or pronoun[0] == "she":
        show a ahh
        a "Do they feel like a \"[pronoun[0]]\" to you?"
        show c ooo
        c "Huh?{w} Sure?"
        show a long
        a "But they're so blurry. How can you tell?"
    else:
        show a ahh
        a "Do they feel weird to you too?"
        show c disappoint
        c "Weird? What do you mean?"
        show a think long
        a "...{w}I don't know..."
    show c long
    c "Uh...{w}[pronoun[0]] [is_conj] hard to make out, huh?"
    show a crossed
    a "Yeah..."
    jump polite_veryglowy


label rude_postnoname_nopronoun:
    show c disappoint
    show a ahh
    a "Okay now they really are screwing with us."
    show c laugh sweat
    c "Well, uh...hahaha! That's what they said they were going to do! Screw with us, right?"
    a "I never would have expected the player's behavior to be this...unpredictable."
    show a long
    show c sicko -sweat
    menu:
        c "...yeah."
        "{i}{b}DANCE!!!!!!!{/b}{/i}":
            $crazytalk1 = "butt"
            stop music fadeout 1.0
            python:
                #prepare dancing music
                dancingnow = True
                renpy.music.play(dancingmusic0, channel="multi0", loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
                renpy.music.play(dancingmusic1, channel="multi1", loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
                renpy.music.play(dancingmusic2, channel="multi2", loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
                renpy.music.play(dancingmusic3, channel="multi3", loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
                renpy.music.play(dancingmusic4, channel="multi4", loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
                renpy.music.play(dancingmusic5, channel="multi5", loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
                renpy.music.play(dancingmusic6, channel="multi6", loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
                renpy.music.play(dancingmusic7, channel="multi7", loop=True, fadeout=1.0, synchro_start=True, fadein=1.0)
                renpy.music.set_volume(0.0, channel="multi1")
                renpy.music.set_volume(0.0, channel="multi2")
                renpy.music.set_volume(0.0, channel="multi3")
                renpy.music.set_volume(0.0, channel="multi4")
                renpy.music.set_volume(0.0, channel="multi5")
                renpy.music.set_volume(0.0, channel="multi6")
                renpy.music.set_volume(0.0, channel="multi7")
            jump rude_butt
        "Actually I'm a cat. Meow Meow.":
            $crazytalk1 = "cat"
            $persistent.crazytalk_cat = True
            jump rude_cat
        "BEEP BOOOP BOP BAM BOOP BOP WEEEEEE!!!!":
            $crazytalk1 = "beep"
            jump rude_BEEP
        "What are you talking about? This behavior is completely normal for our people.":
            $crazytalk1 = "normal"
            jump rude_normal_crazy1

label rude_cat:
    show c ehh
    c "...{w}eh..."
    show a disappoint
    a "Yeah. Okay."
    show c long
    a "So [pronoun[4]] a cat."
    c "Yup."
    a "..."
    show c ohh
    c "Do you think they're actually a cat?"
    show a sad
    show a crossed
    a "No."
    show c long
    c "...{w} you sure?{nw}"
    jump rude_isadora_enter


label rude_BEEP:
    show a sad
    a "...{w}Okay that was kind of mean.{w} Don't be so derogatory towards code based lifeforms."
    show c disappoint
    c "...{w}black humor, I guess?"
    show a crossed
    a "Or [pronoun[4]] outright insulting us..."
    show c sad
    c "No...I don't think that's it..."
    show a disappoint
    a "Hm."
    a "Or maybe it's a poor attempt at communi{nw}"
    jump rude_isadora_enter

label rude_butt:
    #redraw scene lol
    scene black
    show layer master at dance(10)
    show bg school notree at dance(10):
        xpos -20
    show tree at dance(5):
        xpos -20
    show c disappoint at move(0.4, 0.0)
    show a long at move(0.9, 0.0)
    
    c "...{w}what [is_conj] [pronoun[0]] doing?"
    a "I...{w}have no idea."
    a "...{w}It sure is interesting though."
    c "Yeah..."
    show a line
    a "..."
    c "..."
    c "Does it mean something, do you think?"
    show a long
    a "I...maybe? What could it mean?"
    c "No idea."
    a "...{nw}Do you think they're trying to{nw}"
    jump rude_isadora_enter

label rude_normal_crazy1:
    show c disappoint
    c "Um...okay? So is what you just said an actual pronoun where you come from?"
    show a crossed
    a "No I'm pretty sure they just mashed the keyboard or something."
    c "But I thought they made choices from options on a screen?"
    a "Not all the time."
    show c long
    c "...{w}are they...{w}not human?"
    a "Maybe?"
    c "What would they be if they weren't huma{nw}"
    jump rude_isadora_enter

##---------

label rude_isadora_enter:
    ## a 0.4
    ## c 0.8
    if not dancingnow:
        play music toointensebeat_rude
        $ renpy.music.set_volume(0.7, channel='music')
    show i open oohh at enterright(0.8, 0.4)
    show a long
    show c ooo at move(0.1, 0.3, 30)
    iq "I'M BACK"
    show c ahh
    c "Um, are you okay?"
    
    if crazytalk1 == "butt":
        jump rude_isadora_butt

    show i ahh fists
    iq "{i}*huff huff huff*{/i} What? Yeah! I'm fine!"

    if renpy.get_skipping() and not persistent.has_done_skipping_joke:
        jump skip_joke
    else:
        jump rude_isadora_has_just_entered
        
label skip_joke:
    show i laugh
    iq "I brought Hope and{nw}!"
    show c ooo at move (-0.1, 0.1) zorder 3
    show a ahh at move(0.2, 0.05) zorder 4
    show n line at enterright(1.1, 0.8) zorder 1
    show h long at enterright(0.8, 0.8) zorder 2
    show i ahh at move(0.25, 0.06) zorder 5
    pause 0.05
    $renpy.music.set_pause(True)
    $_skipping = False
    play sound impact
    show i open:
        xalign 0.25
        parallel:
            linear 0.2 rotate 20
        parallel:
            easeout 0.4 yoffset 1000
    show a ehh:
        move(0.12, 0.1, 10)
        move(0.20, 0.1, 0)
    iq "OOF!"
    $_skipping = True
    hide i
    show a ahh standard
    a "Hey, are you okay?"
    show i long:
        xalign 0.5 zoom global_zoom yanchor global_yanchor rotate -10 yoffset 1000
        parallel:
            linear 0.7 yoffset -90
        parallel:
            linear 0.7 rotate 0
    iq "Yeah yeah yeah yeah sorry about that, I was going too fast."
    show a disappoint
    show c open
    c "Slow down! You could have really hurt yourself!"
    c "And you're okay Aspen?"
    show c long
    show a long
    a "Yeah I'm fine."
    show a open
    a "Hey, pay more attention!"
    show a disappoint
    show i wah oohh
    iqw "IT'S NOT MY FAULT{w} WHATS HAPPENING RIGHT NOW IS REALLY IMPORTANT"
    $persistent.has_done_skipping_joke = True
    $renpy.music.set_pause(False)
    show i open
    iq "Anyway, I brought Hope and Nari!"
    jump after_skip_joke

label rude_isadora_has_just_entered:
    show c long at move (-0.1, 0.8) zorder 3
    show a long at move(0.2, 0.8) zorder 4
    show n line at enterright(1.1, 0.8) zorder 1
    show h long at enterright(0.8, 0.8) zorder 2
    show i laugh standard at move(0.5, 0.8) zorder 5
    iq "I brought Hope and Nari!"
    
label after_skip_joke:
    show h ahh
    hq "whoah so thats the player"
    show i smile
    iq "Yeah!"
    show h derp
    hq "oh sweet{w} he's so blurry thats so weird"
    show h owo
    show c disappoint
    c "Izzy, why did you...uh?"
    show i ohh
    izq "The player has to meet everyone! So I brought everyone?"
    a "You do realize that we don't constitute as everyone."
    show i wah
    izqw "EVERYONE IN THE GANG.{w} NOT EVERYONE EVER.{w} I'M NOT DUMB ASPEN."
    show c long
    a "...well, maybe one of you can get through to this person."
    show i ohh
    izq "Huh? What do you mean?"
    c "They've been acting a little...{w}uh..."
    a "Special."
    show c sad
    c "...Sure."
    show i long
    menu:
        izq "Special?"
        "I'M SPECIAL AND I KNOOWWWW IT!":
            $crazytalk2 = "special"
            jump rude_special
        "BEEP BOP BLORP BOOPITY BOOPITY BOOPITY BOOOOOOOOOOOOP":
            $persistent.crazytalk_beep = True
            $crazytalk2 = "beep"
            $racist = True
            jump rude_special
        "PFFFFFFTTTTTTTTTTTTTTTTTTTTTT":
            $crazytalk2 = "fart"
            jump rude_special
        # "Huh? What are you talking about?":
        #     $crazytalk2 = "what"
        #     jump rude_normal_crazy2

######----------

label rude_special:
    show i long
    i "Oh."
    if racist:
        show h sad
        hq "wow{w} racist much"
        c "Now I wouldn't call that racist..."
        hq "no thats definitely derogatory towards code-based life forms thats racist in my book"
        hq "not all \"robots\" go beep boop bop you know"
    else:
        show h sad
        hq "what the heck"
    show i ehh
    izq "Well, uh, regardless, we still need to do d-d-demo stuff!"


label rude_jumpfromdancing:
    show a disappoint
    a "Demo stuff?"
    show i open
    izq "Yeah!"
    a "What does that mean?"
    show i inv
    izq "It means what it means!{w} Demo stuff! Stuff you do in demos!"
    show c long
    c "What do you do in demos?"
    show i wah
    izqw "WHY ARE WE PLAYING SIMON SAYS??!?!{w} UGGGG WE'RE WASTING TIME."
    iw "I'M ISADORA, THE DERPY PURPLE HAIRED ONE IS HOPE, AND THE QUIET GREEN HAIRED PERSON IS NARI."
    show i inv
    show h ahh
    h "uh{w} do you know how simon says works"
    show a sad
    show h long
    a "Yeah, I don't think that's how Simon says works."
    show i wah
    iw "I KNOW HOW SIMON SAYS WORKS"
    show i inv
    show a think smirk
    a "But {i}do{/i} you know how Simon says works?"
    show i ahh fists
    i "...yes? You have a Simon and then Simon calls out something for you to do, and then..."
    show i arg at shake(100)
    iw "WAIT NO WHY ARE WE TALKING ABOUT THIS??!?!"
    iw "SOMEONE THINK OF A QUESTION OR SOMETHING"
    show i morty at stop
    show a crossed smile
    a "Okay first of all calm down, everything's fine."
    show a ahh
    a "Second of all, why are you in such a rush? Are we on a timer or something?"
    show a long
    show i open
    i "Aspen.{w} How do I get this though to you.{w} We are a DEMO!{w} DEMOS ARE SHORT!!!!"
    show c ahh
    show i inv
    c "We don't need to blaze through it though...{w}I'm sure we have enough time to...{nw}"
    show c ooo at hop
    show i arg:
        rotate 0
        linear 0.3 rotate 360
        repeat
    iw "SOMEBODY ASK A QUESTION"
    hide i
    show c disappoint
    show i inv fists:
        stop
        move(0.5, 0.0)
    show a disappoint
    a "Okay fine please don't yell so much.{w} That's not good for your voice you know."
    show h ahh
    h "you must have vocal chords of steel isadora cuz you scream like all the time"
    show a sad
    show h long
    a "Alright I have a question.{w} Let's get this over with."
    if not dancingnow:
        stop music
        $renpy.music.set_volume(1.0, channel='music')
    show a ahh
    a "Hey player, who here to you is the cutest?"
    show c open surprised at hop()
    menu:
        c "Aspen! Oh my god! No!"
        "Chris":
            $cute = "c"
        "Isadora":
            $cute = "i"
        "Aspen":
            $cute = "a"
        "Hope":
            $cute = "h"
        "Nari":
            $cute = "n"
        "All of you are cute as hell! Wow!":
            $cute = "ALL"

    $persistent.cutelist.append(cute)

    if not dancingnow:
        play music happymetastupid
    if cute == "c": #Chris
        show c sad
        c "Oh...{w}uh...{w}thanks?"
        show h sad
        show c open fists
        c "But Aspen! Wow! Why in the world?!?!"
    if cute == "i": #Chris
        show i sicko blush standard
        i "Eep!"
        show c sad fists
        show h sad
        c "Ok first of all, please do not do anything to Izzy she doesn't consent to."
        show c open
        c "Second of all, Aspen! What the heck has gotten into you?"
    if cute == "a": #Chris
        show a longbig sweat
        a "Oh!{w} Wonderful!{w} That's wonderful.{w} Yep.{w} Just great."
        show h sad
        show c open fists
        c "Aspen!{w} Why?!{w} What's gotten into you?"
    if cute == "h": #Chris
        show h sad
        h "..."
        h "sorry im not into you"
        show c open fists
        c "Aspen!{w} Why?!{w} What's gotten into you?"
    if cute == "n": #Chris
        show c long
        a "Oh, interesting."
        show h sad
        h "you stay away from nari"
        show c ehh fists
        c "...uh, A-Aspen!{w} Why?!{w} What's gotten into you?"
    if cute == "ALL": #Chris
        show i sicko
        i "Oh!"
        show c disappoint fists
        c "That's...{w}sweet of you...?"
        show h sad
        h "yeah i can read between the lines here i dont think the player was trying to be sweet"
        show c open
        c "...anyway Aspen!{w} Why?!{w} What's gotten into you?"
    show c ahh fists
    c "Just because..."
    show c sad
    c "..."
    show c ehh
    c "You have no excuse to act so ridiculous!"
    show a ahh -sweat
    show c inv
    a "Oh come on Chris, isn't this the whole point of this game anyway? Why not cut to the chase?"
    show a long
    if cute == "c":
        show a laugh
        a "Beside's, [pronoun[0]] think[s_conj] you're cute!"
        show c longbig blush sweat
        c "N-no...we are NOT a dating sim!"
    else:
        show c open
        c "Haven't we been over this?! We are NOT a dating sim!!"
    show a standard happy
    show i standard long
    a "Oh? And how do you know that?"
    if cute != "c":
        show c long
    c "...{w}it just isn't ok?"
    if cute != "a":
        show a smile
    else:
        show a long
    a "According to who?"
    show c ehh -blush -sweat
    c "...even if we are a dating sim, it's still highly inappropriate to just ask someone something like that as soon as you meet them!"
    show c sad
    show a ahh

    if dancingnow:
        a "The player is...{w}STILL dancing...{w}and you think asking who's cute is abnormal?"
    elif crazytalk1 == "beep" or crazytalk2 == "beep":
        a "The player is outright making fun of us and you think asking who's cute is highly inappropriate?"
    elif crazytalk2 == "fart":
        a "The player is making fart noises and you think asking who's cute is abnormal?"
    elif crazytalk2 == "special":
        a "The player is screaming that they're special and you think asking who's cute is abnormal?"
        

    show a open
    a "We're a dating sim!{w} Get over it!{w} Here, I'll prove it to you."
    menu:
        a "Hey, tell us, are we a dating sim?"
        "Yep!":
            jump rude_datingsim_true
        "Nope!":
            jump rude_datingsim_false
        "...what's a dating sim?":
            jump rude_datingsim_idk


    label rude_datingsim_idk:
        show a long
        show c ehh
        c "See, how can we be a dating sim if they don't even know what one is?"
        show c sad
        show a disappoint
        a "Hold on a moment, they might just not know the terminology."
        show a ahh
        a "A dating sim is a genre of visual novel where you date the characters in the game. And you can usually pick which one you want to date in some way."
        show c sad
        c "Oh my god...{w}I think they could have inferred that..."
        menu:
            a "So let me ask again, is that what we are?"
            "Yep!":
                jump rude_datingsim_true
            "Nope!":
                jump rude_datingsim_false

###-------------

    label rude_datingsim_true:
        show a proclaim
        a "Ha! I told you!"
        show i sicko blush
        i "Oh...{w}oh my..."
        if cute != "h":
            show h long
            h "huh"
        else:
            show h sad
            h "not cool"
        show a standard happy
        a "Didn't I tell you Chris? I was right!"
        show c sad
        c "..."
        show h ahh
        h "wait so do each of us have a route"
        i "Oh god."

        if cute == "c":
            i "Everyone has a route?{w} Even...Chrissy?"
        if cute == "a":
            i "Everyone has a route?{w} Even...Aspen?"
        if cute == "i":
            i "Everyone has a route?{w} Even...me?!?!?!?!"
        if cute == "h":
            i "Everyone has a route?{w} Even...Hope?"
        if cute == "n":
            i "Everyone has a route?{w} Even...Nari?"
        show a ahh
        a "Maybe? But we're a demo so maybe not."

        if cute != "h":
            show h disappoint
            h "i wonder if i have a route"
        else:
            show h sad
            h "i better not"

        if cute == "c":
            show a smirk
            a "Well, you really might be in for a good time, Chris."
        if cute == "i":
            show a smirk
            a "Well, you really might be in for a good time, Isadora."
            i "Oh god..."
        if cute == "a":
            show a smirk
            a "Well...um...this might be my time to get lucky then."
            show h sad
            h "as long as they stay away from me im fine"
        if cute == "h":
            show a long
            a "I don't know...you might be in for a good time, Hope."
            show h sad
            h "i kind of doubt that to be honest"
        if cute == "n":
            show a long
            a "Welll...um...you really might be in for a good time there, Nari."
            show h sad
            h "no [pronoun[5]] not this thing isnt laying a finger on her"

        stop music
        if dancingnow:
            stop multi1
            stop multi2
            stop multi3
            stop multi4
            stop multi5
            stop multi6
            stop multi7
        show c angry
        ca "I cannot believe you Aspen."
        ca "I cannot believe any of you."
        show a long
        show i long -blush
        show c mad
        ca "After all the time we've spent debating this over and over and over and you're just going to throw away the endless arguments we've already had and believe anything the player tells you?"
        ca "If the player told you that aliens are real or that Nari can fly or that our bodies are made of organic matter, would you believe them?"
        show c laugh surprised
        ca "Your trust in the player is so admirable!{w} What an amazing leap of faith you've all taken!"
        show c smirk standard
        ca "If the player told you that we're all going to die horrible painful deaths when the game ends, would you believe them?"
        show i ahh standard
        i "Chrissy are you okay?"
        show i long
        show c happy
        ca "If the player told you to rip off your clothes, or quit school, or pull out your teeth, or kill someone in the gang, or hell, if they told you to kill yourself, I bet you'd do it!"
        show c laugh
        if dancingnow:
            ca "The player always knows best! Why would we ever defy the forever-dancing player? It's not like our script could let us anyway!"
        else:
            ca "The player always knows best! Why would we ever defy the all-knowing player? It's not like our script could let us anyway!"
        show a crossed ahh
        a "Jesus Christ calm down. If I didn't already have such strong suspicions about the game being a dating sim I wouldn't be so sure.{w} But I think we can trust the player on this.{w} So please Chris don't{nw}"
        show c mad fists at shake()
        ca "BUT WE {b}{shader=jitter:u__jitter=1.0, 1.0}CAN'T{/shader}{/b} TRUST THE PLAYER! {w}WE CAN'T TRUST THEM WHEN THEY'RE ACTING LIKE THIS!"
        if dancingnow:
            ca "THEY STILL WONT EVEN STOP DANCING!!!!"
        ca "{i}WE CAN'T DO {b}{shader=jitter:u__jitter=5.0, 3.0}{cps=*0.2}FUCKING ANYTHING{/cps}{/shader}{/b} WHEN THEY TREAT US LIKE THIS!{/i}"
        show c sad at stop
        show a long
        show i long
        show h long
        $hardpause(6)
        i "..."
        a "..."
        h "..."
        c "..."
        $hardpause(3)
        show c defeated
        $hardpause(3)
        show c open
        extend "I was really looking forward to them arriving...{w}but..."
        show c closed
        c "..."
        $hardpause(4)
        show c standard sad
        $hardpause(6)
        show c zorder 10:
            parallel:
                ease 3.0 zoom 1.2
            parallel:
                ease 3.0 yanchor 300
        $hardpause(10)
        show c angry
        c "I hope you..."
        $hardpause(4)
        show c sad
        $hardpause(2)
        show c defeated
        $hardpause(2)
        c "{i}*sniff*{/i}"
        show c:
            easeout 1.0 xalign -2.0
        $hardpause(1)
        show i open
        i "Chrissy!"
        h "wow"
        show a ahh
        show i sad
        a "Isadora you know her best, you should follow her."
        show a sad
        show i long at move(-0.5, 4.0) zorder 10
        menu:
            i "On it."
            "{i}Stop dancing and go with Isadora{/i}" if dancingnow:
                jump rude_followchris_dancingnow
            "{i}Go with Isadora{/i}" if not dancingnow:
                jump rude_followchris_true
            "{i}Stay here{/i}":
                jump rude_followchris_false
        
label rude_followchris_true:
    show i open at move(-0.05, 0.8)
    show a long at move(0.4, 2.0)
    i "Wha-? Hey! What are you doing?"
    menu:
        i "You are NOT coming!"
        "I'm sorry. I want to help.":
            jump rude_followchris_try
        "Well screw you then.":
            jump rude_followchris_screwyou

label rude_followchris_screwyou:
    show i angry
    i "Yeah, whatever.{w} Go to hell."
    jump rude_followchris_false

label rude_followchris_dancingnow:
    show i sad at move(0.0, 0.8) 
    i "Go take your dumb dancing somewhere else, freak."
    jump rude_followchris_false

label rude_followchris_try:
    show i sad
    i "..."
    i "I don't believe you."
    menu:
        "I'll stop acting silly, I promise. Please just let me come along.":
            jump rude_followchris_stop
        "I'm sorry that I was racist before. I didn't know it was that offensive for you" if (crazytalk1 or crazytalk2) == "beep":
            jump rude_followchris_beep
        "I'm sorry if I made Chris uncomfortable by saying she was cute." if cute == "c":
            jump rude_followchris_chriscute
        "I'm sorry if I made you uncomfortable by saying you were cute." if cute == "i":
            jump rude_followchris_izzycute
        "I'm the one Chris is upset with. Please let me talk with her.":
            jump rude_followchris_promise1

    label rude_followchris_stop:
        i "..."
        i "Go to hell."
        jump rude_followchris_false
    
    label rude_followchris_beep:
        i "..."
        i "....."
        i "Yeah right. You knew exactly what you were saying."
        jump rude_followchris_false

    label rude_followchris_chriscute:
        i "..."
        i "....."
        i "Well you're not going to make her MORE uncomfortable. Get lost."
        jump rude_followchris_false

    label rude_followchris_izzycute:
        i "Uh huh."
        jump rude_followchris_false

        
    
    label rude_followchris_promise1:
        i "..."
        $hardpause(4)
        i "You promise you'll stop acting like a lunatic?"
        menu:
            "Yes.":
                jump rude_followchris_promise2
            "No.":
                jump rude_followchris_stop

    label rude_followchris_promise2:  
        $hardpause(4)
        i "You sure?"
        menu:
            "I'm sure.":
                jump rude_followchris_promise3
            "No.":
                jump rude_followchris_stop


    label rude_followchris_promise3:
        i "You promise."
        menu:
            "Yes.":
                jump chris_start
            "No.":
                jump rude_followchris_stop


label rude_followchris_false:
    show i sad at move(-0.4, 1.0)
    $hardpause(3)
    a "..."
    $hardpause(4)
    show note_falling at note_falling zorder 20
    play music endmusic
    show a ohh
    a "Oh?{w} What's this?"
    show a long
    a "..."
    show a open
    a "Whoah!"
    show a long
    a "Um...{w}hey, this is for you."
    if dancingnow:
        $EndMessage[-1] = "P.S. You just never stop, huh?"
    else:
        $EndMessage[-1] = "P.S. Don't worry. Chris will be okay."
    show screen Final_Note(EndMessage, True)
    a "...{w}um...{w}alright then."
    h "so its over"
    i "I think so."
    a "Oh hey there's more on the back"
    hide Final_Note
    $EndingComplete("RudeEnd")
    show screen Final_Note(EndMessageMeet, False)
    a "What?"
    i "..."
    h "ahhhhhhhhhhhhhh"
    hide screen Final_Note
    jump nariend_rude

#------------



label rude_datingsim_false:
    show a long
    a "Oh."
    show c open
    c "What did I tell you? NOT a dating sim!"
    show a open
    show c sad
    a "But hold on a minute."
    a "How can we believe the player?"
    if dancingnow:
        a "I mean come on, they're STILL dancing!"
    show c sad
    c "...{w}can you just drop it please?"
    show a ahh
    a "No seriously I mean lets face it this person is a total nut job.{w} Can we take anything they say with any credit{nw}"
    if dancingnow:
        stop multi1
        stop multi2
        stop multi3
        stop multi4
        stop multi5
        stop multi6
        stop multi7
    stop music
    show c fists mad at hop(0.2, 100)
    ca "I said DROP IT Aspen!"
    show c sad
    show a crossed sad
    a "Wow alright alright lower your voice."
    show a long
    $hardpause(6)
    c "..."
    a "..."
    show i ahh
    i "well now what"
    show i long
    c "..."
    a "..."
    show i ahh
    i "I have an idea."
    a "Yes?"
    i "How about we go get mochi?"
    show h ahh
    h "hey thats my line"
    show h long
    i "I know I'm saying it for you."
    i "We almost always go there anyway so let's just go already."
    i "I guess we can do demo stuff on the way there."
    show i long
    c "..."
    a "......"
    h "........."
    $hardpause(5)
    i "............"
    show i ahh
    extend "uh, guys?"
    show i long
    show c ahh
    c "We're not a dating sim."
    show a ahh
    a "I respectfully disagree."
    c "Why does this need to be an argument?"
    show a sad
    show c sad
    a "Yes, why DOES it need to be an argument?{w} We can just agree to disagree."
    c "I don't want you giving the wrong idea to the player that's what."
    a "Well let's just leave the player to their own conclusions then."
    c "Fine."
    a "Fine."
    c "Have it your way."
    a "I will."
    c "Okay."
    a "We're finished."
    c "Yes."
    a "Indeed."
    c "Uh huh."
    $hardpause(2)
    a "Yup."
    $hardpause(2)
    c "It's over."
    $hardpause(5)
    show i ahh
    i "You guys done."
    show i long
    a "Yeah."
    c "...{w}yes."
    i "So{w} can we{w} go get mochi now?"
    c "Yes lets go get mochi."
    i "Ok."
    $hardpause(6)
    i "Why aren't we going anywhere."
    $hardpause(5)
    show a ahh
    if dancingnow:
        jump rude_orangekid
    else:
        a "I don't want mochi today."
    show a long
    pause 5
    show note_falling at note_falling zorder 20
    play music endmusic
    pause 3
    show a ahh
    a "Wait what the heck"
    show i ahh
    i "Um...interesting timing for a random piece of paper to randomly fall from the sky?"
    show a long
    a "Gimmie."
    a "..."
    show a wah at hop()
    a "AHHH"
    show i ahh
    i "What?"
    a "IT'S FROM THE CREATOR"
    show i ehh
    i "WHAT?!?!"
    show a open
    a "Here [player] read it."
    $EndMessage[-1] = "P.S. Sorry to interrupt such a heated moment, but the Player has to go now!"
    show screen Final_Note(EndMessage, True)
    pause 15
    h "dang even the creator called it a heated moment"
    h "the moment has officially been ordained as heated"
    h "anyway bye player nice to meet you"
    c "That was really short."
    a "Yeah."
    i "Well guess that's it."
    a "Oh hey there's more on the other side."
    hide Final_Note
    $EndingComplete("RudeEnd")
    show screen Final_Note(EndMessageMeet, False)
    pause 5 
    a "What is this talking about?"
    i "Dunno."
    h "wait a sec i think i know who that might be{nw}"
    hide screen Final_Note
    jump nariend_rude

label rude_orangekid:
    a "You think Orange Kid over there is going to ever stop dancing?"
    show a sad
    $hardpause(5)
    h "did you just reference what i think you just referenced"
    a "Yes.{w} Yes I did Hope."
    h "are you out of your mind"
    a "What do you mean by that."
    h "i mean do you actually know what orange kid is"
    a "Of course I do.{w} He's the kid who dances."
    a "And his skin is orange."
    $hardpause(5)
    show i smirk
    i "Pfft."
    a "What?"
    i "You don't know where that comes from."
    a "Um...{w}yes I do."
    i "No you don't."
    h "you picked that up from the middle schoolers didnt you"
    show a morty standard blush sweat
    a "...!!!"
    extend " N-n-no!?"
    show i happy
    i "Pfft hahahahaha you doofus."
    show i smile
    $hardpause(3)
    show c long
    $hardpause(4)
    show note_falling at note_falling zorder 20
    play music endmusic
    $hardpause(2)
    show a ahh -blush -sweat
    a "Wait what the heck"
    show i ahh
    i "Um...interesting timing for a random piece of paper to randomly fall from the sky?"
    show i long
    show a long
    a "Gimmie."
    a "..."
    show a wah at hop()
    a "AHHH"
    show i ahh
    i "What?"
    a "IT'S FROM THE CREATOR"
    show i wah fists
    i "WHAT?!?!"
    show a open
    a "Here [player] read it."
    $EndMessage[-1] = "P.S. You never let up, huh?"
    show screen Final_Note(EndMessage, True)
    pause 15
    a "Ok anyway what is Orange Kid really?"
    h "it doesnt matter"
    h "anyway bye player nice to meet you"
    c "That was really short."
    a "No come on tell me."
    h "no"
    a "Chris tell me."
    i "Don't tell them."
    c "...{w}I'm not telling."
    a "Oh come ON."
    hide Final_Note
    $EndingComplete("RudeEnd")
    show screen Final_Note(EndMessageMeet, False)
    pause 1
    c "Just google it."
    a "Okay FINE."
    h "wait a sec what is this on the back{nw}"
    $orangekid = True
    hide screen Final_Note
    jump nariend_rude