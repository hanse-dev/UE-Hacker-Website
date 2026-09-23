import json
karte = {
    "Goldkrone": {"koordinaten": (10, 20), "wert": 800},
    "Silberkelch": {"koordinaten": (30, 40), "wert": 300},
    "Rubin": {"koordinaten": (50, 60), "wert": 650},
}
karte["Smaragd"] = {"koordinaten": [70, 80], "wert": 400}
with open("karte.json", "w") as f:
    json.dump(karte, f)
with open("karte.json", "r") as f:
    geladen = json.load(f)
bester = None
for ort in geladen:
    if bester is None or geladen[ort]["wert"] > geladen[bester]["wert"]:
        bester = ort
print(f"Wertvollster: {bester} ({geladen[bester]['wert']})")
