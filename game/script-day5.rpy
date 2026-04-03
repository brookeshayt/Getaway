
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
    z "What makes you so sure we’d even get blamed in the first place!"
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

    scene bunkbeds
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

    scene broken_cabin
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
    jump van_crash

label van_crash:
    "Mavis grabs [player_name] and books it to the car."
    "You and Mavis hop in the van and she stomps on the gas, you make it about a yard out before..."

    scene black
    with fade
    "HE FUCKED WITH THE VAN!! I CAN'T STOP."
    "Screeeeeeeech. BOOM."

    scene blurry_crash
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
            jump van_crash


label day5_start_good:
    scene cabin_day
    with fade
    show mavis
    m "Hey, has anyone seen my keys? I kind of need them in order to leave.."
    show ezra
    e "No sorry Mavis…I’ll keep an eye out, I can’t find my sunglasses either.."
    hide ezra
    show nash
    n "Oh shoot I forgot I borrowed your keys yesterday sorry Mavis.."
    m "Why'd you have my keys?"
    n " noticed your engine bay was and sure enough it was tampered with.."
    m "what do you mean tampered with?"
    n "The break lines were cut and it looks like more was done but I can’t be sure."
    hide nash
    show ezra concerned
    e "well that’s just fantastic. Can you fix it?"
    hide ezra
    show nash
    n "I would have tried ..but my tools are missing outta Mavis’ car."
    m "So we’re just stuck here then?"
    hide nash
    show ezra
    e " well the owner said-"
    hide ezra
    show cole
    c "I’m sure if we find Nash’s tools we can get the van fixed!"
    hide cole 
    show nash
    n "I don’t know I mean I could try but the issues seem far more severe than a bit of tinkering."
    show zalea
    z "you’re the car guy Nash so I guess we should trust your judgement."
    hide nash
    hide zalea
    show cole
    c "speaking of Nash’s tools I can’t seem to find my journal either"
    hide cole
    show zalea
    z "And my hair flower is also missing."
    hide zalea
    show mavis
    m "My keys are also still, missing unless you still have them Nash."
    show nash
    n "Right yeah sorry, here you go…"
    m "Thanks, not that it means much considering we’re still stranded"
    hide nash
    hide mavis
    show ezra
    e "right… so whose missing what exactly? I’m missing my sunglasses"
    hide ezra 
    show nash
    n "Tools"
    hide nash
    show zalea
    z "My hair clip."
    hide zalea
    show cole
    c "m-my journal but I can look for that on my own…"
    hide cole
    show ezra
    e "Farren? You missing anything"
    show farren
    hide ezra
    f "(Points at face aggressively)"
    show nash
    n "What does that mean? your missing your face? wait where's your mask?"
    f "(Sighs exasperated)"
    n "Ohhhh- that’s what your missing."
    f "(Nods)"
    hide nash
    hide farren
    show ezra
    e "[player_name] are you missing anything?"
    p "No I’m not"
    e "alright"
    hide ezra
    show mavis
    m "I was but we’ve found my keys. No thanks to Nash."
    hide mavis
    show nash
    n "Hey!"
    hide nash
    show cole
    c "looks like we’re stuck here a bit longer then…"
    show zalea
    z "I guess..you don’t seem all to worried Cole"
    c "Me? I’m sure we’ll figure it out, we’ve survived this long… and now we know the van is broken so we won’t crash"
    hide zalea
    show ezra
    e "Hm"
    hide ezra
    c "Plus, I really wanna find my journal it’s really important.."
    show zalea
    z "Do you need help looking for it?"
    c "NO!!- I mean I’m sure I can manage you guys have your own stuff to look for"
    hide zalea 
    hide cole
    show mavis
    m "I guess we better get searching then.."
    hide mavis
    "Search the camp and talk to everyone."
    jump search_camp

