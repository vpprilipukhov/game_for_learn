def shop_buy(pl_choice, pl,shop):
    pl['items'].append(shop[int(pl_choice)-1])
    if shop[int(pl_choice)-1] == "Малое лечебное зелье":
        pl['gold'] -= 20
    if shop[int(pl_choice)-1] == "Большое лечебное зелье":
        pl['gold'] -= 30
    if shop[int(pl_choice) - 1] == "Деревянный меч":
        pl['gold'] -= 10
    shop.pop(int(pl_choice) - 1)

    return pl,shop