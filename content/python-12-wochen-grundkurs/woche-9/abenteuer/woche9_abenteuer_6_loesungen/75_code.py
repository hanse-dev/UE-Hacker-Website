import json
karte = {
    "Goldkrone": {"koordinaten": (10, 20), "wert": 800},
    "Silberkelch": {"koordinaten": (30, 40), "wert": 300},
    "Rubin": {"koordinaten": (50, 60), "wert": 650},
}
with open("karte.json", "w") as f:
    json.dump(karte, f)
with open("karte.json", "r") as f:
    geladen = json.load(f)
print(f"Orte: {len(geladen)}")
print(f"Koordinaten: {geladen['Goldkrone']['koordinaten']}")
