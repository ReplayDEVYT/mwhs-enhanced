label polite_isadora_enter:
    ## a 0.4
    ## c 0.8
    show i open at enterright(0.8, 0.4)
    show a ohh at move(0.6, 0.3, 30)
    show c ohh at move(0.1, 0.3, 30)
    $ renpy.music.set_volume(0.7, channel='music')
    play music toointensebeat
    iq "I'M BACK"
    show c open at hop
    c "Ah!! Izzy! Are you okay?"
    show i ahh
    izq "{i}*huff huff huff*{/i} What? Yeah! I'm fine!"
    show c long at move (-0.1, 0.8) zorder 3
    show a long at move(0.2, 0.8) zorder 4
    show h long at enterright(0.8, 1.5) zorder 2
    show i laugh at move(0.5, 0.8) zorder 5
    show n line at move(1.5, 0.0) zorder 1:
        pause 1.5
        easein 4 xalign 1.1
    izq "I brought Hope and Nari!"
    show h ohh
    hq "whoah so thats the player"
    show i happy
    izq "Yeah!"
    show h tongue
    hq "oh sweet{w} hes so blurry thats so weird"
    if pronoun[0] != "he":
        show c smile
        c "Actually they go by [pronoun[0]]."
        show h owo
        h "oh ok"
    show h owo
    show c ahh
    c "Izzy, why did you...uh?"
    show i ohh
    izq "The player has to meet everyone! So I brought everyone?"
    a "You do realize that we don't constitute as everyone."
    show i oohh wah
    izqw "EVERYONE IN THE GANG.{w} NOT EVERYONE EVER.{w} I'M NOT DUMB ASPEN."
    show c long
    c "This might be kind of overkill Izzy, we shouldn't be introducing all of us to [pronoun[1]] at once."
    show i ahh
    izq "But we don't have much time! We have to do all we can before we run out of time!"
    show a ahh
    a "How do you know that?"
    show i long
    izq "Know what?"
    a "Are we on a timer?"
    show i omg
    izqw "WE'RE A DEMO!!!{w} DEMOS ARE SHORT!!!!!!{w} UUUUGGGGGG WE'RE WASTING TIME ARGUING ABOUT THIS!!!"
    iw "I'M ISADORA, THE DERPY PURPLE HAIRED ONE IS HOPE, AND THE QUIET GREEN HAIRED PERSON IS NARI."
    show h owopose
    h "lol you think im derpy"
    show h smile
    iw "QUICK SOMEONE THINK OF A QUESTION"
    show i longbig
    show c ahh
    c "Izzy calm down, we don't have to rush this."
    show a ahh
    a "Ok I have a question."
    stop music
    $ renpy.music.set_volume(1.0, channel='music')
    a "[player], which one of us do you think is the cutest?"
    if IsBadWord(player):
        show h disappoint
        h "hold the phone what did you just say"
    ##EVERYONE GO MOVE MOVE MOVE MOVE MOVE!!!!
    show c at move (-0.1, 0.0)
    show a at move(0.2, 0.0)
    show h at move(0.8, 0.0)
    show n at move(1.1, 0.0)
    show i at move(0.5, 0.0)
    show c surprised ehh at hop()
    menu:
        c "{i}Aspen!{/i} What's gotten into you?"
        "{color=#cb454c}Chris":
            $cute = "c"
        "{color=#e8ba3e}Aspen":
            $cute = "a"
        "{color=#a8741f}Isadora":
            $cute = "i"
        "{color=#db54dd}Hope":
            $cute = "h"
        "{color=#7dd87d}Nari":
            $cute = "n"
        "Uhhhhhhhhhhhhhhhhhhh.....":
            $cute = False

    $persistent.cutelist.append(cute)
