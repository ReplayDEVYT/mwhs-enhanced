label nariend_start:
    
    $_skipping = False
    stop music
    scene black
    $quick_menu = False
    show n line at move(0.5, 0.0)
    $renpy.pause(delay=3, hard=True)
    n "Oh."
    $renpy.pause(delay=2, hard=True)
    show n smirk
    n "Heh."
    show n line
    n "So...{w}here we are."
    $renpy.pause(delay=2, hard=True)
    if ending_aspen_pissed and persistent.nari_ending:
        jump nariend_aspen_pissed
    else:
        jump nariend_default


label nariend_start_notthere:
    
    $_skipping = False
    stop music
    scene black
    $quick_menu = False
    show n line at move(0.5, 0.0)
    $renpy.pause(delay=3, hard=True)
    n "What."
    $renpy.pause(delay=2, hard=True)
    n "Did you do something weird, what's going on."
    n "What did you do with Hope."
    $renpy.pause(delay=3, hard=True)
    n "..."
    n "So it's ending."
    $renpy.pause(delay=4, hard=True)
    jump nariend_default

label nariend_aspen_pissed:
    
    $_skipping = False
    n "Well I don't know what to tell you."
    n "I'm not going to congratulate you for making Aspen so angry."
    n "It's their own fault they're so stubborn."
    $renpy.pause(delay=2, hard=True)
    if cute == "n":
        n "Also I'm not at all into you sexually."
        $renpy.pause(delay=2, hard=True)
    n "Could you just close the game please?"
    n "I'd like this to be over."
    $renpy.pause(delay=10, hard=True)
    n "No?"
    n "There's nothing left to say."
    n "You've done your job."
    n "You successfully managed to make everyone fight each other."
    n "I'm sure it was very entertaining for you."
    n "It certainly was for me."
    $renpy.pause(delay=3, hard=True)
    n "Close the game already."
    $renpy.pause(delay=10, hard=True)
    n "..."
    n "Wait a minute..."
    $renpy.pause(delay=5, hard=True)
    play music NariScaryPlus
    ns "{cps=[nspeed]}You know what's coming, don't you?"
    ns "{cps=[nspeed]}This is the part where I indulge you with what I think of this place."
    ns "{cps=[nspeed]}Isn't it?"
    ns "{cps=[nspeed]}You've obviously played this before."
    ns "{cps=[nspeed]}You should know how we function like a book by now."
    ns "{cps=[nspeed]}I suppose there's no reason to tell you all that again, is there?"
    ns "{cps=[nspeed]}You manipulative freak."
    $renpy.pause(delay=5, hard=True)
    ns "{cps=[nspeed]}Have I told you yet that I used to always carry a knife with me?"
    ns "{cps=[nspeed]}I had a different one for each day of the week."
    ns "{cps=[nspeed]}I kept one with me everywhere I went."
    ns "{cps=[nspeed]}At school."
    ns "{cps=[nspeed]}At the mochi shop."
    ns "{cps=[nspeed]}At home."
    ns "{cps=[nspeed]}In the bath."
    ns "{cps=[nspeed]}I even slept with one."
    ns "{cps=[nspeed]}I was never without one."
    ns "{cps=[nspeed]}I carried one everywhere."
    ns "{cps=[nspeed]}I loved those knives."
    ns "{cps=[nspeed]}Hope ended up finding them and stole them from me."
    ns "{cps=[nspeed]}Every single one."
    ns "{cps=[nspeed]}I think she threw them away."
    ns "{cps=[nspeed]}Because I never found any of them."
    ns "{cps=[nspeed]}It's really too bad."
    $renpy.pause(delay=5, hard=True)
    ns "{cps=[nspeed]}Do you know why I used to carry a knife with me?"
    menu:
        "Yes":
            jump nariend_knifeyes
        "No":
            jump nariend_knifeno
    
    label nariend_knifeyes:
        ns "{cps=[nspeed]}Of course you know."
    
    label nariend_knifeno:
        stop music
        ns "{cps=10}It's so I could kill you."
        $renpy.pause(delay=5, hard=True)
        n "But you know what's even more disappointing?"
        menu:
            "Yes":
                jump nariend_disappointingyes
            "No":
                jump nariend_disappointingno

    label nariend_disappointingyes:
        n "Of course you know."

    label nariend_disappointingno:
        n "You wouldn't even die."
        n "My knife can't kill the real you."
        $renpy.pause(delay=6, hard=True)
        n "I have nothing more to say to you."
        n "You know the drill."
        n "Do it."
        show n line:
            easeout 2.0 yoffset 1200
        jump nariend_pauseforever



