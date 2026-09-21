import json
pferde = [
    {"name": "Blitz", "rasse": "Hannoveraner", "alter": 8, "punkte": 120},
    {"name": "Sturm", "rasse": "Haflinger", "alter": 12, "punkte": 150},
    {"name": "Luna", "rasse": "Isländer", "alter": 6, "punkte": 90},
]
with open("pferd.json", "w") as f:
    json.dump(pferde, f)
with open("pferd.json", "r") as f:
    geladen = json.load(f)
print(f"Anzahl: {len(geladen)}")
print(f"Letzter: {geladen[-1]['name']}")
