import json
held = {"name": "Aria", "klasse": "Magierin", "level": 15, "leben": 120}
with open("held.json", "w") as f:
    json.dump(held, f)
with open("held.json", "r") as f:
    daten = json.load(f)
daten["mana"] = 80
with open("held.json", "w") as f:
    json.dump(daten, f)
with open("held.json", "r") as f:
    geladen = json.load(f)
print(f"Mana: {geladen['mana']}")
print(f"Eigenschaften: {len(geladen)}")
