label mochi_start:
    scene bg mochi
    show black zorder 50:
        on show:
            alpha 1.0
            easeout 3.0 alpha 0.0

    play music moochishop fadein 10.0
    $hardpause(7)

    a "...I mean it's practicaly tradition now for them to mix up our names here."
    show i open mochi at enterleft(0.2, 1.0)
    i "OMG GUYS OVER HERE"
    show h derp mochi at enterleft (0.0, 1.0)
    h "oh heeeeeeeey nice"

    show c mochi at enterleft (0.5, 1.0)
    show i open mochi at move(1.05, 1.2)
    show h smile mochi at move(0.2, 1.0)
    show a ohh mochi at enterleft(0.8, 1.0)
    show n line mochi at enterleft(-0.15, 5.0)
    c "Mmmm!!!"
    show i wah 
    iw "WHY DID YOU DISAPEAR? YOU WERE GONE FOR LIKE 25 MINUTES."
    show a ahh
    a "Yeah, we thought you had left for good."
    show i fists
    menu: 
        iw "REALLY THOUGH ANSWER ME WHY DID YOU GO AWAY?"
        "No clue. It's only been a few secounds for me.":
            jump mochi_fewsec
        "Are we at Starbucks?":
            jump mochi_starbucks

##------

label mochi_fewsec:
    show i ehh standard
    i "Whaaaaaaaaaa?!!?!"
    show a disappoint 
    a "That's...odd."
    a "So from your prespective, you were just back at the school a few seconds ago?"
    show a smirk
    a "Heh, so you can time travel and teleport. Neat."
    show h ahh
    h "thats not old news{w} anyone playing a visual novel can time travel if you load from a save file"
    show a ahh
    a "I mean yeah, duh, but that doesn't look like time travel from our perspestive.{w} They just jump onto a different timeline."
    if timetraveler:
        show a smirk
        a "And Hope used that trick beautifuly today apparently."
        show h owo
        h "uh huh"
    show i ooo
    i "I wonder if we can time travel too...?"
    show a disappoint
    a "Unlikely."
    show i laugh
    i "Hey you never know!{w} Now that the player is here maybe we have like cool powers or somthing!"
    show a long crossed
    a "Again, unlikely."
    show h derp
    h "hey player make me be able to fly"
    jump mochi_chris_talk


label mochi_starbucks:
    show a ohh
    a "Oh, you mean the sign? That has been a much debaeted mystery between us."
    a "The most agreed upon theory is that the owner wanted to name the shop \"Starbucks\" but changed his mind right before he opened to \"Mochi store\"."
    show a disappoint
    a "He won't tell us anything about it so we can only guess."
    show h long
    h "but thats a dumb theory because starbucks is a dumb name"
    h "why would you name a store after what sounds like a fake sci-fi currensy"
    show i ooo standard
    i "I mean Bill is probably really bad at naming things..."
    if player.lower() == "bill":
        show i ohh at hop()
        i "Oh, not you! The shopkeeper's name is Bill too."
    show h disappoint
    h "but it still doesnt explain why he never replaced the logo of the green lady with somthing else"
    show a ahh
    a "Are we really rehashing this old argrument again?"
    jump mochi_chris_talk

##------

