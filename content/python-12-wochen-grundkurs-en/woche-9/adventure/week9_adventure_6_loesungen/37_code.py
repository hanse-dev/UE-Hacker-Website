import csv
heroes = [
    {"name": "Aria", "class": "Mage", "level": 15, "hp": 120},
    {"name": "Thorin", "class": "Warrior", "level": 18, "hp": 150},
    {"name": "Luna", "class": "Rogue", "level": 12, "hp": 90},
]
with open("heroes.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "class", "level", "hp"])
    writer.writeheader()
    writer.writerows(heroes)
with open("heroes.csv", "r") as f:
    rows = list(csv.DictReader(f))
print(f"Rows: {len(rows)}")
print(f"First: {rows[0]['name']}")
