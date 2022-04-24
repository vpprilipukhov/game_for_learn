import arena.arena_action as arena_action
import main_action.menu as menu

# словари с персонажами
knight = {'hp': 10, 'dmg': 5, 'armor': 7}
orc = {'hp': 17, 'dmg': 12, 'armor': 1}

# списки с выборами действий
ar_main_menu = ["Пойти в магазин", "Пойти на арену","Выход"]
ar_choice_attack = ["В Голову","В Тело", "В Ноги"]
ar_choice_def = ["В Голову","В Тело", "В Ноги"]

player_choice = True

# начало игры, бесконечный цикл выбора действий, пока игрок не выйдет
while player_choice != "0":

    # Показать игроку действия, выбор действия
    player_choice = menu.menu(ar_main_menu)

    # Идем в магазин
    if player_choice == "1":
        print("Вы в магазине")

    # Идем на арену
    elif player_choice == "2":

        # Начинается арена, не закончится, пока хп не упадет ниже 0 у кого нибудь
        while knight["hp"] > 0 and orc["hp"] > 0:

            # Показать игроку действия, выбор действия
            player_choice = menu.menu(ar_choice_attack)

            # Функция наннесения урона противнику
            orc = arena_action.player_attack(player_choice, knight, orc)
            print(orc)

            # Функция защиты

            player_choice = menu.menu(ar_choice_def)
            knight = arena_action.player_def(player_choice,knight,orc)
            print(knight)


