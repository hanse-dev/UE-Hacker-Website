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

strong = []
with open("horses.csv", "r") as f:
    for row in csv.DictReader(f):
        if int(row["age"]) > 7:
            strong.append(row["name"])
with open("horse.json", "w") as f:
    json.dump(strong, f)
with open("horse.json", "r") as f:
    loaded = json.load(f)
print(f"Strong: {loaded}")
