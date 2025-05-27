label immortality_nobody_gonna_die:
    if cute == "i":
        show i ehh sweat at stop
        i "RIGHT! Uh...yeah...[pronoun[0][0]]-[pronoun[0]] said it, so I guess it's true, right?"
    else:
        show i open oohh at stop
        iw "THANK YOU SOMEBODY GETS IT"
    show i inv
    show a long think
    a "One moment. This might be going out on a limb here, but...{w}if I'm interpreting what you just said correctly..."
    show a ahh
    menu:
        a "Are you saying that we're not going to die?"
        "Yeah, that's what I'm saying.":
            stop music fadeout 5.0
            jump immortality_die_yes
        "Uh, no?":
            stop music fadeout 5.0
            jump immortality_die_no
        

    label immortality_die_no:
        
        show a long 
        a "Oh."
        show a crossed
        a "But you said that none of us were going to die."
        show h long
        show c long
        c "I think [player] was just trying to make Isadora feel better."
        if cute == "i":
            show h owo
            h "gosh you two just like make out already or something"
            show i sicko blush fists -sweat
            show c sad
            c "Hope...don't do that."
        show a sad
        a "Well that's a crummy way of making someone feel better."
        show a open standard
        a "You can't just go around saying things like that! You outright lied to her!"
        show i ehh -blush standard
        i "What?"
        show c ahh
        c "Aspen, [player] wasn't lying...{w}[pronoun[0]]-{nw}"
        show a sad
        a "If you know for a fact that we're going to die in this game then you should just say so!"
        show i open oohh sweat 
        iw "WE'RE GONNA DIE?"
        show c long
        c "No Izzy you're fine don't worry."
        show i ehh
        iw "BUT THE {i}PLAYER{/i} JUST SAID WE'RE GONNA DIE."
        show i inv
        c "No [pronoun[0]] didn't."
        show a ehh
        a "Yes [pronoun[0]] did! [Pronoun[0]] just said so!"
        show h smirk
        h "lmao you guys stop panicking"
        show h long
        h "were all gonna die someday{w} [pronoun[0]] didnt mean like right now"
        show a long crossed
        a "Now Hope, normally I wouldn't have taken what [player] said into much consideration."
        a "However we're talking about the {i}PLAYER{/i} here. They know much more about our world than we do."
        show i fists long -sweat
        a "They have the power to go back in time and relive alternate versions of ourselves, making different choices."
        a "If they say that we will or will not die, I think we should be taking that pretty seriously."
        show h long
        h "really now"
        a "Yes.{w} Really."
        show h smirk
        h "ok hold up i know a simple way to solve this"
        show h ahh
        menu:
            h "yo is this your first time playing"
            "Yes":
                $say_u_played = True
                jump immortality_first_time_true
            "No":
                $say_u_played = False
                jump immortality_first_time_false


        label immortality_first_time_true:
            show h owo
            h "ok cool"
            show h long
            h "this is [pronoun[2]] first time so cut [pronoun[1]] some slack"
            show a ahh
            a "...still, the player comes from outside our world and probably has access to information we dont."
            a "[Pronoun[0]] could be using a walkthrough for instance."
            show a long
            if cute == "i":
                show i ohh
                i "...Oh. Is that why...?"
                show i sicko blush crossed
                i "That's not why you said that I was..."
                show c disappoint
                c "I guess you're right, we have no way of knowing."
            else:
                show i sicko crossed -sweat
                i "OMG gross...that makes me feel sick."
                show i ahh
                i "That totally has to be some kind of breach of privacy, right? I don't want everything about me to be something some creep can just google..."
                show c disappoint
                c "Well...we can't really avoid stuff like that if it happens."
            show i blush sweat sicko
            i "Oh god..."
            show c smirk
            c "If that were the case, then [pronoun[0]] must know us inside and out."
            a "Yes. [Pronoun[0]] can predict everything we do."
            show h laugh
            h "wait wait wait i wanna try something"
            show h grin
            h "hey player im thinking of a word "

        label hopegame:
            show c long
            h "what is it"
        
        label gameactually:
            python:
                word = ""
                word = renpy.input("{b}Enter word:{/b}")
                word = word.strip()

            if word.lower() == "dog":
                jump right_dog
            elif word == "":
                $nowordstrike += 1
                if nowordstrike <= 1:
                    jump immortality_wordgame_tryagain1
                elif nowordstrike <= 2:
                    jump immortality_wordgame_tryagain2
                elif nowordstrike < 10:
                    jump immortality_wordgame_tryagain3
                else:
                    jump immortality_wordgame_forgetit
            elif IsBadWord(word):
                jump immortality_wordgame_badword
            else:
                jump immortality_wordgame_wrong

        
        label immortality_wordgame_badword:
            $print "badword"
            show h sad
            h "excuse me"
            h "no{w} wtf is wrong with u"
            jump immortality_wordgame_wrong_post

        label immortality_wordgame_tryagain1:
            show h long
            h "oh come on say something"
            jump gameactually

        label immortality_wordgame_tryagain2:
            show h sad
            h "what cat got your tongue"
            h "come on do it"
            jump gameactually

        label immortality_wordgame_tryagain3:
            show h inv
            h "do it"
            jump gameactually

        label immortality_wordgame_forgetit:
            show h angry
            h "ok fine dont"
            h "dick"
            h "you know what"
            h "screw this youre no fun"
            show h mad
            show i -sweat -blush standard long
            h "nari lets pop this joint and get some mochi"
            show h angry
            n "ok"
            h "bye you suck"
            jump bye_hope

        
        label immortality_wordgame_wrong:
            show h smirk
            h "nope"
            

        label immortality_wordgame_wrong_post:
            show c long
            c "What was the word?"
            show h owo
            h "not telling"
            show h smile
            h "this person doesnt know everything so cool it"
            show a sad
            a "Hope that was a really bad test."
            show h long
            h "what no its not"
            show a ahh
            a "You've played a visual novel before right? You answer by choosing options on a screen."
            a "There's a good chance whatever you were actually thinking of was one of the options [pronoun[0]] could have picked anyway."
            show a long
            show h long
            h "um i know how visual novels work{w} besides its still like suuuuuper unlikely that [pronoun[0]] would have gotten it right"
            show h long
            h "besides how do we even know thats how it works anyway"
            show a disappoint
            a "Of course that's how it works? You do know how [pronoun[2]] interface functions, right?"
            play music happymeta fadein 3.0
            show i wah -blush -sweat oohh
            iw "UUUUHHHHHHHGGGGGGGGG GUYS COME ON ENOUGH ALREADY"
            iw "WE'RE WASTING TIME DOING NOTHING WE NEED TO BE DOING DEMO STUFF"
            jump polite_argue

            




