
label day4_start:
    scene black
    with fade
    "Day 4"

    if farren_alive:
        jump farren_alive
    else:
        jump farren_death

label farren_death:
    scene nash_death
    with fade
    "You wake up to find Nash impaled by a branch on a tree, Mavis is the first to see him."
    
    show ezra sunglasses at Left
    e "What's going on!"
    show mavis shocked at Right
    m "Nash!" 
    hide mavis shocked
    "Ezra looks over to see Nash impaled on the branch and a rare moment of shock crosses their face." 
    show ezra shocked sunglasses at Left
    e "Holy shit."
    show zalea judging flower at Right
    z "What’s going on- oh!"
    hide zalea judging flower
    show zalea shocked flower at Right
    e "Zalea don’t look."
    z "I think I’m gonna be sick.."
    "Farren gestures for Zalea to go with him. They both go to sit down inside the cabin."
    hide zalea shicked flower
    e "I think this proves it’s not accidental, people don’t just-"
    show mavis sad at Right
    m "(shaking her head in denial) I already said I don’t want to point fingers..Who knows what if he simply tripped and fell."
    e "people don’t just trip and impale themselves on branches Mavis.."
    hide ezra shocked sunglasses
    show cole shocked at Left
    c "I don’t understand how this could even happen…"
    p "You know, I thought I heard something last night. I thought I heard Nash talking to someone outside but I couldn’t make out what they were saying."
    p "I thought I was dreaming, I didn’t think it was real until I woke up and saw him like this."
    p "I couln't even push myself to get out of bed, It was like I was weighted down."
    hide mavis angry
    show ezra concerned sunglasses at Left
    e "You’re sure..? You didn’t hear anyone else?"
    p "No, I didn't hear anyone else"
    hide ezra concerned sunglasses
    show mavis angry at Left
    m "Why didn’t you say that sooner? If you heard something why didn’t you help him!"
    show ezra concerned sunglasses at Left
    e "I don’t think player had a choice… I don’t think any of you were sober last night..?"
    hide mavis angry 
    show cole concerned at Right
    c "w-what do you mean?"
    e "I mean you were all so drowsy after dinner that I had to practically carry Zalea back to the cabin."
    hide ezra concerned sunglasses
    show mavis neutral at Left
    m "now that you mention it last night was pretty fuzzy and I slept pretty hard. "
    c "S-same here."
    hide mavis neutral
    show ezra concerned sunglasses at Left
    e "Someone must’ve tampered with the food….based off everyone’s behaviour I’d say it knocked everyone out."
    show mavis neutral at Right
    m "How come you weren’t tired then Ezra?"
    e "Simple, I hadn’t eaten last night."
    hide mavis neutral
    hide ezra concerned sunglasses
    show cole shocked closed at Left
    show ezra angry sunglasses at Right
    c "(looking at Ezra) S-so how do we know you didn’t do it then."
    hide ezra angry sunglasses
    show mavis neutral at Right
    m "we don’t, and none of us would admit it even if we had… we shouldn’t turn on each other without evidence."
    hide cole shocked closed
    show ezra disgusted sunglasses at Left
    e "whatever, can you guys help me move Nash, as horrifying as this is, we should try and stay rational…"
    hide ezra disgusted sunglasses

    scene black
    with fade
    "LATER BY THE CABINS"
    with fade
    "TALK TO EVERYONE" 

label midday_discussion:  
    scene group_day3_fire 
    p "How if everyone feeling about Nash?"
    menu:
        "Ask Ezra?":
            jump ask_ezra
        "Ask Cole?":
            jump ask_cole
        "Ask Zalea?":
            jump ask_zalea
        "Ask Mavis?":
            jump ask_mavis
        "Ask Farren?":
            jump ask_farren
        "Skip to end of day":
            jump day4_end

label ask_ezra:
    show ezra3 sunglasses at Left
    e "He was my best friend yeah he could be a pain in the ass but he was like a brother to me…we grew up together I can’t believe he’s gone.."
    hide ezra3 sunglasses
    jump midday_discussion

label ask_mavis:
    show mavis sad at Left
    m "He was a really close friend to me.."
    m "He could be a little dense but he was a good guy and meant well."
    hide mavis sad
    jump midday_discussion

label ask_zalea:
    show zalea sad flower at Left
    z "He didn’t like me at first, but we wound up being really close after Ezra and I started dating… It doesn’t feel real. That he’s just gone.."    
    hide zalea sad flower
    jump midday_discussion