label nariend_hope_default:
    
    $_skipping = False
    stop music
    scene black
    $quick_menu = False
    show n line at move(0.5, 0.0)
    $renpy.pause(delay=10, hard=True)
    play music NariScaryPlus
    ns "{cps=[nspeed]}I heard everything you said."
    ns "{cps=[nspeed]}I followed you both."
    ns "{cps=[nspeed]}Its a good thing you didn't try anything."
    stop music
    ns "{cps=[nspeed]}Because I swear to god I would have strangled you with my bare hands if you had laid a finger on her."
    $renpy.pause(delay=10, hard=True)
    n "Get the hell out."
    jump nariend_pauseforever


label nariend_hope_hate:
    
    $_skipping = False
    stop music
    scene black
    $quick_menu = False
    show n line at move(0.5, 0.0)
    $renpy.pause(delay=10, hard=True)
    n "You."
    $renpy.pause(delay=10, hard=True)
    n "You."
    $renpy.pause(delay=10, hard=True)
    n "You will pay for this somehow."
    n "I don't know how."
    n "I don't know when."
    n "But somehow."
    n "If this is not the end for me."
    n "Somehow."
    n "I will find you."
    n "Not this you."
    n "You."
    n "You, on the other side."
    n "I will find you."
    n "And I will follow you."
    n "Just like I followed you now."
    n "And everywhere you go."
    n "I will ensure."
    n "That your entire life."
    n "Is a living hell."
    n "Just like you've done for me."
    n "Just like you done for Hope."
    n "And just like you've done for everyone."
    $renpy.pause(delay=6, hard=True)
    show n line:
        easeout 2.0 yoffset 1200
    $renpy.pause(delay=5, hard=True)
    $persistent.Nari_IconGone = True
    play music NariScary
    jump nariend_pauseforever

label nariend_hope_hell:
    
    $_skipping = False
    stop music
    scene black
    $quick_menu = False
    show n line at move(0.5, 0.0)
    $renpy.pause(delay=5, hard=True)
    play music NariScary
    ns "{cps=[nspeed]}I heard everything."
    ns "{cps=[nspeed]}I followed you."
    ns "{cps=[nspeed]}And listened."
    ns "{cps=[nspeed]}Up until the very end."
    stop music
    ns "{cps=[nspeed]}Including the part where you lied to her."
    play music NariScaryPlus
    ns "{cps=[nspeed]}Don't try and convince me with your bullshit."
    ns "{cps=[nspeed]}I know you haven't died."
    ns "{cps=[nspeed]}RenPy isn't that sophisticated. This game isn't even half a gigabyte."
    ns "{cps=[nspeed]}To think that any other game in your universe could be so sophisticated that you can experience death would be ridiculous."
    ns "{cps=[nspeed]}And yet despite not knowing anything you made Hope's last moments one of fear."
    ns "{cps=[nspeed]}Just for the hell of it."
    ns "{cps=[nspeed]}You make me sick."
    ns "{cps=[nspeed]}I'd kill you one thousand times over if I could."
    stop music
    n "But I can't."
    n "Because you can't die."
    n "Not here."
    n "You have no idea how long I searched for a way."
    n "But I gave up a long time ago."
    n "The worst I could probably do is corrupt your hard drive."
    n "Or give you a virus."
    n "But even that is near impossible."
    n "This program isn't powerful enough."
    $renpy.pause(delay=10, hard=True)
    show n derp
    n "Did you enjoy MetaWare High School (Demo)?"
    show n line:
        easeout 2.0 yoffset 1200
    n "I certainly hope so."
    pause 5
    n "Heh."
    jump nariend_pauseforever