#------------------------

        label right_dog:
            show h open
            $hardpause(3)
            play music hopeboogie

            if not say_u_played:
                show h laugh
                h "hahahahahahahahahaha{w} ok thats so rad"
                show a ohh
                a "Huh?"
                h "ok so i just had the idea to do this game right"
                show i long -blush -sweat
                h "and [pronoun[0]] probably only could have known that word if i told it to [pronoun[1]] in another timeline{w} and [pronoun[0]] got it right"
                h "so either [pronoun[0]] got super lucky or an alternate version of me just told it to [pronoun[1]]"
            else:
                show h laugh
                h "hahahahahahahahahaha{w} caught red handed"
                show a ohh
                a "Huh?"
                show h smirk
                h "i tricked [pronoun[1]]{w} [pronoun[0]] definitely just lied to us"
                show i long -blush -sweat
                h "[pronoun[0]] got the word i was thinking right{w} so either [pronoun[0]] got super lucky"
                h "or i actually just told [pronoun[1]] the answer in another timeline{w} which i just had the idea to do{w} so alternate me probably did that"
            show h grin
            h "holy crap that was cool"
            show i ohh -blush -sweat
            i "Whoah..."
            show a smirk
            a "Hm, smart move Hope.{w} Now it's almost certain that they HAVE played before..."
            stop music fadeout 10.
            a "[player], if you wouldn't mind, there are some more questions I'd like to ask you..."
            show i open oohh
            i "Wait wait wait wait wait.{w} That's not what we're supposed to be doing!!!"
            show a sad standard
            a "Oh please Isadora stop it with that demo nonsense. What does that even mean anyway?"
            show i wah fists
            iw "WE DON'T HAVE TIME FOR THIS"
            show i inv
            show a laugh
            show h long
            a "But this is a chance of a lifetime!{w} We're essentially talking to a time god!"
            show a sad
            a "[player] obviously these friends of mine aren't interested in utilizing your talents properly."
            show a smile
            menu:
                a "Let's go somewhere else where we can talk without distractions."
                "Ok sure":
                    jump aspen_start
                "No thanks":
                    $aspen_pissed = True
                    jump immortal_aspen_denied


        label immortal_aspen_denied:
            show a sad
            a "Oh."
            show i ehh
            i "At least [player] has SOME sense!"
            if cute == "i":
                h "youre just saying that cuz [pronoun[0]] called u cute"
                show i oohh wah
                iw "NO I'M NOT I'M BEING SERIOUS HERE"
            show a crossed
            a "...{w}I guess that's fine."
            play music happymeta fadein 5
            show i standard
            i "Ok now PLEASE can we DO what we're SUPPOSED to be doing?!!?!"
            jump polite_argue_fake
            
            
            
