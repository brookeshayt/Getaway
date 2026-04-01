
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

n "I told you Mavis I can’t fix it here!"
m "I spent my hard earned money on this car I refuse to believe it’s done for!"
n "If I knew where my tools were then I’d at least try to fix the breaks but I don’t so I can’t!"
m "Whatever I’m gonna go finish packing"
n "HEY WAIT- Mavis-"
n "Oh hey player sorry can’t talk right now..You find my tools yet?"
p "No not yet sorry Nash."
n "No? That’s fine I’m sure we’ll find them."

p "Hey Cole did you find your journal?"
c "Uhm No but it’s fine, I don’t need any help!"
p "you’re sure? I think I might’ve seen it over-"
c "I SAID ITS FINE! Just leave me alone!"
p "Okay damn I’ll leave you be!"


n "Wait seriously? In a bush?"
m "Great the tools, literally everything else is missing though! And my Van is still broken!"
n "You act as if I’m the one who broke it, which I’m not!"
c "Well you are the Mechanic Nash, what are we supposed to think?"
e "No offence Cole,  but I don’t Nash has the brains to plan something like this!"
n "See!? Thank you- hey wait a minute did you just call me dumb?"
z "You are a little slow sometimes, no offence"
n "Am not! Mavis tell them I'm not."
m "I mean..occasionally.."
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

"nash tackles Cole!"




label the_end:
    "The End"
    $ renpy.pause(hard=True)
