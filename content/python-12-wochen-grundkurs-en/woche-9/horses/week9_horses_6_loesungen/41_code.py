import json
horses = [
    {"name": "Blitz", "breed": "Hanoverian", "age": 8, "points": 120},
    {"name": "Storm", "breed": "Haflinger", "age": 12, "points": 150},
    {"name": "Luna", "breed": "Icelandic", "age": 6, "points": 90},
]
with open("horse.json", "w") as f:
    json.dump(horses, f)
import csv

with open("horse.json", "r") as f:
    loaded = json.load(f)
with open("horses.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "breed", "age", "points"])
    writer.writeheader()
    writer.writerows(loaded)
with open("horses.csv", "r") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fields = reader.fieldnames
print(f"Rows: {len(rows)}")
print(f"Fields: {fields}")
