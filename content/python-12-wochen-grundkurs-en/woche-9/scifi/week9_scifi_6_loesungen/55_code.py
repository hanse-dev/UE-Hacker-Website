import json
member = {"name": "Nova", "role": "Pilot", "rank": 4, "energy": 120}
with open("member.json", "w") as f:
    json.dump(member, f)
with open("member.json", "r") as f:
    loaded = json.load(f)
print(f"Name: {loaded['name']}")
print(f"Rank: {loaded['rank']}")
