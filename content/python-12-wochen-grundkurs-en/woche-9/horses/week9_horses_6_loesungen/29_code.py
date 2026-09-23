import json
horses = [
    {"name": "Blitz", "breed": "Hanoverian", "age": 8, "points": 120},
    {"name": "Storm", "breed": "Haflinger", "age": 12, "points": 150},
    {"name": "Luna", "breed": "Icelandic", "age": 6, "points": 90},
]
with open("horse.json", "w") as f:
    json.dump(horses, f)
with open("horse.json", "r") as f:
    loaded = json.load(f)
print(f"Count: {len(loaded)}")
print(f"Last: {loaded[-1]['name']}")
