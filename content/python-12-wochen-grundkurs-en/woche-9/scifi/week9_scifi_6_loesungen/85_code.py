import json
member = {"name": "Nova", "role": "Pilot", "rank": 4, "energy": 120}
def save(data, name):
    with open(name, "w") as f:
        json.dump(data, f)

def load(name):
    with open(name, "r") as f:
        return json.load(f)

save(member, "member.json")
loaded = load("member.json")
print(f"Equal: {loaded == member}")
