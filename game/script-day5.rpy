
label day5_start_variants:
    scene black
    with fade
    "Day 5"
    "The choice is yours... choose wisely"

    scene camp_entrance
    with fade
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
    "COLE FUCKED WITH THE VAN!! I CAN'T STOP."
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
    "You and those that are left spend the mornings searching the camp for your items and any other clues."
    scene bunkbeds_broken
    with fade
    "You search inside an abandoned cabin and find a bunch of missing items. Including a torn journal page."

    show journal page at Center
    show screen item_hotbar_icons
    $ collect_hotbar_item("journal page", "images/icons/journal page.png")
    " You find a ripped out page on the ground that lists a very detailed description of each of your friends and their habits."
    hide journal page

    "You show the Ezra, Mavis and Zaleas what you found, you all decide to confront Cole about the page."
    scene cabin_night
    "Cole is in his cabin packing his things whistling to himself."
    show cole glasses smirk at Left
    c "O-oh hey guys! What’s up?"
    hide cole glasses smirk
    "Ezra blocks the door and Mavis stands in front of him. Zalea stands near Ezra and player stands with Mavis."
    "Mavis holds up the paper that player found in Cole’s notebook." 
    show cole shocked closed at Left
    c "W-what is that? W-where did you find that."
    show Mavis angry at Right
    m "[player_name] said it’s a page from your journal? It’s got some pretty disturbing detailed notes about us."
    hide Mavis angry
    hide cole shocked closed
    show cole shocked at Left
    c "I-I don’t know what you're talking about…"
    show ezra disgusted sunglasses at Right
    e "If you’re telling the truth you won’t mind showing us that journal to prove yourself."
    c "my journal is private I don’t want people looking in it, is that so wrong?" 
    hide ezra disgusted sunglasses
    hide cole shocked
    show zalea frustrated flower at Left
    z "It is if you’re some sort of stalker freak! "
    hide zalea frustrated flower
    show mavis neutral at Left
    m "Ez is right though…"
    m "If you’re innocent, show us the book. The writing won’t match if it’s not yours."
    hide mavis neutral
    "Cole tightens his grip on his journal his grip so tight his knuckles turn white" 
    show cole angry mouth at Left
    c "Seriously!? Mavis what happened to not pointing fingers..some friends you are.."
    show mavis angry at Right
    m "That was before  we had evidence you might be.."
    hide cole angry mouth
    hide mavis angry
    show cole angry at Left
    c "Might be what? A killer?"
    show ezra disgusted sunglasses at Right
    e "Enough Cole! If you're innocent just show us the damn book and we’ll leave you alone. "
    c "I-I can’t do that, it's embarrassing…"
    hide cole angry
    hide ezra disgusted sunglasses
    "Ezra nods at Mavis and Mavis tackles Cole to the ground and Ezra grabs the book. Ezra opens it" 
    show cole angry at Left
    c "H-hey!"
    hide cole angry
    show era disgusted sunglasses at Left
    e "Well that’s not obvious in the slightest…"
    hide era disgusted sunglasses
    "Ezra reads the book and their face goes pale and they look physically sick." 
    "Cole is struggling against Mavis and ends up throwing her off of him and sprints towards the door."
    "Zalea tries to block the door but Cole pulls a knife on her."
    show ezra shocked sunglassesat Left
    e "ZALEA!"
    hide ezra shocked sunglasses
    "Cole barely misses her and slashes her side instead, and shoves her out of the way."
    "Ezra catches her and Mavis scrambles after Cole and tackles him outside. "
    "Ezra is helping Zalea apply pressure to the wound" 
    show zalea shocked flower at Right
    z "Ez…" 
    show ezra shocked sunglasses at Left
    e "Just don’t look at it Z" 
    hide zalea shocked flower
    hide ezra shocked sunglasses
 
    "Ezra wants to stick together. Mavis wants to take the van to go get help."
    "What do you do next?"
    menu:
        "Stick together and walk to the owners cabin":
            jump day5_okay
        "Send mavis in the van to go get help":
            jump van_crash

label day5_okay:
    scene owners_cabin_night
    with fade
    "The group sprints to the owners Cabin with Cole knocked out and slung over Mavis's shoulder."
    "They explain the situation and the owner is horrified. He calls the authorities and an ambulance immediately." 
    "Zalea survives and Cole is arrested"
    jump the_end

