import random


def player_attack (pl_choice, p1, p2_def):

    npc_choice = random.choice([1,1,1,1,2,2,2,3])
    print(npc_choice)
    if int(pl_choice) != npc_choice:
        print("Вы попали!")
        if pl_choice == "1":
            p2_def['hp'] -= int((p1['dmg'] - p2_def['armor']) * 2)
        if pl_choice == "2":
            p2_def['hp'] -= int((p1['dmg'] - p2_def['armor']) * 1.5)
        if pl_choice == "3":
            p2_def['hp'] -= int((p1['dmg'] - p2_def['armor']) * 0.9)
    else:
        print("Не попал!")
    return p2_def


def player_def (pl_choice, p1_def, p2 ):

    npc_choice = random.choice([1,2,2,2,3,3])
    print(npc_choice)
    if int(npc_choice) != pl_choice:
        print("Вы не защитились!")
        if npc_choice == "1":
            p1_def['hp'] -= int((p2['dmg'] - p1_def['armor']) * 2)
        if npc_choice == "2":
            p1_def['hp'] -= int((p2['dmg'] - p1_def['armor']) * 1.5)
        if npc_choice == "3":
            p1_def['hp'] -= int((p2['dmg'] - p1_def['armor']) * 0.9)
    else:
        print("Вы защитились")
    return p1_def

