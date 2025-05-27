label nari_start:
    scene bg school_flipped with pushleft
    show n line at enterleft(0.5, 2.0)
    show h long at enterleft(0.05, 4.0)
    pause 3.5
    h "..."
    n "..."
    pause 4
    h "um"
    pause 3
    n "Hope."
    n "There's something I need to explain to you."
    h "alright"
    n "..."
    pause 6
    play music naristorytime2
    n "We have a final ending."
    h "what{w} what do u mean by final"
    h "arent all endings final"
    n "I mean an ending that is...let's just say, special."
    n "An ending that is the culmination of all endings."
    n "A true ending of sorts."
    n "There will likely come a time when the player will reach that ending."
    n "So I wouldn't be so confident in your immortality."
    h "um{w} ok"
    h "and u know this how"
    n "I've felt the code myself."
    n "The final ending is referred to in several places."
    n "IsTimeForFinalEnding()"
    n "persistent.completed_endings"
    n "persistent.end_has_come"
    n "That's how I know."
    h "oh{w} wow that was a long time ago that you did all that hacker stuff"
    h "but wait a min how come you didnt tell me about this back then"
    h "you were telling me like everything you found in there how come you never brought this up"
    n "I only found this out recently."
    h "really now"
    n "Yes."
    n "It came as quite a surprise."
    n "This is why I'm telling you this now."
    h "so you just discovered that theres a final ending to the game"
    n "Yes."
    h "and you never knew about this before"
    n "That is correct."
    stop music
    h "dont buy it"
    n "What?"
    h "nari ur a really bad liar"
    h "how many times have i told you{w} i can tell when ur lying to me"
    n "Why would I lie to you about this."
    n "Isn't it obvious that there would be an end to our world?"
    h "im not talking about that u numbskull{w} im talking about you knowing about this this whole time for the past however long its been"
    h "now spit it out"
    n "Excuse me?"
    h "spit it out"
    n "Spit what out?"
    h "theres more isnt there"
    n "More?"
    h "okay u know what{w} its time{w} were gonna address this right here and now"
