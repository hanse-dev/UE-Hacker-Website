import csv
pferde = [
    {"name": "Blitz", "rasse": "Hannoveraner", "alter": 8, "punkte": 120},
    {"name": "Sturm", "rasse": "Haflinger", "alter": 12, "punkte": 150},
    {"name": "Luna", "rasse": "Isländer", "alter": 6, "punkte": 90},
]
with open("pferde.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "rasse", "alter", "punkte"])
    w.writeheader()
    w.writerows(pferde)
import json

eintraege = []
with open("pferde.csv", "r") as f:
    for zeile in csv.DictReader(f):
        zeile["alter"] = int(zeile["alter"])
        eintraege.append(zeile)
with open("pferd.json", "w") as f:
    json.dump(eintraege, f)
with open("pferd.json", "r") as f:
    geladen = json.load(f)
summe = 0
for eintrag in geladen:
    summe += eintrag["alter"]
print(f"Anzahl: {len(geladen)}")
print(f"Summe: {summe}")
