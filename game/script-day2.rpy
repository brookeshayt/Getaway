label day2_start:
    scene black
    with fade
    "Day 2"
    scene cabin_morning
    with fade
    "The next morning, you wake up to the sound of birds chirping and the smell of fresh pine. You step outside your cabin and take a deep breath of the crisp morning air."
    
    "While your group is not big on mornings, most are up and at em' by 8am, Jade and Ezra are the last to get up."
    "You see Jade exit her cabin and sit on a nearby stump. She pulls out a hand mirror and a black liquid liner."

    scene firepit_day
    with fade
    "You and the rest of the group are sat around the firepit"
    show zalea flower at Left
    z "I'm going to go grab some coffee, anyone want some?"
    hide zalea flower
    "Zalea scans her eyes over Mavis and Nash already holding a mug, they must have brought their own. Zalea moves her eyes over to Mavis and Nash."
    show mavis neutral at Left
    m "I'm good, thanks."
    hide mavis neutral
    show nash smirk at Left
    n "Same here."
    hide nash smirk
    "Zalea pans to Cole"
    show zalea flower at Left
    z "Cole, do you want coffee?"
    hide zalea flower
    show cole glasses neutral at Left
    c "H-huh? Oh uh... no thankyou. I can get it myself"
    hide cole glasses neutral
    show zalea judging flower at Left
    z "*shrugs* Suit yourself."
    hide zalea judging flower
    "Zalea walks off to her cabin to make her coffee, and you can see her through the window as she makes it." 
    "She pulls out her instant coffee contained in a plastic bag, puts a spoonful or two in a mug and adds water. Z seems to be in a good mood, humming to herself as she works."
    show cole glasses neutral at Left
    c "H-has anyone seen Ezra? I thought he would have been u-up by now."
    hide cole glasses neutral
    show nash happy at Left
    n "*visibly amused* Nah, that one sleeps like a fucken rock, I swear you could run a lawnmower right outside their window and they’d sleep right through it."
    hide nash happy
    show cole glasses smirk at Left
    c "Oh... okay, right. I forgot ha-ha, I guess I'll just wait for them to wake up then."
    hide cole glasses smirk

label day2_midday:
    scene firepit_day
    with fade
    show zalea flower at Left
    z "Oh hey Ez.. I saved you some coffee."
    hide zalea flower
    show ezra sunglasses at Left
    "Ezra sits next to Jade and takes the coffee"
    e "Thanks Z"
    hide ezra sunglasses
    show zalea flower at Left
    z "I feel like were missing someone"
    hide zalea flower
    show nash smirk at Left
    n "Hmm... now that you mention it, has anyone seen Jade yet this morning?"
    hide nash smirk
    show zalea flower at Left
    z "I thought I saw her leave her cabin to go put on her makeup. But that was a while ago..."
    hide zalea flower
    show mavis neutral at Left
    m "I'll go check the cabins"
    hide mavis neutral
    "Mavis returns a few minutes later, looking concerned."
    show mavis neutral at Left
    m "I didn't see her in or near the cabins..."
    hide mavis neutral
    show ezra sunglasses at Left
    "Ezra is suddenly awake and alert"
    e "She's not the type to just wander off."
    hide ezra sunglasses
    show cole glasses neutral at Left
    c "M-maybe we should go look for her"
    hide cole glasses neutral
    show zalea judging flower at Left
    z "Agreed..."
    hide zalea judging flower

"You join the group to look for Jade"

label camp_map_jade:
    menu:
        "Cabin":
            $ interactions_count += 1
            jump cabin2
        "Firepit":
            $ interactions_count += 1
            jump firepit2
        "Cabin Closeup":
            $ interactions_count += 1
            jump cabin_closeup2 

label cabin2:
    scene cabin_day
    with fade
    "Cabin 1 is the closest to the entrance, and you can see it from the road. It has a nice porch and a cozy vibe. 3 and 4 look a little worn down"
    jump camp_map_jade

label firepit2:
    scene firepit_day
    with fade
    "A great place for roasting marshmallows and sharing you deepest DARKEST secrets." 
    jump camp_map_jade

label cabin_closeup2:
    scene stairs_day
    with fade
    "just some stairs."
    show bracelet at Center
    "A green bracelet was found on the ground, It looks to be held together by fine string and beads."
    show screen item_hotbar_icons
    $ collect_hotbar_item("bracelet", "images/icons/bracelet.png")
    hide bracelet
    jump jades_death

