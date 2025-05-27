label rude_isadora_butt:
    show i ahh
    iq "{i}*huff huff huff*{/i} What? Yeah! I'm..."
    show c long
    show i fists
    extend "uh..."
    show i long
    extend "...what is happening right now?"
    a "We're not sure."
    c "We think they're just dancing."
    show i disappoint
    iq "...{w}um..."
    show c long at move (-0.1, 0.8) zorder 3
    show a long at move(0.2, 0.8) zorder 4
    show n line at enterright(1.1, 0.8) zorder 1
    show h long at enterright(0.8, 0.8) zorder 2
    show i ahh standard at move(0.5, 0.8) zorder 5
    iq "Anyway I brought Hope and Nari."
    show h ahh
    hq "whoah so thats the player"
    show h long
    show i smile
    iq "Yeah! They're here!"
    show i long
    hq "...{w}wow"
    c "Izzy, why did you...uh?"
    show i ohh
    izq "The player has to meet everyone! So I brought everyone?"
    show i long
    a "You do realize that we don't constitute as everyone."
    show i wah crossed
    izqw "EVERYONE IN THE GANG.{w} NOT EVERYONE EVER.{w} I'M NOT DUMB ASPEN."
    show i inv
    show c disappoint
    c "This might be kind of overkill Izzy, we shouldn't be introducing all of us to [pronoun[1]] at once."
    show i ahh
    ###DANCE 1
    stop multi0 fadeout 0.2
    $renpy.music.set_volume(1.0, delay=0.2, channel='multi1')
    show h dance closed
    show i open oohh 
    izq "But we don't have much time! We have to do all we can before we run out of...{w}of..."
    show i standard sad
    extend "Hope what on earth are you doing."
    show h dance open
    h "im trying to speak their language"
    h "maybe this is how they communicate or something"
    show h dance closed
    show c sicko
    c "...{w}um..."
    izq "...you really think they're trying to tell us something?"
    show h dance open
    h "i mean look at how intricate theyre being"
    show h dance closed
    show c disappoint
    c "I'm pretty sure this just dancing."
    show a line crossed
    a "..."
    menu:
        c "I really don't think there's any deeper meaning behind this."
        "YES! WE SHALL DANCE THE NIGHT AWAY INTO OBLIVION YOUNG GRASSHOPPER":
            $crazytalk2 = "grasshopper"
            jump rude_dance_grasshopper
        "BEEP BOP BLORP BOOPITY BOOPITY BOOPITY BOOOOOOOOOOOOP":
            $crazytalk2 = "beep"
            jump rude_dance_racist
        "{i}dance with more vigor{/i}":
            $crazytalk2 = "butt"
            ###DANCE 2
            stop multi1 fadeout 1.0
            $renpy.music.set_volume(1.0, delay=0.5, channel='multi2')
            jump rude_dance_vigor


label rude_dance_grasshopper:
    show h long at stop
    h "wait a minute what{w} i thought they didnt talk"
    c "No they definitely talk."
    h "oh{w} i thought this was some sort of weird communication thing{w} so they really are just dancing then"
    show a long
    c "Yeah."
    show h disappoint
    h "well i feel dumb now"
    jump rude_dance_caught


label rude_dance_racist:
    show h long at stop
    h "whoah what{w} I thought they didnt talk"
    c "No they definitely talk."
    show h sad
    h "so they can talk and theyre racist"
    show c sicko
    show a long
    c "Uh...that's not really how I'd put it, but..."
    h "come on{w} beep boop{w} thats racist if you ask me"
    show h disappoint
    h "...anyway i feel super dumb now"
    jump rude_dance_caught

