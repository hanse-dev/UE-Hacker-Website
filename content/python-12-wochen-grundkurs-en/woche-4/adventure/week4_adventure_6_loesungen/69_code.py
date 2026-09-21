for row in range(8):
    for column in range(8):
        if row == 0 and column == 0:
            print("M", end="")
        elif row == 7 and column == 7:
            print("Z", end="")
        else:
            print(".", end="")
    print()
