import json
einheiten = [
    {"name": "Springen üben", "schwierigkeit": 1, "status": "offen"},
    {"name": "Ausritt planen", "schwierigkeit": 2, "status": "offen"},
    {"name": "Fell pflegen", "schwierigkeit": 3, "status": "offen"},
]
einheiten[0]["status"] = "abgeschlossen"
with open("trainingslog.json", "w") as f:
    json.dump(einheiten, f)
with open("trainingslog.json", "r") as f:
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
