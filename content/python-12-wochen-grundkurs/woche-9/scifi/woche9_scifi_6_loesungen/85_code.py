import json
mitglied = {"name": "Nova", "rolle": "Pilotin", "rang": 4, "energie": 120}
def speichere(daten, name):
    with open(name, "w") as f:
        json.dump(daten, f)

def lade(name):
    with open(name, "r") as f:
        return json.load(f)

speichere(mitglied, "mitglied.json")
geladen = lade("mitglied.json")
print(f"Gleich: {geladen == mitglied}")
