from arena import arena_action
from main_action.menu import menu


knight = {'hp': 10, 'dmg': 5, 'armor': 7}
orc = {'hp': 17, 'dmg': 12, 'armor': 1}


def arena_main(pl,npc):
    print("Началась арена!")
    ar_choice_attack = ["В Голову", "В Тело", "В Ноги"]
    ar_choice_def = ["В Голову", "В Тело", "В Ноги"]


    # Начинается арена, не закончится, пока хп не упадет ниже 0 у кого нибудь
    while pl["hp"] > 0 and npc["hp"] > 0:
        print()
        # Показать игроку действия, выбор действия
        player_choice =menu(ar_choice_attack)

        # Функция наннесения урона противнику
        npc = arena_action.player_attack(player_choice, pl, npc)
        print(npc)

        # Функция защиты
        player_choice = menu(ar_choice_def)
        pl = arena_action.player_def(player_choice, pl, npc)
        print(pl)


    return pl,npc