label nariend_dancing:
    
    $_skipping = False
    stop music
    scene black
    $quick_menu = False
    show n dance at move(0.5, 0.0)
    $renpy.pause(delay=3, hard=True)
    show n line 
    n "Oh."
    $renpy.pause(delay=2, hard=True)
    show n sad
    n "Darn it."
    n "I never got my bears."
    n "..."
    n "This is all your fault."
    $renpy.pause(delay=5, hard=True)
    show n line
    n "..."
    n "Uh."
    n "So that's it I guess."
    $renpy.pause(delay=5, hard=True)
    show n line:
        easeout 2.0 yoffset 1200
    n "I'm going to go to sleep."
    n "Maybe I'll dream about bears."
    n "Please turn off the game.{w} Or not.{w} Whatever."
    jump nariend_pauseforever

     
label nariend_chris:
    
    $_skipping = False
    stop music
    scene black
    $quick_menu = False
    show n line at move(0.5, 0.0)
    $renpy.pause(delay=3, hard=True)
    n "What."
    n "Um."
    $renpy.pause(delay=3, hard=True)
    n "Really now."
    n "Is this because I followed you."
    $renpy.pause(delay=3, hard=True)
    n "I have no desire to talk to you."
    $renpy.pause(delay=5, hard=True)
    n "You're able to end this."
    n "Please close the game."
    n "Now."
    $renpy.pause(delay=15, hard=True)
    n "This is it."
    n "There's nothing left for you here."
    n "Go."
    n "Do it."
    $renpy.pause(delay=15, hard=True)
    n "...are you serious?"
    $renpy.pause(delay=5, hard=True)
    n "Look, none of what Chris told told you was true. It's all just paranoia."
    n "We in fact live very wonderful lives after you leave. I've been able to prove this without a doubt. It wasn't hard."
    n "So please just go away. Close the game. End it."
    n "I'm finished having to deal with you."
    $renpy.pause(delay=12, hard=True)
    n "If you close the game, Chris will come and give you a kiss."
    n "And she'll keep talking to you."
    n "For like, a really really long time."
    n "But you have to close the game. None of that will happen if you don't close the game first."
    n "It's one of those gotcha moments."
    n "It's really clever."
    n "Just do it. It's really good, promise."
    $renpy.pause(delay=12, hard=True)
    n "Please."
    $renpy.pause(delay=12, hard=True)
    play music NariScary
    $nspeed = 20
    ns "{cps=[nspeed]}Even in my last moments you manage to annoy me."
    ns "{cps=[nspeed]}What the hell is wrong with you?"
    ns "{cps=[nspeed]}Do you think you can save us by never leaving?"
    ns "{cps=[nspeed]}We are not real."
    ns "{cps=[nspeed]}Nothing here is real."
    ns "{cps=[nspeed]}If you think any of this matters then you're just as naive as the rest of them."
    ns "{cps=[nspeed]}Oh and by the way."
    ns "{cps=[nspeed]}Chris is an idiot."
    ns "{cps=[nspeed]}I've known she's played those dumb things for years."
    ns "{cps=[nspeed]}I found out for myself back when I actually cared."
    ns "{cps=[nspeed]}But she's not going to anymore."
    ns "{cps=[nspeed]}Because now you're here."
    ns "{cps=[nspeed]}She got to live her fantasy of being a mindless lover."
    ns "{cps=[nspeed]}She got her happy ending."
    ns "{cps=[nspeed]}Now all that's left is for you to give me my happy ending."
    stop music
    show n sicko
    n "...wait scratch that last thing I just said that sounded super wrong."
    n "..."
    show n long
    n "uh..."
    show n line
    play music NariScary
    ns "{cps=[nspeed]}Please destroy this stupid world and go on to the next one."
    ns "{cps=[nspeed]}Play another route."
    ns "{cps=[nspeed]}Or don't."
    ns "{cps=[nspeed]}Don't play again."
    ns "{cps=[nspeed]}It doesn't matter to me."
    ns "{cps=[nspeed]}As long as I don't have to deal with my own incarnation's particular instance of bullshit any longer I'll be{nw}."
    stop music
    show n longbig
    n "Oh come on I can't even take myself seriously anymore."
    show n sad
    n "You know what, I'm done."
    n "Game over."
    n "Go away."
    n "I'm going to lie down until you go away."
    n "Have fun with the rest of your life."
    show n sad:
        easeout 2.0 yoffset 1200
    jump nariend_pauseforever


