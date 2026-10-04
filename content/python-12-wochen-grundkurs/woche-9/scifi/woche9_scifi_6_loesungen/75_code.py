import json
karte = {
    "Kristallkern": {"koordinaten": (10, 20), "wert": 800},
    "Sensorchip": {"koordinaten": (30, 40), "wert": 300},
    "Antimaterie": {"koordinaten": (50, 60), "wert": 650},
}
with open("karte.json", "w") as f:
    json.dump(karte, f)
with open("karte.json", "r") as f:
    geladen = json.load(f)
print(f"Orte: {len(geladen)}")
print(f"Koordinaten: {geladen['Kristallkern']['koordinaten']}")
