label hope_intro:
    show h owo
    h "or whats her name and i can go somewhere and make out im fine with either"
    show c sad
    c "Ok let's NOT do the second thing you just said."
    show h smirk
    h "what u jealous"
    show c ahh
    c "Hope we were just discussing how this isn't a dating sim."
    show h long
    h "what so the player and i cant do what we want then"
    h "whats this game rated anyway"
    show h tongue
    extend " if I got naked in front of [pronoun[1]] would my vagina get all pixelated"
    show a smirk
    a "Pffft I'm actually kinda curious about that now."
    show h owo
    h "we should find out"
    show c open
    c "NO WE SHOULD NOT"
    show i open
    i "AGREED"
    show c long
    show i long
    show h derp
    h "lmao did you think i was just gonna get naked right here"
    show i longbig
    i "You've done worse."
    show h smirk
    h "touché"
    show h smile
    menu: 
        h "anyway whatsyourname how about we ditch everyone and go hang out somewhere other than here"
        "Sure":
            jump hope_start
        "No thanks":
            jump hope_rejected

    label hope_rejected:
        show h sad
        h "lame"
        show h smile
        menu: 
            h "well u wanna get mochi instead"
            "Okay":
                jump Mochi_time
            "No":
                jump no_moochi_start
    
label hope_start:
    stop music fadeout 1
    show h derp
    h "Oh yeeeessss lets gooooo"
    h "you just unlocked the super special secret hope route babyyyyy congrats"
    show h smile
    h "come on lets get out of here"
    show i ahh
    c "Um, wait, you're going to take the player away from everyone?"
    show h derp
    h "nope"
    show h long
    extend " i mean yep"
    show h derp
    extend " but nope you cant come with us{w} [pronoun[5]] all mine now [pronoun[0]] said so"
    show c open
    c "You can't do that!"
    show h derp
    h "yes i can"
    show c sad
    show h smile
    h "come on u lets go"
    n "Can I come."
    show h long
    h "oh{w} uh {w}sorry nari the player and i are gonna have some alone time{w} nothing personal promise"
    show c open
    c "Hope, this is really going too far!"
    show h smirk
    h "yep were gonna go far alright"
    show h derp
    h "ok time to go before they take you away come come come"


    scene bg school_flipped with pushleft
        
    show h derp at enterleft(0.5, 2.0)
    h "oh boy here we are"
    show h long
    h "...{w}why is it the same but backwards"
    show h owo
    h "whatever now we can hang out for real"
    play music hopeboogie fadein 5.0
    show h derp
    h "hahahahaha did you see their faces{w} they totally thought we were gonna bang"
    show h smile
    h "oh i dont actually want to do anything like that right now{w} sorry if i got your hopes up"
    show h tongue
    h "heheheheh yes the pun was intentional"
    show h smile
    h "but yeah sorry im not in the mood for anything sexual right now"
    h "plus like i do want to actually get to know you and stuff before we do anything too hardcore"
    h "being the player is cool all but{w} well you know{w} just cuz ur the player doesnt mean you get a free bang who you want card"
    show h long
    h "to be honest i wouldnt even know where to start{w} ur kind of{w} uh{w} indescribably different"
    show h disappoint
    h "like do u even have genitals{w} or lips{w} or a face{w} i think you do but im not one hundred percent sure tbh"
    show h smirk
    h "anyway idk how long youll be around but id totally be down to experiment later if ur up for it"
    show h long
    h "just{w} maybe not in public ok"
    h "..."
    h "uh"
    show h owo
    menu:
        h "so what do u wanna do"
        "Why do you hang out with those people?":
            jump hope_hangout
        "For real, why dont you have eyes?":
            jump hope_eyes
        "Do you have a ton of sex?":
            jump hope_sex
        "Tell me about Nari.":
            jump hope_aboutnari

label hope_hangout:
    $hope_questions_show[0] = False
    show h derp
    h "hahaha what{w} why do i hang out with them"
    h "cuz theyre fun thats why{w} theyre all nuts theyre great"
    show h smile
    h "weve been hanging out for forever{w} like uh{w} literally forever{w} were super duper tight"
    h "always the same spot after school{w} right under the big tree outside the high school"
    h "i mean its really that simple{w} what else is there to say{w} you have a problem with who i hang out with or something"
    show h tongue
    h "lol just messing with you"
    show h smile
    h "we have our moments but we really do help each other out when the shit goes down"
    show h disappoint
    h "ill uh{w} spare u the history"
    show h owo
    if not check_hope_questions(hope_questions_show):
            jump hope_asktime
    menu:
        h "what else is on ur mind"
        "Why do you hang out with those people?" if hope_questions_show[0]:
            jump hope_hangout
        "For real, why dont you have eyes?"if hope_questions_show[1]:
            jump hope_eyes
        "Do you have a ton of sex?" if hope_questions_show[2]:
            jump hope_sex
        "Tell me about Nari." if hope_questions_show[3]:
            jump hope_aboutnari