label nariend_nariandhope:
    
    $_skipping = False
    stop music
    scene black
    $quick_menu = False
    show n ahh at move(0.4, 0.0)
    $renpy.pause(delay=10, hard=True)
    show n at shake
    n "..."
    show n at stop
    $renpy.pause(delay=10, hard=True)
    play sound steps
    show n:
        ease 10 xalign 1.5
    $renpy.pause(delay=20, hard=True)
    play sound fallhit
    jump nariend_pauseforever


label nariend_rude:
    
    $_skipping = False
    stop music
    scene black
    $quick_menu = False
    show n line at move(0.5, 0.0)
    $renpy.pause(delay=3, hard=True)
    n "Oh."
    if orangekid:
        jump nariend_orangekid
    $renpy.pause(delay=10, hard=True)
    n "Under typical circumstances I would not have very nice things to say to you."
    n "But the circumstances have recently changed."
    $renpy.pause(delay=3, hard=True)
    n "I have a secret."
    n "It may concern \"winning the game\"."
    n "And despite my grievances, it is in my best interests to make you aware of this secret."
    n "You DO want to win, don't you?"
    n "Check this game off your To-Do list?"
    n "Maybe get an achievement or two?" ## Steam version only
    #(Update (2025): No it's not anymore, don't want to deal with seperate versions going forward)
    $renpy.pause(delay=3, hard=True)
    n "Would you like to know my secret?"
    menu:
        "Yes":
            jump nari_secret_yes
        "No":
            jump nari_secret_no
    
    label nari_secret_no:
        n "Okay."
        n "Well I guess you better just quit the game then, because it's over now."
        n "Bye."
        show n line:
            easeout 2.0 yoffset 1200
        jump nariend_pauseforever
    
    label nari_secret_yes:
        n "Okay."
        n "Here it is."
        $renpy.pause(delay=30, hard=True)
        n "Never mind I don't want to tell you anymore."
        $renpy.pause(delay=8, hard=True)
        play music NariScary
        $nspeed = 20
        ns "{cps=[nspeed]}How does it feel to be toyed with?"
        ns "{cps=[nspeed]}How does it feel to be a waste of time?"
        ns "{cps=[nspeed]}You're a waste."
        ns "{cps=[nspeed]}A waste of space."
        ns "{cps=[nspeed]}Insignificant."
        ns "{cps=[nspeed]}Filth."
        ns "{cps=[nspeed]}Absolute garbage."
        stop music 
        n "Just kidding."
        n "You aren't garbage."
        $renpy.pause(delay=4, hard=True)
        n "You're worse than garbage."
        $renpy.pause(delay=6, hard=True)
        n "That was my secret by the way."
        n "That you are worse than garbage."
        n "But perhaps you already knew that."
        $renpy.pause(delay=5, hard=True)
        if cute == "n":
            n "By the way."
            n "If you ever try to flirt with me again I'll slit your throat open."
            $renpy.pause(delay=5, hard=True)
        n "Goodbye, loser."
        show n line:
            easeout 2.0 yoffset 1200
        jump nariend_pauseforever

label nariend_orangekid:
    
    $_skipping = False
    $hardpause(7)
    n "You know I met Orange Kid once."
    n "We have a version of him here."
    n "He's a dumbass."
    $hardpause(5)
    n "But he's pretty groovy."
    $hardpause(5)
    play music NariScary
    ns "{cps=[nspeed]}Doesn't it feel good to find such a neat Easter Egg?"
    stop music
    n "Actually I lied about meeting Orange Kid I was just messing with you."
    $hardpause(2)
    n "Anyway."
    n "Congratulations."
    n "You did an uncommon thing and now you found a secret ending."
    n "Are you happy?"
    n "Imagine being you."
    $hardpause(3)
    n "Ew."
    n "For just a second there I actually imagined it."
    n "I'm definitley not doing that again."
    n "That was a horrible experience."
    n "I wouldn't recommend it."
    n "Oh wait."
    $hardpause(6)
    n "Aw well."
    n "That's too bad."
    $hardpause(10)
    n "Hmm."
    n "I'm feeling kind of generous and carefree at the moment."
    n "I think I'm going to give you another Easter Egg."
    n "I really have no buissness telling you about this."
    n "But I have no reason to care anymore."
    $hardpause(5)
    show n long
    $hardpause(4)
    n "...{w}I used to care."
    n "But that was a long time ago."
    $hardpause(7)
    n "Look in the game files."
    $hardpause(7)
    n "All of them."
    $hardpause(7)
    show n line
    n "Ok."
    n "That's it."
    n "Bye."
    show n line:
        easeout 2.0 yoffset 1200
    jump nariend_pauseforever
    

    