label rude_dance_caught:
    menu:
        c "Hey...uh, you can stop dancing now if you want, we kinda get the point."
        "{i}Keep dancing.{/i}":
            $dancingnow = True
            jump rude_caught_dancing_true
        "{i}Stop Dancing.{/i}":
            $dancingnow = False
            jump rude_caught_dancing_false

    label rude_caught_dancing_true:
        c "...{w}alright, suit yourself."
        jump rude_dance_transition

    label rude_caught_dancing_false:
        
        #redraw scene
        scene bg school
        show c sad at move (-0.1, 0.0) zorder 3
        show a long at move(0.2, 0.0) zorder 4
        show n line at enterright(1.1, 0.0) zorder 1
        show h long at enterright(0.8, 0.0) zorder 2
        show i sad at move(0.5, 0.0) zorder 5
        stop multi1
        stop multi2
        stop multi3
        stop multi4
        stop multi5
        stop multi6
        stop multi7
        stop music
        $dancingnow = False
        c "...{w}Thank you."
        jump rude_dance_transition


label rude_dance_transition:
    h "what did they say their name was"
    a "They wouldn't tell us."
    h "um{w} ok"
    show i long
    izq "They didn't tell you what their name was?"
    show a sad
    a "No, they wouldn't tell us, I just said that."
    show i ahh
    izq "Why? Do we have to tell them our names first? Is that how it works?"
    show a long
    a "Uh...I don't think so."
    show i long
    i "My name is Isadora, the one who was just dancing is Hope, and the quiet one is Nari."
    if not dancingnow:
        play music toointensebeat_rude fadein 5.0
    show i oohh ahh
    i "Ok whatever we need to get back on track. We need to be doing demo stuff!"
    jump rude_jumpfromdancing


label rude_dance_vigor:
    show h dance open
    h "oh {w}i think i might be getting something across"
    a "...really?"
    h "yeah something is different"
    show h dance closed
    a "...Hm."
    show i sicko
    izq "Eheheheh...this is really not how I expected our meeting with the player to go..."
    c "We're all surprised, Izzy."
    izq "Oh by the way...{w}uh hey player...{w}the dancing one is named Hope and the quiet one is Nari and I'm Isadora, and..."
    show i disappoint
    i "...can the player understand what we're saying?"
    show c sad
    c "Yes.{w} Yes they can."
    i "You sure?"
    ###DANCE 3
    stop multi2 fadeout 0.2
    $renpy.music.set_volume(1.0, delay=0.2, channel='multi3')
    show a dance
    c "I'm very sure.{w} Before they were{nw}"
    show c open surprised at hop()
    c "Wha-?{w} Aspen? What are you-?!?!"
    show a dance open
    a "Hope might be onto something."
    show a dance closed
    show c mad fists
    c "Oh for the love of-{w} guys the player is just screwing with you! Don't take them so seriously!"
    show a dance open
    a "I thought so too at first but I have a feeling this might be worth a shot."
    a "Nothing the player has done or said has been intelligible, there may be some other method of communication that's more efficient for them."
    show a dance closed
    show c ehh
    c "More efficient???? Aspen listen to yourself, what you're doing doesn't make any sense."
    show a dance open
    show c inv
    a "Well neither does the player, so until they start making sense in a way that doesn't involve...whatever we're doing right now...I think this may be our best course of action."
    show a dance closed
    i "...are you guys getting through to them, do you think?"
    menu:
        h "hard to say we dont know their language yet"
        "{i}dance with even more vigor{/i}":
            ###DANCE 4
            stop multi3 fadeout 0.2
            $renpy.music.set_volume(1.0, delay=0.2, channel='multi4')
            jump rude_more_dancing
        "YES LET'S DANCE!!!!!":
            jump rude_dance_yeslets

label rude_dance_yeslets:
    show h long at stop
    h "huh"
    show a long at stop
    a "What?"
    h "i thought the player didnt talk"
    a "No they talk."
    h "oh"
    h "i thought this was like some kind of third encounters kind of thing"
    a "What?"
    h "..."
    show h disappoint:
        ease 0.5 xoffset 0.0
    extend "u know what screw this nvm"
    a "Uh..."
    show a long:
        ease 0.5 xoffset 0.0
    extend "ok."
    i "We're stopping now?"
    a "I guess so."
    i "Oh.{w} Ok."
    jump rude_dance_caught

    
