
label day5_start_variants:
    scene black
    with fade
    "Day 5"
    "The choice is yours... choose wisely"

    menu:
    "Spend the morning searching the camp":
        jump okay_variant
    "Spend the morning packing to leave":
        jump bad_variant

label bad_variant:
    scene cabin_day  
    with fade

    show zalea frustrated at Left
    z "remind me why we haven’t gotten the hell outta here yet!?"
    show cole ng frown at Right
    c "Because we might get arrested without proper proof."
    z "you’ve seemed pretty adamant to stay this entire time Cole"
    c "well pardon me for trying to make sure we don’t go to prison!"
    z "What makes you so sure we’d even get blamed in the first place! "
    hide zalea frustrated
    hide cole ng frown
    show ezra concerned at Left
    e "Cole makes a good point, Zalea, we don’t really have anything to prove ourselves.."
    hide ezra concerned
    show mavis neutral at Left
    m "we’re alone with no service and 3 of us have died.. it doesn’t look good."
    hide mavis neutral
    show zalea frustrated at Left
    z "So we’re just sitting ducks then? This is all Cole’s fault, it was his idea to come to this stupid camp in the first place! "
    show cole ng frown at Right 
    c "H-hey! Well if you didn’t invite Jade then maybe she’d still be alive! You knew none of us liked her!"
    z "Well sorry for trying to be nice! Jade had no friends besides us!"
    c "You mean you’re her only friend!"
    hide zalea frustrated
    hide cole ng frown
    show ezra concerned at Left
    e "Enough-"
    hide ezra concerned
    show zalea frustratedat Left
    z "That’s not true, I know she was mean but-you guys didn’t hate her right?"
    hide zalea frustrated
    show mavis neutral at Left
    m "…I didn’t enjoy having her here.."
    hide mavis neutral
    show ezra concerned at Left
    e "I tolerated her because you insisted on her being here…"
    hide ezra concerned
    show cole ng frown at Left
    c "maybe you’re just as shallow and selfish as she was! "
    c "There’s a reason only you liked her!"
    show zalea frustrated at Left
    Z "..."
    hide zalea frustrated
    show mavis neutral at Left
    m "That's enough out of you two!"
    hide mavis neutral
    show ezra concerned at Left
    e "That’s a bit much, don’t you think, Cole? Zalea means well we all know that.."
    hide ezra concerned
    show zalea frustrated at Left
    z "SERIOUSLY!? I can’t do this right now!"
    hide zalea frustrated 
    show cole ng frown at Left
    c "Sure, do what you do best. Run from your problems!"
    hide cole ng frown
    show zalea
    z "…Whatever! I'm gonna go pack! Let me know if you see my hair flower.."
    show ezra concerned at Left
    e "Sorry about her! We’ve all been pretty worked up since Jade…"
    hide ezra concerned
    show cole ng frown at Left
    c "I-it’s okay, I understand, emotions are heightened in stressful situations.."
    hide cole ng frown
    show mavis angry at Left
    m "that still doesn’t give her the right to snap like that!"
    hide mavis angry
    show ezra concerned at Left
    e "Z can be difficult.. just give her time to cool off, she’ll come around.."
    hide ezra concerned
    show mavis neutral at Left
    m "I guess"
    hide mavis neutral
    show cole ng frown at Left
    c "Has anyone seen my journal?..."
    hide cole ng frown
    "The group responds with a collective 'no'"
    show ezra concerned at Left
    e "I might’ve seen it by the fire…"
    hide ezra concerned
    show cole ng frown at Left
    c "O-oh okay I’m gonna go look for it then..I’ll meet up with you guys later…"
    hide cole ng frown
    show mavis neutral at Left
    m "Ez, [player_name], why don’t we go towards the lake maybe attempt to catch some food…?"
    hide mavis neutral
    show ezra concerned at Left
    e "(looks back in he direction of Z)"
    hide ezra concerned

    scene black
    with fade
    "Cut to evening"
    "The group failed to catch any fish"

    scene cabin_day
    with fade
    show ezra disgusted at Left
    e "Well that was useles..."
    show mavis neutral at Right
    m "Yup. Whatever it’s fine we’re leaving tomorrow anyways…speaking of which have either of you seen my keys, I misplaced them while packing earlier…"
    e "Oh shoot yeah sorry, I was using them earlier to load our bags into the van"
    hide ezra disgusted
    hide mavis neutral
    "Ezra hands Mavis her keys"
    show mavis neutral at Left
    m "phew thanks, that's our one way ticket outta here."
    show ezra concerned at Right
    e "Haha yeah, Z mentioned missing her hair flower earlier too and I’m missing my sunglasses…"
    m "Strange.. I’ll make sure to do a thorough search before we head out..."
    e "Good idea. I’m gonna go check on Z."
    m "I’ll go with you… she’s been gone for a while,"
    hide ezra concerned
    hide mavis neutral
    p "I'll join too"
    "[player_name] follows Mavis and Ezra. Ezra enters their cabin."
    show ezra concerned at Left
    e "She's not here..."
    hide ezra concerned
    show mavis shocked at Left
    m "What do you mean?"
    hide mavis shocked
    show ezra concerned at Left
    e "I MEAN she's gone."
    hide ezra concerned
    show mavis neutral at Left
    m "Okay, she couldn't have gone far... let's spread out and look for her."
    hide mavis
    "The group splits up to search for Zalea."
    "While investigating the camp, [player_name] watches Ezra go check the abandoned cabins, you see a hand lying onn the ground ouside the door"
    show ezra shocked at Left
    e "NO! Z!"
    hide ezra shocked
    "Ezra rushes into the cabin and pauses. An arm yanks them inside nd the door slams shut"
    show  mavis shocked at Left
    m "What's going on? Ezra?!"
    hide mavis shocked
    "Mavis rushes towards the door and kicks it down forcefully and immediately looks sick."

    scene ezra_zalea_death
    with fade
    "You look inside and you see Zalea lying dead by the bunk bed. Ezra had been pushed into the bed and its fallen on top of their head crushing their airway."
    show cole pupils ng smirk at Left
    c "oh... hey Mavis. [player_name]."
    hide cole pupils ng smirk
    show mavis shocked at Left
    m "What the hell did you do!"
    show cole pupils ng smirk at Left
    c "Me? Oh, I'm just finishing what I started. Isn’t it beautiful? I figured it was only fair they died together."
    c "True love... y'know?"
    hide cole pupils ng smirk
    show mavis angry at Left
    m "You're a freak!"
    m "I'm gonna be sick. We need to get out of here. NOW."
    hide mavis angry
    show cole pupils ng smirk at Left
    c "Leaving? Already? You’re just gonna abandon your friends?"
    hide cole pupils ng smirk
    "Mavis grabs [player_name] and books it to the car."
    "You and Mavis hop in the van and she stomps on the gas, you make it about a yard out before..."

    scene black
    with fade
    "HE FUCKED WITH THE VAN!! I CAN'T STOP."
    "Screeeeeeeech. BOOM."

    scene blurry crash
    with fade
    "You look to you side and see Mavis unconscious, blood pouring from her head"
    "You are barely conscious, all you hear is a faint whitsle in the background."
    p "...Cole?"
    show cole pupils ng smirk at Left
    c "Lights out...!"
    hide cole pupils ng smirk

    scene black 
    with fade
    "Cole enters his workshop"
    scene workshop
    with fade
    scene wk shadow
    scene whistle wk
    play music "audio/Cole whistle.mp3"
    jump the_end

