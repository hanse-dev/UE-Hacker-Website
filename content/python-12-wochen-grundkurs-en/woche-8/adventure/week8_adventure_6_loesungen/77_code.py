heroes = [
    {"name": "Aria", "class": "Mage", "level": 15, "hp": 120},
    {"name": "Thorin", "class": "Warrior", "level": 18, "hp": 150},
    {"name": "Luna", "class": "Rogue", "level": 12, "hp": 90},
    {"name": "Mira", "class": "Mage", "level": 13, "hp": 110},
]
level_values = [h["level"] for h in heroes]
ranking = sorted(level_values, reverse=True)
best = heroes[0]
for h in heroes:
    if h["level"] > best["level"]:
        best = h
print(f"Best: {best['name']}")
print(f"Ranking: {ranking}")
