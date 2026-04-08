# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("[player_name]", color="#5CF7C5")
define z = Character("Zalea", color="#dc57bb")
define e = Character("Ezra", color="#9248c6")
define m = Character("Mavis", color="#e18849")
define n = Character("Nash", color="#d64545")
define f = Character("Farren", color="#55cbd3")
define j = Character("Jade", color="#5acf5a")
define c = Character("Cole", color="#306330")

transform Left:
    xalign 0.0
    yalign 1.0
    zoom 0.5
transform Right:
    xalign 1.0
    yalign 1.0
    zoom 0.5
transform Center:
    xalign 0.5
    yalign 0.5
    zoom 0.5

#####################
#     Player name   #
#####################
default player_name = "Player"
default nash_is_bunkmate = False
default nash_alive = True
default farren_alive = True

screen name_input_screen():
    modal True
    zorder 200

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 800
        background "#111d"
        padding (30, 20)

        vbox:
            spacing 20
            text "Choose your name:" size 36 xalign 0.5
            
            input default "" value VariableInputValue("player_name") length 20 xalign 0.5
            
            textbutton "Start Game" xalign 0.5 action Return()

# The game starts here.
label start:

    call screen name_input_screen

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black
    with fade
    "A group of six friends decided that this summmer was going to be one for the books"
    "AND... You're invited!"
    "A get a way of sorts"
    "They're not too sure why they booked a campsite, no one quite likes camping but they found themselves drawn to the forest anyways."
    "Disclaimer: Blood and Death :)"

    scene car_on_road
    with fade

    show jade upset at Left
    j "How long till we get there?" 
    hide jade upset

    show mavis neutral at Left
    m "Ermm. I’d say about 15 minutes?"
    hide mavis neutral
   
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "zalea happy.png" to the images
    # directory.

    show jade upset at Left
    "Jade scoffs and looks out the window"
    hide jade upset
    "Mavis rolls her eyes and turns up the music"
    
    scene black
    with fade

    scene camp_entrance
    with fade
    
    "Mavis hits the brakes and parks the red van" 
    "Alright. We're here."
    show jade upset at Left
    j "Jade gestures with two hands in the air and a sarcastic tone" 
    "Yippee."
    hide jade upset
    "Mavis gets out to grab her bags and everyone else follows suit. Ezra walks up to the camp entrance and looks around"
    show ezra at Left
    e "I found a note left by the camp owner, wanna see it?"

    menu:
        "Sure, show me the note.":
            jump shownote
        "No thanks, I don't like to read.":
            jump nonote

    label shownote:
        $ shownote = True
        "Ezra pulls out the note and shows it to you, it reads: “Welcome to Camp Getaway! We hope you enjoy your stay. Please note that cabins 3-4 are off limits due to maintenance. If you need anything, my place is a 20 minute walk from here. -Camp Owner”"
        show owner note at Center
        with dissolve

        "Maybe you should keep the note, just in case you need it later. It will be stored in your hotbar."
        hide owner note
        hide ezra

        show screen item_hotbar_icons
        $ collect_hotbar_item("owner note", "images/icons/owner note.png")
        "Look at that, a handy dandy hotbar! You can click on the note to read it again, or you can click on it later if you forget what it says."
        
        $ bunkmate_count = 0
        $ selected_bunkmates = []
        "Now its time to pick your bunkmates. You can choose up to 3 bunkees"
        jump pickabunkee

    label nonote:
        $ nonote = True
        "Ezra shrugs and puts the note back in his pocket"
        hide ezra

        "Everyones standing outside the entrance waiting to enter, you can’t help but feel a little uneasy about the note. You wonder what it says."

        $ bunkmate_count = 0
        $ selected_bunkmates = []
        "Now its time to pick your bunkmates. You can choose up to 3 bunkees"
        jump pickabunkee

    
    label pickabunkee:
        scene bunkmates
        $ use_custom_choice = False
    
        if bunkmate_count >= 3:
            jump bunkmate_done

        "Click to learn more about each character. [3 - bunkmate_count] picks left."
        menu:
            "Room with Mavis?" if "Mavis" not in selected_bunkmates:
                jump mavisbio
            "Room with Jade?" if "Jade" not in selected_bunkmates:
                jump jadebio
            "Room with Farren?" if "Farren" not in selected_bunkmates:
                jump farrenbio
            "Room with Cole?" if "Cole" not in selected_bunkmates:
                jump colebio
            "Room with Nash?" if "Nash" not in selected_bunkmates:
                jump nashbio
            "Room with Ezra?" if "Ezra" not in selected_bunkmates and bunkmate_count < 2:
                jump ezrabio
            "Room with Zalea?" if "Zalea" not in selected_bunkmates and bunkmate_count < 2:
                jump zaleabio
      
    label mavisbio:
        scene camp_entrance
        show mavis happy at Left
        show mavisbio at Transform(zoom=0.4, xalign=0.5, ypos=100)
        $ use_custom_choice = True
        menu:
            "Pick Mavis":
                $ selected_bunkmates.append("Mavis")
                $ bunkmate_count += 1
                "Great! You'll room with Mavis. [3 - bunkmate_count] picks left."
                hide mavisbio
                hide mavis happy
                if bunkmate_count >= 3:
                    jump bunkmate_done
                jump pickabunkee

            "Don't pick Mavis":
                hide mavisbio
                hide mavis happy
                jump pickabunkee

    label jadebio:
        scene camp_entrance
        show jade happy at Left
        show jadebio at Transform(zoom=0.4, xalign=0.5, ypos=100)
        $ use_custom_choice = True
        menu:
            "Pick Jade":
                $ selected_bunkmates.append("Jade")
                $ bunkmate_count += 1
                "Great! You'll room with Jade. [3 - bunkmate_count] picks left."
                hide jadebio
                hide jade happy
                if bunkmate_count >= 3:
                    jump bunkmate_done
                jump pickabunkee

            "Don't pick Jade":
                hide jadebio
                hide jade happy
                jump pickabunkee

    label farrenbio:
        scene camp_entrance
        show farren at Left
        show farrenbio at Transform(zoom=0.4, xalign=0.5, ypos=100)
        $ use_custom_choice = True
        menu:
            "Pick Farren":
                $ selected_bunkmates.append("Farren")
                $ bunkmate_count += 1
                "Great! You'll room with Farren. [3 - bunkmate_count] picks left."
                hide farrenbio
                hide farren
                if bunkmate_count >= 3:
                    jump bunkmate_done
                jump pickabunkee
                
            "Don't pick Farren":
                hide farrenbio
                hide farren
                jump pickabunkee

    label colebio:
        scene camp_entrance
        show cole glasses smirk at Left
        show colebio at Transform(zoom=0.4, xalign=0.5, ypos=100)
        $ use_custom_choice = True
        menu:
            "Pick Cole":
                $ selected_bunkmates.append("Cole")
                $ bunkmate_count += 1
                "Great! You'll room with Cole. [3 - bunkmate_count] picks left."
                hide colebio
                hide cole glasses smirk
                if bunkmate_count >= 3:
                    jump bunkmate_done
                jump pickabunkee

            "Don't pick Cole":
                hide colebio
                hide cole glasses smirk
                jump pickabunkee

    label nashbio:
        scene camp_entrance
        show nash smile at Left
        show nashbio at Transform(zoom=0.4, xalign=0.5, ypos=100)
        $ use_custom_choice = True
        menu:
            "Pick Nash":
                $ selected_bunkmates.append("Nash")
                $ bunkmate_count += 1
                "Great! You'll room with Nash. [3 - bunkmate_count] picks left."
                hide nashbio
                hide nash smile
                if bunkmate_count >= 3:
                    jump bunkmate_done
                jump pickabunkee

            "Don't pick Nash":
                hide nashbio
                hide nash smile
                jump pickabunkee

    label ezrabio:
        scene camp_entrance
        show ezra sunglasses at Left
        show ezrabio at Transform(zoom=0.4, xalign=0.5, ypos=125)
        $ use_custom_choice = True
        menu:
            "Pick Ezra (and Zalea - THEY COME AS A PACKAGE DEAL)":
                $ selected_bunkmates.extend(["Ezra", "Zalea"])
                $ bunkmate_count += 2
                "Great! You'll room with Ezra and Zalea. [3 - bunkmate_count] picks left."
                hide ezrabio
                hide ezra sunglasses
                if bunkmate_count >= 3:
                    jump bunkmate_done
                jump pickabunkee

            "See more about Zalea?":
                hide ezrabio
                hide ezra sunglasses
                jump zaleabio
                
            "Don't pick Ezra":
                hide ezrabio
                hide ezra sunglasses
                jump pickabunkee

    label zaleabio:
        scene camp_entrance
        show zalea excited flower at Left
        show zaleabio at Transform(zoom=0.4, xalign=0.5, ypos=125)
        $ use_custom_choice = True
        menu:
            "Pick Zalea (and Ezra - THEY COME AS A PACKAGE DEAL)":
                $ selected_bunkmates.extend(["Zalea", "Ezra"])
                $ bunkmate_count += 2
                "Great! You'll room with Zalea and Ezra. [3 - bunkmate_count] picks left."
                hide zaleabio
                hide zalea excited flower
                if bunkmate_count >= 3:
                    jump bunkmate_done
                jump pickabunkee

            "See more about Ezra?":
                hide zaleabio
                hide zalea excited flower
                jump ezrabio
                
            "Don't pick Zalea":
                hide zaleabio
                hide zalea excited flower
                jump pickabunkee

    label bunkmate_done:
        $ nash_is_bunkmate = "Nash" in selected_bunkmates
        $ nash_alive = True
        "Your bunkmates are [', '.join(selected_bunkmates)]."

    "Now that you've picked your bunkmates, you head to your cabin to settle in. Now its time to explore the camp and have fun with your friends!"

    "Click to see the different locations you can explore at the camp!"