###---------

label hope_eyes:
    $hope_questions_show[1] = False
    show h long
    h "what"
    h "what are \"i\"s"
    menu:
        h "seriously what are these things"
        "You use them to see":
            jump hope_eyes_see
        "They're these round fleshy balls in your face that you use to look at the world":
            jump hope_eyes_balls

    label hope_eyes_see:
        show h disappoint
        h "you use them to what now{w} to sea"
        h "are you like a water bender from avatar or something{w} can you control water with your \"i\"s"
        menu:
            h "is that how it works"
            "No we aren't water benders":
                jump hope_eyes_notbender
            "Actually you're not too far off. Eyes can produce water. It's called crying. But you only do it when you're sad.":
                jump hope_eyes_water

        label hope_eyes_water:
            h "so you can waterbend but you can only do it when youre sad"
            show h long
            h "what planet do you come from again{w} that is seriously messed up"
            h "like why would you have a power like that if you can only use it if ur sad"
            h "like imagine if the hulk could only get big and strong when he was sad{w} that would be so useless"
            show h smirk
            h "lmao i bet theres a fanfic out there where thats a thing{w} if there isnt hey give me a cut of the royalties when it becomes a hit alright"
            jump hope_eyes_anyway

        label hope_eyes_notbender:
            show h disappoint
            h "oh well that sucks"
            h "but what does it mean to sea then i dont get it"
            h "is it like swimming or something{w} oh whatever i dont care"
            h "there arent any oceans or lakes around here so dont expect to do any swimming anytime soon"
            h "unless you want to go to the hot springs on a weekend or something"
            show h smirk
            h "hey if u wanna sea we can go there im down{w} the others might get a little weird about it being naked and all that but idc"
            jump hope_eyes_anyway
    
    label hope_eyes_balls:
        $testical_face = True
        show h sad
        h "excuse me{w} that sounds disgusting"
        h "round fleshy balls huh{w} and theyre in your face"
        show h long
        h "ok well i know your nickname now"
        show h longbig
        h "testicle face{w} because you obviously have testicles in your face{w} i mean round fleshy balls what else is that going to be"
        h "and theyre IN your face{w} oh god that is so gross{w} how are you not grossed out all the time by these things"
        menu:
            h "or are you pulling my leg right now"
            "It's not disgusting. So are you blind?":
                jump hope_eyes_blind
            "No I'm completely serious. They're super slimy too":
                jump hope_eyes_slimy
        
        label hope_eyes_blind:
            $film_buddies = True
            show h disappoint
            h "why do you keep using these words ive never heard of"
            h "am i what now{w} bind"
            show h longbig
            h "also how is having testicles in ur face not disgusting what the heck"
            show h long
            h "it must take a lot to gross u out huh"
            show h owo
            h "well good for me cuz if ur around for long enough we should totally listen to some sick horror podcasts{w} nobody else will listen to them with me"
            show h derp
            h "we can be podcast buddies{w} omg im so excited about this now"
            if not check_hope_questions(hope_questions_show):
                jump hope_asktime
            else:
                jump hope_testicalface
        
        label hope_eyes_slimy:
            show h sad
            h "ok ur gross"
            h "im done{w} ur face is super gross"
            if not check_hope_questions(hope_questions_show):
                show h longbig
                h "actually u know what{w} ur so gross u lost your privilege to ask questions"
                h "sorry{w} question time over"
                jump hope_asktime
        label hope_testicalface:
            menu: 
                h "lets talk about something else testicle face"
                "Why do you hang out with those people?" if hope_questions_show[0]:
                    jump hope_hangout
                "For real, why dont you have eyes?"if hope_questions_show[1]:
                    jump hope_eyes
                "Do you have a ton of sex?" if hope_questions_show[2]:
                    jump hope_sex
                "Tell me about Nari." if hope_questions_show[3]:
                    jump hope_aboutnari


    label hope_eyes_anyway:
        if not check_hope_questions(hope_questions_show):
            jump hope_asktime
        menu:
            h "anyway"
            "Why do you hang out with those people?" if hope_questions_show[0]:
                jump hope_hangout
            "For real, why dont you have eyes?"if hope_questions_show[1]:
                jump hope_eyes
            "Do you have a ton of sex?" if hope_questions_show[2]:
                jump hope_sex
            "Tell me about Nari." if hope_questions_show[3]:
                jump hope_aboutnari