label okay_variant:
    "You find a bunch of missing items around camp. Including Cole's journal."
    $ collect_hotbar_item("cole notebook", "images/icons/cole notebook.png")
    "the notebook is missing a page. it must have been the one you found earlier. The page lists a very detailed description of each of your friends and theri habits."

    "You show the group and they suggest a few options. Ezra wants to stick together. Mavis wants to take the van to go get help."
    "What do you do next?"
    menu:
        "Stick together and walk to the owners cabin":
            jump day5_start_good
        "Send mavis in the van to go get help":
            jump van scene

label van_scene:
    "Mavis hops in the van and she stomps on the gas, she makes it about a yard out before..."
    scene black
    with fade
    "HE FUCKED WITH THE VAN!! I CAN'T STOP."
    "Screeeeeeeech. BOOM."
    scene blurry crash
    with fade

    "Mavis is unconscious, blood is pouring from her head. Ezra and "



label day5_start_good:
    m "Hey, has anyone seen my keys? I kind of need them in order to leave.."
    e "No sorry Mavis…I’ll keep an eye out, I can’t find my sunglasses either.."
    n "Oh shoot I forgot I borrowed your keys yesterday sorry Mavis.."
    m "Why'd you have my keys?"
    n " noticed your engine bay was and sure enough it was tampered with.."
    m "what do you mean tampered with?"
    n "The break lines were cut and it looks like more was done but I can’t be sure."
    e "well that’s just fantastic. Can you fix it?"
    n "I would have tried ..but my tools are missing outta Mavis’ car"
    m "So we’re just stuck here then?"
    e " well the owner said-"
    c "I’m sure if we find Nash’s tools we can get the van fixed!"
    n "I don’t know I mean I could try but the issues seem far more severe than a bit of tinkering."
    z "you’re the car guy Nash so I guess we should trust your judgement."
    c "speaking of Nash’s tools I can’t seem to find my journal either"
    z "And my hair flower is also missing."
    m "My keys are also still, missing unless you still have them Nash."
    n "Right yeah sorry, here you go…"
    m "Thanks, not that it means much considering we’re still stranded"
    e "right… so whose missing what exactly? I’m missing my sunglasses"
    n "Tools"
    z "My hair clip."
    c "m-my journal but I can look for that on my own…"
    e "Farren? You missing anything"
    f "(Points at face aggressively)"
    n "What does that mean? your missing your face? wait where's your mask?"
    f "(Sighs exasperated)"
    n "Ohhhh- that’s what your missing."
    f "(Nods)"
    e "[player_name] are you missing anything?"
    p "No I’m not"
    m "I was but we’ve found my keys. No thanks to Nash."
    n "Hey!"
    c "looks like we’re stuck here a bit longer then…"
    z "I guess..you don’t seem all to worried Cole"
    c "Me? I’m sure we’ll figure it out, we’ve survived this long… and now we know the van is broken so we won’t crash"
    e "Hm"
    c "Plus, I really wanna find my journal it’s really important.."
    z "Do you need help looking for it?"
    c "NO!!- I mean I’m sure I can manage you guys have your own stuff to look for"
    m "I guess we better get searching then.."

    p "Do you remember where you had your sunglasses last?"
    e "Not really I think I set them on my end table last night? But they were gone this morning…"
    p "alright I’ll keep looking.."
    p "Where did you guys see your things last"
    f "(Mimicks is a sleeping pose)"
    z "Same here, I had it when I went to bed and when I woke up it was gone. No idea where it went."
    p "I’ll keep looking."

    
label the_end:
    scene black
    with fade
    "The End"
    scene end credits
    with fade
    $ renpy.pause(hard=True)
