
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



label day5_start_good:
    scene black
    with fade
    "Day 5"




    
label the_end:
    scene black
    with fade
    "The End"
    scene end credits
    with fade
    $ renpy.pause(hard=True)
