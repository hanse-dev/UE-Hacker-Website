potions = 1
runes = True
escape_route = True

if potions >= 3 or (runes and escape_route):
    print("Escape successful")
else:
    print("Escape failed")