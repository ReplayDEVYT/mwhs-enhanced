label noname_polite:
    ## c: 0.4
    ## a: 0.8
    $default_player_name = True;
    c "Um, alright! That's okay...I guess?"
    show c long
    extend " But we should call you something..."
    c "..."
    show c happy
    c "Uh...{w}how about Mr. Player?"
    show a crossed sad
    a "That's a horrible name.{w} Also how do you know they're a dude?"
    show c disappoint
    c "...he's not?"
    a "...{w}do they feel kind of blurry to you too?"
    show c long
    c "Kind of? They feel...{w}uh...{w}big?"
    a "Yeah, I don't know..."
    show c ahh
    c "I know what you mean..."
    show a ahh
    show c long
    menu:
        a "...uh, what pronoun do you go by? I use \"they/them\" pronouns."  
        "He/Him": 
            $pronoun = pronoun_he
            $Pronoun = Pronoun_he
            $is_conj = is_conj_heshe
            $s_conj = verb_conj_heshe
            $player = "Mr. Player"
            $persistent.pronoun_list.append("he")
            jump no_name_he
        "She/Her":
            $pronoun = pronoun_she
            $Pronoun = Pronoun_she
            $is_conj = is_conj_heshe
            $s_conj = verb_conj_heshe
            $player = "Ms. Player"
            $persistent.pronoun_list.append("she")
            jump no_name_she
        "They/Them":
            $pronoun = pronoun_they
            $Pronoun = Pronoun_they
            $is_conj = is_conj_they
            $s_conj = verb_conj_they
            $persistent.pronoun_list.append("they")
            $player = "Tim"
            jump no_name_they

#----

    label no_name_he:
        show a long
        show c happy
        c "Ah, Ok! So we'll call you Mr. Player then!"
        show a sad
        a "That's still a horrible name."
        show c long
        c "But that's what he is...right? The player?"
        show a ahh
        a "That's like calling a dog \"Mr. Dog\". He's not a dog."
        show a standard long
        menu: 
            a "Don't tell me you actually want to be called Mr. Player?"
            "That's fine with me!":
                jump mr_ok
            "Please call me something else, I don't care what.":
                jump choosename
            "Actually I changed my mind, let me just tell you my name.":
                jump changedmind

    label mr_ok:
        $player_name_is_a_name = False
        show a long
        show c happy
        c "See? They like it!"
        show a disappoint
        a "I...{w}well alright then.{w} If you're fine with it I guess I am too."
        show c smile
        c "Oh come on, it's cute!"
        show a sad
        a "I wouldn't describe it as such, but if you say so."
        show c ahh
        c "Now now, Mr. Player has the right to be called whatever he wants to be{nw}"
        jump polite_isadora_enter

#----

    label no_name_she:
        show a standard happy
        a "Ah Ha! I was right!"
        show a smile
        show c smile
        c "So, then...we'll call you Ms. Player?"
        show a crossed long
        a "That's such a horrible name."
        show c smirk
        c "I think it's cute!"
        show a disappoint
        a "It's the opposite of cute. I feel like I'm talking to a fish."
        show a standard
        a "Hold on, how do you know she isn't married?"
        show c ahh
        c "What?"
        show c disappoint
        extend " Oh, right, Ms. vs. Mrs..."
        show a ahh
        menu:
            a "Hey, are you married?"
            "Yeah":
                $married = True
                $player = "Mrs. Player"
                $player_name_is_a_name = False
                jump married_true
            "No":
                jump married_false
            "None of your business":
                jump married_unknown
            "Please call me something else, I don't care what.":
                jump choosename
            "Actually I changed my mind, let me just tell you my name.":
                jump changedmind

    label married_true:
        show a ohh
        a "Oh, wow."
        show c laugh
        c "Ok! So we'll call you Mrs. Player then!"
        show c smile
        show a crossed long
        a "I have to be honest, I wasn't expecting you to be married."
        show c ahh
        c "Huh? Why?"
        show c long
        a "...{w}no reason."
        show c disappoint
        c "Oh come on, I know you better than that. You definitely have a reason."
        show a disappoint
        a "I just...wasn't expecting someone who's married to be playing our game, you know?"
        show c ahh
        c "Huh? Why not?"
        show a long
        a "...{w}well aren't we a da{nw}"
        jump polite_isadora_enter

    label married_false:
        $player_name_is_a_name = False
        show c laugh
        c "Alright! We'll call you Ms. Player then."
        show a pout
        a "That's still a horrible name."
        show c ahh
        c "But that's what she is...right? The player?"
        show a crossed
        a "That's like calling a cat \"Ms. Cat\". She's not a cat."
        show c happy
        c "I think it's cute!"
        a "It's the opposite of cute."
        show c smile
        c "Well she seems to be fine with it, so I think it's alright!"
        show a long
        a "...{w}I suppose I can't complai{nw}"
        jump polite_isadora_enter


    label married_unknown:
        $player_name_is_a_name = False
        show a long
        a "Oh."
        show c smile
        c "Uh, wow, you really are a secretive person!"
        show a crossed disappoint
        a "I suppose you can never be too safe this day in age."
        show a smirk
        a "I mean not that we are, but for all you know we could be some sort of virus or malware. We could totally steal your info if we wanted."
        show a smirk
        a "Ha, \"MalWare High School\".{w} Think it exists?"
        show c ohh
        c "Oo, Maybe! That'd be pretty mean but also pretty cool!"
        a "Yeah, a visual novel stealing your info for dirty secrets would be groovy."
        c "I wonder if one already exists{nw}"
        jump polite_isadora_enter

