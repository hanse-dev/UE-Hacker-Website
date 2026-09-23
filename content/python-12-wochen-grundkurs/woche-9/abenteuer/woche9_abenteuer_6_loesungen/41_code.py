import json
helden = [
    {"name": "Aria", "klasse": "Magierin", "level": 15, "leben": 120},
    {"name": "Thorin", "klasse": "Krieger", "level": 18, "leben": 150},
    {"name": "Luna", "klasse": "Schurkin", "level": 12, "leben": 90},
]
with open("held.json", "w") as f:
    json.dump(helden, f)
import csv

with open("held.json", "r") as f:
    geladen = json.load(f)
with open("helden.csv", "w", newline="") as f:
    schreiber = csv.DictWriter(f, fieldnames=["name", "klasse", "level", "leben"])
    schreiber.writeheader()
    schreiber.writerows(geladen)
with open("helden.csv", "r") as f:
    leser = csv.DictReader(f)
    zeilen = list(leser)
    felder = leser.fieldnames
print(f"Zeilen: {len(zeilen)}")
print(f"Felder: {felder}")