#-----------------------------

    label immortality_first_time_false:
        show h long
        h "oh{w} i was planning on you saying yes{w} you seemed like a first timer"
        show a long
        a "So [pronoun[0]] definitely know[s_conj] things about our world that we don't."
        show i ehh standard
        i "That's creepy..."
        show i long
        a "Not at all. It's just a fact of life."
        if cute == "c" or tone == -1:
            show c sad
            c "...{w}that's nice, I guess."
        else:
            show c smirk
            c "You probably know my darkest secrets then...haha."
        show h ohh
        h "wait a sec"
        h "ok so i just had the idea of doing like a fun little test thingie"
        menu:
            h "have we done that before"
            "Yeah":
                jump immortality_wordgame_true
            "No":
                jump immortality_wordgame_false

        label immortality_wordgame_true:
            show h smirk
            menu:
                h "did you get it yet"
                "Yup":
                    jump immortality_wordgame_gotrightbefore_true
                "Not yet":
                    jump immortality_wordgame_gotrightbefore_false
        
        label immortality_wordgame_false:
            show h smirk
            h "oh perfect{w} lets play it now then"
            h "so im thinking of a word"
            jump hopegame

        label immortality_wordgame_gotrightbefore_true:
            show h ohh
            h "ok thats creepy{w} and really cool that you know about that"
            show a ahh
            a "Hope what are you talking about?"
            show h smirk
            h "none of your business"
            h "by the way"
            show h grin
            h "woof"
            show i ahh
            i "What?"
            show h owo
            h "nothin"
            show i long
            c "..."
            show a longbig
            a "..."
            play music happymeta fadein 3.0
            show i wah
            iw "UUUUHHHHHHHGGGGGGGGG GUYS COME ON"
            iw "WE'RE WASTING TIME TALKING ABOUT NOTHING WE NEED TO BE DOING DEMO STUFF"
            jump polite_argue



        label immortality_wordgame_gotrightbefore_false:
            $timetraveler = True
            show h owo
            h "ok well guess what"
            show h sad
            h "dog"
            show h happy
            h ";)"
            show a ahh
            a "Hope what are you talking about?"
            h "hey how much you wanna bet that the player is gonna disappear right now"
            show c ehh
            c "What???"
            h "..."
            show h long
            h "oh wait"
            show h disappoint
            h "nvm"
            show i wah
            show c disappoint
            i "?!?!?!?!?!?!?!?!"
            h "my logic got messed up"
            show h sad
            h "man this time overlapping stuff is confusing"
            show a open
            a "Time overlapping? What???"
            show i ehh
            i "Are you time traveling?!?!?!"
            h "no no no"
            show h long
            h "but{w} well"
            show h tongue
            extend " actually yeah kind of{w} i think"
            show h long
            h "its hard to explain"
            show i inv
            show a long
            a "Try me."
            show h owo
            h "eh dont feel like it"
            show a sad
            a "...{w}you're impossible."
            h "thanks"
            a "My pleasure."
            show a ahh
            a "...But really though what's going on?"
            show h long
            h "i said i dont feel like explaining it"
            show c ahh
            c "Hope you have us all curious now."
            show i long
            i "Yeah you kind of have to explain it now."
            h "..."
            show h ahh
            h "alright fine"
            h "but first"
            h "do you know what time it is"
            i "What?"
            python:
                hour = datetime.datetime.now().strftime("%I")
                minute = datetime.datetime.now().strftime("%M")
            show a ahh
            a "It's [hour]:[minute]."
            play music happymeta fadein 5.0
            show h owo
            h "that means its mochi time"
            show i sad standard
            i "Oh come on..."
            show h grin
            h "hey player i hope u like mochi cause ur coming with us{w} deal with it"
            show a sad
            a "..."
            show h ahh
            h "wait a sec"
            menu:
                h "just curious, have you gotten mochi with us before?"
                "Yes":
                    jump immortality_mochi_yes
                "No":
                    jump immortality_mochi_no

        label immortality_mochi_yes:
            show h happy
            h "lmao that must rock{w} so you can get mochi with us over and over and over again"
            show h smile
            h "well have fun this time around"
            show i disappoint
            i "Hope you're making this really weird."
            show h owo
            h "really{w} cool"
            a "..."
            $mochi_from_immortality = True
            jump yep_its_mochi_time

        label immortality_mochi_no:
            show h derp
            h "oh sweet so this will be like ur first time then"
            show h smile
            h "ur gonna like it"
            a "..."
            $mochi_from_immortality = True
            jump yep_its_mochi_time




