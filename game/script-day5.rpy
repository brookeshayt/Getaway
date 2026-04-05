
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
    show zalea frustrated at Left
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
    hide cole ng frown
    show zalea frustrated at Left
    z "..."
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
    show zalea frustrated at Left
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
    c "oh... hey Mavis. [player_name]."
    show mavis shocked at Left
    m "What the hell did you do!"
    c "Me? Oh, I'm just finishing what I started. Isn’t it beautiful? I figured it was only fair they died together."
    c "True love... y'know?"
    show mavis angry at Left
    m "You're a freak!"
    m "I'm gonna be sick. We need to get out of here. NOW."
    hide mavis angry
    c "Leaving? Already? You’re just gonna abandon your friends?"
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
    show cole workshop
    with fade
    show cole wk shadow
    show cole whistle wk
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
    show mavis neutral at Left
    m "Hey, has anyone seen my keys? I kind of need them in order to leave.."
    show ezra concerned at Right
    e "No sorry Mavis…I’ll keep an eye out, I can’t find my sunglasses either.."
    hide ezra concerned
    show nash frown at Right
    n "Oh shoot I forgot I borrowed your keys yesterday sorry Mavis.."
    m "Why'd you have my keys?"
    n " noticed your engine bay was and sure enough it was tampered with.."
    m "what do you mean tampered with?"
    n "The break lines were cut and it looks like more was done but I can’t be sure."
    hide nash frown
    show ezra concerned at Left
    e "well that’s just fantastic. Can you fix it?"
    hide ezra concerned
    show nash frown at Left
    n "I would have tried ..but my tools are missing outta Mavis’ car."
    show mavis neutral at Right
    m "So we’re just stuck here then?"
    hide mavis neutral
    hide nash frown
    show ezra concerned at Right
    e " well the owner said-"
    hide ezra
    show cole glasses neutral at Left
    c "I’m sure if we find Nash’s tools we can get the van fixed!"
    hide cole glasses neutral
    show nash frown at Left
    n "I don’t know I mean I could try but the issues seem far more severe than a bit of tinkering."
    show zalea judging at Right
    z "you’re the car guy Nash so I guess we should trust your judgement."
    hide nash frown
    hide zalea judging
    show cole glasses neutral at Left
    c "speaking of Nash’s tools I can’t seem to find my journal either"
    hide cole glasses neutral
    show zalea sad at Right
    z "And my hair flower is also missing."
    hide zalea sad
    show mavis neutral at Right
    m "My keys are also still, missing unless you still have them Nash."
    show nash frown at Left
    n "Right yeah sorry, here you go…"
    m "Thanks, not that it means much considering we’re still stranded"
    hide nash frown
    hide mavis neutral
    show ezra concerned at Left
    e "right… so whose missing what exactly? I’m missing my sunglasses"
    hide ezra concerned
    show nash frown at Left
    n "Tools"
    hide nash frown
    show zalea sad at Right
    z "My hair clip."
    hide zalea sad
    show cole glasses neutral at Left
    c "m-my journal but I can look for that on my own…"
    hide cole glasses neutral
    show ezra concerned at Left
    e "Farren? You missing anything"
    show farren nm at Right
    hide ezra concerned
    f "(Points at face aggressively)"
    show nash frown at Left
    n "What does that mean? your missing your face? wait where's your mask?"
    f "(Sighs exasperated)"
    n "Ohhhh- that’s what your missing."
    f "(Nods)"
    hide nash frown
    hide farren nm
    show ezra concerned at Left
    e "[player_name] are you missing anything?"
    p "No I’m not"
    e "alright"
    hide ezra concerned
    show mavis disgusted at Right
    m "I was but we’ve found my keys. No thanks to Nash."
    hide mavis disgusted
    show nash angry at Left
    n "Hey!"
    hide nash angry
    show cole glasses neutral at Left
    c "looks like we’re stuck here a bit longer then…"
    show zalea judging at Right
    z "I guess..you don’t seem all to worried Cole"
    c "Me? I’m sure we’ll figure it out, we’ve survived this long… and now we know the van is broken so we won’t crash"
    hide zalea judging
    show ezra concerned at Right
    e "Hm"
    hide ezra concerned
    c "Plus, I really wanna find my journal it’s really important.."
    show zalea
    z "Do you need help looking for it?"
    c "NO!!- I mean I’m sure I can manage you guys have your own stuff to look for"
    hide zalea judging
    hide cole glasses neutral
    show mavis neutral at Left
    m "I guess we better get searching then.."
    hide mavis neutral
    "Search the camp and talk to everyone."
    jump search_camp

