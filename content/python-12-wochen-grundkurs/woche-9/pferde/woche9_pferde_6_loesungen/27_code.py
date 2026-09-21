import json
pferd = {"name": "Blitz", "rasse": "Hannoveraner", "alter": 8, "punkte": 120}
with open("pferd.json", "w") as f:
    json.dump(pferd, f)
with open("pferd.json", "r") as f:
    daten = json.load(f)
daten["alter"] += 1
with open("pferd.json", "w") as f:
    json.dump(daten, f)
with open("pferd.json", "r") as f:
    geladen = json.load(f)
print(f"Alter: {geladen['alter']}")
