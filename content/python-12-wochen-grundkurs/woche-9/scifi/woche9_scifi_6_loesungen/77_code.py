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
geladen["Energiezelle"] = {"koordinaten": [70, 80], "wert": 400}
with open("karte.json", "w") as f:
    json.dump(geladen, f)
with open("karte.json", "r") as f:
    neu = json.load(f)
print(f"Orte: {len(neu)}")
