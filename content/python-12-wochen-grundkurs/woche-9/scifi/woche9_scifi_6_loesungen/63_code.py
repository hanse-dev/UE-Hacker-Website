import csv
crew = [
    {"name": "Nova", "rolle": "Pilotin", "rang": 4, "energie": 120},
    {"name": "Rex", "rolle": "Ingenieur", "rang": 6, "energie": 150},
    {"name": "Zara", "rolle": "Botanikerin", "rang": 3, "energie": 90},
    {"name": "Kai", "rolle": "Pilotin", "rang": 5, "energie": 110},
]
with open("crew.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "rolle", "rang", "energie"])
    w.writeheader()
    w.writerows(crew)
summe = 0
with open("crew.csv", "r") as f:
    zeilen = list(csv.DictReader(f))
for zeile in zeilen:
    summe += int(zeile["rang"])
print(f"Summe: {summe}")
print(f"Durchschnitt: {summe / len(zeilen)}")
