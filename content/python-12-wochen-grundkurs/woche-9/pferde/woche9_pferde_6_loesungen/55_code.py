import json
pferd = {"name": "Blitz", "rasse": "Hannoveraner", "alter": 8, "punkte": 120}
with open("pferd.json", "w") as f:
    json.dump(pferd, f)
with open("pferd.json", "r") as f:
    geladen = json.load(f)
print(f"Name: {geladen['name']}")
print(f"Alter: {geladen['alter']}")
