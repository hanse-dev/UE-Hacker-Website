for zeile in range(3):
    for spalte in range(3):
        if zeile == 1 and spalte == 1:
            print("P", end="")
        else:
            print(".", end="")
    print()