label ask_cole:
    show cole glasses neutral at Left
    c "He could be a tad irritating. He always bent the rules.. but.. I could tell he was a good person I didn’t hate him we just didn’t get along"
    hide cole glasses neutral
    jump midday_discussion

label ask_farren:
    show farren at Left
    f "..."
    p "You two were pretty close?"
    f "*nods*"
    p "did you hear anything last night? See anything?"
    f "*shakes head no*"
    hide farren
    jump extra_dialogue

label extra_dialogue:
    show mavis neutral at Left
    m "I think it's obvious none of us disliked Nash"
    hide mavis neutral
    show zalea sad flower at Left
    z "Yeah, it’s hard to wrap my head around the fact someone could do something so horrendous."
    hide zalea sad flower
    show ezra concerned sunglasses at Left
    e "yeah…I don’t want to talk about this anymore."
    e "I need some space…"
    hide ezra concerned sunglasses
    jump day4_end

label day4_end:
    scene black
    with fade
    scene group_day3_fire
    show mavis neutral at Left
    m "what are we gonna do about cooking.. if the food is tampered with whose to say the rest of it isn’t "
    hide mavis neutral
    show farren at Left
    f "(Points to lake and a fishing rod against the tree)"
    hide farren
    show ezra sunglasses at Left
    e "I suppose we could try! Do any of us even know how to use a fishing rod?"
    hide ezra sunglasses
    show mavis neutral at Left
    m "No clue"
    show cole glasses neutral at Left
    c "I’ve never even touched one"
    hide cole glasses neutral
    show zalea flower at Left
    z "*shrugs*"
    hide zalea flower
    show ezra sunglasses at Left
    e "I used to know but it’s been a really long time"
    hide ezra sunglasses
    show farren at Left
    f "(nods, and goes to grab the fishing rod)"
    show zalea flower at Right
    z "I don’t know Farren, you can’t swim, and based on recent events I feel like we shouldn’t risk it."
    f "(Huffs and grabs the rod and heads toward the dock.)"
    hide farren
    hide zalea flower
    show cole glasses neutral at Left
    c "I’m sure he’ll be fine…we won’t be far if he needs us.."
    hide cole glasses neutral
    show ezra sunglasses at Left
    e "Farrens responsible enough to know where not to go."
    hide ezra sunglasses
    show zalea flower at Left
    z "Yeah.."
    hide zalea flower

    scene black
    with fade
    "The group splits up while Farren catches Fish. Except he doesn’t come back, it is now dark outside."
    scene group_night3_fire
    show mavis neutral at Left
    m "Do you think he’s caught anything by now?"
    hide mavis neutral
    show ezra concerned sunglasses at Left
    e "We should probably go check on him…"
    hide ezra concerned sunglasses

    scene farren_death
    with fade
    "Farren's body is submerged in the water by the shoreline."  
    show zalea shocked flower at Left
    z "Oh my god.. FARREN!!"
    hide zalea shocked flower
    "The fishing line appear to be wrapped around his hands as if to restrain him."
    show cole shocked at Left
    c "This can’t be an accident anymore.."
    hide cole shocked 
    show mavis shocked at Left
    m "We need to get out of here!"
    hide mavis shocked
    show zalea angry flower at Left
    z "Why did we stay!! We should have left by now we should have gone to get help after Jade! Now three of our friends have died."
    z "THis is your fault COLE! It was your stupid idea to come to this rundown camp in the middle of nowhere!"
    show cole angry teeth at Left
    c "Hey!! Don’t b-blame me!"
    c "How was I supposed to know everyone would end up dying!"
    hide cole angry teeth
    show ezra angry sunglasses at Left
    e "ENOUGH!"
    e "We do need to leave. We will spend tomorrow packing and gathering information we can give to the police for when we go back. "
    hide ezra angry sunglasses
    show mavis sad at Left 
    m "I just want to go home.."
    hide mavis sad
    show ezra concerned sunglasses at Left
    e "Z.. you go sit down at the cabin…you look like you’re gonna pass out."
    show zalea shocked flower at Right
    "Zalea nods"
    hide zalea shocked flower
    e "Cole and Mavis you help me with Farren.. [player_name] can you stay with Z?"
    hide ezra concerned sunglasses
    "You agree"
    "Cole and Mavis help Ezra move Farren."

    scene dock_night
    with fade
    "You sit with Zalea and try to comfort her"
    show zalea sad flower at Left
    z "He was my best friend…"
    hide zalea sad flower

    scene black
    with fade
    "END OF DAY"
    "You lost two more friends today. Be careful with your choices from here on out."
    jump day5_start_variants

