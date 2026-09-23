dunkel = True
for reihe in range(8):
    for spalte in range(8):
        if dunkel:
            print("#", end="")
        else:
            print(".", end="")
        dunkel = not dunkel
    print()
    dunkel = not dunkel
