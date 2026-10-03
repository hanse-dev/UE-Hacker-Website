import json
einheiten = [
    {"name": "Springen üben", "schwierigkeit": 1, "status": "offen"},
    {"name": "Ausritt planen", "schwierigkeit": 2, "status": "offen"},
    {"name": "Fell pflegen", "schwierigkeit": 3, "status": "offen"},
]
with open("trainingslog.json", "w") as f:
    json.dump(einheiten, f)
with open("trainingslog.json", "r") as f:
    geladen = json.load(f)
print(f"Training-Anzahl: {len(geladen)}")
print(f"Status: {geladen[0]['status']}")