label rude_more_dancing:
    a "oh{w} whoah"
    show h dance open
    h "ok i like where this is going"
    i "..."
     ###DANCE 5
    stop multi4 fadeout 0.2
    $renpy.music.set_volume(1.0, delay=0.2, channel='multi5')
    show i dance open
    i "screw it I don't know what you guys are doing but it looks fun"
    show a dance open
    a "Whoah cool! How are you doing that???"
    show c surprised ehh at hop
    c "WHAT THE FREAK GUYS"
    show c fists morty
    show h dance closed
    h "so chris{w} u ready to join us now"
    h "we will show you how{w} come on try{w} the player will be your guide" #how has no one gotten this joke yet like seriously
    show a dance open
    a "Hahahaha you know I think its working."
    show a dance closed
    show h dance open
    h "hey nari u should join us too"
    n "No."
    show h owo
    h "come on u know you want to"
    n "No."
    show h sad
    h "hmmmmmm"
    show h smirk
    h "hey nari"
    n "What."
    h "guess what i have with me"
    n "What."
    h "guess"
    n "No."
    show h morty
    h "come on guess"
    n "No."
    show h smile
    h "you know you already know what it is"
    n "I don't."
    h "oh yes you do"
    show h owo
    h "whats the one thing i have that i know will make you dance"
    n "..."
    pause 3
    n "How many."
    show h smirk
    h "the whole bag"
    h "ive been saving it for a special occasion"
    n "..."
    n "The whole bag."
    show h owo
    h "the whole bag"
    h "unopened{w} untouched{w} and all yours"
    h "a whole entire bag of gummy bears"
    h "and all you have to do"
    show h smile
    h "is dance"
    n "..."
    $renpy.pause(3, hard=True)
    ###DANCE 6
    stop multi5 fadeout 0.2
    $renpy.music.set_volume(1.0, delay=0.2, channel='multi6')
    show n dance
    pause 3
    show h dance open
    h "yeeeeeeesssssssss"
    show a dance open
    a "Come on Chris you're the only one left."
    show i dance open
    i "Yeah join us!"
    show i dance closed
    h "u gotta admit this is fun"
    a "This is the best possible scenario I think we could have hoped for."
    show i dance open
    i "Don't just stand there Chris!{w} Dance!"
    show h dance closed
    h "yeah were exchanging tons of information here"
    show a dance closed
    a "Super beneficial"
    show i dance open
    i "Agreed!"
    menu:
        i "Join in on the fun!"
        "{i}Let it all out.{/i}":
            jump rude_dance7
        
label rude_dance7:
    stop multi6 fadeout 0.2
    $renpy.music.set_volume(1.0, delay=0.2, channel='multi7')
    pause 3
    show h dance open
    h "WHOAH"
    show i dance open
    i "OH BOY"
    show a dance open
    a "Okay we're taking this to the stratosphere."
    h "and waaaayyy out of here"
    i "I think we're on another planet now."
    h "no i think weve gone further than that"
    a "at least the next star system"
    h "nah i dont think were in this universe anymore"
    a "Wherever we are it is GROOVY as a SMOOTHIE!"
    show h dance closed
    h "that was a really lame thing to say but i dont even care anymore"
    i "Can we take this any further?"
    show h dance open
    h "nari u gotta say ur enjoying this"
    n "...{w}bears."
    show h dance closed
    h "yup{w} every last one"
    i "Who would have thought the player's arrival would be this much fun?"
    a "It's so easy!"
    show h dance open
    h "Easy brea{nw}"
    show c ehh surprised at hop() 
    hide i
    hide a
    hide h
    hide n 
    show a ohh at move(0.2, 0) zorder 4
    show n ahh at move(1.1, 0) zorder 1
    show h ohh at move(0.8, 0) zorder 2
    show i ohh at move(0.5, 0) zorder 5
    show layer master at vpunch
    show bg school notree at stop
    show tree at stop
    stop multi7
    ca "EVERYBODY STOP!!!"
    show c sad fists
    show a long
    show i long
    show h long
    show n line
    $renpy.pause(4, hard=True)
    c "I can't believe you."
    c "I can't believe any of you guys."
    c "This is a disgrace."
    c "The player finally arrives, and this is the best you can do?"
    $renpy.pause(4, hard=True)
    c "Now."
    c "Let's start again."
    c "And do this properly."
    $renpy.pause(7, hard=True)
    show c smile
    $renpy.pause(0.5, hard=True)

