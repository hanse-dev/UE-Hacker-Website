import json
horses = [
    {"name": "Blitz", "breed": "Hanoverian", "age": 8, "points": 120},
    {"name": "Storm", "breed": "Haflinger", "age": 12, "points": 150},
    {"name": "Luna", "breed": "Icelandic", "age": 6, "points": 90},
]
with open("horse.json", "w") as f:
    json.dump(horses, f)
with open("horse.json", "r") as f:
    items = json.load(f)
best = items[0]
for entry in items:
    if entry["age"] > best["age"]:
        best = entry
print(f"Best: {best['name']}")
