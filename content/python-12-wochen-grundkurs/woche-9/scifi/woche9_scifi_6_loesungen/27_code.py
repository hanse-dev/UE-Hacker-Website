import json
mitglied = {"name": "Nova", "rolle": "Pilotin", "rang": 4, "energie": 120}
with open("mitglied.json", "w") as f:
    json.dump(mitglied, f)
with open("mitglied.json", "r") as f:
    daten = json.load(f)
daten["rang"] += 1
with open("mitglied.json", "w") as f:
    json.dump(daten, f)
with open("mitglied.json", "r") as f:
    geladen = json.load(f)
print(f"Rang: {geladen['rang']}")