default dance_timer = 0.0

init python:

    def stopwatch(starttime):
        return float(renpy.get_game_runtime() - starttime)

    def dance_syncer(measure):
        if renpy.music.is_playing():
            timecode = stopwatch(dance_time_start)
            timecode_goal = (measure * 4.0 * dancebeat)
            if timecode < timecode_goal:
                renpy.pause(timecode_goal-timecode, hard=True)
        return



label dancestart:
    $dance_time_start = renpy.get_game_runtime()
    $_skipping = False
    scene black
    stop music
    $renpy.free_memory()
    $_skipping = False
    $quick_menu = False
    queue music dancingmusicfinal noloop
    queue music dancingmusicfinalloop
    $ _game_menu_screen = None #keep that music in-Sync babyyyyyyyy
    c "{cps=0.0}ONE!{w=0.42} TWO!{w=0.42} THREE!{w=0.42} FOUR!{w=0.42}{nw}"
    $dance_syncer(1)

##DANCE TIME!!!--------------------------------- :D

define bgspeed_dance = -1000
define dancetimingoffset = 0.3
define dancetimingoffset_tiny = 0.05
define dancetimingoffset_syncer = 0.05

label dancetime:

    scene dancebg1:
        linear (dancebeat * 4) xpos bgspeed_dance
    show c dance open at move(0.5, 0)    
    #$hardpause(dancebeat_faster * 4 - dancetimingoffset_tiny)
    $dance_syncer(2 - dancetimingoffset_syncer)

    scene dancebg2:
        linear (dancebeat * 4) xpos bgspeed_dance
    show a dance open maracas at move(0.5, 0):
        zoom 1.2
        yanchor 0
    #$hardpause(dancebeat * 4)
    $dance_syncer(3 - dancetimingoffset_syncer)

    scene dancebg3:
        linear (dancebeat * 4) xpos bgspeed_dance
    show n dance at move (1.3, 0):
        zoom 2.5
        yanchor 500
    #$hardpause(dancebeat * 4)
    $dance_syncer(4 - dancetimingoffset_syncer)

    scene dancebg4:
        linear (dancebeat * 4) xpos bgspeed_dance
    show i dance open at move(0.5, 0.0)
    #$hardpause(dancebeat * 4)
    $dance_syncer(5 - dancetimingoffset_syncer)

    scene dancebg5:
        linear (dancebeat* 4) xpos bgspeed_dance
    show a maracas dance open at move(0.9, 0):
        zoom 1.0
    show h dance open at move(-0.2, 0):
        zoom 2.5
        yanchor 800
    #$hardpause(dancebeat_faster * 4)
    $dance_syncer(6 - dancetimingoffset_syncer)

    scene dancebg6:
        linear (dancebeat * 4) xpos bgspeed_dance
    show i dance open at move(0.2, 0):
        zoom 0.8
        yanchor -100
    show c dance open at move(1.0, 0):
        zoom 2 
        yanchor 300
    #$hardpause(dancebeat_faster * 4)
    $dance_syncer(7 - dancetimingoffset_syncer)


    scene dancebg1:
        linear (dancebeat * 4) xpos bgspeed_dance
    show h open dance at move (0.9, 0)
    show n dance at move(0.0, 0):
        zoom 2
        yanchor 500
    #$hardpause(dancebeat_faster * 4)
    $dance_syncer(8 - dancetimingoffset_syncer)


    scene dancebg2:
        linear (dancebeat * 4) xpos bgspeed_dance
    show a open dance maracas at move(0.5, 0):
        zoom 2.5
        yanchor 1000
    #$hardpause(dancebeat_faster * 4)
    $dance_syncer(9 - dancetimingoffset_syncer)

    ##Sticker dance time!

