import json
crew = [
    {"name": "Nova", "role": "Pilot", "rank": 4, "energy": 120},
    {"name": "Rex", "role": "Engineer", "rank": 6, "energy": 150},
    {"name": "Zara", "role": "Botanist", "rank": 3, "energy": 90},
]
with open("member.json", "w") as f:
    json.dump(crew, f)
with open("member.json", "r") as f:
    loaded = json.load(f)
print(f"Count: {len(loaded)}")
print(f"Last: {loaded[-1]['name']}")
