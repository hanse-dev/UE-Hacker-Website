import csv
heroes = [
    {"name": "Aria", "class": "Mage", "level": 15, "hp": 120},
    {"name": "Thorin", "class": "Warrior", "level": 18, "hp": 150},
    {"name": "Luna", "class": "Rogue", "level": 12, "hp": 90},
    {"name": "Mira", "class": "Mage", "level": 13, "hp": 110},
]
with open("heroes.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "class", "level", "hp"])
    w.writeheader()
    w.writerows(heroes)
total = 0
with open("heroes.csv", "r") as f:
    rows = list(csv.DictReader(f))
for row in rows:
    total += int(row["level"])
print(f"Total: {total}")
print(f"Average: {total / len(rows)}")
