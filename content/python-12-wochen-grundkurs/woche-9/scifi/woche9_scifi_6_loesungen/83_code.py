import json
quests = [
    {"name": "Signal orten", "schwierigkeit": 1, "status": "offen"},
    {"name": "Sonde starten", "schwierigkeit": 2, "status": "offen"},
    {"name": "Hülle reparieren", "schwierigkeit": 3, "status": "offen"},
]
quests[0]["status"] = "abgeschlossen"
with open("questlog.json", "w") as f:
    json.dump(quests, f)
with open("questlog.json", "r") as f:
    geladen = json.load(f)
fertig = 0
for quest in geladen:
    if quest["status"] == "abgeschlossen":
        fertig += 1
with open("bericht.txt", "w") as f:
    f.write(f"Abgeschlossen: {fertig}\n")
with open("bericht.txt", "r") as f:
    inhalt = f.read()
print(f"Bericht: {inhalt.strip()}")