label jades_death:
    scene jades_death
    with dissolve
    "As you examine the bracelet, you look closer at the cabin and see a figure under the stairs."
    p "Oh shit, is that...?"
    "You yell at the group and tell them your found Jade. Everyone rushes over."
    show zalea shocked flower at Left
    z "I-is she d-dead??"
    hide zalea shocked flower
    "Mavis bends down to check for a pulse"
    show mavis sad at Left
    m "*nods* I don't feel a pulse"
    hide mavis sad
    "Mavis gently closes Jade's eyes. The whole group stands in shock."
    show nash frown at Left
    n "Now what?... I mean yeah, she was kind of a bitch but I don't think that warrranted murder."
    hide nash
    show cole shocked closed at Left
    c "H-How do we know she's been murdered?"
    hide cole shocked closed
    show mavis shocked at Left
    m "We don't and I refuse to point fingers without proper evidence."
    hide mavis shocked
    "Everyone stands in silence for a moment, still processing the gravity of the situation."
    show nash frown at Left
    n "Why don't we recount what happened from when we all woke up until now."
    hide nash frown
    show cole shocked closed at Left
    c "Yeah... that's a good idea."
    hide cole shocked closed
    show zalea judging flower at Left
    z "Does anyone know who was with her last?"
    hide zalea judging flower
    show nash frown at Left
    n "*shrugs* No idea, I'm pretty sure most of us have been at the campfire all morning. Everyone except... (Nash looks at Ezra)"
    show ezra shocked sunglasses at Right
    e "*raises an eyebrow* Me?"
    hide nash frown
    show mavis neutral at Left
    m "Ezra, you were the only other group member missing, the rest of us were at the campfire."
    show ezra disgusted sunglasses at Right
    e "Serously Mavis? I might not have liked her but I wouldn't have killed her!"
    show mavis disgusted at Left
    m "Chill Ez, I'm not accusing you of anything. I'm just trying to figure out who was with her last."
    show ezra angry sunglasses at Right
    e "*glares*"
    hide mavis neutral
    hide mavis disgusted
    hide ezra disgusted sunglasses
    hide ezra angry sunglasses
    show cole shocked at Left 
    c "L-let's all j-just c-c-calm down. I'm sures t-there's a perfectly reasonable explanation for all of this."
    hide cole shocked
    show nash frown at Left
    n "Cole's right. Besides, how do we know it wasn't [player_name]. They're the one who found her."
    hide nash frown
    show farren angry at Left
    f "*narrows eyes at [player_name] ..."
    jump p_response

label p_response:
    hide farren angry
    "What do you want to say [player_name]?"
    menu:
        "It wasn't me!":
            jump defensive
        "I was with the group all morning.":
            jump alibi
        "Say nothing":
            jump silent

label defensive: 
    show nash frown at Left
    n "That's exactly what a murderer would say. MURDEeRuR."
    show ezra at Right
    e "Enough Nash, let's talk to everyone about what they did this morning before we accuse anyone."
    hide nash frown
    hide ezra
    jump group
label alibi: 
    show farren at Left
    f "...(nods once)"
    hide farren
    show zalea judging flower at Left
    z "I trust Farren's judgement, he seems to believe [player_name]."
    hide zalea judging flower
    jump group
label silent:
    p "..."
    show cole glasses neutral at Left
    c "Y-you ok?"
    hide cole glasses neutral
    show mavis neutral at Left
    m "Let's just step back and talk about what everyone did this morning"
    hide mavis neutral 
    jump group

label group:
    show ezra at Right
    e "Let's all sit down and talk things out.."
    hide ezra 
    jump jade_chat

label jade_chat:
    scene firepit_lit
    with dissolve
    "The rest of the group gathers around the firepit"
    "Talk to your friends to get their perspectives"

label talk_to_friends:
    menu:
        "Talk to Zalea":
            jump zalea_chat
        "Talk to Mavis":

            jump mavis_chat
        "Talk to Nash":

            jump nash_chat
        "Talk to Cole":

            jump cole_chat
        "Talk to Ezra":

            jump ezra_chat
        "Talk to Farren":

            jump farren_chat
        "Continue with the story":
            jump day2_end

