
# """
# trailer

# Generic fun music. Logo swings by.

# "MetaWare High School. A free Visual Novel Demo by Not Fun Games."

# (shows different shots of in-game fottege)

# c "Welcome to MetaWare High School (Demo)! I'm so happy you're here!"

label trailer:
    scene bg school
    $quick_menu = True
    "Introducing a brand new visual novel!"
    show c laugh at move(0.5, 0.0)
    show i long at move(0.0, 0.0)
    c "Welcome to MetaWare High School (Demo)! I'm so happy you're here!"


    # Text flies by: Meaningful Choices!
    show i angry at move(1.0, 0.0)
    show c smile at move(0.4, 0.0)
    show a think ahh at move(0.0, 0.0)
    a "Does anything feel off to you guys? Something feels weird..."
    show a sad
    menu:
        "I love you! Let's get married!":
            pass
        "I hate you! I hope you fail math class!":
            pass

    show i omg:
        move(0.5, 0.0)
        shake(30)
    show h long at move (-0.1, 0.0)
    show a standard disappoint at move(0.9, 0.0)
    show c ahh surprised at move(0.2, 0.0)
    i "WE KEEP CHANGING PLACES WHAT THE HECK IS GOING ON?!?!?!??!!"


# Text flies by: Multiple Endings!
# 


    c "pass"


# (single character montage)

# CHRIS: Always at Your Service
# "Um...where did everyone go?"

# ASPEN: Agent of Chaos
# "Are we...in a trailer?" 

# ISADORA: Filled with Determination
# "THIS IS WAY TOO FAST I'M GONNA THROW UP"

# HOPE: The Spunky Rebel
# "yus im animated watch me goooooooooooooo"

# NARI: Searching for the Truth
# "This game will maliciously attempt to reset your harddrive to factory settings, erase all system data, and corrupt your BIOS files. Do not download this game under any"

# logo pops in.

# Download now!

# Not Fun Games Logo fades in and out on screen.

# """


label test:

    image green = "#008000"

    scene green
    show c inv at move (-0.08, 0.8) zorder 3
    show a ooh at move(0.2, 0.8) zorder 4
    show h owo at enterright(0.8, 1.5) zorder 2
    show i wah at move(0.5, 0.8) zorder 5
    show n owo at move(1.1, 4)

    pause 999999

    return


label screenshots:

    scene bg school
    $quick_menu = True

    show c long at move (-0.08, 0.8) zorder 6
    show a long standard at move(0.6, 0.8) zorder 4
    show i ahh oohh at move(0.25, 0.8) zorder 5
    show h long at enterright(1.0, 1.5) zorder 2
    
    i "Hey! Where did all the sound go?"
    show i disappoint fists
    show a disappoint crossed
    a "Yep. We're definitely inside the itch.io store page right now."
    show c ooh surprised at move (-0.1)
    show h owo
    c "So many colors..."
    show c smile standard
    show i crossed wah sweat
    i "I DON'T LIKE THIS THIS FEELS WEIRD"
    show a dance open
    show i sicko
    a "Quick! Everyone strike a pose! We gotta sell the game!"
    show a dance closed
    show h smirk at move(1.2, 0)
    h "ok then im gonna take one for the team and take off my shirt brb"
    hide h
    show c ehh sweat surprised  at move(0.9)
    show a standard sad
    show i -sweat sad
    c "HOPE! NO!!! PUT YOUR CLOTHES BACK ON!!!"


label letsplayers:

    scene bg school
    $quick_menu = True 

    show i oohh ehh at move(0.8, 0.0)
    show a crossed long at move(0.3, 0.0)
    i "TOM NOOK IS GOING TO REVIEW US????"
    show a ahh
    show i ooo
    a "No, I said Nook Gaming MIGHT review us, but it's not a guare-"
    show i omg
    i "TOM NOOK REVIEWS VIDEO GAMES?!?!? LIKE PEWDIPIE?!?!"
    show i sicko
    show a standard ehh
    a "Um, no, what? This has nothing to do with YouTube. Nook Gaming is a review website..."

