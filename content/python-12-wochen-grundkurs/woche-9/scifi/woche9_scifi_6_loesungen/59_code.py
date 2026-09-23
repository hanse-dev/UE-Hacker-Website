import json
crew = [
    {"name": "Nova", "rolle": "Pilotin", "rang": 4, "energie": 120},
    {"name": "Rex", "rolle": "Ingenieur", "rang": 6, "energie": 150},
    {"name": "Zara", "rolle": "Botanikerin", "rang": 3, "energie": 90},
]
with open("mitglied.json", "w") as f:
    json.dump(crew, f)
with open("mitglied.json", "r") as f:
    liste = json.load(f)
bester = liste[0]
for eintrag in liste:
    if eintrag["rang"] > bester["rang"]:
        bester = eintrag
print(f"Bester: {bester['name']}")
