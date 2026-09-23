import json
member = {"name": "Nova", "role": "Pilot", "rank": 4, "energy": 120}
with open("member.json", "w") as f:
    json.dump(member, f)
with open("member.json", "r") as f:
    data = json.load(f)
data["shield"] = 80
with open("member.json", "w") as f:
    json.dump(data, f)
with open("member.json", "r") as f:
    loaded = json.load(f)
print(f"Shield: {loaded['shield']}")
print(f"Properties: {len(loaded)}")
