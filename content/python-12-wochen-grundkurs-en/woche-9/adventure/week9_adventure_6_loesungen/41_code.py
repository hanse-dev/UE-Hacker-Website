import json
heroes = [
    {"name": "Aria", "class": "Mage", "level": 15, "hp": 120},
    {"name": "Thorin", "class": "Warrior", "level": 18, "hp": 150},
    {"name": "Luna", "class": "Rogue", "level": 12, "hp": 90},
]
with open("hero.json", "w") as f:
    json.dump(heroes, f)
import csv

with open("hero.json", "r") as f:
    loaded = json.load(f)
with open("heroes.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "class", "level", "hp"])
    writer.writeheader()
    writer.writerows(loaded)
with open("heroes.csv", "r") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fields = reader.fieldnames
print(f"Rows: {len(rows)}")
print(f"Fields: {fields}")