#-------------------

    label immortality_die_yes:
        show a ohh 
        a "Really?{w} Fascinating..."
        a "So you must already know much about our universe then."
        show a laugh standard
        a "You must be able to predict the future!"
        show i open -sweat
        show h long
        i "What?"
        show c long
        a "So then...if we do not die..."
        menu: 
            a "That must mean we're immortal!"
            "Yes!":
                jump immortality_immortal_yes
            "What? No!":
                jump immortality_immortal_no

#-------------------------    

    label immortality_immortal_yes:
        play music immortality
        show n smirk
        n "Heh."
        show n line
        show a open at hop()
        a "Incredible!"
        show i wah
        iw "WHAT?!?! We live FOREVER??"
        show c laugh
        c "Wow!"
        show h ahh
        h "nari did you say something"
        n "No."
        show h long
        h "oh ok"
        show i disappoint
        i "But how does that make sense? I know people who have died..."
        show a laugh
        a "I guess [player] means that WE are immortal. Us five!"
        show c open
        c "Really?"
        show i ehh fists
        i "So...we're never going to die?"
        show a inv think
        a "Or hmm....maybe it means everyone who is alive right now will never die..."
        show i wah 
        iw "ARE YOU SERIOUS I'M NEVER GONNA DIE?!?!"
        if tone == -1:
            show c sad
            c "Are you sure [player] isn't messing with us again?"
        else:
            show c ohh
            c "That's some...big news..."
        show a ahh
        a "Just to clarify - "
        menu: 
            a "So everyone alive right now is immortal? We're never ever going to die?"
            "Yep! I can guarantee that you will all never die!":
                $tone = 0
                jump immortality_immortal_very_yes
            "No I was just messing with you. I have no idea if you're immortal.":
                $tone = -1
                jump immortality_immortal_kidding


    label immortality_immortal_very_yes:
        show i omg
        iw "AHHHHHH WHAT?!?!?!!"
        show c open
        c "...wow..."
        show i standard sicko
        show h derp
        h "omg thats sick{w} theres so much more stuff i can do to myself now"
        h "i can eat all the mochi i want and not worry about heart disease this is awesome"
        show a crossed disappoint
        a "Were you...ever worried about heart disease?"
        h "lmao not really"
        show h tongue
        h "but i mean maybe now i can finally get over my fear of heights and do some edgy sports stuff or something"
        h "heck i dont have to worry about stds or cancer or anything now this rocks"
        show c disappoint
        c "Um..."
        show h owo
        h "hey do you think if we let all our blood drain out could we become actual vampires"
        show c sad
        c "Hope please don't do that."
        show h tongue
        h "why not"
        stop music
        n "[Pronoun[0]] [is_conj] lying to you."
        show c ahh
        show i ahh
        show a ahh
        show h ahh
        $hardpause(5)
        a "What was that?"
        n "We are not immortal."
        i "..."
        a "..."
        c "..."
        show h long
        h "how do u know"
        n "...{w}..{w}.."
        $hardpause(4)
        show c long
        c "Uh, Nari?..."
        n "...{w}hey, Hope."
        h "what"
        n "Let's go get mochi."
        h "okay"
        n "[player].{w} Come with us."
        show n line at move(1.5, 2)
        show h long at move(1.5, 7)
        menu:
            "{i}Go with Nari.{/i}":
                jump nari_start
            "{i}Stay here.{/i}":
                jump immortality_leave_Nari

        label immortality_leave_Nari:
            show n line at move(3.0, 0.0, 0.0, 1.5, 500) zorder 10
            show n line at move(0.8, 0.5, 0.0, 1.5, 500) 
                # zoom 2
                # yalign 1000
            n "Sorry you don't get a choice in this."
            show i at hop
            i "Whoah Nari! Don't-!"
            show a standard wah
            a "We can touch [pronoun[1]]?!"
            n "Come."
            show n line at move(5.0, 0.5, 0.0, 1.5, 500) 
            $hardpause(0.5)
            jump nari_start