label day5_start_good:
    scene cabin_day
    with fade
    show mavis neutral at Left
    m "Hey, has anyone seen my keys? I kind of need them in order to leave.."
    show ezra concerned at Right
    e "No sorry Mavis…I’ll keep an eye out, I can’t find my sunglasses either.."
    hide ezra concerned
    show nash frown at Right
    n "Oh shoot, I forgot I borrowed your keys yesterday sorry Mavis.."
    m "Why'd you have my keys?"
    n "I wanted to top up the oil in the van and noticed the engine bay was a little funky"
    n "Took a closer look and sure enough it was tampered with.."
    m "What do you mean tampered with?"
    n "The break lines were cut and it looks like more was done but I can’t be sure."
    hide nash frown
    hide mavis neutral
    show ezra concerned at Left
    e "well that’s just fantastic. Can you fix it?"
    hide ezra concerned
    show nash frown at Left
    n "I would have tried ..but my tools are missing outta Mavis’ car."
    show mavis neutral at Right
    m "So we’re just stuck here then?"
    hide mavis neutral
    hide nash frown
    show ezra concerned at Left
    e " Well the owner said-"
    hide ezra
    show cole ng frown at Left
    c "I’m sure if we find Nash’s tools we can get the van fixed!"
    hide cole ng frown
    show nash frown at Left
    n "I don’t know, I mean I could try, but the issues seem far more severe than a bit of tinkering."
    show zalea judging at Right
    z "You’re the car guy Nash, so I guess we should trust your judgement."
    hide nash frown
    hide zalea judging
    show cole ng frown at Left
    c "Speaking of Nash’s tools I can’t seem to find my journal either"
    hide cole ng frown
    show zalea sad at Left
    z "And my hair flower is also missing."
    hide zalea sad
    show mavis neutral at Right
    m "My keys... Nash?"
    show nash frown at Left
    n "Right yeah sorry, here you go…"
    m "Thanks, not that it means much considering we’re still stranded"
    hide nash frown
    hide mavis neutral
    show ezra concerned at Left
    e "Right… so whose missing what exactly? I’m missing my sunglasses"
    hide ezra concerned
    show nash frown at Left
    n "Tools"
    hide nash frown
    show zalea sad at Right
    z "My hair clip."
    hide zalea sad
    show cole ng frown at Left
    c "M-my journal but I can look for that on my own…"
    hide cole ng frown
    show ezra concerned at Left
    e "Farren? You missing anything"
    show farren pupils nm at Right
    hide ezra concerned
    f "(Points at face aggressively)"
    show nash frown at Left
    n "What does that mean? your missing your face? Wait where's your mask?"
    hide farren pupils nm 
    show farren scowl nm at Right
    f "(Sighs exasperated)"
    hide farren scowl nm
    n "Oohhhh, gotcha."
    show farren nm at Right
    f "(Nods)"
    hide nash frown
    hide farren nm
    show ezra concerned at Left
    e "[player_name] are you missing anything?"
    hide ezra concerned
    p "No I’m not"
    show ezra concerned at Left
    e "Alright"
    hide ezra concerned
    show mavis disgusted at Left
    m "I was, but we’ve found my keys. No thanks to Nash."
    hide mavis disgusted
    show nash angry at Left
    n "Hey!"
    hide nash angry
    show cole ng frown at Left
    c "Looks like we’re stuck here a bit longer then…"
    show zalea judging at Right
    z "I guess..you don’t seem all to worried Cole"
    c "Me? I’m sure we’ll figure it out, we’ve survived this long… and now we know the van is broken so we won’t crash"
    hide zalea judging
    show ezra concerned at Right
    e "Hm"
    hide ezra concerned
    c "Plus, I really wanna find my journal it’s really important.."
    show zalea judging at Right
    z "Do you need help looking for it?"
    c "NO!!- I mean I’m sure I can manage you guys have your own stuff to look for"
    hide zalea judging
    hide cole ng frown
    show mavis neutral at Left
    m "I guess we better get searching then.."
    hide mavis neutral
    "Search the camp and talk to everyone."
    jump search_camp

label search_camp:
    menu:
        "Cabins":
            scene cabin_day
            p "Hey Cole did you find your journal?"
            show cole ng frown at Left
            c "Uhm No but it’s fine, I don’t need any help!"
            hide cole ng frown
            p "you’re sure? I think I might’ve seen it over-"
            show cole ng frown at Left
            c "I SAID ITS FINE! Just leave me alone!"
            hide cole ng frown
            p "Okay. Damn, I’ll leave you be!"
            jump search_camp

        "Lake":
            scene dock
            pause 2
            jump search_camp

        "Fire Pit":
            scene firepit_day
            p "Farren, Zalea, where did you guys see your things last?"
            show farren nm at Left
            f "(Mimicks is a sleeping pose)"
            show zalea sad at Right
            z "Same here, I had my hair flower when I went to bed and when I woke up it was gone. No idea where it went."
            hide farren nm
            hide zalea sad
            p "I’ll keep looking."
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
            hide nash angry
            show nash sigh at Left
            n "Oh hey [player_name]. sorry can’t talk right now..You find my tools yet?"
            hide nash sigh
            p "No not yet, sorry Nash."
            show nash sigh at Left
            n "No? That’s fine I’m sure we’ll find them."
            hide nash sigh 
            jump search_camp

        "Meet with group":
            jump day5_next
        
  