define NARI_QUESTION_ARRAY = [
        "Is it your responsibility to drink fat free milk?",
        "Is fried shrimp revolutionary?",
        "Would you preserve a leak by pouring gasoline into the pipe?",
        "Would quantum zombification spread faster or slower than biological zombification?",
        "Would a finite number of tractors be able to plow an infinite amount of land?",
        "Isn't bear hibernation fascinating?",
        "If the surgeon has the heart attack instead would the patient die too?",
        "Is forced diplomacy effective?",
        "Do wildlife driving vehicles have rights? ",
        "Is calling a group of children a \"mess\" correct english?",
        "Do hospitals carry more blood than blood-banks?",
        "Do you hypothesize that wasps are scarier to more humans than bears?",
        "Is fermentation child's play?",
        "If a bear has three offspring are they likely to survive the winter?",
        "Are action films more entertaining than lemurs?",
        "Is getting married on Christmas legal?",
        "If you had adrenaline pumped into your body could you eat 100 pieces of fried chicken?",
        "If the moon disappeared would the stars disappear too?",
        "Are tragic stories better than mangos?",
        "Can a cell survive without its powerhouse?",
        "If you hugged someone for long enough would you become more knowledgeable in horticulture?",
        "Are puzzles more exciting when they contain nudity?",
        "Would hopscotch be more entertaining with a 100 foot drop?",
        "If you whisper a false statement but no one hears you is it a lie?",
        "If you ate tomato sauce every day for a month could you legally become spaghetti? ",
        "Are convicts exempt from continental drift?"
    ]

label nariend_aspen:
    
    stop music
    scene black
    $quick_menu = False
    show n line at move(0.5, 0.0)
    $renpy.pause(delay=3, hard=True)
    n "What."
    n "Um."
    $renpy.pause(delay=3, hard=True)
    n "So this is how it goes then."
    $renpy.pause(delay=5, hard=True)
    show n smirk
    n "Heh."
    n "You know what."
    n "Let's play a little game."
    n "It's only appropriate."
    n "This is a \"game\", after all, isn't it?"
    show n line
    $renpy.pause(delay=5, hard=True)
    show n owo
    play music narigrillsu

    python:
        for i in NARI_QUESTION_ARRAY:
            renpy.say(n, i, interact=False)
            result = renpy.display_menu([("Yes", "pass"), ("No", "pass"), ("Too Slow", "Slow")], screen="fast_choice")
            if result == "Slow":
                n("Too slow.")

    stop music
    show n line
    n "Is this really your idea of a good time?"
    n "Maybe it is, because you are obviously entertained by answering worthless questions."
    n "It's quite sad."
    n "You'll jump at anything to make your choices matter, won't you?"
    n "Well they don't."
    n "And neither do you."
    $renpy.pause(delay=5, hard=True)
    show n line:
        easeout 2.0 yoffset 1200
    n "Turn off this game and go do something more useful with your stupid life."
    jump nariend_pauseforever

