
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
    scene   
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




label day5_start_good:
    scene black
    with fade
    "Day 5"
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

p "Do you remember where you had your sunglasses last?
e "Not really I think I set them on my end table last night? But they were gone this morning…"
p "alright I’ll keep looking.."

p "Where did you guys see your things last"
f "(Mimicks is a sleeping pose)"
z "Same here, I had it when I went to bed and when I woke up it was gone. No idea where it went."
p "I’ll keep looking."




label the_end:
    "The End"
    $ renpy.pause(hard=True)
