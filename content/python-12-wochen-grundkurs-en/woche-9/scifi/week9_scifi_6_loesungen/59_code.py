import json
crew = [
    {"name": "Nova", "role": "Pilot", "rank": 4, "energy": 120},
    {"name": "Rex", "role": "Engineer", "rank": 6, "energy": 150},
    {"name": "Zara", "role": "Botanist", "rank": 3, "energy": 90},
]
with open("member.json", "w") as f:
    json.dump(crew, f)
with open("member.json", "r") as f:
    items = json.load(f)
best = items[0]
for entry in items:
    if entry["rank"] > best["rank"]:
        best = entry
print(f"Best: {best['name']}")
