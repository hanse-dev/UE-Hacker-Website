for row in range(3):
    for column in range(3):
        if row == 1 and column == 1:
            print("P", end="")
        else:
            print(".", end="")
    print()
