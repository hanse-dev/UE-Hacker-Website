import json
pferde = [
    {"name": "Blitz", "rasse": "Hannoveraner", "alter": 8, "punkte": 120},
    {"name": "Sturm", "rasse": "Haflinger", "alter": 12, "punkte": 150},
    {"name": "Luna", "rasse": "Isländer", "alter": 6, "punkte": 90},
]
with open("pferd.json", "w") as f:
    json.dump(pferde, f)
import csv

with open("pferd.json", "r") as f:
    geladen = json.load(f)
with open("pferde.csv", "w", newline="") as f:
    schreiber = csv.DictWriter(f, fieldnames=["name", "rasse", "alter", "punkte"])
    schreiber.writeheader()
    schreiber.writerows(geladen)
with open("pferde.csv", "r") as f:
    leser = csv.DictReader(f)
    zeilen = list(leser)
    felder = leser.fieldnames
print(f"Zeilen: {len(zeilen)}")
print(f"Felder: {felder}")
