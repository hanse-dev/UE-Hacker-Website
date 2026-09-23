import csv
heroes = [
    {"name": "Aria", "class": "Mage", "level": 15, "hp": 120},
    {"name": "Thorin", "class": "Warrior", "level": 18, "hp": 150},
    {"name": "Luna", "class": "Rogue", "level": 12, "hp": 90},
]
with open("heroes.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "class", "level", "hp"])
    w.writeheader()
    w.writerows(heroes)
import json

strong = []
with open("heroes.csv", "r") as f:
    for row in csv.DictReader(f):
        if int(row["level"]) > 14:
            strong.append(row["name"])
with open("hero.json", "w") as f:
    json.dump(strong, f)
with open("hero.json", "r") as f:
    loaded = json.load(f)
print(f"Strong: {loaded}")