default interactions_count = 0

$ use_custom_choice = False
label camp_map:
    menu:
        "Cabin":
            $ interactions_count += 1
            jump cabin
        "Firepit":
            $ interactions_count += 1
            jump firepit
        "Cabin Closeup":
            $ interactions_count += 1
            jump cabin_closeup
        "Continue with the story" if interactions_count >= 3:
            jump continue_story

    label cabin:
        scene cabin_day
        with fade
        "Cabin 1 is the closest to the entrance, and you can see it from the road. It has a nice porch and a cozy vibe. 3 and 4 look a little worn down"
        jump camp_map

    label firepit:
        scene firepit_day
        with fade
        "A great place for roasting marshmallows and sharing you deepest DARKEST secrets." 
        jump camp_map
        
    label cabin_closeup:
        scene stairs_day
        with fade
        "just some stairs."
        jump camp_map

hide cabin_day
hide firepit_day
hide stairs_day        

label continue_story:
    scene firepit_lit
    with fade
    "The group decides to spend the rest of the night by the campfire"

    show cole glasses neutral at Left
    c "Hey, d-did anyone remember to bring the bug spray?"
    hide cole glasses neutral
    show ezra sunglasses at Left
    e "Yeah, I'm pretty sure Zalea packed some in her bag."
    hide ezra sunglasses
    show cole glasses smirk at Left
    c "Oh thank god, I forgot to pack some and I'm already getting eaten alive by mosquitoes. Plus I don't want anyone getting bitten by ticks."
    hide cole glasses smirk
    show jade upset at Left
    j "God Cole, you're such a wimp. There's hardly any bugs around here."
    hide jade upset
    show cole glasses neutral at Left
    c "H-hey! I’m just trying to help!"
    hide cole glasses neutral
    show zalea judging flower at Left
    z "Lighten up Jade, Cole's just trying to be prepared. Plus, I don't mind sharing my bug spray if anyone needs it."
    hide zalea judging flower
    show jade upset at Left
    j "Whatever, I'm going to bed. Goodnight losers."
    hide jade upset
    "Jade leaves toward her cabin, and everyone glances at Cole."
    show zalea flower at Left
    z "Sorry about her Cole, she means well... usually."
    hide zalea flower
    show cole glasses neutral at Left
    c "I-I don’t understand why you invited her, she’s always so mean…"
    hide cole glasses neutral
    show zalea judging flower at Left
    z "...She's got no other friends."
    hide zalea judging flower
    show cole glasses neutral at Left
    c "R-Right... whatever."
    hide cole glasses neutral
    show zalea sad flower at Left
    z "Sorry.. I-"
    hide zalea sad flower
    show ezra sunglasses at Left
    e "It's alright Z, We're all trying to give her a chance. Anyways, Jade had the right idea. It's getting kinda late, we should head in."
    hide ezra sunglasses
    show nash smirk at Left
    n "Agreed."
    hide nash smirk
    show mavis neutral at Left
    m "Yeah, let's call it a night. Who wants to make breakfast tomorrow?"
    hide mavis neutral
    "Everyone says 'No thanks' in unison, Mavis scoffs and everyone heads to their cabins. Breakfast is a mystery."

    scene black
    with fade
    jump day2_start