label farren_alive:
    #lost items of players#
    "The group spends the day looking around camp for any clues that would lead them to the murderer."
    scene group_day2_fire
    with fade

    show nash smirk at Left
    n "(Nash gestures to the group) I haven’t found anything useful have you guys? I’m still half asleep."
    show ezra disgusted sunglasses at Right
    e "Yeah I don’t think any of you were sober last night…"
    n "Now that you mention it, the food did taste a little strange last night…"
    hide nash smirk
    hide ezra disgusted
    show mavis neutral at Left
    m "I felt really drowsy afterwards..I almost passed out in my chair."
    hide mavis neutral
    show zalea sad flower at Left
    z "I don’t remember much after I ate dinner…"
    hide zalea sad flower
    show ezra concerned sunglasses at Left
    e "…You were pretty out of it too Z."
    hide ezra concerned sunglasses
    show mavis angry at Left
    m "maybe it was just a coincidence..?"
    show zalea frustrated flower at Right
    z "Oh so all of us nearly passing out after eating dinner last night was just a happy little accident?"
    m "I’m trying not to think about it like that!"
    hide mavis angry
    hide zalea frustrated flower
    show cole ng frown at Left
    c "It’s ok Mavis I’m sure Zalea’s just a bit on edge like the rest of us…"
    hide cole ng frown
    show zalea frustrated flower at Left
    z "I’m just trying to be realistic, calling everything a simple coincidence isn’t realistic "
    show mavis neutral at Right
    m "Sorry for trying to be optimistic. maybe we should look around camp again.."
    hide zalea frustrated flower
    hide mavis neutral
    show cole ng frown at Left
    c "Yeah that’s a good idea"
    hide cole ng frown

    scene black
    with fade
    menu:
        "Look around the cabins":
            jump look_cabins
        "Look around the firepit":
            jump look_firepit
        "Look around the lake":
            jump look_lake
        "Look around the woods":
            jump look_woods
        "Meet up with the group":

            jump group_chat

label group_chat: 
    p "Did you see anything while looking around, Ezra?"
    "Maybe you should talk to a few of your friends. You walk up to everyone and ask them if they found anything while looking around."
    show ezra concerned sunglasses at Left
    e "Nothing besides a scrap of fabric… no one’s clothes are damaged though.."
    "Player gains a scrap of tan coloured fabric"
    hide ezra concerned sunglasses
    show zalea judging flower at Left
    z "I’ve been pretty down on my luck.. I’ve not got anything, sorry Player."
    hide zalea judging flower
    show mavis neutral at Left
    m "Nothing, but I can’t seem to find my car keys, Cole had them last but he said he put them with my stuff…"
    hide mavis neutral
    show nash frown at Left
    n "no but my tools seem to be missing out of Mavis’s Van."
    "You talk to Farren next, but he doesn't same much.. except"
    show farren at Left
    f "(Silent for a moment but then hands you an empty pill bottle with the Name scratched out)"
    f "It’s a prescription bottle for extremely strong sleeping medication"
    hide farren 
    p "Do you know who takes sleeping meds?"
    show farren at Left
    f "(Shakes head and shrugs)"
    hide farren 
    show cole ng frown
    c "no sorry if anything I’ve been counter productive, I lost my glasses and my notebook.."
    
    menu:
        "Offer cole help to look for his stuff":
            jump offer_cole_help
        "Wish him good luck finding his items":
            jump wish_cole_luck

label offer_cole_help:
    p "do you need help looking for them?"
    c "NO! haha I mean no thanks I’m sure they’ll turn up soon I don’t want anyone else touching my stuff." 
    c "Can’t trust anyone right now yknow..?"
    hide cole ng frown
    jump meet_up_with_group

label wish_cole_luck:
    p "Good luck finding them then, I’m gonna go meet up with the group"
    c "t-thanks I’ll be there in a minute.."
    hide cole ng frown
    jump meet_up_with_group

