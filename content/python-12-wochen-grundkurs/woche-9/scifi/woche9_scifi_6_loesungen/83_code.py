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
geladen[0]["status"] = "abgeschlossen"
with open("missionslog.json", "w") as f:
    json.dump(geladen, f)
with open("missionslog.json", "r") as f:
    neu = json.load(f)
print(f"Erste: {neu[0]['status']}")
