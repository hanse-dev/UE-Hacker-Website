import json
member = {"name": "Nova", "role": "Pilot", "rank": 4, "energy": 120}
def safe_load(name):
    try:
        with open(name, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

print(f"Empty: {safe_load('does_not_exist.json') == {}}")
with open("member.json", "w") as f:
    json.dump(member, f)
print(f"Name: {safe_load('member.json')['name']}")
