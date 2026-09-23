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
starke = []
with open("pferde.csv", "r") as f:
    for zeile in csv.DictReader(f):
        if int(zeile["alter"]) > 7:
            starke.append(zeile["name"])
print(f"Starke: {starke}")
