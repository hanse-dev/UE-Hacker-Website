import csv
crew = [
    {"name": "Nova", "rolle": "Pilotin", "rang": 4, "energie": 120},
    {"name": "Rex", "rolle": "Ingenieur", "rang": 6, "energie": 150},
    {"name": "Zara", "rolle": "Botanikerin", "rang": 3, "energie": 90},
]
with open("crew.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "rolle", "rang", "energie"])
    w.writeheader()
    w.writerows(crew)
import json

eintraege = []
with open("crew.csv", "r") as f:
    for zeile in csv.DictReader(f):
        zeile["rang"] = int(zeile["rang"])
        eintraege.append(zeile)
with open("mitglied.json", "w") as f:
    json.dump(eintraege, f)
with open("mitglied.json", "r") as f:
    geladen = json.load(f)
summe = 0
for eintrag in geladen:
    summe += eintrag["rang"]
print(f"Anzahl: {len(geladen)}")
print(f"Summe: {summe}")
