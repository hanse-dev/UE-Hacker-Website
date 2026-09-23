import json
crew = [
    {"name": "Nova", "rolle": "Pilotin", "rang": 4, "energie": 120},
    {"name": "Rex", "rolle": "Ingenieur", "rang": 6, "energie": 150},
    {"name": "Zara", "rolle": "Botanikerin", "rang": 3, "energie": 90},
]
with open("mitglied.json", "w") as f:
    json.dump(crew, f)
import csv

with open("mitglied.json", "r") as f:
    geladen = json.load(f)
with open("crew.csv", "w", newline="") as f:
    schreiber = csv.DictWriter(f, fieldnames=["name", "rolle", "rang", "energie"])
    schreiber.writeheader()
    schreiber.writerows(geladen)
with open("crew.csv", "r") as f:
    leser = csv.DictReader(f)
    zeilen = list(leser)
    felder = leser.fieldnames
print(f"Zeilen: {len(zeilen)}")
print(f"Felder: {felder}")