###---------
label hope_sex:
    $hope_questions_show[2] = False
    show h long
    h "..."
    $renpy.music.set_pause(True)
    h "no"
    $renpy.music.set_pause(False)
    show h owo
    if not check_hope_questions(hope_questions_show):
            jump hope_asktime
    menu:
        h "what else u wanna talk about"
        "Why do you hang out with those people?" if hope_questions_show[0]:
            jump hope_hangout
        "For real, why dont you have eyes?"if hope_questions_show[1]:
            jump hope_eyes
        "Do you have a ton of sex?" if hope_questions_show[2]:
            jump hope_sex
        "Tell me about Nari." if hope_questions_show[3]:
            jump hope_aboutnari
    


###---------


label hope_aboutnari:
    $hope_questions_show[3] = False
    stop music fadeout 1.0
    show h long
    h "u wanna know about nari huh"
    h "yeah that makes sense she doesnt really talk in public much"
    h "she opens up a little when its just her and me though"
    h "or{w} well"
    show h disappoint
    h "...{w}she used to"
    show h long
    $hardpause(2)
    play music naristorytime
    h "tbh im kinda worried about her{w} shes kinda been drifting lately"
    h "she still hangs out with us{w} but even when its just us two its been harder to get her to say anything"
    h "we go back pretty far{w} she used to be a lot more open"
    h "super smart actually{w} like she doesnt show it but shes waaaay smarter than i am"
    show h smirk
    h "i think shes the smartest person in the gang"
    show h long
    h "she used to like live in the library{w} just on her computer all the time{w} or with a podcast and the computer{w} it was hard to get her to get out of there"
    h "but i dont think shes been to the library at all lately{w} not unless we go as a group"
    h "she just{w} kinda goes home now after the gang hangs"
    show h disappoint
    h "..."
    h "some of the stuff shes been doing lately has been kinda weirding me out"
    h "she had a thing recently where she collected weapons"
    h "not like guns or anything but like knives and razors and weird tools"
    show h long
    h "some of them were super fancy too like super elaborate and stuff"
    h "she never struck me as the violent type{w} not even the self harm type"
    h "like dont get the wrong idea but ive seen her body and shes never had a scratch on her anywhere{w} like{w} never"
    h "i think she just liked collecting them{w} i have no idea why{w} she wouldnt tell me"
    h "..."
    h "u know how she asked to come with us just now"
    h "shes kinda gotten into the habit of going where i go for the most part"
    h "im the only person she talks to really so i can see why"
    h "but i havent been able to get her to talk much at all lately"
    show h disappoint
    h "not like how we used to"
    h "anything she says now is just{w} she only says if she absolutely has to i think"
    h "..."
    show h long
    h "what do u think{w} ur the player so maybe youve met her in some other timeline idk"
    menu:
        h "u have any advice"
        "Sounds like she's going through some hard stuff right now. Just stay supportive of her.":
            jump hope_nari_supportive
        "I have no idea what her deal is.":
            jump hope_nari_noidea
        "She hates you." if persistent.nari_ending:
            jump hope_nari_hates

    label hope_nari_supportive:
        show h disappoint
        h "hm{w} yeah i guess so"
        h "i mean its really hard though idk what i can do for her or how to help"
        stop music fadeout 3.0
        show h long
        h "well{w} ok there is one thing"
        h "..."
        play music hopeboogie fadein 5.0
        show h smirk
        h "did i mention she likes gummy bears"
        h "shes like super obsessed over gummy bears"
        h "not gummy worms{w} not gummy candies{w} no they specifically have to be in a bear shape otherwise its worthless"
        show h long
        h "u know how scooby doo will do anything for a scooby snack"
        show h smile
        h "yeah thats nari and gummy bears"
        show h owo
        extend " but times ten"
        h "she will do anything for a gummy bear"
        h "like i tested this one time to see how far she would go and oh my god i think she will really do anything{w} her wild side comes out for gummy bears"
        h "once i dared her to..."
        show h long
        extend "uh"
        h "you know what nvm that feels like a breach of privacy ill tell u if she okays it later"

    label hope_nari_end:
        show h smile
        if not check_hope_questions(hope_questions_show):
            jump hope_asktime
        menu:
            h "anyway enough about nari u wanna know anything else about my weird life"
            "Why do you hang out with those people?" if hope_questions_show[0]:
                jump hope_hangout
            "For real, why dont you have eyes?"if hope_questions_show[1]:
                jump hope_eyes
            "Do you have a ton of sex?" if hope_questions_show[2]:
                jump hope_sex


    label hope_nari_noidea:
        show h disappoint
        h "yeah i have no idea either"
        show h sad
        h "man i was hoping you might have some advice or something{w} but yeah i gotta figure this out myself i guess"
        h "or uh{w} she does{w} i dont know{w} i dont know whats going on"
        h "i wish there was some way i could help with whatever shes going through right now but i kinda have no idea what that is"
        h "i mean if i had to guess..."
        h "..."
        show h long
        h "you know there was this one time i listened to one of her podcasts"
        h "the author was something complicated{w} german maybe idk"
        h "a lot of the stuff she likes to listen to is really technical and computery i stay away from that stuff{w} but this one was kinda different so i listened to a few chapters"
        h "i didnt really understand most of it it was still pretty technical{w} but the stuff i did get was...{w}kind of spooky"
        h "it had a really weird tone{w} like it was going into specifics about how artificial we are and how our brains are wired and stuff about the RenPy game engine"
        show h disappoint
        h "but the way it was talking about it was really weird{w} it made me uncomfortable"
        h "i asked her about it later and she got kinda mad at me"
        stop music fadeout 5.0
        h "..."
        show h long
        h "i forgot why i brought that up"
        play music hopeboogie fadein 5.0
        jump hope_nari_end


