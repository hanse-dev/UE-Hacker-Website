import json
heroes = [
    {"name": "Aria", "class": "Mage", "level": 15, "hp": 120},
    {"name": "Thorin", "class": "Warrior", "level": 18, "hp": 150},
    {"name": "Luna", "class": "Rogue", "level": 12, "hp": 90},
]
with open("hero.json", "w") as f:
    json.dump(heroes, f)
with open("hero.json", "r") as f:
    loaded = json.load(f)
print(f"Count: {len(loaded)}")
print(f"Last: {loaded[-1]['name']}")
