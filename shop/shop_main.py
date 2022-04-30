from main_action.menu import menu
from shop.shop_buy import shop_buy

def shop_main(pl,shop_flask,shop_armory):

    shop_swodka = ["Деревянный меч - 2dmg 10g"
                   " Малоче лечебное зелье - 2hp 20g"
                   " Большое лечебное зелье - 10hp 30g"]
    # списки с выборами действий

    ar_shop_menu = ["Посмотреть товары", "Посмотреть хар-ки", "Выход"]
    shop_item = ["Зелье", "Армори"]

    player_choice = True


    while player_choice != "0":
        player_choice = menu(ar_shop_menu)
        if player_choice == "1":
            player_choice = menu(shop_item)
            if player_choice == "1":
                player_choice = menu(shop_flask)
                pl,shop_flask = shop_buy(player_choice,pl,shop_flask)

            elif player_choice == "2":
                player_choice = menu(shop_armory)
                pl, shop_armory = shop_buy(player_choice, pl, shop_armory)
        elif player_choice == "2":
            print(shop_swodka)


    return pl,shop_flask,shop_armory