#----
    label no_name_they:
        show a standard smile
        a "Ok great!"
        show c think
        c "Hm, I don't know if calling you Mr. Player would be appropriate..."
        show a crossed disappoint
        a "That's a horrible name, please let's not call them that."
        c "Yeah, we should think of something else..."
        c "..."
        show c ohh at hop()
        c "Ohhh! I know!"
        show c happy
        c "How about Tim?"
        show a inv
        a "...{w}really?{w} Tim?"
        c "Yeah!"
        a "...Tim isn't really gender neutral."
        show c smile
        c "But it's a good name, isn't it? I think they feel like a Tim."
        a "What does a Tim feel like."
        show c long
        c "You know...{w}like a Tim."
        a "..."
        show a ahh
        menu:
            a "Are you alright with this?"
            "Tim is fine!":
                jump tim_ok
            "Please call me something else, I don't care what.":
                jump choosename
            "Actually I changed my mind, let me just tell you my name.":
                jump changedmind


    label tim_ok:
        $player_name_is_a_name = True
        show c smile
        c "Ok! We'll call you Tim."
        show c laugh
        c "Thanks for letting us name you!"
        show c smile
        show a inv
        a "More like thanks for letting Chris name you. I would have given you a much better name."
        show c sad
        c "Oh get a grip, it doesn't really matter all that much anyway."
        show a ehh
        a "A name doesn't matter? But it's your {i}name!{/i} It has to be right!"
        show c disappoint
        c "I'm not sure you can have a \"right\" name..."
        show a inv
        a "What are you talking about? Some names are definitely better than others!"
        show c long
        c "Aspen you've just insulted all of the Tims in the world."
        show a morty
        a "I don't care."
        c "Do you know how many people that is?"
        a "No."
        show c line
        c "...{w}Me neither.{w} But it's probably a lot."
        c "Aspen you just insulted like probably over a thousand people."
        show a long
        a "I'd bet you that it's more than that{nw}"
        jump polite_isadora_enter

#-----------------
 
    label choosename:
        $player = "Charlie"
        $player_name_is_a_name = True
        show a open
        a "See, I told you that was a horrible name!"
        show c disappoint
        c "Ok ok ok, well hm...{w}what should we call you..."
        show a inv
        a "No, you've lost your naming privileges. I'm going to think of the name."
        show c smile
        c "Fine with me!"
        show a think long
        a "Hm..."
        a "..."
        a "....."
        a "......."
        a "........."
        show c long
        c "...{w}You okay?"
        show a standard ahh
        a "Thinking of a name takes time, be patient!"
        show a think long
        show c disappoint
        c "Just pick something, it doesn't really matter..."
        show a ehh
        a "Of course it matters! It's a name!"
        show a crossed long
        a "Okay I thought of a good name."
        show a smile
        a "Charlie."
        show c long
        c "Um, that works."
        show c disappoint
        c "But do they feel like a Charlie?"
        show a standard ehh
        a "What?{w} Sure!"
        show a inv
        a "But Charlie is certainly a lot better than what you came up with!"
        show c long
        c "Oh come now, my name wasn't that bad{nw}"
        jump polite_isadora_enter


    label changedmind:
        c "Oh! Alright then..."
        a "Yeah good call. Terrible name."
        c "So what should we call you?"
        jump inputname
            
