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

starke = []
with open("pferde.csv", "r") as f:
    for zeile in csv.DictReader(f):
        if int(zeile["alter"]) > 7:
            starke.append(zeile["name"])
with open("pferd.json", "w") as f:
    json.dump(starke, f)
with open("pferd.json", "r") as f:
    geladen = json.load(f)
print(f"Starke: {geladen}")