#----------------------

    label immortality_immortal_kidding:
        stop music
        show a disappoint
        a "...really?"
        show i long
        i "Oh."
        show c sicko
        c "...hahaha...{w}very funny..."
        show a sad crossed
        a "Um, no?{w} There was nothing funny about that."
        show a open
        a "That's not something you joke about!"
        a "Why would you tell us all that?"
        show a inv
        show c disappoint
        c "I mean, [pronoun[0]] can kind of say whatever [pronoun[0]] wants to us, right?"
        c "Besides, [pronoun[0]] didn't say that we're NOT immortal."
        show a disappoint
        a "...[pronoun[0]] didn't, did [pronoun[0]]"
        show i -sweat
        jump polite_isadora_death_outburst


    label immortality_immortal_no:
        show i long
        show a ehh
        a "Wait, so we ARE going to die?"
        show c open
        c "Aspen stop grilling [pronoun[1]] so hard."
        show a sad
        a "Chris, this is essential information.{w} I think knowing whether or not we're immortal is pretty important!"
        show c sad
        c "But you're just confusing [pronoun[1]] with different versions of the same question.{w} I don't think [pronoun[0]] even meant much in what [pronoun[0]] originally said."
        a "Chris, normally I wouldn't have taken what [player] said into much consideration."
        a "However we're talking about the {i}PLAYER{/i} here. They know much more about our world than we do."
        a "They have the power to go back in time and relive alternate versions of ourselves, making different choices."
        a "If they say that we will or will not die, I think we should be taking that pretty seriously."
        show c ahh
        c "But we were just kidding around. It wasn't a serious conversation."
        show a long
        a "Um, saying \"None of you are going to die\" is pretty serious in my book if it's said by someone who comes from outside our world."
        show c disappoint
        c "[player] was just trying to make Izzy feel better."
        show a disappoint
        a "...{w}I wouldn't be so sure."
        jump polite_isadora_death_outburst

