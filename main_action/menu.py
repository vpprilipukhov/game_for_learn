def menu(ar):
    print()
    for i in range(len(ar)):

        if ar[i] == "Выход":
            print(str(0)+")"+" "+"Выход")
        else:
            print(str(i + 1) + ")" + " " + ar[i])
    return input('Выберите действиe: ')