label meet_up_with_group:
    scene cabin_day
    with fade
    "Cole comes back with nothing in hand and looks pretty defeated."
    show cole ng frown at Left
    c "Well that was a waste of time did we even find anything useful"
    hide cole ng frown
    show nash frown at Left
    n "Okay hang on let’s just think back, what did we all do last night. "
    show ezra concerned sunglasses at Right
    e "from what I remember.. Nash you cooked. You guys ate, got tired and went to bed and I helped player carry Nash to bed."
    n "Ezra you didn’t eat last night…"
    hide ezra concerned sunglasses
    hide nash frown
    show farren at Left
    f "(Looks suspiciously at Ezra)"
    show ezra angry sunglasses at Right
    e "Seriously Nash!? Again!? It wasn’t me!"
    hide farren
    e "Can we all just stop and think instead of assuming?"
    show nash smirk at Left
    n "Sorry..(laughs nervously)"
    hide ezra angry sunglasses
    show ezra disgusted sunglasses at Right
    e "It’s not my fault your cooking is rancid!"
    hide nash smirk
    hide ezra disgusted sunglasses
    show mavis neutral at Left
    m "How do we know it wasn’t you Nash!"
    hide mavis neutral
    show ezra at Left
    e "Yeah.. the dumbass could’ve died if he was left out there alone,"
    hide ezra
    show farren
    f "… (Narrows looks at player expectantly)"

    $ collect_hotbar_item("pill bottle", "images/icons/pill bottle.png")
    p "Farren found this near the firepit."
    show ezra concerned sunglasses at Left
    e "Sleeping medication. And way too strong of a dosage to be for casual use. The name on the label is scratched out."
    hide ezra concerned sunglasses
    show nash scared at Left
    n "You don't think..."
    hide nash scared
    show mavis neutral at Left
    m "No!! We can’t turn on each other."
    hide mavis neutral
    show ezra disgusted sunglasses at Left
    e "I do think it would be wise not to split up but what if one of us is lying…"
    hide exra disgusted sunglasses
    show cole ng frown
    c "L- let’s not go there…but if the food really was tampered with whose to say the rest isn’t…"
    hide cole
    show Zalea frustrated flower at Left
    z "Cole has a point but we can’t just not eat what the heck do we do instead. "
    hide zalea frustrated flower
    show farren at Left
    f "(Points to the rod resting against a tree)"
    show nash smile at Right
    n "Awe hell yeah! Farren your with me let’s go get us some fish"
    hide nash smile
    show cole frown at Right
    c "You sure Farren? Didn’t Z say you can’t swim..? I could go with Nash instead."
    hide cole frown
    f "(Narrows eyes at Cole and shakes his head)"
    hide farren
    "Farren and Nash go toward the water to catch some fish. "
    
    scene black
    with fade
    "LATER THAT NIGHT"
    scene group_night2_fire
    with fade
    show zalea flowerat Left
    z "That was far better then last night…"
    show ezra sunglasses at Right
    e "mmhhmm"
    hide zalea flower
    hide ezra sunglasses
    show nash sigh at Left
    n "Jesus I get it, it was awful. "
    hide nash sigh
    show mavis happy at Left
    m "It’s okay Nash I’ll help you learn to cook when we go home.."
    hide mavis happy
    show cole ng frown at Left
    c "I don’t know about any of you but I’m really tired… I’m gonna head in."
    hide cole ng frown
    show nash at Left
    n "Me too,..I think that’s a good plan, sleep off whatever this is."
    hide nash
    show mavis neutral at Left
    m "I agree"
    hide mavis neutral
    show zalea flower
    z "I think we should probably try and get out of here ASAP like pack up and leave tomorrow morningkind of thing."
    show cole ng frown at Right
    c "I don’t know Z… we still don’t know exactly what happened with Jade…"
    hide zalea flower
    show zalea judging flower at Left
    z "So what I refuse to stay here any longer then necessary!"
    hide cole ng frown
    show ezra sunglasses at Left
    e "I agree with Z here let’s back up and leave tomorrow. And hopefully we can find our stuff.."
    hide ezra sunglasses
    show nash smirk at Left
    n "yeah… all those in favour of leaving tomorrow say I!"
    hide nash smirk
    "The group collectively says I and agrees to leave"
    show cole frown at Left
    c "I guess that’s a fine idea, I just hope we can find my stuff before then.."
    hide cole frown

    scene black
    with fade
    "SUMMARY"
    "Did someone tamper with the food if so then who..?"
    "Farren seems to be paying close attention to his surroundings, might be worth talking to him again tomorrow."
    jump day5_start_good

 
    
    
