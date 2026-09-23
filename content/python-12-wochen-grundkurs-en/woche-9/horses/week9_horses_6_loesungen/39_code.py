import csv
horses = [
    {"name": "Blitz", "breed": "Hanoverian", "age": 8, "points": 120},
    {"name": "Storm", "breed": "Haflinger", "age": 12, "points": 150},
    {"name": "Luna", "breed": "Icelandic", "age": 6, "points": 90},
]
with open("horses.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "breed", "age", "points"])
    w.writeheader()
    w.writerows(horses)
import json

entries = []
with open("horses.csv", "r") as f:
    for row in csv.DictReader(f):
        row["age"] = int(row["age"])
        entries.append(row)
with open("horse.json", "w") as f:
    json.dump(entries, f)
with open("horse.json", "r") as f:
    loaded = json.load(f)
total = 0
for entry in loaded:
    total += entry["age"]
print(f"Count: {len(loaded)}")
print(f"Total: {total}")
