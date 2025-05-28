label polite_argue_fake:
    show i wah
    iw "WE'RE RUNNING OUT OF TIME"
    show a long
    show i inv:
        xalign 0.5
    show c ahh
    c "Izzy, what do you mean by demo stuff?"
    show i ahh
    i "We uh...have to show [player] the game!"
    show h long
    show c ahh
    c "What do you mean?"
    show i fists
    i "THE GAME"
    show c long
    c "The demo?"
    show i laugh
    i "YES"
    show i open
    extend " I mean wait {w=0.1}{nw}"
    i "NO THE FINAL GAME"
    show c ahh
    c "But we don't know anything about the final game."
    show i wah
    iw "UGGGGG NO YOU'RE MISSING THE POINT CHRISSY"
    show i inv
    i "We don't know everything, but we know SOME things!"
    jump aspen_pissed


label aspen_pissed:
    stop music
    show a mad
    ap "Well thanks to you we know NOTHING."
    show i ahh
    show c ooo surprised
    i "W-What?"
    ap "You keep insisting that we do demo stuff, whatever the hell that means, and it seems [player] probably agrees with you to some extent because [pronoun[0]] won't do the sensible thing and tell us more about our universe!"
    show c ahh
    show i disappoint
    c "Whoah Aspen are you ok?"
    show a inv
    ap "I'M FINE."
    c "You should go get a drink of water."
    show a wah
    ap "I DON'T NEED WATER THANK YOU FOR YOUR CONSIDERATION."
    show a ehh standard
    ap "ISADORA THIS IS ALL YOUR FALUT!"
    show i ehh standard
    i "What!??"
    show a mad
    ap "YOU'RE PROHIBITING THE PROGRESS OF MANKIND BY BEING A WHINY LITTLE {i}BITCH!{/i}"
    show a angry
    show i open fists
    i "I-{w} WHAT DID YOU JUST CALL ME?!?!?!"
    show h ahh
    h "wow aspen is going ham"
    show a mad
    ap "Yeah! You heard me right! A whiny little BITCH."
    show c sicko
    c "Okaaaaayyyy we need to calm down..."
    show h long
    if cute == "c":
        show a ehh
        ap "Hey shut up whore! Let me talk!"
        show c open
        c "Whoah! Aspen!"
    show a ehh
    ap "Isadora, you're going to be the reason that the secrets of our future world become lost to us forever!"
    ap "We're never going to know our true potential in this shitty little game and it's all YOUR FAULT!"
    if cute == "a":
        show i open
        i "What the hell is wrong with you? Has [player] calling you cute gone to your head?"
        show a wah
        ap "Wha-{w} OH NO YOU JUST DIDN'T."
        ap "THE PLAYER'S PREFERENCES IN ROMANTIC PARTNERSHIPS HAVE NOTHING TO DO WITH THIS!"
        show i open standard
        i "Well I don't know WHAT is it but something is SERIOUSLY wrong with you!"
    elif cute == "i":
        ap "I bet [pronoun[4]] just trying to please you cause [pronoun[0]] think[s_conj] you're cute!"
        show i open standard
        i "OH MY GOD ASPEN WHAT IS WRONG WITH YOU"
    else:
        show i open standard
        i "I have NO idea what you're talking about."
        i "What is WRONG with you?"
    show a mad
    ap "There's SO MUCH we could learn from [player] but oh noooooooooo we need to be doing the sensible thing and do ABSOLUTELY NOTHING."
    show i ehh
    i "WE'RE DOING ABSOLUTELY NOTHING RIGHT NOW!"
    show a think laugh
    ap "RIGHT! YOU PROVE MY POINT EXACTLY!"
    show a wah
    ap "SO HOW ABOUT WE USE OUR STUPID LITTLE COMPUTER BRAINS FOR ONCE AND TRY TO LEARN SOMETHING FROM THIS LITERAL GOD BEFORE US?"
    show i open
    i "NOBODY IS GOD! STOP SAYING THE PLAYER IS GOD!"
    i "THE ONLY PERSON YOU SHOULD BE CALLING GOD IS THE CREATOR!"
    show a inv crossed
    ap "Well God or no the Creator hasn't told us SHIT.{w} If we're going to learn anything about our sorry excuse as human beings then it might as well be from the player!"
    i "THAT'S NOT WHAT DEMOS ARE FOR."
    show a mad standard at shake()
    ap "I DON'T CARE WHAT YOU THINK A DEMO IS!!!"
    hide a 
    show a open at move(0.2, 0)
    show c mad fists at shake()
    ca "{shader=jitter:u__jitter=5.0, 5.0}EVERYBODY STOP!!!!!!!!!{/shader}"
    show c sad at stop
    show i long
    show a long
    $hardpause(6)
    a "..."
    i "..."
    show c ahh
    c "If there's anything this demo shouldn't be, it's us arguing like this."
    c "The player entering our world shouldn't be the reason we lose our friendship.{w} I would hate for the gang to split up because of us arguing over something so trivial."
    show a open
    ap "None of this is trivial!!!"
    show a sad
    show c long
    c "...{w}you know what, yes, you're right.{w} It isn't."
    show c ahh
    c "I agree that learning more about the world would be wonderful, especially since there's so much about ourselves that we don't understand."
    c "But even if we grilled [player] for hours, I don't think it would bring us any closer to any answers."
    c "[player] doesn't know the secret to the universe or anything like that. If [pronoun[0]] did, I doubt [pronoun[0]] would even tell us anyway."
    show a open
    ap "You don't know that!"
    show a sad
    show c open
    c "I don't, but who would have told [pronoun[1]]!? The Creator?!"
    show a open
    ap "Maybe!"
    show a sad
    show c long
    c "No.{w} I don't think so."
    show i krying
    i "{i}*sniff*{/i}"
    show c standard sad
    c "Oh no Izzy..."
    show i krying open
    i "I've ruined everything."
    i "Our game is awful. I'm so sorry you have to put up with this [player]."
    show i krying closed
    menu:
        c "Oh don't say that Izzy..."
        "Isadora, how are you crying without eyes?":
            jump aspen_pissed_crying
        "Don't worry. I'm actually having a good time.":
            jump aspen_pissed_goodtime



    label aspen_pissed_goodtime:
        show a sad
        a "Oh sure.{w} I'm glad."
        a "Having a fun time seeing us prance around, are you?"
        show c disappoint
        c "Aspen...that's not what [pronoun[0]] meant..."
        show a long
        a "No no no.{w} It's okay.{w} I'm glad we're a good source of entertainment for you."
        i "Aspen...why..."
        show i krying open
        i "You've been mean before, but never this mean..."
        show i krying closed
        show a sad
        a "Oh shut up. I've been meaner than this."
        show c sad
        c "I don't think you have."
        show h sad
        h "can confirm{w} this is more than your usual temper dude"
        show a ahh
        a "Well it's for a good cause."
        show a sad
        a "You've all missed a huge opportunity. I'm quite disappointed in all of you."
        a "..."
        show a long
        a "Uh."
        a "..."
        show a sad
        a "God Dammit."
        $hardpause(1.0)
        show a sicko at move(-0.5, 1.5)
        $hardpause(1.0)
        show i ooo oohh
        $hardpause(0.3)
        show i ahh fists at move(0.4, 0.7)
        i "Wait no Aspen!"
        show c sad
        c "..."
        show i sad
        i "Should one of us follow them?"
        c "I don't know..."
        i "..."
        show h sad
        h "damn"
        c "Hope watch your language."
        h "sorry"
        $hardpause(4.0)
        play music endmusic
        show note_falling at note_falling zorder 20
        $hardpause(2.0)
        show c ohh
        c "Oh! What's this?"
        show c ohh
        i "Did that just fall from the sky?"
        show h disappoint
        h "oh no we broke the sky its raining paper"
        show i long
        i "Wait I think there's something written on this."
        i "..."
        show i open oohh
        iw "OH MY GOD"
        show c ahh
        c "What?"
        show i ehh
        iw "IT'S FROM - FROM..."
        show i ehh
        iw "HERE EVERYONE"

        $EndMessage[-1] = "P.S.: Don't worry about Aspen. They will be in a much better place soon."

        show screen Final_Note(EndMessage, True)
        pause 15

        c "A much better place soon?"
        c "That's...{w}um..."
        h "so its over"
        c "I think so..."        
        iw "WAIT THERE'S MORE ON THE OTHER SIDE"

        $EndingComplete("AspenPissed")

        hide screen Final_Note
        show screen Final_Note(EndMessageMeet, False)
        pause 2

        i "Huh?"
        h "Oh."
        c "..."
        $ending_aspen_pissed = True
        hide screen Final_Note
        jump nariend_start




    label aspen_pissed_crying:
        show i long
        i "{i}*sniff*{/i} Huh?"
        if ask_about_eyes:
            c "Again about \"I\"s..."
            c "What is an \"I\"?"
            i "What's krying?"
            show c long
            c "[Pronoun[0]] brought this up before, Aspen and I couldn't figure out what [player] was talking about."
        else:
            show c long
            c "What did you say? \"I\"s..."
            c "What's an \"I\"?"
            show i ooo
            i "What's krying?"
        show h ahh
        h "uh do you mean getting a runny nose"
        show i long
        h "maybe where the player comes from krying or whatever means getting a runny nose"
        show h long
        show c disappoint
        c "Maybe..."
        show a long
        a "[Pronoun[0]] didn't say krying."
        show c long
        c "Hm?"
        a "[Pronoun[0]] said..."
        a "..."
        show a crossed
        a "Never mind, that's not what [pronoun[0]] said."
        c "..."
        i "..."
        if pronoun[0] == "she":
            h "what"
            a "Hm?"
            h "sorry i wasnt listening i missed it"
            a "how could that have been what she said"
            a "...{w}Hope what are you talking about?"
            h "...{w}actually forget it im dumb nvm"
        $hardpause(3)
        show a ahh
        a "Hey Izzy."
        show i sad
        i "Yeah?"
        show a long
        a "Sorry I yelled at you."
        i "..."
        show i krying open
        extend "it's okay. {i}*sniff*{/i}"
        show i krying closed
        a "..."
        show h ahh
        h "hey uh"
        h "are we still trying to think of something to do"
        show h long
        i "..."
        show i long
        extend "sure Hope. Let's go get some mochi."
        i "I wouldn't mind some right now."
        a "..."
        a "Alright."
        show c smile
        c "Yes, let's go."
        play music endmusic
        show note_falling at note_falling zorder 20
        show c smile
        c "And we can take [player] with us!"
        show i ahh
        i "Wait, what's that?"
        show c ahh
        c "Is that a...{w}piece of paper?"
        show i ohh
        i "I think so."
        show h inv
        h "wow{w} forecast today: paper"
        show c ohh
        c "...OH!{w} Guys this is from{nw}"
        a "It's from the Creator, right?"
        show c long
        c "..."
        a "Just a logical conclusion.{w} [player] has been here long enough, yeah?"
        c "...{w}I suppose so."


        $EndMessage[-1] = "P.S.: Say your goodbyes now. You will likely never see [player] again."

        show screen Final_Note(EndMessage, True)
        pause 15

        c "Wait, never? Like, never ever???"
        i "[Pronoun[4]] going away forever? I mean I guess that makes sense...{w}but wow."
        a "So no more players? [Pronoun[0]]'ll be the only one?"
        c "I guess?"
        i "Hey, there's more on the back."
        
        $EndingComplete("AspenPissed")
        show screen Final_Note(EndMessageMeet, False)
        pause 7

        c "Huh?"
        i "Um."
        h "oh"
        hide screen Final_Note
        $ending_aspen_pissed = True
        jump nariend_start







