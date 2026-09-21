import csv
horses = [
    {"name": "Blitz", "breed": "Hanoverian", "age": 8, "points": 120},
    {"name": "Storm", "breed": "Haflinger", "age": 12, "points": 150},
    {"name": "Luna", "breed": "Icelandic", "age": 6, "points": 90},
    {"name": "Wind", "breed": "Hanoverian", "age": 7, "points": 110},
]
with open("horses.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "breed", "age", "points"])
    writer.writeheader()
    writer.writerows(horses)
with open("horses.csv", "r") as f:
    rows = list(csv.DictReader(f))
print(f"Rows: {len(rows)}")
