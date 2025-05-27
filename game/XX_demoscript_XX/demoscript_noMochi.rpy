
label no_moochi_start:
    stop music fadeout 15
    show h long
    h "huh mochi not your thing"
    show h smile
    h "thats alright{w} see you all later then im gonna go get some mochi"
    show i open
    i "WHAT??!?!{w} You're just gonna leave?"
    show h long
    h "yeah{w} what is that bad"
    n "Can I come."
    show h smirk
    h "yeah totally"
    show h derp
    h "see you guys have fun with the player"

label bye_hope:
    show h at move(1.5, 2.0)
    pause 0.5
    show n at move(1.5, 2.0)
    pause 2
    hide h
    hide n

label hope_is_gone:
    a "Huh."
    show i fists ehh
    i "omg I cannot BELIEVE her! This happens and she ditches us for MOCHI?!?!?!"
    show c sad standard
    c "Hope does have a tendency to do her own thing, doesn't she?"
    show a sad at move(0.9, 3.0)
    a "Should we go with her?"
    show i sad
    i "No, we all need to be doing demo stuff!"
    show a disappoint
    a "Again, I still have no idea what that means."
    i "Isn't it obvious? We tell the player about ourselves! How is that so complicated?"
    show c disappoint
    c "...just like - Hi, I'm so-and-so? "
    if IsBadWord(player):
        a "I mean since we're probably a dating sim...it would be most optimal to just let...um...{w}the player...{w}pick someone to...{w}...you know...{w}to f{nw}"
    else:
        a "I mean since we're probably a dating sim...it would be most optimal to just let [player] pick someone to...{w}...you know...{w}to f{nw}"
    show c sad
    c "I don't know what you're about to say Aspen but how about we NOT do that?!"
    show i open
    i "Okay FINE, you guys obviously don't know how to do this properly so I'll start."
    play music intromusic
    show i smile standard
    if IsBadWord(player):
        i "Hi!{w} My name is Isadora.{w} I'm 161cm, I weigh 123 pounds, and my blood type is AB.{w} My birthday is April 19th, and{nw}"
    else:
        i "Hi [player].{w} My name is Isadora.{w} I'm 161cm, I weigh 123 pounds, and my blood type is AB.{w} My birthday is April 19th, and{nw}"
    $renpy.music.set_pause(True)
    show c ahh
    c "Whoah hey now, this is what you meant by demo stuff?"
    show i sad
    show a open
    a "You're just listing off facts! How is that \"demo stuff\"?"
    show i open fists
    i "It's not just listing off facts! I'm just getting warmed up."
    show i inv standard
    i "Now if you wouldn't interrupt I have a lot to get through, as do all of you. And again..."
    show i arg at shake(40)
    iw "WE DON'T HAVE MUCH TIME LEFT!"
    show i inv at stop
    i "God."
    $renpy.music.set_pause(False)
    show i smile
    extend " Anyway, so since I was born on April 19th I'm an Aries.{w} My favorite food is tomatoes and my least favorite food is{nw}"
    stop music
    show a sad
    if IsBadWord(player):
        a "Ok we're not doing this. I don't consent to giving [pronoun[1]] a list of statistics."
    else:
        a "Ok we're not doing this. I don't consent to giving [player] a list of statistics."
    show i long
    i "..."
    show i wah crossed
    iw "WELL WHAT DO YOU SUGGEST WE DO THEN"
    show i inv
    show c laugh
    c "How about we go for a walk?"
    show i wah
    iw "WHERE?"
    c "Does it matter where? Anywhere!"
    show i omg
    iw "THAT'S NOT PRODUCTIVE"
    c "Well it'd get us on our feet."
    show i:
        easein 0.2 yoffset -800
    iw "WE DON'T HAVE FEET"
    show c disappoint
    c "...touché."
    show i inv crossed:
        easein 0.2 yoffset 0
    show a smirk
    a "Oh, I know what might be a lot of fun."
    a "How about we go to someone's house?"
    if cute == "c":
        show a laugh
        a "...like maybe Chris's?"
        show c disappoint
        c "...let's not do that..."
        show a ohh
        a "Oh?{w} And Why not?"
        show c sad
        c "You know why."
        a "I most certainly don't."
        c "No you know why."
        if IsBadWord(player):
            a "Oh! But for whatever reason?{w} For I think [pronoun[0]] would VERY much like to come to your house..."
        else:
            a "Oh! But for whatever reason?{w} For I think [player] would VERY much like to come to your house..."
        show c inv
        c "..."
        show c open
        extend "for the last time, we are NOT a dating sim!"
        a "Oh! Is THAT what you meant!?{w} My my, I never would have{nw}"
        show i sad
        i "Aspen cut it out."
        show a long
        if IsBadWord(player):
            a "Okay joking aside, why is this a bad idea? Are you that skeptical of [pronoun[1]] for some reason?"
        else:
            a "Okay joking aside, why is this a bad idea? Are you that skeptical of [player] for some reason?"
        jump nomochi_chirs_mansplains
    elif cute == "i":
        show a laugh
        a "...like maybe Isadora's?"
        show i sad blush
        i "...I'm...{w}uh...{w}not really a fan of that idea."
        a "Oh?{w} And Why not?"
        show c sad
        c "You know why."
        show a smirk
        a "I most certainly don't."
        c "No you know why."
        show a ohh
        if IsBadWord(player):
            a "Oh! But for whatever reason?{w} For I think [pronoun[0]] would VERY much like to go to Isadora's house..."
        else:
            a "Oh! But for whatever reason?{w} For I think [player] would VERY much like to go to Isadora's house..."
        show c inv
        c "..."
        show c open
        extend "for the last time, we are NOT a dating sim!"
        a "Oh! Is THAT what you meant!?{w} My my, I never would have{nw}"
        show i sad -blush
        i "Aspen cut it out."        
        show a long
        if IsBadWord(player):
            a "Okay joking aside, why is this a bad idea? Are you that skeptical of [pronoun[1]] for some reason?"
        else:
            a "Okay joking aside, why is this a bad idea? Are you that skeptical of [player] for some reason?"
        jump nomochi_chirs_mansplains
    elif cute == "a":
        show a laugh
        a "...like maybe mine?"
        show c sad
        c "...{w}yeah no we're not doing that."
        show a ohh
        a "Oh?{w} And Why not?"
        c "You know why."
        a "I most certainly don't."
        c "No you know why."
        if IsBadWord(player):
            a "Oh! But for whatever reason?{w} For I think [pronoun[0]] would VERY much like to come to my house..."
        else:
            a "Oh! But for whatever reason?{w} For I think [player] would VERY much like to come to my house..."
        show a owo
        a "But if you must insist, I certainly wouldn't mind if none of you wanted to come along..."
        show c open
        c "Oh my god!{w} For the last time, we're NOT a dating sim!"
        show a ohh
        a "Oh! Is THAT what you meant!?{w} My my, I never would have{nw}"
        show i sad
        i "Aspen cut it out."
        show a long
        a "Okay joking aside, why is this a bad idea? Are you that skeptical of [player] for some reason?"
        jump nomochi_chirs_mansplains
    else:
        show i sad
        i "...{w}um...{w}let's not do that today."
        show c disappoint
        c "Yeah I'm not really a fan of that idea either."
        show a ohh
        a "Oh? Why not?"
        i "...I just would rather do something else, you know?"
        c "Yeah."
        a "..."
        if pronoun[0] == "he":
            show a disappoint
            if IsBadWord(player):
                a "Is it because he's guy?"
            else:
                a "Is it because [player] is a guy?"
            show c ahh
            c "What?"
            show i sad
            i "Actually yeah, that's why."
            show c long
            c "Oh."
            show a sad
            a "Hmph!{w} Sexist."
            show i ahh
            i "Whaaa???{w} How is that sexist?"
            a "If I were a guy, would you feel weird if I was in your house?"
            show i open
            i "You're a friend! That's different! We just met [player]!"
            a "Oh so now [player] is untrustworthy?"
            jump nomochi_chirs_mansplains
        elif cute != False:
            show a disappoint
            if IsBadWord(player):
                a "Is it because [pronoun[0]] said one of us was cute?"
            else:
                a "Is it because [player] said one of us was cute?"
            show c ahh
            c "What?"
            show i disappoint
            i "I mean...kind of?"
            a "What does that have to do with anything?"
            jump nomochi_chirs_mansplains
        else:
            show a open
            if IsBadWord(player):
                a "...Come on! You have no reason to be suspicious of [pronoun[1]] for anything!"
            else:
                a "...Come on! You have no reason to be suspicious of [player] for anything!"
            show i disappoint
            i "I'm just not comfortable with it, ok?"
            a "Why?"
            show i sad
            i "Just because, okay?"
            show a disappoint
            a "Are you that skeptical of [player] for some reason?"
    label nomochi_chirs_mansplains:
        show c ahh
        c "Aspen it's not that at all.{w} I'd gladly have [player] over under different circumstances, really.{w} But the way you've been putting it makes me kind of uncomfortable."
        c "If you weren't so set on us being a dating sim I'd feel differently.{w} But I reeeaaaaaly don't want to give that impression off to [player]. It'd be a disservice to the final game."
        show a long
        a "But...{w}we are...{w}we have to be."
        show c sad
        c "No.{w} We.{w} Are.{w} Not."
        c "So if we can avoid anyone getting into anyone else's pants I'd really appreciate it."
        show i long
        i "But we aren't wearing pants."
        show c line
        c "Izzy it's a figure of speech.{w} You don't need to be wearing pants to get into someone else's pants."
        show a smirk
        a "Pfft."
        show c ahh
        c "What?"
        a "I mean if you're getting into someone's pants it's likely you're not wearing pants yourself."
        show c long
        c "Um...{w}okay?"
        i "..."
        a "..."
        show a sad
        extend "never mind, I think that was only funny to me."
        c "..."
        i "...{w}well what should we do then."
        a "Dunno."
        c "Want to go get mochi with Hope?"
        i "..."
        i "No."
        c "Okay."
        show a ahh
        a "Wait - we're forgetting a really simple solution."
        a "Let's just ask [player] what [pronoun[0]] want[s_conj] to do and we can just do that."
        show c smile
        play music happymeta fadein 5.0
        c "That's a good idea!"
        if IsBadWord(player):
            i "Uhhg is that really [pronoun[2]] name?"
            show a sad
            a "I doubt it, but that's what we should call [pronoun[2]]."
            show a long
            a "Anyway, what's been suggested so far?"
        else:
            a "What's been suggested so far?"
        show i ooo standard
        i "Uh..."
        c "Getting mochi, taking a walk...uh..."
        show i inv crossed
        i "Not a fan but okay."
        a "Or...go to the library."
        i "Also not a fan."
        show a sad
        a "Well maybe [player] might be a fan."
        show a ahh
        menu:
            a "What do you want to do?"
            "Go get mochi":
                $goget = "go get mochi"
                jump noMochi_prenotefall_mochi
            "Go for a walk":
                $goget = "go for that walk"
                jump noMochi_prenotefall_walk
            "Go to the library":
                $goget = "go to the library"
                jump noMochi_prenotefall_library

    label noMochi_prenotefall_mochi:
        show i sad
        i "Uhhhg alright."
        show c smile
        c "Well at least we'll all be together again! Good choice."
        show a long
        a "...mochi it is then."
        jump noMochi_notefall

    label noMochi_prenotefall_walk:
        show i ehh
        i "Really?"
        show c laugh
        c "Good choice! There's nothing like a good walk!"
        show a disappoint
        a "Our aimless walks have not been so...successful...in the past."
        show c ohh
        c "Oh, but anything can happen! That's the exciting part."
        show i inv
        i "That's not how I would describe our past walks..."
        show a long
        a "Whatever, if it's what [player] wants we may as well."
        jump noMochi_notefall

    label noMochi_prenotefall_library:
        show i ehh oohh
        i "The LIBRARY? WHAT?"
        show a proclaim
        a "Ah, a logical choice. Who wouldn't want to know more about our world? And there's no better place to do it than the library!"
        show a happy standard
        a "This is just as good a way as any to do \"Demo Stuff\". You should be more excited Isadora!"
        show i sad crossed
        i "..."
        show c smile
        c "...this should be interesting!"
        jump noMochi_notefall