label day5_next:
    scene cabin_day
    with fade
    "You find Nash's tools in a bush in the main camp area"

    show nash toolbox at Center
    show screen item_hotbar_icons
    $ collect_hotbar_item("nash toolbox", "images/icons/nash toolbox.png")
    p "Hey Nash! I found your tools!"
    "Nash comes jogging over and everyone else follows behind."
    hide nash toolbox

    show nash frown at Left
    n "Wait seriously? In a bush?"
    show mavis angry at Right
    m "Great the tools. Literally everything else is missing though! And my van is still broken!"
    n "You act as if I’m the one who broke it, which I’m not!"
    hide mavis angry
    hide nash frown
    show cole ng frown at Left
    c "Well you are the mechanic Nash, what are we supposed to think?"
    show ezra concerned at Right
    e "No offence Cole.. or Nash, but I don’t think Nash has the brains to plan something like this."
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
    show nash angry at Left
    n "Unbelievable!"
    hide nash angry
    show ezra concerned at Right
    e "Anyways, why don’t we start gathering all our belongings by the van. Maybe we’ll find our stuff in the process!"
    hide ezra concerned
    show nash frown at Left
    n "Yeah, whatever."
    hide nash frown
    "Nash takes his tools and goes to gather his stuff."
    scene black
    with fade
    "Group gathers belongings in front of camp, but still haven't found their belongings"

    scene camp_entrance
    with fade

    show ezra concerned at Left
    e "Seriously? Still nothing?"
    hide ezra concerned
    show cole ng frown at Left
    c "M-maybe it’s a sign we’re supposed to stay..? find o-out what happened?"
    hide cole ng frown
    show zalea frustrated at Left
    z "Yeah cause the universe wants us to stay in a camp, YOU invited us too in the middle of no where after one of our friends just died."
    hide zalea frustrated
    show ezra concerned at Left
    e "Z-"
    hide ezra concerned
    show cole ng frown at Left
    c "You mean YOUR friend died, none of us actually liked Jade!"
    show zalea frustrated at Right
    z "That’s not true! sure she could be a little mean but-"
    c "Really? She’d been nothing but mean to me. Ezra said it themselves that they didn’t like her."
    hide zalea frustrated
    hide cole ng frown
    show ezra concerned at Right
    e "..."
    hide ezra concerned

    "Zalea and Cole start to argue. Ezra stands in the background."
    "Zalea screams in frustration and pushes Cole backwards causing him to stumble and drop his bag"
    "Cole scrambles to gather all of his belongings back into his bag."
    show ezra shocked at Left
    e "Woah! Calm down both of you"
    hide ezra shocked
    show zalea frustrated at Left
    z "He started it!"
    show cole ng frown at Right
    c "She pushed me! Psycho!"
    z "who the hell are you calling a psycho! I'll show you-"
    hide cole ng frown
    hide zalea frustrated

    "Farren approaches [player_name] looking distressed"
    show farren scowl nm at Left
    f "(Points at face then at Cole's bag)"
    hide farren scowl nm
    p "What are you doing?"
    show farren nm at Left
    f "(sighs frustrated. and goes up to Cole and yanks on his bag trying to pull it open)"
    show cole ng frown at Right
    c " H-Hey! What the hell Farren!"
    hide cole ng frown
    hide farren scowl nm

    "Cole shoves Farren off of him spilling his bag all over the ground and revealing all his friends missing items."
    "Zalea's hair clip, Ezra's sunglasses, Farren's mask, Cole's journal..."
    "Cole's journal lands open on the ground, revealing some very disturbing notes."
    "His scribbles painted details describing how he had planned to kill all his friends"

    show mavis shocked at Left
    m "What the Fuck is that?"
    hide mavis shocked

    show ezra angry at Left
    e "You- You better start explaining yourself!"
    hide ezra angry
    show acole nervous at Right
    c "You weren't supposed to see that!"
    hide acole nervous
    show zalea frustrated at Left
    z "He has all our stuff!"
    hide zalea frustrated
    show acole sideye at Right
    c "This wasn't supposed to happen! you were all supposed to die!"
    hide acole sideye

    show nash angry at Left 
    n "Shut up, Freak"
    hide nash angry 

    show acole smile at Left
    c "(laughing) you were supposed to be next Zalea! Then Ezra!" 
    c "At least you and Ezra would have died together."
    hide acole smile
    "Nash tackles Cole!"
    
    "Nash knocks Cole out. He falls to the ground."
    "Everyone stands in shock, staring at Cole's journal and all their strewn items."
    "It was Cole who killed Jade and he had plans to kill everyone else."
    "The rest of the group makes their way to the Owners cabin, lugging Cole along."
    scene owners cabin
    "The owner is shocked to see Cole and immediately calls the police. The group explains everything that happened and the police take Cole into custody."
    "A funeral is held for Jade and the friends go their separate ways."
    with fade
    jump the_end


label the_end:
    "The End... so far"
    scene end credits
    with fade
    $ renpy.pause(hard=True)
