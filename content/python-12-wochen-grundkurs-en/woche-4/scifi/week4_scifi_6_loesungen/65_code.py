dark = True
for row in range(8):
    for column in range(8):
        if dark:
            print("#", end="")
        else:
            print(".", end="")
        dark = not dark
    print()
    dark = not dark
