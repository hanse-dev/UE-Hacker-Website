heroes = [
    {"name": "Aria", "class": "Mage", "level": 15, "hp": 120},
    {"name": "Thorin", "class": "Warrior", "level": 18, "hp": 150},
    {"name": "Luna", "class": "Rogue", "level": 12, "hp": 90},
    {"name": "Mira", "class": "Mage", "level": 13, "hp": 110},
]
total = 0
for h in heroes:
    total += h["level"]
average = total / len(heroes)
print(f"Average: {average}")
