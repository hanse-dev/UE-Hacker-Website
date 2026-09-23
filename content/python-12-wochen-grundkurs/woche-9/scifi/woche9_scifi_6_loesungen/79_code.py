import json
quests = [
    {"name": "Signal orten", "schwierigkeit": 1, "status": "offen"},
    {"name": "Sonde starten", "schwierigkeit": 2, "status": "offen"},
    {"name": "Hülle reparieren", "schwierigkeit": 3, "status": "offen"},
]
with open("questlog.json", "w") as f:
    json.dump(quests, f)
with open("questlog.json", "r") as f:
    geladen = json.load(f)
print(f"Mission-Anzahl: {len(geladen)}")
print(f"Status: {geladen[0]['status']}")
