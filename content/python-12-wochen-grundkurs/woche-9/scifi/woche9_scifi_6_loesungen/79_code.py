import json
missionen = [
    {"name": "Signal orten", "schwierigkeit": 1, "status": "offen"},
    {"name": "Sonde starten", "schwierigkeit": 2, "status": "offen"},
    {"name": "Hülle reparieren", "schwierigkeit": 3, "status": "offen"},
]
with open("missionslog.json", "w") as f:
    json.dump(missionen, f)
with open("missionslog.json", "r") as f:
    geladen = json.load(f)
print(f"Mission-Anzahl: {len(geladen)}")
print(f"Status: {geladen[0]['status']}")