label mochi_chris_talk:
    c "Mmmm mmmm Mhmmmm MGmgmgmgmmmm mmmm!"
    show a disappoint
    a "...{w}what?"
    c "..."
    show i disappoint
    i "Uh Chrissy? You ok?"
    c "Mmmmm?!!??!!"
    show a ehh
    a "Why is Chris's mouth gone?"
    show h line
    h "more importantly why is her mochi stuck in her hair"
    show i ehh fists
    i "wait WHAT IS GOING ON WITH OUR MOCHI"
    show a think
    a "It seems to be stuck to our uh...?"
    show h disappoint
    h "tits"
    show a standard
    a "...uh, yeah. What the heck?"
    show h longbig
    h "chris can u braethe rn without a mouth u are really freaking me out"
    c "Mmm MMMM!"
    i "WAIT A MINUTE"
    show i wah oohh
    iw "HOPE THIS IS YOUR FAULT"
    show h long
    h "what"
    iw "WHY THE HECK DID WE COME HERE"
    iw "THE MOCHI STORE WASN'T SUPOSED TO BE IN THE DEMO YOU IDIOT, THAT'S WHY WE CANT DO ANYTING!!!!!"
    show i smirk
    iw "WE WERE SUPPOSSED TO BE DOING DEMO STUFF BUT INSTEAD WE GOT DISTRACTEDDD!!!!"
    show h laugh
    h "are you kiding me{w} we come here all the time this isnt my fault"
    if timetraveler or mochi_from_immortality:
        show i sad
        iw "IT'S TOTALALY YOUR FAULT, WE WOULDN'T HAVE CUM HERE IF YOU DIDN'T INSIST ON IT AFTER YOUR WHOLE TIME TRAVEL SHTICK!"
        h "hey thats totaly not fair"
        h "why would you resist the urge to do cool time shenanigans"
        show i open
        i "Wha-? I'm not talking about that! I'm talking about comeing here you moron!"
        show h long
        h "oh"
        h "well in that case why would you resist the urge to do cool eating mochi shenanigons"
    else:
        show i morty
        iw "IT'S TOTALY YOUR FAULT, WE WOULDN'T HAVE COME HERE IF YOU DIDNT INSIST ON IT!"
        if mochi_players_idea:
            show h poggers
            show hopemouth at move(0.2, 0.0):
                yoffset -20
            h "hey for your information it wasnt all my desision"
            h "what-[pronoun[2]]-name agreed to come here to thats why we came remember"
            show i disappoint fists
            i "...so I guess it's [pronoun[2]] fault too??!!!"
            c "Mmmm mmmmMm MMMm mm Mmm!!!"
        else:
            show h line
            h "hey for your infomation we were destined by fate to come here"
            show i open
            i "No, you just ran off to the Mochi store and we were forced to folow you!"
            show h poggers
            show hopemouth at move(0.2, 0.0):
                yoffset -20
            h "i cannot controll the whims of fate young one"
            show i arg
            iw "I'M JUST AS OLD AS YOU YOU MORON!"
            c "Mmmm MmmMmmmm!!!"
    show a open
    a "Wait I have an idea."
    a "[player] close your eyes for a sec."
    show a long
    show i open
    menu: 
        i "Close your what?"
        "Uh...ok.":
            jump mochi_close_eyes
        "No":
            jump mochi_close_eyes_no
    
    label mochi_close_eyes_no:
        show i long
        show a disappoint
        a "No?{w} What?"
        show i standard
        i "Aspen what did you just say?"
        a "Close your eyes."
        show i ehh
        i "Close your whats?"
        show a sad
        menu:
            a "Come on just do it. I'm not gonna do anything wierd."
            "Allright fine":
                jump mochi_close_eyes_yes2
            "No":
                $tone = -1
                $chris_mochi_mouth = True
                jump mochi_close_eyes_nono


    label mochi_close_eyes_yes2:
        show a longbig
        a "Weirdo.{w} Ok do it."
        jump mochi_close_eyes
    

    label mochi_close_eyes_nono:
        show a disappoint crossed
        show i morty
        a "...uh...is there a reason you won't do it?"
        hide hopemouth
        show h disappoint
        h "what the heck are \"i\"s"
        show a long
        a "Never mind, it was a dumb idea."
        show a ahh
        a "Well, I guess mochi is out if we can't eat it anymore."
        show a long
        c "...{w}Mmm."
        show h sad
        h "darn"
        show i sad standard
        i "I hope youre happy Hope."
        h "again not my fault"
        show i ahh
        i "So now that's over with, what should we be actualy doing?"
        show a disappoint
        a "...want to play that icebreaker game?"
        show i sad
        i "Let's not please."
        c "Mmm"
        show i crossed inv
        i "Ugggggg this has been such a waste of time."
        jump mochi_note_fall


define eyesclose = ImageDissolve("other/tr_eyes.png", 1.0, reverse=True)
define eyesopen = ImageDissolve("other/tr_eyes.png", 1.0)