label search_camp:
    menu:
        "Cabins":
            scene cabin_day
            show cole glasses neutral at Left
            p "Hey Cole did you find your journal?"
            c "Uhm No but it’s fine, I don’t need any help!"
            p "you’re sure? I think I might’ve seen it over-"
            hide cole glasses neutral
            show cole angry mouth at Left
            c "I SAID ITS FINE! Just leave me alone!"
            p "Okay damn I’ll leave you be!"
            hide cole angry mouth
            jump search_camp

        "Lake":
            scene dock
            jump search_camp

        "Fire Pit":
            scene firepit_day
            show farren nm at Left
            p "Where did you guys see your things last"
            f "(Mimicks is a sleeping pose)"
            show zalea sad at Right
            z "Same here, I had it when I went to bed and when I woke up it was gone. No idea where it went."
            p "I’ll keep looking."
            hide farren nm
            hide zalea sad
            jump search_camp

        "Camp entrance":
            scene camp_entrance
            show nash angry at Left
            show mavis disgusted at Right
            n "I told you Mavis I can’t fix it here!"
            m "I spent my hard earned money on this car I refuse to believe it’s done for!"
            n "If I knew where my tools were then I’d at least try to fix the breaks but I don’t so I can’t!"
            m "Whatever I’m gonna go finish packing!"
            hide mavis disgusted
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
    hide nash frown
    hide zalea judging
    show mavis neutral at Left
    m "I mean..occasionally.."
    hide mavis neutral
    n "unbelievable!"
    show ezra concerned at Right
    e "anywayssss why don’t we start gathering all our belongings by the van maybe we’ll find our stuff in the process!"
    hide ezra concerned
    show nash frown at Left
    n "Yeah whatever."
    hide nash frown
    "Nash takes his tools and goes to gather his stuff."
    scene black
    with fade
    "Group gathers belongings in front of the camp sign but still doesn’t find their belongings"

    scene camp_entrance
    with fade

    show ezra concerned at Left
    e "seriously? Still nothing?"
    hide ezra concerned
    show cole ng frown at Left
    c "maybe it’s a sign we’re supposed to stay..? find out what happened?"
    hide cole ng frown
    show zalea frustrated at Left
    z "Yeah cause the universe wants us to stay in a camp, YOU invited us too in the middle of no where after one of our friends just died."
    hide zalea frustrated
    show ezra concerned at Left
    e "Z-"
    hide ezra concerned
    c "You mean YOUR friend died, none of us actually liked Jade!"
    show zalea frustrated at Left
    z "That’s not true! sure she could be a little mean but-"
    show cole ne frown at Left 
    c "Really? She’d been nothing but mean to me, Ezra said it themselves that they didn’t like her."
    hide zalea frustrated
    show ezra concerned at Right
    e "..."
    hide ezra concerned
    hide cole ng frown

    "Zalea and Cole start to argue. It starts to get pretty heated."
    "Zalea screams in frustration and Pushes Cole backwards causing him to stumble backwards and drop his bag, Cole scrambles to gather all of his belongings back into his bag."
    show ezra concerned at Left
    e "Woah! Calm down both of you"
    hide ezra concerned
    show zalea frustrated at Left
    z "He started it!"
    show cole ng frown at Right
    c "She pushed me! psycho!"
    z "who the hell are you calling a psycho! I'll show you-"
    hide cole ng frown
    hide zalea frustrated

    "Farren approaches [player_name] looking distressed"
    show farren scowl nm at Left
    f "(Points at face then at Cole's bag)"
    p "what are you doing?"
    f "(sighs frustrated. and goes up to Cole and yanks on his bag trying to pull it open)"
    show cole ng frown at Right
    c " H-Hey! What the hell Farren!"
    hide cole ng frown
    hide farren scowl nm

    "Cole shoves Farren off of him spilling his bag all over the ground revealing all the missing items."
    "Cole's Journal lands open and reveals some very disturbing notes. and details describing that he planned to kill all his friends"

    show mavis shocked at Left
    m "What the Fuck is that?"
    hide mavis shocked

    show ezra angry at Left
    e "You- You better start explaining yourself!"
    hide ezra angry
    show cole ng frown at Right
    c "You weren't Supposed to see that!"
    hide cole ng frown
    show zalea frustrated at Left
    z "He has all our stuff!"
    hide zalea frustrated
    show cole ng frown at Right
    c "This wasn't supposed to happen! you were all supposed to die!"
    hide cole ng frown

    show nash angry at Left 
    n "Shut up, Freak"
    hide nash angry 

    show acole smile at Left
    c "(laughing) you were supposed to be next Zalea! Then Ezra!" 
    c "At least you and Ezra would have died together."
    hide acole smile
    "nash tackles Cole!"
    
    "Nash knocks Cole out, They find out that it was Cole who killed Jade and find out that he had planned this entire trip to attempt to kill everyone off"
    "They make their way to the owners Cabin 20 mins away and Cole is arrested and they all make it home safe, (sorry we ran outta time)"
    jump the_end


label the_end:
    "The End"
    scene end credits
    with fade
    $ renpy.pause(hard=True)