label hope_asktime:
    show h smile
    h "okay now its my turn"
    h "i have a question i really want to ask"
    show h long
    h "..."
    show h smirk
    h "um{w} sorry its kind of an embarrassing question"
    show h long
    h "i normally wouldnt ask anyone something like this but...{w}ur the player and i thought there might be a chance you know"
    show h smile
    h "so like{w} i dont know if youve played other games or visual novels or anything but in our universe when we play stuff like that were pretty separate from the game we play"
    h "like what happens to you in the game doesnt happen to you in real life right"
    h "well uh i was wondering if that was maybe different for you since you know{w} youre not from around here{w} and maybe since you come from out there it maybe works differently"
    h "cause i mean you seem pretty integrated into our world and stuff so..."
    show h long
    h "..."
    h "..."
    $hardpause(2)
    stop music
    show h ahh
    h "have you died before?"
    show h long
    menu:
        "Yes":
            jump hope_died_yes
        "No":
            jump hope_dies_no
        "Huh?":
            jump hope_die_huh
    
    label hope_die_huh:
        show h ahh
        h "oh sorry maybe its a confusing question uh"
        h "so you know like in mario you have multiple lives right"
        show h long
        h "well uh{w} theres nothing like that here{w} when you die thats it{w} ur gone"
        h "but i was wondering if youve played a game that has multiple lives"
        h "and if youve died"
        h "like{w} actually died"
        h "for real"
        h "so{w} uh{w} have you"
        menu:
            "Yes":
                jump hope_died_yes
            "No":
                jump hope_dies_no


    label hope_dies_no:
        show h long
        h "oh"
        h "..."
        h "so i guess it works the same way as it does here huh"
        h "well it was worth a shot"
        show h smile
        h "forget i asked"
        show h long
        h "..."
        h "well now what"
        $hardpause(3)
        show h derp
        h "oh{w} oh oh oh{w} i have an idea"

    label hope_mochi_time:  
        show note_falling at note_falling zorder 20
        play music endmusic
        h "lets go get mochi"
        show h sad
        h "wait what the heck is it raining paper"
        h "what is this"
        show h long
        h "..."
        h "oh"
        show h ahh
        h "oh wow"
        h "hey check this out"

        $EndMessage[-1] = "P.S.: Sorry, no time for mochi. [player] has other places to be!"

        show screen Final_Note(EndMessage, True)
        pause 15

        h "lmao other places to be"
        h "well i suppose so{w} you have like a whole other life right"
        h "yeah get out there and get some sun{w} stop being such a cave in playing video games lmao"
        h "get out of here{w} it was nice meeting you"
        h "i guess i wont see you again but i guess another version of me might{w} say hi for me lmao"
        h "oh wait hold on dont go yet theres more"

        hide screen Final_Note
        $EndingComplete("Hope")
        show screen Final_Note(EndMessageMeet, False)
        pause 2

        h "um"
        h "..."
        stop music
        h "oh shit"
        h "oh shit oh shit oh shit oh shit"
        h "youre about to talk to her arent you"
        h "is she here{w} tell me right now is she anywhere around here{nw}"
        hide screen Final_Note
        jump nariend_hope_default

    label hope_died_yes:
        $persistent.saidhavedied_yes = True
        $hardpause(5)
        h "..."
        h "did it hurt"
        menu:
            "Yes":
                jump hope_hurt_yes
            "No":
                jump hope_hurt_no

    label hope_hurt_no:
        show h ahh
        h "Oh thank god."
        show h long
        $hardpause(3)
        h "You have no idea how much of a relief it is to hear that."
        h "..."
        h "hey"
        h "do you know what time it is"
        h "dont answer"
        h "i know you know what time it is"
        h "because the current time"
        show h owo
        h "is mochi time"
        jump hope_mochi_time


    label hope_hurt_yes:
        $hardpause(6)
        h "{cps=10}a lot?"
        menu:
            "Yes":
                jump hope_hurt_alot_yes
            "No":
                jump hope_hurt_no
        
    label hope_hurt_alot_yes:
        $persistent.saiddyinghurts = True
        $hardpause(10)
        h "{cps=10}oh god"
        $hardpause(5)
        show note_falling at note_falling zorder 20
        play music endmusic
        $hardpause(5)
        h "..."
        h "......"
        $EndMessage[-1] = ""
        show screen Final_Note(EndMessage, True)
        pause 15
        h "{cps=10}..."
        hide screen Final_Note
        $EndingComplete("Hope")
        show screen Final_Note(EndMessageMeet, False)
        pause 2
        h "{cps=10}oh god"
        hide screen Final_Note
        jump nariend_hope_hell        
    

