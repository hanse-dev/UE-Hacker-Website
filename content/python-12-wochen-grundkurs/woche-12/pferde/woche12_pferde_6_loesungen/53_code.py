import json
daten = {"name": "Mira", "hp": 20}
with open("stand.json", "w") as f:
    json.dump(daten, f)
print("💾 Spielstand von Mira gespeichert.")
