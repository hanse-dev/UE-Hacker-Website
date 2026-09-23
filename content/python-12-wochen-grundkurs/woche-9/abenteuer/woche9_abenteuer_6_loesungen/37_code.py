import csv
helden = [
    {"name": "Aria", "klasse": "Magierin", "level": 15, "leben": 120},
    {"name": "Thorin", "klasse": "Krieger", "level": 18, "leben": 150},
    {"name": "Luna", "klasse": "Schurkin", "level": 12, "leben": 90},
]
with open("helden.csv", "w", newline="") as f:
    schreiber = csv.DictWriter(f, fieldnames=["name", "klasse", "level", "leben"])
    schreiber.writeheader()
    schreiber.writerows(helden)
with open("helden.csv", "r") as f:
    zeilen = list(csv.DictReader(f))
print(f"Zeilen: {len(zeilen)}")
print(f"Erster: {zeilen[0]['name']}")
