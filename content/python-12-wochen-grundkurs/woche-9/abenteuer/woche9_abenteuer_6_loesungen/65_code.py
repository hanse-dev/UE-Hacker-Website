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
starke = []
with open("helden.csv", "r") as f:
    for zeile in csv.DictReader(f):
        if int(zeile["level"]) > 14:
            starke.append(zeile["name"])
print(f"Starke: {starke}")