##---------

    scene bg school
    show i laugh oohh at move(1.0)
    show a long standard at move(0.6)
    show c smile at move(0.3)
    show h long at move(-0.05)
    i "Hey guys, guess what? Oprah might be reviewing us!"
    show c ooo
    show i smile at move(0.9)
    c "Huh? I thought she was a talk show host? I didn't know she reviewed visual novels..."
    show c disappoint
    show a crossed ahh
    show i long fists
    a "...Isadora, I said that OPRAINFALL might review us. It's short for Operation Rainfall."
    show a sad
    show h ahh
    h "what i dont get it what does rainfall have to do with video games"

    scene bg school
    show i laugh oohh at move(1.0)
    show a long crossed at move(0.6)
    show c smile at move(0.3)
    show h long at move(-0.05)
    i "Hey guys, look at this website where the Creator is sending a review copy. It looks kinda neat!"
    show i smile standard at move(0.9)
    show c laugh surprised
    c "Oh, you see that screenshot of the girl in the white dress at the top? That was also made in RenPy I think!"
    show c smile standard
    show a standard wah
    a "Whoah! It says here that this guy has a PhD! You can get a PhD in visual novels?!?!"
    show h ahh
    show a long
    h "no he doesnt it says he has a phd on hold besides it doesnt say what the PhD is in"
    show h disappoint
    show a disappoint
    show c think
    show i ooo fists
    c "CAN you get a PhD in reviewing visual novels? That would be pretty cool..."

    scene bg school
    show i ehh oohh at move(0.9)
    show c smile at move(-0.05)
    show h long at move(0.4)
    i "HUH? Wait, why is the Creator sending a review copy to this person? We don't speak spanish!!"
    show c long
    show h ahh
    show i disappoint fists
    h "uhhhh there are reviews of english only games here too i think its ok"


    scene bg school
    show i smile at move(0.6)
    show c happy at move(-0.05)
    show h long at move(0.4)
    c "Hey! What is that on your phone?"
    show c at move(0.2)
    show h laugh
    show c smile
    h "oh hey chris were listening to this dweeb otaku letsplayer mispronounce japanese"
    show h owo
    show c disappoint
    c "...um...ok?"
    show c line
    pause 5
    show c ahh
    show h line
    show i long
    c "...um, didn't the Creator send a review copy to this person?"

    scene bg school
    show h happy at move(0.6)
    show c long at move(0.2)
    h "hey chris check this out the creator was looking for recommendations for people to send a review copy to right"
    show c disappoint
    c "...Hope, this blog page only has reviews of Yuri."
    show h smirk
    h "yea so"
    show c ehh surprised
    c "It's literally called \"The Lily Garden\". Under what logic would you classify us as Yuri?!?!?"
    show h owo
    show c sad fists
    h "hey not all of us r straight"


    scene bg school
    show i ahh at move(0.7)
    show c smile at move(0.3)
    i "Hey Chrissy, are we a Metagame?"
    show c disappoint
    show i long
    c "Hmm? No, we're \"MetaWare\". I don't know what a Metagame is."
    show i ooo
    i "Well, according to this person who the Creator sent a review copy to there's a visual novel that has \"International Metagames\". What does that mean?"
    show i long
    show c sad
    c "...Fate/Stay Night? Erm...I've heard of this series, but I've only seen some the anime...they're pretty different than us."


    scene bg school
    show i long standard at move(1.0)
    show a long crossed at move(-0.05)
    show c smile at move(0.28)
    show h owo at move(0.6)
    c "...interesting. So this reviewer who the Creator sent a review copy to has started doing smaller reviews in groups of five or more."
    show a proclaim
    show c long
    show i ooo
    show h long
    a "Five? Ahhahahahaha! The situation couldn't be more perfect! There are five of us in the gang...so they can write a review on each one of us! We'll get TONS of coverage!!!!"
    show h sad
    show a standard smile
    show i long
    h "aspen u dumbass do u even know how game reviews work"
    show a sad
    show h smirk
    show c inv
    h "besides aspen u wouldnt get any more than a final score of 3/10"

    scene bg school 
    show i smile at move(1.0)
    show h laugh at move(0.75)
    h "wow why would you want a scar figurine for 17 dollars it looks kinda ugly too"
    show h owo
    show i sicko
    show c disappoint at move(0.0)
    i "Ewwwwwwwww she buys Pepperidge Farm cookies? Those things are disgusting..."
    show i open oohh at move(1.05)
    show h morty at move(0.8)
    show c ehh fists at move(0.4)
    c "GUYS FOR THE LAST TIME STOP STALKING THE LETSPLAYERS' AMAZON WISH LISTS!!!!!"

    jump letsplayers



    

