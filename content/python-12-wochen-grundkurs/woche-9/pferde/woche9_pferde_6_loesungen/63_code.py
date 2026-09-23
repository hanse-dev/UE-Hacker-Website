import csv
pferde = [
    {"name": "Blitz", "rasse": "Hannoveraner", "alter": 8, "punkte": 120},
    {"name": "Sturm", "rasse": "Haflinger", "alter": 12, "punkte": 150},
    {"name": "Luna", "rasse": "Isländer", "alter": 6, "punkte": 90},
    {"name": "Wind", "rasse": "Hannoveraner", "alter": 7, "punkte": 110},
]
with open("pferde.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "rasse", "alter", "punkte"])
    w.writeheader()
    w.writerows(pferde)
summe = 0
with open("pferde.csv", "r") as f:
    zeilen = list(csv.DictReader(f))
for zeile in zeilen:
    summe += int(zeile["alter"])
print(f"Summe: {summe}")
print(f"Durchschnitt: {summe / len(zeilen)}")
