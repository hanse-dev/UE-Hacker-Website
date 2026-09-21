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
geladen[0]["status"] = "abgeschlossen"
with open("questlog.json", "w") as f:
    json.dump(geladen, f)
with open("questlog.json", "r") as f:
    neu = json.load(f)
print(f"Erste: {neu[0]['status']}")