label noMochi_notefall:
    show note_falling at note_falling zorder 20
    play music endmusic
    show a smile
    a "Let's go."
    show c ohh
    c "Wait what's that?"
    show a long
    a "What?"
    c "Something just fell from the sky."
    show i ooo
    i "That on the ground?"
    c "Yeah, I'll pick it up."
    c "...oh.{w} It's a note?"
    show c open
    c "...{w}OH!{w} WOW!"
    c "It's from the Creator!"
    show i ehh fists
    iw "WHAT?"
    show a wah
    a "HUH?"
    show i wah
    iw "WHAAAAATT!!?!?!"
    show a open
    a "Show it here!"
    show c smile
    c "It's intended for [player]."

    $EndMessage[-1] = "P.S.: Sorry that you didn't get to [goget]. But we only have so much time, don't we?"

    show screen Final_Note(EndMessage)
    pause 15

    a "Are we over?"
    c "I guess...{w}that's it..."
    c "...hey!{w} There's more on the other side!"

    hide screen Final_Note
    $EndingComplete("NoMochi")
    show screen Final_Note(EndMessageMeet, False)
    pause 2

    c "Huh?"
    i "What is this talking about?"
    c "Not sure..."
    c "Wait, so what's going to happen to [player] now{nw}"
    $ending_aspen_pissed = True

    $persistent.goget = goget

    hide screen Final_Note
    jump nariend_start_notthere


    c "END"





    