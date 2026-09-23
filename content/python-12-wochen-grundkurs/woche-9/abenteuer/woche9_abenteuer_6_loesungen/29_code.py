import json
helden = [
    {"name": "Aria", "klasse": "Magierin", "level": 15, "leben": 120},
    {"name": "Thorin", "klasse": "Krieger", "level": 18, "leben": 150},
    {"name": "Luna", "klasse": "Schurkin", "level": 12, "leben": 90},
]
with open("held.json", "w") as f:
    json.dump(helden, f)
with open("held.json", "r") as f:
    geladen = json.load(f)
print(f"Anzahl: {len(geladen)}")
print(f"Letzter: {geladen[-1]['name']}")
