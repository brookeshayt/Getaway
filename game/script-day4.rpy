
label day4_start:
    scene black
    with fade
    "Day 4"

    if farren_alive:
        jump farren_alive
    else:
        jump farren_death

label farren_death:
    scene group_day3_fire

label farren_alive:
    scene group_day2_fire
    with fade
    