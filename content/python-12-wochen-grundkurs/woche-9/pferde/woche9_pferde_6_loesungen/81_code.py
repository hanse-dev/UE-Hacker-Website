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
geladen[0]["status"] = "abgeschlossen"
with open("trainingslog.json", "w") as f:
    json.dump(geladen, f)
with open("trainingslog.json", "r") as f:
    neu = json.load(f)
print(f"Erste: {neu[0]['status']}")