#----Cute Remarks

    play music happymeta
    show a long

    if IsBadWord(player):
        h "hold on aspen what did you just say"
        a "Um, I asked the player who was the cutest?"
        h "no i mean what did you just call them"
        show c sweat sicko fists
        c "..."
        a "They want to be called [player]."
        show h sad
        h "omg r u serious"
        h "wtf"
        show c sad -sweat
        if cute == "h":
            h "and ur advances are not reciprocated btw"
            show h angry
            h "screw off"
        if cute == "n":
            h "btw you stay far away from nari"
        c "...I cannot believe this is happening right now."

    elif cute == "c": #Chris
        if tone == 1: #Player polite
            show c long blush at hop
            c "...wha-?{w} Really?{w} Erm..."
            show h smile
            h "awwwwwwwwww thats cute"
            show c fists ehh blush
            c "H-h-hope! No! D-d-don't encourage this!"
        elif tone == -1: #Player rude
            c "..."
            c "Aspen, you shouldn't be encouraging [pronoun[1]] to screw around with us even more."
    elif cute == "i": #Isadora
        show c fists sad
        show i sicko blush at hop
        i "Eep!"
        show h smile
        h "awwwwwwwww thats cute"
        show c open
        c "Hope!{w} Don't encourage this!"
    elif cute == "a": #Aspen
        show a proclaim
        show c sad
        a "Whahahahahaha! Of course! Who else would [pronoun[0]] choose? I am undeniably the best option!"
        show c fists ehh
        c "Aspen!{w} I can't believe you!"
    elif cute == "h": #Hope
        show h derp
        h "LMAO u think im cute"
        if pronoun[0] == "she":
            show h owopose
            h "well ur lucky cause im gay af lets make out"
            c "HOPE OH MY GOD NO"
        if pronoun[0] == "he":
            h "sorry im super gay go for someone else"
            h "but if u were a chick i think id def be all over u"
            show c ehh fists
            c "HOPE{w} NO{w} DON'T DO THAT"
        if pronoun[0] == "they":
            h "gonna be real i have no idea if im into u but we should hang out later if ur still around"
            show c fists sad
            c "...I cannot believe this is happening right now."
    elif cute == "n": #Nari
        show c sad
        show h derp
        h "aw [pronoun[0]] like[s_conj] the quiet one"
        show h owo
        h "you hear that nari{w} maybe you have a chance to bang the player"
        show c fists open
        c "Hope!{w} Oh my god!{w} Don't encourage this!"
    else: #No One
        show c fists open
        c "In what universe of yours is a question like that anywhere NEAR appropriate?"