label mochi_close_eyes:
    ## Fade to black on the eyes closed image you need to find
    show black zorder 100 with eyesclose:
        alpha 1.0
    $renpy.pause(3.0, True)
    iw"OMG WHAT"
    c "Pfffaaa!! {i}gasp!!!{/i}"
    a "Hey! That worked!"
    h "{i}NOM{/i}"
    c "Is everyone ok?"
    i "Oh my god are YOU ok?!?!?!?"
    a "Quick everyone take a bite!"
    i "Ewww it's all soggy and gross now!"
    ## Open eyes again
    
    show c smile 
    show i sad mochieaten standard
    show h nom -mochi
    hide hopemouth
    show a morty mochieaten
    show n -mochi
    hide black with eyesopen
    show a open
    a "Quick! Eat as much as you can before..."
    show a long
    a "...{w}Oh."
    show c smile
    c "Hello again!"
    show i omg
    iw "WHAT THE FZXKKLQALXKVQEFKDFXJTLOQEIBPP"
    a "So it looks like we can only move our arms when [player] isn't looking at us."
    show a disappoint
    a "I'm not sure if our mochi is worth it if we have to eat it like that..."
    show i at shake
    i "I DON'T UNDERSTAND ANYTHING"
    show i at stop
    show c ohh
    c "Hope did you...?"
    h "mmmmm"
    show c smlie
    show i sad
    i "Ok whatever, I don't want this anymore."
    show a ehh at hop
    a "Ahh!! Why is Chris's mouth gone again?"
    show c ahh
    c "What?"
    show i ahh
    i "Yeah, Crissy your mouth was totally missing again for a secound."
    show c ooo
    c "Really?"
    show c laughh
    c "Cool!"
    show i omg
    i "AAAHHHH!!!"
    show a sicko
    a "Uggg...I feel sick..."
    show c sad
    c "Oh no..."
    show i longbig
    i "..."
    show a morty
    a "..."
    h "..."
    show i crossed ahh
    i "...ok this is all super weird and all but can ew PLEASE get back on track!?!?"
    jump mochi_note_fall
        
        
        

label mochi_note_fall:
    show note_falling at note_falling zorder 20
    play music endmusic
    show i open
    i "We've had our little mochi adventure, not we really should get back to doing dem{nw}"
    show a open
    a "Hold on, what is that?"
    if chris_mochi_mouth:
        c "Mmmmm?"
    else:
        show c ohh
        c "Is that a piece of paper?"
    show a ohh
    a "We can pick that up, right?"
    if chris_mochi_mouth:
        show h ahh
        h "did that just fall from the sky"
        c "Mm." 
    else:  
        show c long  
        c "Did that just fall from...?"
        h "mm"
    show i ahh
    i "I got it."
    show a ahh
    a "You picked ti up?"
    show i disappoint
    i "Uh, yeah? Is that..."
    show i longbig
    extend "oh.{w} Right, that's weird."
    show a open
    if chris_mochi_mouth:
        a "How does that make sense??!?!?!!"
    else:
        a "How the heck do our bodies work whgen the player is around?"
    show a long
    a "Anyway, what is that, anyway?"
    show i open
    i "OMG"
    show i omg
    iw "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH{nw}"
    iw "IT'S FROM THE CREATOR"
    show a wah standard
    a "WHAT"
    show i open fists
    i "[player] here I think this is for you!"
    show a ehh
    a "What does it say???"
    $EndMessage[-1] = "P.S. Sorry this place looks so terrible, that's on me!"

    show screen Final_Note(EndMessage, True)
    pause 15

    if chris_mochi_mouth:
        jump mochi_chris_swallows
    else:  
        jump mochi_note_response

label mochi_chris_swallows:
    c "{i}nom nom nom nom nom{/i}"
    c "{i}gulp!{/i}"
    c "Whew!{w} That took a while but I did it!{w} I ate it hands free!"
    i "Oh."
    a "Uh..."
    c "...What?"
    i "But it was in your hair."
    c "Yeah? So?"
    a "..."
    i "....."
    h ".......{w}chris what the fuck"
    c "What?"
    h "thats not how{w} oh never mind"
    c "...um...{w}anyway, this note oh my god!"

label mochi_note_response:
    a "So there ARE multiple possibilities..."
    i "Did we run out ofd time already?"
    c "Why is the Creator apologizing? This is like our favorite hangout place."
    a "...what happens now?"
    i "WAIT THERE'S MORE ON THE OTHER SIDE"
    hide screen Final_Note
    $EndingComplete("Mochi")
    show screen Final_Note(EndMessageMeet, False)

    pause 2

    i "Huh? Who is this talking about?"
    a "There's a fraction thing here gtoo..."
    c "So does this really means that it's all over{nw}"
    stop music
    hide screen Final_Note
    jump nariend_fakeout



    








        


    

    