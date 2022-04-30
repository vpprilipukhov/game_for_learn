from main_action.menu import menu
from arena.arena_main import arena_main
from shop.shop_main import shop_main

# словари с персонажами
knight = {'hp': 10, 'dmg': 15, 'armor': 7, 'gold': 100, 'items': ["Малое лечебное зелье"]}
orc = {'hp': 17, 'dmg': 12, 'armor': 1}

ar_main_menu = ["Пойти в магазин", "Пойти на арену", "Посмотреть героя", "Выход"]

shop_flask = ["Малое лечебное зелье", "Малое лечебное зелье", "Большое лечебное зелье"]
shop_armory = ["Деревянный меч"]

player_choice = True

# начало игры, бесконечный цикл выбора действий, пока игрок не выйдет
while player_choice != "0":

    # Показать игроку действия, выбор действия
    player_choice = menu(ar_main_menu)

    # Идем в магазин
    if player_choice == "1":
       knight,shop_flask,shop_armory = shop_main(knight,shop_flask,shop_armory)


    # Идем на арену
    elif player_choice == "2":

        knight, orc = arena_main(knight, orc)

    elif player_choice == "3":
        print(knight)
