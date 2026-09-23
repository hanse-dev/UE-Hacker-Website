import json
held = {"name": "Aria", "klasse": "Magierin", "level": 15, "leben": 120}
def speichere(daten, name):
    with open(name, "w") as f:
        json.dump(daten, f)

def lade(name):
    with open(name, "r") as f:
        return json.load(f)

speichere(held, "held.json")
geladen = lade("held.json")
print(f"Gleich: {geladen == held}")
