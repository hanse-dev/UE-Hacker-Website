import json
pferd = {"name": "Blitz", "rasse": "Hannoveraner", "alter": 8, "punkte": 120}
def speichere(daten, name):
    with open(name, "w") as f:
        json.dump(daten, f)

def lade(name):
    with open(name, "r") as f:
        return json.load(f)

speichere(pferd, "pferd.json")
geladen = lade("pferd.json")
print(f"Gleich: {geladen == pferd}")