label zalea_chat:
    show zalea flower at Left
    menu:
        "Where were you this morning?":
            z " I was sitting with you guys at the shelter, and I was with Ezra during the search"
            hide zalea flower
            jump talk_to_friends
        "Do you think it was Ezra?":
            z "God no, Ezra didn’t like her but they wouldn’t have done that."
            hide zalea flower
            jump talk_to_friends
        "How do you feel about Jade?":
            z "I invited her to come with us because she didn’t have a ton of friends, she could be kind of mean but I didn’t mind having her around."
            hide zalea flower
            jump talk_to_friends
   

label mavis_chat:
    show mavis neutral at Left
    menu:
        "Where were you this morning?":
            m "I was making breakfast cause I was the first one awake, and Nash came to help me out a little later. I was checking the campfire with Nash during the search."
            hide mavis neutral
            jump talk_to_friends
        "Who do you think it was?":
            m "I have no idea, and I don’t want to point any fingers. It’s how you start to lose sight of the real truth."
            hide mavis neutral
            jump talk_to_friends
        "How do you feel about Jade?":
            m "Jade? She was kind of rude, but she wasn’t all that bad and is actually rather reliable if you could get past her backhanded compliments. She didn’t deserve to die like that."
            hide mavis neutral
            jump talk_to_friends
    

label nash_chat:
    show nash frown at Left
    menu:
        "Where were you this morning?":
            n "I was helping Mavis with breakfast after I woke up, and was with you guys afterwards. I was checking by the campfire, during the search."
            hide nash frown
            jump talk_to_friends
        "Did you see anything at all this morning?":
            n "(shakes head) no I haven’t, sorry. I was too busy helping with breakfast."
            hide nash frown
            jump talk_to_friends
        "How do you feel about Jade?":
            n "I mean.. she was kind of a bitch, but I didn’t hate her."
            hide nash frown
            jump talk_to_friends
   

label cole_chat:
    show cole glasses neutral at Left
    menu:
        "Where were you this morning?":
            c "I-I was with you guys the whole time, I woke up after Farren. And I was checking by the camp entrance during the search."
            hide cole glasses neutral
            jump talk_to_friends
        "Did you hear or see anything this morning?":
            c "Not-t that I rem-member, there-e was nothing o-out of the ordinary"
            hide cole glasses neutral
            jump talk_to_friends
        "How do you feel about Jade?":
            c "S-she was kind of rude but I didn’t hate her.. not really. S-she pushed me a-around a lot but no one d-deserves to die."
            hide cole glasses neutral
            jump talk_to_friends
    

label ezra_chat:
    show ezra at Left
    menu:
        "Where were you this morning?":
            e "Asleep, as I usually am in the morning. I didn’t kill Jade, I was with Zalea during the search."
            hide ezra
            jump talk_to_friends
        "Did you hear anything in the area? Considering you were the last one awake.":
            e "No, like I said I was sleeping and no I didn’t see anything when I woke up."
            hide ezra
            jump talk_to_friends
        "How do you feel about Jade?":
            e "I may not have liked her all that much she used to be really rude to Z, but I wouldn’t risk jail time over something so petty."
            hide ezra
            jump talk_to_friends

label farren_chat:
    show farren at Left
    menu:
        "Where were you this morning?":
            f "(stares then nods towards the campfire)"
            hide farren
            jump talk_to_friends
        " Z said you're quite observant, did you see anything?":
            f "(looks away as if recounting thoughts)"
            "Farren gestures towards Ezra, and mimicking a sleeping pose."
            hide farren
            jump talk_to_friends
        "How do you feel about Jade?":
            "Farren just shrugs. [player_name] assumes he's neutral on the topic."
            hide farren
            jump talk_to_friends