#----  
    if cute == "a":
        show c inv
        show a smile
        a "Oh come on Chris, isn't this the whole point of everything anyway? Besides, wasn't that question super beneficial information?"
        show a happy blush
        a "{shader=wave}{i}I certainly think so~ <3{/i}{/shader}"
        show a smile -blush
        show c open
        c "Oh my god {shader=jitter:u__jitter=1.0, 1.0}STOP THAT!{/shader}"
    else:
        show a ahh
        show c inv
        a "Oh come on Chris, isn't this the whole point of everything anyway? Why not cut to the chase?"
        show a long
    
    if cute == "c":
        show a laugh
        a "Beside's, [pronoun[0]] think[s_conj] you're cute!"
        show c longbig blush
        c "N-no...we are NOT a dating sim!"
    else:
        show c ehh
        c "Haven't we been over this?! We are NOT a dating sim!!"

    show a standard smirk
    a "Oh? And how do you know that?"
    if cute != "c":
        show c long
    c "...{w}it just isn't ok?"
    show a smile
    a "According to who?"
    show c open -blush
    c "...even if we are a dating sim, you don't just ask someone something like that as soon as you meet them!"
    if married:
        c "Especially to someone who's...{w=0.5}"
        show c ohh at hop
        extend "OH!{w} That's why you were surprised that she was married!"
        show a long
        a "Well obviously \"[player]\" doesn't consider it a problem, so neither should we."
        show c open
        c "It's not a problem in the first place! WE'RE NOT A DATING SIM!!!!"
        show c sad
        c "I cannot believe we are talking about this..."
    show c sad
    if cute == "n" and not IsBadWord(player):
        show h smirk
        h "hey this is nari were talking about here{w} im sure she can take it"
        show i long
        i "...{w}is she...{w}taking it?"
        show h smile
        h "ur taking it right buddy"
        n "..."
        show n line
        extend "I'm taking it."
        show h smirk
        h "see shes taking it"
        i "...{w}okay..."
        show i disappoint
        i "It's hard to tell if Nari takes in much of anything these days."
        show h long
        h "...{w}shes taking it dont worry"
        a "Well anyway, we probably don't have much time. May as well use it doing what matters."
    else:
        show a crossed ooh
        a "Hey, Isadora said it herself. We don't have much time. May as well use it doing what matters."
    if not IsBadWord(player):
        if (pronoun[0] == "she"):
            show h owopose
            h "heheheheheheh doing what matters{w} yes please {shader=wave}lets \"do it\" as soon as possible{/shader}"
            show h tongue
            show c sicko
            c "HOPE!{w} Don't encourage this!"
        else:
            show h owopose
            h "heheheheheheh doing what matters{w} what sort of \"doing\" do you have in mind"
            show h tongue
            show c sicko
            c "Hope!"
    if cute == "n":
        show n disappoint
    show a smile
    show i standard long -blush
    i "Um...a-are we?"
    show n line
    show c standard disappoint
    c "Hm?"
    show i ahh
    i "Is t-that what we are now? A dating sim?"
    
    if cute == "i":
        if tone == -1:
            show i disappoint
            i "I really hope that's not the case..."
        else:
            show i crossed long
            i "I don't know...uh...but if we are..."
            show i sicko blush at shake(4)
            i "I don't know what that would mean...{w}{shader=jitter:u__jitter=1, 0.5}{cps=*0.6}if [pronoun[0]]{/cps}{/shader}..."
    
    show i long at stop
    show c open
    c "No! We most definitely aren't!"
    show a smile
    a "I bet you we are."
    show c sad
    c "You don't get to make the rules, Aspen!"
    show a crossed long
    a "...{w}okay to be fair, we do only have conjecture, but..."
    show c ehh
    c "Right! We don't know anything!"
    show c inv
    show a ahh
    a "However given of what we know of our universe, I think it's most likely that we are a dating sim."
    a "I mean - the player appeared in front of us, outside of our high school. What else are we going to be, a horror game?"
    show i crossed sad -blush
    i "...I sure hope we aren't some subversive horror game."
    show h derp
    h "{shader=jitter:u__jitter=2, 2}ISADORAS GONNA DIE FIRST{/shader}"
    if cute == "i":
        show i fists open
        i "Wha-? Hey! Are you saying that just because [pronoun[0]]...?!?!?!"
        show a smile
        a "Hm...{w} no, I think Hope said that because it's true. You kind of fit the archetype."
    else:
        show i fists open
        i "Wha-? No! You would die first, dingus!"
        show a smile
        a "Hm...{w} yeah Isadora would die first. You kind of fit the archetype."
    show i wah at shake(4)
    iw "WHAT ARCHETYPE"
    show c smirk
    c "...sorry Izzy, I kinda have to agree. You're a goner."
    show i omg at shake
    menu:
        iw "NOOOOOOOO YOU GUYS ARE HORRIBLE." 
        "None of you are going to die, don't be silly!":
            jump immortality_nobody_gonna_die
        "I agree too. She's as good as dead.":
            jump polite_isadora_gonna_die
        "ALL OF YOU ARE GOING TO DIE":
            jump horror_start

