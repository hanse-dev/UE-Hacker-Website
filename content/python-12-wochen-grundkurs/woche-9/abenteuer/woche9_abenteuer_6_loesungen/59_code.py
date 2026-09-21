import json
helden = [
    {"name": "Aria", "klasse": "Magierin", "level": 15, "leben": 120},
    {"name": "Thorin", "klasse": "Krieger", "level": 18, "leben": 150},
    {"name": "Luna", "klasse": "Schurkin", "level": 12, "leben": 90},
]
with open("held.json", "w") as f:
    json.dump(helden, f)
with open("held.json", "r") as f:
    liste = json.load(f)
bester = liste[0]
for eintrag in liste:
    if eintrag["level"] > bester["level"]:
        bester = eintrag
print(f"Bester: {bester['name']}")