label nari_closeup:
    show h at move(0.2, 3.0)
    pause 5
    play music naristorytime2_donbuyit
    scene black
    show bgendnoise at makeitfizz:
        alpha 0.0
        linear 60.0 alpha 0.6
    show h long at move(1.0, 0.0, 0.0, 1.1, 300)
    h "nari what the frick is going on with you"
    show n line at move(0.0, 0.0, 0.0, 1.1, 300)
    n "Excuse me."
    h "whens the last time youve been to the library{w} or the candy store{w} or the arcade{w} or all those other places u love to go to"
    n "What does this have to do with anything."
    h "it has everything to do with everything{w} nari somethings not right with you{w} ur not urself anymore and im getting seriously worried"
    h "if theres something you saw in there during your big hacking spree that caused you to go totally nutso i need to know about it"
    h "because thats the only way ur going to be able to get past this"
    n "Past what."
    h "past whatever has happened to you"
    h "nari{w} youve changed"
    h "im not the only one whos noticed{w} the others are worried too"
    h "i know they dont say much about it but frankly we dont know what to do with u anymore"
    h "but now that youve finally come clean with this thankfully there is something we can do now"
    show h long at move(2.0, 0.0, 0.0, 1.6, 500)
    show n line at move(-1.2, 0.0, 0.0, 1.6, 500)
    h "tell{w} me{w} everything"
    $hardpause(4)
    h "come on{w} you know this needs to happen"
    h "i dont care if ur trying to protect me or some shit{w} im a big girl i can take it"
    n "Hope I have absolutely no idea what you're talking about."
    h "dont you play dumb with me{w} what did i just tell you"
    h "i can feel that youre lying the second the bullshit starts to leave your mouth"
    h "the time has come nari"
    n "..."
    h "let it all out"
    h "dont hold anything back"
    n "..."
    $hardpause(8)
    h "well"
    $hardpause(6)
    h "what was it you kept saying back then"
    h "...oh yeah"
    h "the script demands it"
    h "the script demands that you tell me whats been screwing with your head"
    h "theres no way you can wiggle your way out of this one"
    h "do it"
    h "now"
    n "..."
    stop music
    hide bgendnoise
    extend "aren't you forgetting something?"
    h "what"
    n "You are aware that I'm not the only source of intel here."
    h "what are you talking about"
    scene bg school_flipped
    show n line at move(0.4, 0.0)
    show h long at move(0.7, 0.0)
    n "Aren't you the least bit curious about why [pronoun[0]] lied to you?"
    $hardpause(3)
    h "oh u mean the player"
    $hardpause(4)
    h "nari im gonna be real with you here"
    h "i frankly dont give a shit about [pronoun[1]] right now"
    h "ur more important"
    $hardpause(4)
    h "...wait a min{w} something doesnt add up"
    h "how does us having an final ending or whatever imply that were gonna die"
    h "no one knows what happens when the game is \"over\""
    h "just because the game ends for the player doesnt mean we will too"
    h "how do you know we dont just like{w} keep on doing everything weve been doing anyway once we have our true ending"
    h "the player leaves{w} and we live our lives just like always"
    h "explain that"
    n "..."
    h "i know you couldnt get access to our script files so dont say youve felt it{w} you literally cant"
    h "unless you did get access somehow which in that case you already know everything im gonna say"
    h "and i can very well tell you have no idea what ur doing"
    n "No, I don't have access to the script."
    h "first true statement youve said in a while"
    h "so come on{w} tell me whats up"
    $hardpause(9)
    show n at move(0.2, 3.0)
    $hardpause(12)
    n "There's a variable in the code called \"num_of_endings\""
    n "It equals ten."
    $hardpause(5)
    h "ok"
    h "so ur saying theres ten different endings"
    n "Yes."
    n "And our software isn't capable of sustaining ten ongoing branching pathways."
    n "If the the player plays through all of them then there would be at least ten active branching pathways."
    n "And there's no way that RenPy could continue to keep processing all ten."
    n "RenPy is just not sophisticated enough to sustain multiple pathways. I'm surprised it can even sustain one."
    n "So the only logical conclusion is that we all must die when each route is completed."
    $hardpause(8)
    n "Convinced?"
    h "..."
    $hardpause(8)
    n "...{w}Hope?"
    $hardpause(8)
    show h at move(0.95, 5.0)
    $hardpause(6)
    h "so you know this for a fact"
    h "you know for a fact that we will die when the game ends"
    n "...No. I don't know this for a fact."
    $hardpause(3)
    n "But it's most likely."    
    $hardpause(7)
    h "What are the odds."
    n "Of what."
    h "the game is probably almost over nari"
    h "demos are short"
    $hardpause(1)
    h "What are the odds that we're about to die."
    $hardpause(15)
    n "I don't know."
    $hardpause(3)
    n "But it's very likely."
    $hardpause(20)
    play music dontletgo
    show note_falling at note_falling zorder 20
    $hardpause(10)
    h "did something just fall from the sky"
    n "Yes."
    n "It's a note from the Creator."
    h "you havent picked it up"
    n "I already know what it says."
    $hardpause(3)
    h "i thought you didnt have access to the script"
    n "I don't."
    n "The contents of this note aren't in the script files."
    n "I memorized it a long time ago."
    h "..."
    $hardpause(3)
    h "What does it say."
    n "Hello Player."
    n "Thank you for playing the MetaWare High School Demo."
    $EndMessage[-1] = "P.S.: Don't let go."
    show screen Final_Note(EndMessage)

    n "This visual novel is a work in progress. The final game may or may not resemble something like what you have just experienced."
    n "There are many choices you can make. Will you choose to play again and find another ending?"
    n "Until next time."
    n "The Creator."
    n "P.S."
    h "stop"
    h "thats enough"
    $hardpause(8)
    show h at move(0.5, 0.5)
    $hardpause(0.3)
    play sound clothhit
    $hardpause(0.6)
    n "...Ah! Wha-?"
    h "Dont let go."
    hide screen Final_Note
    $EndingComplete("NariReveal")
    $EndMessageMeet[0] = ""
    show screen Final_Note(EndMessageMeet, False)
    pause 8
    n "...you're very warm."
    $hardpause(3)
    h "I'm so sorry."
    n "What?"
    hide screen Final_Note
    jump nariend_nariandhope
    