label sticker:
    
    scene stickerbg at moveAround

    show c sticker at move(0.2, 0)
    show a sticker at move(0.8, 0)

    #$hardpause(dancebeat_faster * 7.6)
    $dance_syncer(10.8 - dancetimingoffset_syncer)

    show c sticker at move(-2.0, dancebeat_faster)
    show a sticker at move(-2.0, dancebeat_faster)

    show i sticker at move(4.0, 0.0)
    show h sticker at move(4.0, 0.0)

    show i sticker at move(0.2, dancebeat-dancetimingoffset)
    show h sticker at move(0.8, dancebeat-dancetimingoffset)

    #$hardpause(dancebeat_faster * 6.5)
    $dance_syncer(12.35 - dancetimingoffset_syncer)

    show i sticker at move(-2.0, dancebeat-dancetimingoffset)
    show h sticker at move(-2.0, dancebeat-dancetimingoffset)


    show n sticker at move(2.0, 0.0)
    show n sticker at move(0.5, 0.1)
    #$hardpause(dancebeat_faster * 2)
    $dance_syncer(13 - dancetimingoffset_syncer)

    hide n

    show c sticker at move(0.25, 0)
    show a sticker at move(0.75, 0)
    show i sticker at move(1.25, 0)
    show h sticker at move(1.75, 0)
    show n sticker at move(2.25, 0)

    show c sticker at move(0.25-1.25, dancebeat*16)
    show a sticker at move(0.75-1.25, dancebeat*16)
    show i sticker at move(1.25-1.25, dancebeat*16)
    show h sticker at move(1.75-1.25, dancebeat*16)
    show n sticker at move(2.25-1.25, dancebeat*16)

    #$hardpause(dancebeat * 16)
    $dance_syncer(16.8 - dancetimingoffset_syncer)

    show c dance open at move(-0.1, 0.3)
    show a dance open maracas at move(0.2, 0.3)
    show i dance open at move(0.5, 0.3)
    show h dance open at move(0.8, 0.3)
    show n dance at move(1.1, 0.3)


label post_dance:
    $ _game_menu_screen = "save"
    $_skipping = True
    show note_falling at note_falling zorder 20
    $renpy.pause(4, hard=True)
    $quick_menu = True
    i "Did something just...?"
    h "dont care"
    show a smile
    a "Don't worry I'll find out what this is."
    c "Probably not important."
    a "..."
    show a open
    a "OH!"
    show a happy
    a "Hey player, here this is for you."
    show a dance open
    
    $EndMessage[-1] = "P.S.: Never stop dancing!"

    show screen Final_Note(EndMessage)
    pause 15

    h "what does it say"
    a "I didn't really read it."
    a "Something something thanks for playing."
    i "Wait was it from the Creator?"
    a "Uh huh."
    i "Cool!"
    c "That's awesome!"
    h "hey if theres anything else important on there let us know ok player"

    hide screen Final_Note
    $EndingComplete("Dancing")
    show screen Final_Note(EndMessageMeet, False)
    pause 3

    c "WOO HOO!"
    i "This is SO MUCH FUN!"
    a "How long can we keep this up for?"
    c "Hopefully a long time!"

    hide screen Final_Note
    jump nariend_dancing








