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

entries = []
with open("heroes.csv", "r") as f:
    for row in csv.DictReader(f):
        row["level"] = int(row["level"])
        entries.append(row)
with open("hero.json", "w") as f:
    json.dump(entries, f)
with open("hero.json", "r") as f:
    loaded = json.load(f)
total = 0
for entry in loaded:
    total += entry["level"]
print(f"Count: {len(loaded)}")
print(f"Total: {total}")