label day2_end:
    scene firepit_lit
    with fade
    p "I didn't find anything concrete."
    show cole glasses neutral at Left
    c "What e-even is there to talk about?"
    hide cole glasses neutral
    show zalea frustrated flower at Left
    z "oh I don’t know that she’s DEAD!? And that every single one of you wasn’t keen on her being around…"
    hide zalea frustrated flower 
    show nash frown at Left
    n "I mean... She was kind of a jerk"
    hide nash frown
    show mavis angry at Right
    m "That doesn't warrant killing her!!"
    show nash angry at Left
    n "I didn't say it did!"
    hide nash angry
    hide mavis angry
    show ezra concerned sunglasses at Left
    e "Let's back track. She wasn’t under the cabin when any of us woke up, right? So when, and how was she moved there?" 
    e "We all have a basic understanding about where everyone was, [player_name] found Jade.."
    hide ezra concerned sunglasses
    show zalea judging flower at Left
    z "This is useless, obviously no one would just openly admit to killing anyone."
    show ezra concerned sunglasses at Right
    e "True.."
    hide zalea judging flower
    hide ezra concerned sunglasses
    show cole glasses neutral at Left
    c "Does anyone-e e-even know how s-she died?"
    show ezra concerned sunglasses at Right
    e "(With a look of focus) No, but I'll take a look and see what I can find."

    scene jades_death
    with fade
    show nash frown at Left
    show ezra concerned sunglasses at Right
    n "So... what do you see?"
    e "Looks like a contact based substance from her makeup.. there’s a burn near her eye that looks pretty severe…"
    hide nash frown
    hide ezra concerned sunglasses
    show zalea judging flower at Left
    z "Okay, but even expired product wouldn't just kill her..."
    hide zalea judging flower
    show mavis neutral at Left
    m "Maybe her stuff was tampered with? But I don't like what that implies..."
    hide mavis neutral
    show nash frown at Left
    n "And what exactly does that imply?"
    hide nash frown
    show zalea sad flower at Left
    z "One of us killed her..."
    hide zalea sad flower
    show mavis neutral at Left
    m "If that's the case, we need evidence. I think I saw Jade's makeup by the abandoned cabin, maybe we can find some clues there."
    hide mavis neutral
    show farren at Left
    f "(nods)"
    hide farren
    "Mavis comes back holding a bag"
    show mavis neutral at Left
    m "Z, you know the most about makeup and Jade, why don't you check if anything is off?"
    hide mavis neutral
    "Zalea takes a peek inside the bag"
    show zalea judging flower at Left
    z "Well her eyeliner isn’t there, she used it every day so it wouldn’t make sense if she left it behind."
    show mavis neutral at Right
    m "I didn't see anything else by her bag. But how could it have been tampered with?"
    hide zalea judging flower
    hide mavis neutral
    show ezra concerned sunglasses at Left
    e "toxins and illnesses can be absorbed into the body through your eyes. It’d have to be a really high dosage though."
    show cole glasses neutral at Right
    c "How do you even k-know that?"
    e "(raises an eyebrow) I work as a Forensic Toxicologist."
    hide ezra concerned sunglasses
    show zalea judging flower at Left
    z "Oh- I forgot you re-united with us recently.. Ezra's pretty amazing!"
    c "I d-did, I-I don't doubt it!"
    hide zalea judging flower
    hide cole glasses neutral
    show mavis neutral at Left
    m "This is... a lot to handle. Why don't we take a break for now."
    hide mavis neutral
    "The group falls silent for the second time today"
    scene black 
    scene jades_death
    show cole glasses neutral at Left
    c "S-so now what do we do... we can't j-just leave her like that, r-right?"
    show nash frown at Right
    n "Shouldn't we be leaving? Calling the cops or something?"
    c "I don't know if that's the b-best idea. We don't know what happened yet. W-We might get blamed without p-proper e-v-idence."
    n "I hadn't even thought about that."
    hide cole glasses neutral
    show zalea judging flower at Left
    z "So we're staying then...?"
    hide zalea judging flower
    n "Looks like it."
    hide nash frown
    show zalea judging flower at Left
    z "What do we do about Jade?.."
    show ezra concerned sunglasses at Right
    e "We should probably bury her, we can't just leave her body out here."
    hide zalea judging flower
    hide ezra concerned sunglasses
    "What do you think [player_name]?"
    menu:
        "Agree with Ezra":
            p "Yeah, I think that's the best option for now."
            jump conclusion
        "Suggest calling the cops":
            jump call_cops
        "Say nothing":
            p "..."
            jump conclusion

label call_cops:
    scene black
    with fade
    "This actaully isn't an option... sucks to be you."
    jump conclusion

label conclusion:
    "Mavis and Ezra go to move Jade and bury her off screen out of respect the group holds a small funeral. Despite some better judgement, the group decides to stay to try and solve this."
    "End of Day 2"

    scene black
    with fade
    "You lost a friend today"
    window hide
    play sound "audio/death gong.mp3" 
    show jade closeup at Center
    pause 2
    show jade blank at Center
    pause 2
    show jade blood at Center
    pause 2

    jump day3_start
