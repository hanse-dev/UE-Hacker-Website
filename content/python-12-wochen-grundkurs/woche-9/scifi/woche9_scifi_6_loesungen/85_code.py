import json
missionen = [
    {"name": "Signal orten", "schwierigkeit": 1, "status": "offen"},
    {"name": "Sonde starten", "schwierigkeit": 2, "status": "offen"},
    {"name": "Hülle reparieren", "schwierigkeit": 3, "status": "offen"},
]
missionen[0]["status"] = "abgeschlossen"
with open("missionslog.json", "w") as f:
    json.dump(missionen, f)
with open("missionslog.json", "r") as f:
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