label polite_isadora_gonna_die:
    show i omg at shake(40)
    iw "OH MY GOD WHAT?{w} YOU TOO?!?!?!"
    show i crossed inv at stop
    if not IsBadWord(player):
        show h derp
        h "lololololol even [pronoun[0]] say[s_conj] ur gonna die"
        show h long
        h "uhhhhh whats [pronoun[2]] name again"
        show c smile
        c "[player]."
        if not IsName(player):
            show h long
            h "what"
            show a disappoint
        else:
            show h owo
            h "cool"
    else:
        show h derp
        if pronoun[0] == "he":
            h "lololololol even this dumb dude says ur gonna die"
        if pronoun[0] == "she":
            h "lololololol even this stupid chick says ur gonna die"
        if pronoun[0] == "they":
            h "lololololol even this stupid person says ur gonna die"
    show i wah
    iw "UUUUHHHHHHHGGGGGGGGG GUYS COME ON"
    iw "WE'RE WASTING TIME DOING NOTHING WE NEED TO BE DOING DEMO STUFF"
    jump polite_argue


    label polite_isadora_death_outburst:
        show i line standard
        i "Uh huh."
        a "...{w}Uh...yeah?"
        i "Just talking about death and dying and stuff."
        i "Yep. Just standing here. Contemplating existence. That's nice."
        show i line
        a "..."
        i "..."
        show c ahh
        c "Uh, Izzy? You doing ok{nw}"
        show i arg at shake(200)
        show c ohh at hop()
        show a ohh at hop()
        show h ooo at hop()
        play music happymeta
        iw "ARE YOU STUPID OF COURSE WE DIE YOU IDIOT"
        iw "WE'RE WASTING TIME DOING NOTHING WE NEED TO BE DOING DEMO STUFF"
        show a ahh
        show i fists inv at stop
        a "Holy cow calm down..."
        jump polite_argue

##--------
    label polite_argue:
        show i wah
        iw "WE'RE RUNNING OUT OF TIME."
        show a long
        show i inv:
            xalign 0.5
        a "What are you talking about? We have plenty of time."
        show c ahh
        c "Izzy, what do you mean by demo stuff?"
        if not IsBadWord(player):
            show i ahh
            i "We uh...have to show [player] the game!"
            if not player_name_is_a_name:
                show h long
                h "who now"
        else:
            show i ahh
            i "We uh...have to show the player the game!"
        show h long
        show a ahh
        a "But what game?"
        show i open
        i "THE GAME"
        a "Our game?"
        show i laugh
        i "YES"
        show i open
        extend " I mean wait {w=0.1}{nw}"
        i "NO THE FINAL GAME."
        show c ahh
        c "Nobody knows anything about the final game."
        show i arg
        iw "UGGGGG NO YOU'RE MISSING THE POINT"
        show i inv
        i "We don't know everything, but we know SOME things!"
        if aspen_pissed:
            jump aspen_pissed
        show a disappoint
        a "Well then we're back to where we were earlier. What should we do today?"
        show c think
        c "...Hm...{w}you know, you have a point there Izzy."
        c "We're a demo, so we should somehow be able to give [player] a preview of what the final game is going to be like, right?"
        show c smile
        if IsBadWord(player):
            show h angry
            h "good god why do you have to keep saying it"
        c "So maybe we actually know much more than we think!"
        show i arg at shake(50)
        iw "THAT'S WHAT I'VE BEEN SAYING!!!"
        if not player_name_is_a_name and not IsBadWord(player):
            show i fists inv at stop
            h "guys am I the only one hearing this"
            $playerLowercase = player.lower()
            h "why are we calling the player [playerLowercase]"
            show c long
            c "That's...what they wanted to be called."
            h "...{w}"
            show h tongue
            extend "lmao ok"
        show i fists inv at stop
        show c laugh
        c "...maybe we should all introduce ourselves a little more formally? We've kind of gotten off to a rough start."
        show a ahh
        a "Like play an ice breaker game or something?"
        show c long
        show i standard ahh
        i "Uhhhhhhh...{w}that's not really what I had in mind..."
        show a ahh
        a "Well what did you have in mind?"
        show i disappoint
        i "I don't know, like...{w}uh...{w}just telling [pronoun[1]] about our lives and school and stuff?"
        show a disappoint
        a "...not gonna lie that sounds boring."
        show i open
        i "Well do you have a better idea?!?!"
        show i inv
        show a ahh
        a "I threw in the icebreaker idea already. I think that's not a bad idea."
        show c ahh
        c "What game would it be?"
        show a long
        a "I dunno...something you play at camp?"
        show c disappoint
        c "...I'm with Izzy, playing a camp game doesn't sound like the greatest idea."
        show h owo
        h "hey i got a game we can play"
        show i sad
        i "No Hope we are not playing Truth or Dare."
        show h sad
        h "wow quick to make assumptions there"
        show h tongue
        extend " hey that rhymed cool"
        show h smile
        h "no what i was actually going to suggest was lets play go and get some mochi because this is getting boring and mochi sounds like a really good idea right now"
        if IsBadWord(player):
            show h sad
            h "i guess this dumbass can come too if they want"
        elif cute == "h" and (pronoun[0] == "she" or pronoun[0] == "they"):
            jump hope_intro
        elif pronoun[0] == "he":
            h "if u werent a dude id prob suggest wed make out or something but ur are def a dude i think so sorry"
        elif pronoun[0] == "she" or pronoun[0] == "they":
            h "id suggest wed make out or something cuz how cool would that be but idk if you'd be into that"
        show c open
        c "Hope!"
        show c inv
        show i disappoint
        i "Oh geez, here we go with the mochi again..."
        if not player_name_is_a_name or IsBadWord(player):
            h "but yeah anyway hey crazy name you wanna get ur mochi on"
        else:
            h "but yeah anyway i forgot your name you wanna get ur mochi on"
        menu:
            "Sure":
                $mochi_players_idea = True
                jump Mochi_time
            "No thanks":
                jump no_moochi_start
            "What's mochi?":
                $mochi_players_idea = False
                jump whats_mochi


