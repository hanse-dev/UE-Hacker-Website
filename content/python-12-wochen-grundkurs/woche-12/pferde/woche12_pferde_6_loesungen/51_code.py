import json
data = {"name": "Mira", "hp": 20}
with open("stand.json", "w") as f:
    json.dump(data, f)
print("💾 Spielstand von Mira gespeichert.")