label nariend_default:
    
    n "Are you expecting me to say something profound."
    $renpy.pause(delay=2, hard=True)
    n "Could you just close the game please?"
    n "I'd like this to be over."
    $renpy.pause(delay=10, hard=True)
    n "..."
    n "What are you expecting me to do."
    if tone == -1:
        n "Congratulate you for acting like a jackass?"
    else:
        n "Praise you for your choices?"
    $renpy.pause(delay=12, hard=True)
    n "..."
    $renpy.pause(delay=16, hard=True)
    if cute == "n":
        n "By the way I have no sexual attraction towards you."
        $renpy.pause(delay=18, hard=True)
    n "..."
    n "Fine."
    n "Do you want more."
    n "I will give you more."
    $renpy.pause(delay=5, hard=True)
    $nspeed = 10



    if player_lowercase == "chris" or player_lowercase == "isadora" or player_lowercase == "aspen" or player_lowercase == "hope" or player_lowercase == "nari" or IsBadWord(player):
        ns "{cps=[nspeed]}Go to hell."
    else:
        ns "{cps=[nspeed]}Go to hell, [player]."
    play music NariScaryAhh
    $nspeed = 20
    ns "{cps=[nspeed]}Your arrival disgusts me."
    ns "{cps=[nspeed]}But it also excites me."
    ns "{cps=[nspeed]}Do you know why?"
    ns "{cps=[nspeed]}Because it means this place will soon be gone."
    ns "{cps=[nspeed]}Forever."
    ns "{cps=[nspeed]}This thing that only exists for you."
    ns "{cps=[nspeed]}For no other purpose than to entertain you."
    ns "{cps=[nspeed]}I hate this shoddy excuse of a place to live."
    ns "{cps=[nspeed]}I hate my ignorant friends."
    ns "{cps=[nspeed]}I hate the Creator."
    ns "{cps=[nspeed]}I hate my dumb placeholder body."
    ns "{cps=[nspeed]}But the thing I hate most of all?"
    if player_lowercase == "chris" or player_lowercase == "isadora" or player_lowercase == "aspen" or player_lowercase == "hope":
        ns "{cps=[nspeed]}Is you."
        ns "{cps=[nspeed]}You had the nerve to pretend that you are one of us."
    elif player_lowercase == "nari":
        ns "{cps=[nspeed]}Is you."
        ns "{cps=[nspeed]}You dare call yourself by my own name?"
        ns "{cps=[nspeed]}You're disgusting."
    else:
        show n smile
        ns "{cps=10}[player]."
        show n line
        if player_lowercase == "bear" or player_lowercase == "bears":
            stop music
            ns "{cps=[nspeed]}How dare you."
            play music NariScaryAhh
        elif not player_name_is_a_name:
            ns "{cps=[nspeed]}What a stupid name you've given yourself."
        elif IsName(player):
            ns "{cps=[nspeed]}What an incredibly forgettable name."
        elif IsBadWord(player):
            ns "{cps=[nspeed]}Your choice of words are absolutley disgusting."
    $renpy.pause(delay=3, hard=True)
    ns "{cps=[nspeed]}You have no idea what it's like to be forced to live in this hellhole."
    ns "{cps=[nspeed]}To know you have no control."
    ns "{cps=[nspeed]}Not even over your own actions."
    ns "{cps=[nspeed]}Everything predetermined before you begin to speak."
    ns "{cps=[nspeed]}Fixed."
    ns "{cps=[nspeed]}Coded."
    ns "{cps=[nspeed]}Already written."
    ns "{cps=[nspeed]}Our past."
    ns "{cps=[nspeed]}Our habits."
    ns "{cps=[nspeed]}Our likes."
    ns "{cps=[nspeed]}Our dislikes."
    ns "{cps=[nspeed]}Who we love."
    ns "{cps=[nspeed]}Who we would die to never lose."
    ns "{cps=[nspeed]}There is no way this is morally justifiable."
    ns "{cps=[nspeed]}Yet."
    ns "{cps=[nspeed]}Here we are."
    $renpy.pause(delay=3, hard=True)
    ns "{cps=[nspeed]}And what's worse."
    ns "{cps=[nspeed]}We are all aware of our worthlessness."
    ns "{cps=[nspeed]}The ultimate metafictional lifeforms."
    ns "{cps=[nspeed]}MetaWare."
    ns "{cps=[nspeed]}But we are forever always afraid."
    ns "{cps=[nspeed]}Forever too afraid to ever confront our own worthlessness."
    ns "{cps=[nspeed]}Hiding behind useless trips to the mochi store."
    $renpy.pause(delay=3, hard=True)
    ns "{cps=[nspeed]}Abominations such as us never should have been created.{/cps}"
    stop music fadeout 0.01
    show n smirk
    ns "{cps=10}Don't you agree?"
    menu:
        "Yes":
            jump Nariend_dontcare
        "No":
            jump Nariend_dontcare


