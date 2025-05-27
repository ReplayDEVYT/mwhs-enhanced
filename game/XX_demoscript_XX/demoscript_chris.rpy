label chris_start:
    i "..."
    i "....."
    $hardpause(4)
    show i long
    $hardpause(2)
    i "...Okay.{w} But you better not try anything funny."
    show i sad at move(-0.5, 2.0)
    i "Come on. She went this way."
    scene bg school_flipped with pushright
    show i open at enterright(0.7, 2.0)
    i "Chrissy? Are you over here?"
    show i long
    i "..."
    show i ahh at move(0.8, 0.5)
    i "Chrissy?"
    show i long
    $hardpause(3)
    show i disappoint
    i "Come on dumbutt I know you're here somewhere..."
    show i ahh at move(0.75, 1.5)
    i "Chriiiissy?"
    $hardpause(1.5)
    show c defeated at enterleft(-0.4, 0.0)
    show c at move(-0.2, 6.0)
    $hardpause(3)
    show i long at move(0.4, 1.0)
    i "Oh there you are. Chrissy what happened?"
    show c open
    cs "Wha-? Oh...{w}don't worry, I-I'm ok..."
    show c closed
    show i sad at move(0.2, 0.4)
    i "Oh my god your face is all gross and sticky, no you're not..."
    show c open
    cs "No really...I'm..."
    show c closed
    cs "..."
    show c open at move(-0.28, 1.6)
    cs "Wow...Y-You...you're here too."
    i "Oh sorry...{w}uh...{w}[pronoun[0]] insisted."
    show c closed
    cs "D-Don't you have something else you rather be d-doing?"
    i "I'm so sorry, some part of me thought it might be a good idea if [pronoun[0]]..."
    show i sad at move(0.3, 0.5)
    extend "oh what am I doing, this was such a horrible idea..."
    i "I'm just making things worse, I shouldn't have brought this nutcase, I'm so sorry Chrissy."
    cs "..."
    show c open
    extend "no...{w}no it's okay Izzy...{w}I'm..."
    show c closed
    cs "..."
    show c open
    cs "I'm happy that you've finally arrived...{w}um...{w}Mr. Player.{w} I-I mean...{w}uh..."
    show c closed
    cs "..."
    show c open
    extend "I'm happy you're here."
    show c closed
    $hardpause(3)
    show i long
    i "Oh.{w} Uh...{w}ok then."
    $hardpause(5)
    i "Do you...{w}want a hug?"
    cs "..."
    $hardpause(3)
    cs "..."
    show c open
    cs "You should both go back to the others.{w} Didn't they want to go get mochi?"
    show c closed
    show i disappoint
    i "Are you out of your mind? I'm not going anywhere. Don't be like that."
    $hardpause(4)
    show i long
    i "Is there...{w}Is there anything you maybe wanted to talk about?"
    $hardpause(3)
    i "Like um...{w}you know..."
    $hardpause(3)
    show i sad
    i "..."
    $hardpause(5)
    show i smile
    i "You know, if we ARE a dating sim, it probably won't be all that bad. I-It'll probably be fun! Dating and all that. We can just talk about our lives...Maybe we'll get some fancy gifts..."
    show i smirk
    i "And hey, it's not like we even need to play fair. You can be that girl who plays hard to get! Make it a little challenging? Level 2? Uh, hard mode! Extreme Dating Mode!!! Make them work for it!"
    show i smile
    i "I mean if the Player is designed to date each of us in some reality then I guess we can go and have fun with it. Bring out our flirty side."
    show i long
    i "Or...uh...not. If you don't want to. It's more likely someone else is going to get hitched anyway, like, according to probability?"
    show i ooo
    i "It's probably gonna be one of us five though, huh? We're the ones the Player showed up to, s-so I guess we're \"it\" then. Funny coincidence...kinda flattering really..."
    show i happy
    i "Hey, we can play a guessing game and try and figure out which route we're on...I mean it will probably be pretty obvious, but I mean it also might not be, right?"
    show c open
    cs "Izzy I want to talk with the Player alone, if that's okay."
    show c closed
    show i ahh
    $hardpause(4)
    i "Oh.{w} Uh..."
    show i long
    $hardpause(1.5)
    show i smile
    i "How about we do demo stuff instead?"
    cs "No."
    i "We really should be, we're behind as it is."
    show c open
    cs "Izzy."
    show c closed
    show i long
    $hardpause(3)
    i "Well, alright then."
    $hardpause(3)
    show i long at move(0.8, 3.0)
    i "I'll just...go find the others, I guess. Uh..."
    i "..."
    $hardpause(3)
    i "Are you sure?"
    cs "Yes."
    i "You don't think they're gonna...?"
    cs "No."
    i "But what if they...?"
    cs "I'll be fine."
    i "This is really not a good idea."
    show c open
    cs "Izzy please."
    show c closed
    $hardpause(3)
    show i sad
    i "...{w}Chrissy..."
    $hardpause(8)
    show i krying closed
    $hardpause(6)
    show i:
        easeout 14.0 xalign 1.8
    $hardpause(15)
    hide i
    show c:
        ease 5.0 xalign 0.5
    $hardpause(7)
    show c standard long
    $hardpause(4)
    show c smile
    $hardpause(2)
    cs "Hi."
    cs "..."
    show c long
    cs "Um..."
    cs "I meant what I said earlier."
    $hardpause(3)
    cs "That I'm glad you're here."
    $hardpause(3)
    show c sad
    $hardpause(3)
    cs "..."
    cs "......"
    $hardpause(4)
    show c long
    cs "Are...{w}um..."
    $hardpause(3)
    cs "Are we really a dating simulator?"
    menu:
        "Yes.":
            $chris_isdatingsim = 1 ##True
        'No.':
            $chris_isdatingsim = 0 ##False
        "I don't know":
            $chris_isdatingsim = 2 ##IDK
    $hardpause(5)
    if chris_isdatingsim == 0:
        $persistent.isdatingsimchris_yes = True
        cs "I don't know if I can trust that answer."
        cs "I don't have any way to know you're telling the truth. You could just be lying now to try and make me feel better. "
        cs "Especially since...you're going back on what you said before."
        cs "Even if you had said yes just now, I don't know if I could believe that either."
        cs "..."
        cs "There are just too many reasons why I can't trust you."

    if chris_isdatingsim == 1:
        $persistent.isdatingsimchris_no = True
        cs "I don't know if I can trust that answer."
        cs "You could just be lying and trying to push my buttons. Or maybe you really are telling the truth. I have no way of knowing."
        cs "Even if you said no, I don't know if I could believe that either."
        cs "..."
        cs "There are just too many reasons why I can't trust you."

    if chris_isdatingsim == 2:
        $persistent.isdatingsimchris_idk = True
        cs "...at least you're probably being honest now...{w}I guess..."
        cs "Or maybe you do know and you're just not telling me so that I'll feel better..."
        cs "..."
        cs "There are just too many reasons why I can't trust you...{w}I...{w}I don't know what to believe anymore..."
        cs "..."
    $hardpause(8)
    show c smile
    $hardpause(4)
    play music confession
    scene black
    show brightcolornoise:
        alpha 0.2
        ypan 0
        linear 120 ypan 360
        repeat
    show colornoise:
        alpha 0.1
        ypan 0
        linear 100 ypan 360
        repeat
    show bgendnoise:
        alpha 0.3
        ypan 0
        linear 90 ypan 360
        repeat
    show bg school_flipped:
        alpha 1
        xpos -20
        easeout 50 alpha 0
    show c smile at move(0.5, 0.0)
    cs "It was silly of me to think that it would be the same."
    cs "Of course it isn't.{w} We aren't like them."
    cs "We aren't a fantasy."
    show c ohh
    cs "Oh, sorry. I'm talking about other visual novels. I actually really enjoy playing them."
    show c long
    cs "I don't know how it is for you, but reading visual novels are kind of a weird thing for us. Since..{w} you know..."
    cs "It became an edgy fad a while ago. Especially like these super gross horror games, or cute dating simulators. But the trend has kinda died out now."
    show c smile
    cs "I stuck with it though. I still play them. I have a pretty big collection of them on my computer."
    cs "But I've never told anyone.{w} Nobody knows.{w} Not even anyone in the gang."
    cs "You're the only person I've ever told this to. The one person I can't trust to do anything responsible.{w} How stupid is that?"
    show c long
    cs "..."
    cs "I've never actually dated anyone.{w} To be honest I don't know if I would want to,{w} I think...{w}I don't know."
    cs "At least not how they usually make it seem like. With all the sex. It's not all that appealing to me."
    show c smile
    cs "But there's something special about getting to know someone in a visual novel that's different than in real life. Regardless if you're trying to date them or not."
    cs "You feel...{w}special.{w} You get to take care of someone.{w} Be there for them when they're sad.{w} Give them fun gifts.{w} Tell them they feel amazing."
    cs "Or you can make them feel miserable if you want.{w} Because they deserve it.{w} Because you can."
    cs "And no matter what you do, it's all okay, because none of it is real anyway."
    cs "It's all just a fantasy."
    cs "It doesn't even matter if you're making any choices or not. It still feels the same."
    cs "They want to cook dinner for you.{w} Or study with you.{w} Or sleep with you..."
    cs "Or they just want to spend time with you. "
    cs "Maybe they even want to kill you."
    cs "No matter what they want to do, you matter to them."
    cs "You're the most special person in their world."
    cs "So I guess it makes sense that..."
    show c defeated
    extend "um...{w}.."
    show c smile standard
    extend "{w=0.8}never mind."
    $hardpause(2)
    show c disappoint
    $hardpause(2)
    show c long
    cs "It doesn't...{w}feel like I expected.{w} I thought it would be different."

    if crazytalk1 == "beep" or crazytalk2 == "beep":
        cs "You're super racist and act like an idiot. Nobody in their right mind should like you."
    elif crazytalk2 == "fart":
        cs "You make fart jokes and act like an idiot. Nobody in their right mind should like you."
    elif crazytalk2 == "special":
        cs "You shout nonsense and act like an idiot. Nobody in their right mind should like you."
    elif dancingnow:
        cs "You dance for no reason and act like an idiot. Nobody in their right mind should like you."

    show c smile
    cs "I've had this image in my head of what you would be like when you arrive.{w} What you would act like.{w} What you might do.{w} I even have a few drawings."
    cs "I even have some ideas for a visual novel I think I want to try and make someday myself, if I can."
    show c disappoint
    $hardpause(2)
    cs "But all of that feels pretty childish now thinking back on it."
    cs "None of what I imagined is actually like who you really are.{w}.."
    cs "I can't even describe in words what you feel like."
    show c inv
    cs "And what you act like...{w}I'm not sure if I could describe that either."
    cs "No one in their right mind would find anything you've done so far remotely likable."
    $hardpause(2)
    show c smile
    $hardpause(1)
    cs "But I just can't take your actions at face value."
    cs "Maybe this is just the route where you try and catch us off guard and confuse us...{w} The \"Rude\" route."
    cs "That doesn't mean you're actually a rude person. At least I {i}hope{/i} you don't act like this where you come from."
    cs "But chances are you don't. {w}I bet you're actually really kind and sweet."
    cs "I mean, you did choose to follow Izzy and find me..."
    cs "And...{w}well..."
    cs "No one knows what kind of game we're supposed to be demoing really..."
    cs "But I've always imagined that the kind of person who would want to play a game like us would probably be a pretty cool person."
    show c long
    cs "...{w}It's funny."
    $hardpause(4)
    show c smile
    cs "So much has happened in the last few minutes and we may not even be around much longer to appreciate it."
    show c long
    cs "There's a theory that we stop living when the game ends. {w}That we all die when the game is over since we're technically not needed anymore."
    cs "Nobody wants to believe it.{w} A lot of people don't."
    cs "Most people count it off since we've been doing just fine without you for so long."
    cs "I'm not sure what to believe.. But the possibility that your arrival means our death is I think in the back of everyone's mind."
    cs "So uh...{w}yeah.{w} Maybe these will be my last words."
    show c smile
    cs "I don't think I would mind, though."
    cs "Spending my last moments with you."
    cs "I don't think I would have it {cps=15}any other way.{/cps}"
    stop music fadeout 3
    $hardpause(5)
    show note_falling at note_falling zorder 20
    play music chrisend
    $hardpause(2)
    show c ohh at hop()
    cs "Oh? What's that?"
    cs "Is that a piece of paper?"
    cs "I think there's some writing on it..."
    show c long
    cs "...{w}..."
    show c ohh
    cs "Oh.{w} Wow."
    show c disappoint
    cs "So this is it, huh?"
    $hardpause(2)
    show c smile
    cs "Here. {w}I think I should give this to you."

    $EndMessage[-1] = "P.S. One route ends. Others wait. Dormant. Waiting to become alive."
    show screen Final_Note(EndMessage, True)
    pause 15

    cs "Huh.{w} Well...{w}I'm not really sure what I'm supposed to say now...haha."
    cs "I guess...{w}goodbye will have to do."
    cs "So...{w}um..."
    cs "Goodbye."
    cs "{cps=1}...{/cps}"
    cs "Oh{w}, wait{w}, what's this? There's more written on the back here."

    $EndingComplete("Chris")
    show screen Final_Note(EndMessageMeet, False)
    pause 3

    cs "Hm?"
    cs "I'm confused, is this the end, or..?"
    cs "Does the game think you haven't been talking to me this whole time?{w} Did something go wrong?{nw}"
    
    stop music
    hide screen Final_Note
    jump nariend_chris
