potions = 5
runes = True
escape_route = False
if potions >= 3 or (runes and escape_route):
    print("Escape succeeds!")
else:
    print("Escape fails!")
