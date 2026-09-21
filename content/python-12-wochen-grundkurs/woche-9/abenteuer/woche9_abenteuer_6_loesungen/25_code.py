import json
held = {"name": "Aria", "klasse": "Magierin", "level": 15, "leben": 120}
with open("held.json", "w") as f:
    json.dump(held, f)
with open("held.json", "r") as f:
    geladen = json.load(f)
print(f"Geladen: {geladen['name']}")
print(f"Gleich: {geladen == held}")
