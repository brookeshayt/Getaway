
label day3_start:
    scene black
    with fade
    "Day 3"
    scene cabin_day 
    "[player_name] is helping Nash and Mavis around camp"
    show nash smirk at Left
    n "Hey Mav! Pass me that log!"
    show mavis happy at Right
    m "ONE LOG COMING UP! (throw's log towards Nash)"
    n "Thanks Mav (sound of axe hitting wood)"
    hide mavis happy
    "Nash looks up at you"
    n "Help me take these to the firepit for me will yah?"
    "[player_name] brings the wood to the firepit. the rest of the group is sitting by the fire."
    show mavis happy at Right
    m "There we go all set. Try not to murder us with your cooking this time, huh?"
    show nash sigh at Left
    n "Rude! I've improved tremendously. Though I still doubt Ezra would eat it. They haven't touched my cooking since day one."
    hide mavis happy
    show ezra disgusted sunglasses at Right
    e "(visibly shudders) Nash, I was bed ridden with food poisoning for 3 days."
    n "Seriosuly, you're being dramatic."
    n "(turns to Farren) was it really that bad?"
    hide ezra disgusted sunglasses
    show farren at Right
    f "(Nods) *mimicking a gagging reaction*"
    hide nash sigh
    hide farren
    show mavis happy at Left
    m "Haha! Even Farren agrees."
    hide mavis happy
    show cole glasses neutral at Left
    c "I am not l-looking foward to eating later..."
    hide cole glasses neutral
    show ezra disgusted sunglasses at Left
    e "That makes at least two of us"
    hide ezra sunglasses
    show nash sigh at Left
    n "*groans* It's not my fault cooking is hard."
    show farren at Right
    f "(snickers) and shakes his head"
    hide farren
    "Nash brushes off farren's reaction and reaches to touch the book Cole is writing in."
    n "Hey Cole, what are you writing in there?"
    show cole shocked closed at Right
    c "(yanks book back abruptly)"
    n "You good?"
    c "Y-yeah, just... please d-don't touch my stuff."
    n "Damn, sorry. I was just curious"
    c "It's fine, I'm just self c-conscious about people reading my s-stuff..."

    scene black
    with fade
    "Later that day, at the campfire"
    scene group_night2_fire 
    with fade
    "Everyone starts to feel strangely drowsy after dinner and jokes about Nash putting something in the food."
    "Zalea is leaning on Ezra’s shoulder basically asleep and Ezra is looking concerned at everyone’s drowsy state of mind"
    show mavis neutral at Left
    m "Anyone else feel drowsy?"
    hide mavis neutral
    show ezra concerned at Left
    e "...You all look like you're about to collapse.."
    hide ezra concerned
    show cole shocked closed at Left
    c "(looks ill) Ezra was right, it really was bad."
    hide cole shocked closed
    show nash smirk at Left
    n "*slurred voice* Nuh-uh, you're just- jealous of my cooking skills."
    show ezra concerned sunglasses ar Right
    e "This isn't food posioning. Nash, did you drug the food..?"
    n "h-huh? No, I didn't slug the roof. What-does that-evenmean?"
    e "OOOOOoookaayyyy."
    hide nash sigh
    hide ezra concerned sunglasses
    show cole shocked closed at Left
    c "I d-don't feel good, I'm gonna h-head in..."
    hide cole shocked closed
    show ezra concerned at Left
    "Ezra looks over at Zalea who is about to fall over, he gives a short sigh"
    e "I’m gonna get this one to bed (Ezra gestures towards Zalea). And then head to bed myself, you good here Nash?"
    hide ezra concerned
   
    if nash_is_bunkmate:
        jump day3_nash_survives
    else:
        jump day3_nash_dies

label day3_nash_survives:
    $ nash_alive = True
    $ farren_alive = True
    p "I'm going to help bring Nash back to the cabin, he seems pretty out of it."
    show cole glasses neutral at Left
    c "Do you-u need h-help moving him?"
    show ezra at Right
    e "No, it's okay Cole. I'll help [player_name] with him."
    c "O-okay, if you're sure. Zalea was asking for you"
    e "It's fine, I got this, just tell her I'll be there in a minute."
    hide ezra
    "Cole stands there awkwardly for a moment then nods and heads to his cabin."
    hide cole neutral
    "You're on one side of Nash and Ezra is on the other. You both carry him back to the cabin."
    show ezra concerned at Left
    e "There we go, idiot would've stayed out there all night.. If you're good here I'm going to head to bed."
    "In the distance you hear Zalea calling for Ezra"
    z "Ezraaaaaa, I'm tireddd. Hurry up!"
    e "Haha, duty calls, I'll see you in the morning!"
    jump day3_end
    

label day3_nash_dies:
    $ nash_alive = False
    $ farren_alive = False
    show nash sigh at Right
    n "yeahyeah...I'll be in in a bit- *snore*"
    e "alright then."
    n "*continues snoring*"
    hide nash sigh
    hide ezra concerned
    "Nash passes out in his chair and everyone else heads to bed. You were the last to be with Nash but decide to head to your cabin"

    scene black
    with fade
    "In a half-awake state you hear the sound of a muffled conversation outside. You can hear what you think is Nash's voice but the other voice is too quiet to make out."
    n "What... fuck.. you.. doing"
    n "st-STOP- sOMEOne- HEL---"
    n "..."
    "You fall back asleep without fully realizing what's happening"
    jump day3_end

label day3_end:
    scene black
    "You and your freinds sleep through the night"
    jump day4_start

    "The End... so far"
    $ renpy.pause(hard=True)
    