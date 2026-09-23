import json
heroes = [
    {"name": "Aria", "class": "Mage", "level": 15, "hp": 120},
    {"name": "Thorin", "class": "Warrior", "level": 18, "hp": 150},
    {"name": "Luna", "class": "Rogue", "level": 12, "hp": 90},
]
with open("hero.json", "w") as f:
    json.dump(heroes, f)
with open("hero.json", "r") as f:
    items = json.load(f)
best = items[0]
for entry in items:
    if entry["level"] > best["level"]:
        best = entry
print(f"Best: {best['name']}")
