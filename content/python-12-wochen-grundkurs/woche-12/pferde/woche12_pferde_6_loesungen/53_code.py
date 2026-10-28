import json
daten = {"name": "Mira", "puste": 20}
with open("stand.json", "w") as f:
    json.dump(daten, f)
print("💾 Spielstand von Mira gespeichert.")