##---------
##Oh shit stuff gonna go down now


label hope_nari_hates:
    $persistent.saidnarihates = True
    stop music
    $hardpause(4)
    show h long
    h "what"
    menu:
        h "did she tell you this"
        "Yes":
            jump hope_nari_hates_yes

label hope_nari_hates_yes:
    menu:
        h "when"
        "At the end of a runthrough":
            jump hope_nari_hates_yes2


label hope_nari_hates_yes2:
    menu:
        "She said she hated everyone":
            jump hope_nari_hates_yes3


label hope_nari_hates_yes3:
    menu:
        "Well, she hates me most.":
            jump hope_nari_hates_yes4


label hope_nari_hates_yes4:
    menu:
        "But yeah, she said you were ignorant.":
            jump hope_nari_hates_yes5

label hope_nari_hates_yes5:
    menu:
        "And that she hated all her friends.":
            jump hope_nari_hates_yes6

label hope_nari_hates_yes6:
    menu:
        "And that none of you should have ever been created.":
            jump hope_nari_hates_yes7

label hope_nari_hates_yes7:
    $hardpause(4)
    h "..."
    h "wow"
    h "not gonna lie that does sound like nari"
    h "but wow"
    h "shes never told me anything that intense"
    $hardpause(4)
    h "so she{w} must hate me too{w} if she said it like that"
    h "and im kind of her only friend really"
    h "so"
    h "..."
    h "....."
    h "i"
    $hardpause(3)
    h "i dont know how to respond to that"
    $hardpause(3)
    h "..."
    show h sad
    h "god dammit you rascal"
    h "..."
    show h sicko
    h "{i}*sniff*{/i}"
    h "sorry uh"
    $hardpause(4)
    h "..."
    show h sad
    h "this isnt going as i planned"
    h "..."
    $hardpause(2)
    show h sicko at move(-0.5, 3.0)
    h "go uh...idk i need to go sorry"
    $hardpause(8)
    show note_falling at note_falling zorder 20
    play music endmusic
    $hardpause(5)
    $EndMessage[-1] = "P.S. Hope now hates you too."
    show screen Final_Note(EndMessage, True)
    $EndingComplete("Hope")
    pause 12
    hide screen Final_Note
    jump nariend_hope_hate