label search_camp:
    menu:
        "Cabins":
            scene cabin_day
            show cole
            p "Hey Cole did you find your journal?"
            show cole
            c "Uhm No but it’s fine, I don’t need any help!"
            p "you’re sure? I think I might’ve seen it over-"
            show cole
            c "I SAID ITS FINE! Just leave me alone!"
            p "Okay damn I’ll leave you be!"
            hide cole
            jump search_camp

        "Lake":
            scene dock
            jump search_camp

        "Fire Pit":
            scene firepit_day
            show zalea
            show farren
            p "Where did you guys see your things last"
            f "(Mimicks is a sleeping pose)"
            z "Same here, I had it when I went to bed and when I woke up it was gone. No idea where it went."
            p "I’ll keep looking."
            hide farren
            hide zalea
            jump search_camp

        "Camp entrance":
            scene camp_entrance
            show nash
            show mavis
            n "I told you Mavis I can’t fix it here!"
            m "I spent my hard earned money on this car I refuse to believe it’s done for!"
            n "If I knew where my tools were then I’d at least try to fix the breaks but I don’t so I can’t!"
            m "Whatever I’m gonna go finish packing!"
            hide mavis
            n "HEY WAIT- Mavis-"
            n "Oh hey player sorry can’t talk right now..You find my tools yet?"
            p "No not yet sorry Nash."
            n "No? That’s fine I’m sure we’ll find them."
            hide nash
            jump search_camp

        "Meet with group":
            jump next
        
  
label next:
    scene cabin_day
    with fade
    "You find Nash's tools in a bush in the main camp area"
    p "Hey Nash! I found your tools!"
    "Nash comes joggong over and everyone else follows behind."
    show nash frown at Left
    n "Wait seriously? In a bush?"
    show mavis angry at Right
    m "Great the tools, literally everything else is missing though! And my Van is still broken!"
    n "You act as if I’m the one who broke it, which I’m not!"
    hide mavis angry
    hide nash frown
    show cole ng frown at Left
    c "Well you are the Mechanic Nash, what are we supposed to think?"
    show ezra concerned at Right
    e "No offence Cole,  but I don’t Nash has the brains to plan something like this!"
    hide ezra concerned
    hide cole ng frown
    show nash frown at Left
    n "See!? Thank you- hey wait a minute did you just call me dumb?"
    show zalea judging at Right
    z "You are a little slow sometimes, no offence"
    n "Am not! Mavis tell them I'm not."
    hide zalea judging
    show mavis 
    m "I mean..occasionally.."
    hide mavis
    n "unbelievable!"
    e "anywayssss why don’t we start gathering all our belongings by the van maybe we’ll find our stuff in the process!"
    n "Yeah whatever, Nash takes his tools and goes to gather his stuff."

    "Group gathers belongings in front of the camp sign but still doesn’t find their belongings"

    e "seriously? Still nothing?"
    c "maybe it’s a sign we’re supposed to stay..? find out what happened?"
    z "Yeah cause the universe wants us to stay in a camp, YOU invited us too in the middle of no where after one of our friends just died."
    e "Z-"
    c "You mean YOUR friend died, none of us actually liked Jade!"
    z "That’s not true! sure she could be a little mean but-"
    c "Really? She’d been nothing but mean to me, Ezra said it themselves that they didn’t like her."
    e "..."
    "Zalea and Cole start to argue and it starts to get pretty heated."
    "Zalea screams in frustration and Pushes Cole backwards causing him to stumble backwards and drop his bag, Cole scrambles to gather all of his belongings back into his bag."

    e "Woah! Calm down both of you"
    z "He started it!"
    c "She pushed me! psycho!"
    z "who the hell are you calling a psycho! I'll show you-"

    "Farren approaches the player looking distressed"
    f "(Points at face then at Cole's bag"
    p "what are you doing?"
    f "(sighs frustrated. and goes up to Cole and yanks on his bag trying to pull it open"
    c " H-Hey! What the hell Farren!"
    "Cole shoves Farren off of him spilling his bag all over the ground revealing all the missing items."
    "Cole's Journal lands open and reveals some very disturbing notes. and details describing that he planned to kill all his friends"

    show mavis
    m "What the Fuck is that?"
    hide mavis

    show ezra
    e "You- You better start explaining yourself!"
    show cole
    c "You weren't Supposed to see that!"
    hide Cole
    show zalea
    z "He has all our stuff!"
    hide zalea
    show cole
    c "This wasn't supposed to happen! you were all supposed to die!"
    hide cole

    show nash
    n "Shut up, Freak"
    hide nash

    show cole
    c "(laughing) you were supposed to be next Zalea! Then Ezra!" 
    c "At least you and Ezra would have died together."
    hide cole

    "nash tackles Cole!"
    
    "Nash knocks Cole out, They find out that it was Cole who killed Jade and find out that he had planned this entire trip to attempt to kill everyone off"
    "They make their way to the owners Cabin 20 mins away and Cole is arrested and they all make it home safe, (sorry we ran outta time)"
    jump the_end


label the_end:
    "The End"
    scene end credits
    with fade
    $ renpy.pause(hard=True)