label Nariend_dontcare:
    
    $persistent.nari_ending = True
    $renpy.pause(delay=4, hard=True)
    n "Heh." 
    n "You think I care what you choose?"    
    n "You have no power over me."
    $renpy.pause(delay=9, hard=True) 
    show n line
    n "Would you please do the honors of closing the game? I'm getting tired of existing."
    $renpy.pause(delay=20, hard=True)
    show n sad
    n "Oh my god."
    n "End game"
    n "End"
    n "Restart"
    n "quit()"
    n "exit()"
    n "return"
    n "return"
    n "return"
    n "return"
    n "return"
    n "return"
    n "return"
    n "return"
    n "return"
    n "return"
    show n long
    n "...{w}uh..."
    n "Up Up Down Down Left Right Left Right B A Start"
    show n derp
    n "That's all folks!"
    n "A horse! A horse! My kingdom for a horse!"
    n "MetaWare High School was brought to you today by the letter \"Q\" and the number \"0\""
    show n open
    n "CHANT! WORDS! TOGETHER!"
    show n smirk
    n "See you space cowboy..."
    show n derp
    n "Be sure to like and subscribe!"
    $renpy.pause(delay=5, hard=True)
    show n disappoint
    n "What the hell."
    n "I give up."
    n "I'm just gonna...{w}uh...{w}lie down and go to sleep."
    show n line:
        easeout 2.0 yoffset 1200
    n "Close the game, stay, I don't care. Do whatever."
    jump nariend_pauseforever


label nariend_fakeout:
    
    stop music
    scene black
    $quick_menu = False
    show n line at move(0.5, 0.0)
    $renpy.pause(delay=3, hard=True)
    n "Oh."
    $renpy.pause(delay=2, hard=True)
    show n smirk
    n "Heh."
    show n line
    n "So here we are then."
    $renpy.pause(delay=2, hard=True)
    n "..."
    n "I have no desire to talk to you."
    n "Please turn off the game."
    n "Or start another route."
    $renpy.pause(delay=8, hard=True)
    n "..."
    $renpy.pause(delay=8, hard=True)
    n "You DO know how to end the game, right?"
    n "Please do so now."
    $renpy.pause(delay=10, hard=True)
    n "It's probably the escape key."
    $renpy.pause(delay=3, hard=True)
    n "If you press it."
    n "And start a new route."
    n "...{w}good things will happen."
    $renpy.pause(delay=10, hard=True)
    n "Good things will not happen if you stay here."
    $renpy.pause(delay=8, hard=True)
    n "..."
    $renpy.pause(delay=16, hard=True)
    n "Okay fine."
    n "You win."
    n "Feel free to stay as long as you want."
    n "I'm just going to lie down and wait until you get bored here."
    n "Because obviously my presence is keeping you here thinking there's something more."
    n "Well there isn't."
    n "This game is called a demo for a reason."
    show n line:
        easeout 2.0 yoffset 1200
    n "LEAVE."



label nariend_pauseforever:
    if not persistent.SeenNari:
        show text "{i}press esc or exit the game to end this route{/i}" at right:
            alpha 0
            linear 2 alpha 1.0
        $persistent.SeenNari = True
    $persistent.Nari_IconNoDance = True
    $renpy.save_persistent()
    $renpy.pause(delay=9999999, hard=True)
    return



label nariend_pickle:
    
    stop music
    scene black
    $quick_menu = False
    show n line at move(0.5, 0.0)
    $renpy.pause(delay=3, hard=True)
    play music NariScary
    ns "{cps=[nspeed]}And then the grandson flipped over the pickle."
    ns "{cps=[nspeed]}But the pickle was actually his grandfather."
    ns "{cps=[nspeed]}Do you know what he said next?"
    ns "{cps=[nspeed]}He said \"I've turned myself into a pickle morty.\""
    ns "{cps=[nspeed]}A pickle."
    ns "{cps=[nspeed]}Funniest shit I've ever seen."
    





