import csv
helden = [
    {"name": "Aria", "klasse": "Magierin", "level": 15, "leben": 120},
    {"name": "Thorin", "klasse": "Krieger", "level": 18, "leben": 150},
    {"name": "Luna", "klasse": "Schurkin", "level": 12, "leben": 90},
    {"name": "Mira", "klasse": "Magierin", "level": 13, "leben": 110},
]
with open("helden.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "klasse", "level", "leben"])
    w.writeheader()
    w.writerows(helden)
summe = 0
with open("helden.csv", "r") as f:
    zeilen = list(csv.DictReader(f))
for zeile in zeilen:
    summe += int(zeile["level"])
print(f"Summe: {summe}")
print(f"Durchschnitt: {summe / len(zeilen)}")
