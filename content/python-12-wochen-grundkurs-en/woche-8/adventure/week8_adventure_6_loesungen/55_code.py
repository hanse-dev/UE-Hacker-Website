heroes = [
    {"name": "Aria", "class": "Mage", "level": 15, "hp": 120},
    {"name": "Thorin", "class": "Warrior", "level": 18, "hp": 150},
    {"name": "Luna", "class": "Rogue", "level": 12, "hp": 90},
    {"name": "Mira", "class": "Mage", "level": 13, "hp": 110},
]
def find_heroes(items, kind):
    names = []
    for h in items:
        if h["class"] == kind:
            names.append(h["name"])
    return names

print(f"Found: {find_heroes(heroes, 'Mage')}")
