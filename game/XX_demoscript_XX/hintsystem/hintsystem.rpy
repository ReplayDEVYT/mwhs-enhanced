



init python:

    def CheckHintSystemState():
        if persistent.completed_endings == None:
            return

        if len(persistent.completed_endings) >= 5:
            persistent.hintSystemActive = True
        else:
            persistent.hintSystemActive = False

    CheckHintSystemState()

    def GetHintToShow():
        undiscovered = list(filter(lambda ending : ending not in persistent.completed_endings, list_of_endings))
        hint_to_show = None
        if len(undiscovered) > 0:
            hint_to_show = undiscovered[0]
        return hint_to_show

    def fuzzyimage(trans, st, at):
        trans.ypos = renpy.random.randint(-2000, 0)
        return 0.002 #rate of fizz

transform fuzzy:
    alpha 0.05
    ytile 2
    function fuzzyimage

define list_of_endings = [
    "GoodbyeShort",
    "Mochi",
    "NoMochi",
    "Dancing",
    "Chris",
    "Hope",
    "NariReveal",
    "RudeEnd",
    "AspenDrillsU",
    "AspenPissed",
]





label hintSystem:

    $hint_to_show = GetHintToShow()
    scene black
    stop music
    stop sound
    play music noise
    $quick_menu = False

    show colornoise at fuzzy()
        

    pause 3 

label hintSystemLoop:

    if hint_to_show == None:
        centered "Congratulations.{w=4}{nw}"
        return

    elif hint_to_show == "Mochi":
        centered "WE'RE RUNNING OUT OF TIME{w=3}{nw}"
        centered "Well do you have a better idea?!?!{w=3}{nw}"
        centered "Oh geez, here we go with the mochi again...{w=3}{nw}"
        centered "but yeah anyway i forgot your name you wanna get ur mochi on{w=3}{nw}"
        menu:
            "I understand. I will go with her.":
                jump storycontinues
            "I do not understand.":
                pause 2
                jump hintSystemLoop

    elif hint_to_show == "NoMochi":
        centered "WE'RE RUNNING OUT OF TIME{w=3}{nw}"
        centered "Well do you have a better idea?!?!{w=3}{nw}"
        centered "Oh geez, here we go with the mochi again...{w=3}{nw}"
        centered "but yeah anyway i forgot your name you wanna get ur mochi on{w=3}{nw}"
        menu:
            "I understand. I will not go with her.":
                jump storycontinues
            "I do not understand.":
                pause 2
                jump hintSystemLoop

    elif hint_to_show == "Dancing":
        centered "I think they're just messing with us.{w=3}{nw}"
        centered "Well, uh...hahaha! That's what they said they were going to do! Screw with us, right?{w=3}{nw}"
        centered "I never would have expected the player's behavior to be this...unpredictable.{w=3}{nw}"
        menu:
            "I understand. I will dance.":
                jump storycontinues
            "I do not understand.":
                pause 2
                jump hintSystemLoop

    elif hint_to_show == "GoodbyeShort":
        centered "Is that blurry thing...a person?!?!{w=3}{nw}"
        centered "T-THAT'S THEM. THEY'RE HERE.{w=3}{nw}"
        centered "It's wonderful to finally meet you!{w=3}{nw}"
        menu:
            "Goodbye.":
                jump storycontinues
            "I do not understand.":
                pause 2
                jump hintSystemLoop

    elif hint_to_show == "Hope":
        centered "LMAO u think im cute{w=3}{nw}"
        centered "HOPE OH MY GOD NO{w=3}{nw}"
        centered "anyway whatsyourname how about we ditch everyone and go hang out somewhere other than here{w=3}{nw}"
        menu:
            "I understand. I will go with her.":
                jump storycontinues
            "I do not understand.":
                pause 2
                jump hintSystemLoop

    elif hint_to_show == "NariReveal":
        centered "...sorry Izzy, I kinda have to agree. You're a goner.{w=3}{nw}"
        centered "THANK YOU SOMEBODY GETS IT{w=3}{nw}"
        centered "So then...if we do not die...{w=3}{nw}"
        centered "That must mean we're immortal!{w=3}{nw}"
        menu:
            "I understand. I will agree with them.":
                jump storycontinues
            "I do not understand.":
                pause 2
                jump hintSystemLoop

    elif hint_to_show == "AspenDrillsU":
        centered "WHAT ARCHETYPE{w=3}{nw}"
        centered "hey player im thinking of a word{w=3}{nw}"
        centered "But this is a chance of a lifetime!{w} We're essentially talking to a time god!{w=3}{nw}"
        centered "Let's go somewhere else where we can talk without distractions.{w=3}{nw}"
        menu:
            "I understand. I will go with them.":
                jump storycontinues
            "I do not understand.":
                pause 2
                jump hintSystemLoop

    elif hint_to_show == "AspenPissed":
        centered "One moment. This might be going out on a limb here, but...{w=3}{nw}"
        centered "hey player im thinking of a word{w=3}{nw}"
        centered "WE DON'T HAVE TIME FOR THIS.{w=3}{nw}"
        centered "Let's go somewhere else where we can talk without distractions.{w=3}{nw}"
        menu:
            "I understand. I will not go with them.":
                jump storycontinues
            "I do not understand.":
                pause 2
                jump hintSystemLoop

    elif hint_to_show == "RudeEnd":
        centered "Chris...{w}did you just hear...{w=3}{nw}"
        centered "They've been acting a little...{w=3}{nw}"
        centered "Oh come on Chris, isn't this the whole point of this game anyway? Why not cut to the chase?{w=3}{nw}"
        centered "We're a dating sim!{w} Get over it!{w} Here, I'll prove it to you.{w=3}{nw}"
        menu:    
            "I understand. I will disagree with them.":
                jump storycontinues
            "I do not understand.":
                pause 2
                jump hintSystemLoop

    elif hint_to_show == "Chris":
        centered "Chris...{w}did you just hear...{w=3}{nw}"
        centered "They've been acting a little...{w=3}{nw}"
        centered "You have no excuse to act so ridiculous!{w=3}{nw}"
        centered "We're a dating sim!{w} Get over it!{w} Here, I'll prove it to you.{w=4}{nw}"
        centered "I don't think I would have it {cps=15}any other way.{/cps}{w=4}{nw}"
        menu:
            "I understand. I will agree with them.":
                jump storycontinues
            "I do not understand.":
                pause 2
                jump hintSystemLoop
        
    return


label storycontinues:
    stop music
    hide colornoise
    $hardpause(2)
    centered "{cps=20}Then the story continues.{w=3}{nw}"
    return
    




    