label whats_mochi:
    stop music
    $persistent.cluelessaboutmochi = True
    show h sad
    h "excuse me{w} did i just hear the words whats mochi come out of your mouth and into my head"
    show c disappoint
    c "[player] isn't from around here, please be kind..."
    if IsBadWord(player):
        jump hope_has_had_it
    show h disappoint
    h "oh no{w} of all the crazy things i have heard this one of the most unfortunate"
    show h sad
    h "actually its a real tragedy{w} congrats you have successfully converted this visual novel into a new genre:{w} tragedy"
    h "theres only one way we can fix this"
    show i longbig
    i "Hope..."
    show h line
    h "we need to get this player some mochi stat or else we will all be doomed to bad endings"
    show h ohh
    h "quick we need to act fast"
    show h open
    h "we must move like the wind"
    h "because fate has called out to us"
    show h line
    h "its mochi time"
    show h laugh at move(2.0, 1.0, 30)
    h "pew"
    $hardpause(3.5)
    i "...Looks like we're getting Mochi again then."
    a "Yep."
    c "Once again."
    a "...{w}well, let's go before Hope gets too far ahead of us."
    jump going_to_mochi



#---------
    label Mochi_time:
        h "sweet u guys coming"
        show a disappoint
        a "Well that answers that then."
    label yep_its_mochi_time:
        stop music fadeout 5
        show c long
        c "Looks like we're getting Mochi again."
        show i ahh
        i "Don't we always end up choosing mochi?"
        show h smirk
        h "imo we dont choose mochi enough"
        show h derp at move(2.0, 3.5)
        h "come on lets go"
    label going_to_mochi:
        show n line at move(2.0, 5.0)
        show a long at move(2.0, 5.0)
        show i long at move(2.0, 5.0)
        show c long at move(0.9, 1.5)
        pause 0.5
        show black zorder 50:
            alpha 0.0
            easein 2.0 alpha 1.0
        pause 1.0
        show c open at move (0.5, 0.5)
        if not IsBadWord(player):
            c "What the heck? [player] is disappearing!"
        else:
            c "What the heck? The player is disappearing!"
        pause 3
        jump mochi_start

label hope_has_had_it:
    h "omfg why are we taking the creep named [player] so seriously"
    show h mad
    h "u know wat ive had it screw you guys im out"
    show h sad at move(2.0, 3.5)
    h "have fun with \"[player]\""
    show c surprised ehh
    c "Wha- Hope, no!!!"
    $hardpause(3)
    show n at move(2.0, 5.0)
    $hardpause(4)
    jump hope_is_gone

