# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Player", color="#000000")
define z = Character("Zalea", color="#dc10a9")
define e = Character("Ezra", color="#5b0e92")
define m = Character("Mavis", color="#e7721e")
define n = Character("Nash", color="#d01414")
define f = Character("Farren", color="#18ccd8")
define j = Character("Jade", color="#17d217")
define c = Character("Cole", color="#286c28")

default inventory_slots = [
    {"id": "owner note", "icon": "images/icons/owner note.png"},
    None,
    None
]
default selected_slot = -1

screen item_hotbar_icons():
    zorder 120

    frame:
        xalign 1.0
        yalign 0.5
        xoffset -20
        background "#111a"
        padding (10, 10)

        vbox:
            spacing 8
            text "Items" size 24

            for i, slot in enumerate(inventory_slots):
                fixed:
                    xsize 72
                    ysize 72

                    imagebutton:
                        idle "gui/slot_idle.png"
                        hover "gui/slot_hover.png"
                        xpos 0
                        ypos 0
                        action SetVariable("selected_slot", i)

                    if slot:
                        add slot["icon"] xalign 0.5 yalign 0.5 xysize (60, 60)
                       

    if selected_slot >= 0 and selected_slot < len(inventory_slots) and inventory_slots[selected_slot]:
        frame:
            xalign 0.72
            yalign 0.88
            background "#0008"
            padding (10, 6)
            text "Selected: [inventory_slots[selected_slot]['id']]"

# The game starts here.
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene car on road
    with fade

    show jade at Transform(zoom=0.5)
    with dissolve
    j "How long till we get there?" 
    hide jade

    show mavis at Transform(zoom=0.5)
    with dissolve
    m "Ermm. I’d say about 15 minutes?"
    hide mavis
   
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "zalea happy.png" to the images
    # directory.

    show jade at Transform(zoom=0.5)
    with dissolve
    "Jade scoffs and looks out the window"
    hide jade

    "Mavis rolls her eyes and turns up the music"
    
    scene black
    with fade

    scene camp entrance
    with fade
    
    show mavis at Transform(zoom=0.5)
    with dissolve
    m "Mavis hits the break and parks the orange van" 
    "Alright. We're here."
    hide mavis

    show jade at Transform(zoom=0.5)
    with dissolve
    j "Jade gestures with two hands in the air and a sarcastic tone" 
    "Yippee."
    hide jade

    "Mavis gets out to grab her bags and everyone else follows suit. Ezra walks up to the camp entrance and looks around"
    
    show ezra at Transform(zoom=0.5)
    with dissolve
    e "I found a note left by the camp owner, wanna see the note?"

    menu:
        "Sure, show me the note.":
            jump shownote
        "No thanks, I don't like to read notes.":
            jump nonote

label shownote:
    $ shownote = True
    "Ezra pulls out the note and shows it to you, it reads: “Welcome to Camp Getaway! We hope you enjoy your stay. Please note that cabins 3-4 are off limits due to maintenance. If you need anything, my place is a 20 minute walk from here. -Camp Owner”"
    show owner note at Transform(zoom=0.5, xalign=0.5, yalign=0.5)
    with dissolve

    "Maybe you should keep the note, just in case you need it later. It will be stored in your hotbar."
    hide owner note
    hide ezra

    show screen item_hotbar_icons
    "Look at that, a handy dandy hotbar! You can click on the note to read it again, or you can click on it later if you forget what it says."

    "Now its time to pick your bunkmates, who do you want to room with? You can choose up to 3 bunkees"
    show bunkmates
    jump pickabunkee

label nonote:
    $ nonote = True
    "Ezra shrugs and puts the note back in his pocket"
    hide ezra

    "Everyones standing outside the entrance waiting to enter, you can’t help but feel a little uneasy about the note. You wonder what it says."
    show bunkmates
    with fade

    "Now its time to pick your bunkmates, who do you want to room with? You can choose up to 3 bunkees"
    jump pickabunkee  

label pickabunkee:
    
    "Click to learn more about each character."
    menu:
        "Room with Mavis?":
            jump mavisbio
        "Room with Jade?":
            jump jadebio
        "Room with Farren?":
            jump farrenbio
        "Room with Cole?":
            jump colebio
        "Room with Nash?":
            jump nashbio
        "Room with Ezra?":
            jump ezrabio
        "Room with Zalea?":
            jump zaleabio

label mavisbio:

    scene cabin morning
    
    # This ends the game.
    return
