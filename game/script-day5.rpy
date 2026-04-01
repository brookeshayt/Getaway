
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


label day5_start_good:
    scene black
    with fade
    "Day 5"



    
label the_end:
    "The End"
    $ renpy.pause(hard=True)