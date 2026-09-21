for zeile in range(8):
    for spalte in range(8):
        if zeile == 0 and spalte == 0:
            print("M", end="")
        elif zeile == 7 and spalte == 7:
            print("Z", end="")
        else:
            print(".", end="")
    print()
