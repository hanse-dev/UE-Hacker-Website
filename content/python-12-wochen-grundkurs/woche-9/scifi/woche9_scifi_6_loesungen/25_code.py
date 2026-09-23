import json
mitglied = {"name": "Nova", "rolle": "Pilotin", "rang": 4, "energie": 120}
with open("mitglied.json", "w") as f:
    json.dump(mitglied, f)
with open("mitglied.json", "r") as f:
    geladen = json.load(f)
print(f"Geladen: {geladen['name']}")
print(f"Gleich: {geladen == mitglied}")
