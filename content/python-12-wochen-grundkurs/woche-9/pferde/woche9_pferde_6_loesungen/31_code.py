import csv
import csv

with open("pferde.csv", "w", newline="") as f:
    schreiber = csv.writer(f)
    schreiber.writerow(["name", "alter"])
    schreiber.writerow(["Blitz", 8])
    schreiber.writerow(["Sturm", 12])
    schreiber.writerow(["Luna", 6])
with open("pferde.csv", "r") as f:
    leser = csv.reader(f)
    next(leser)
    zeilen = list(leser)
print(f"Zeilen: {len(zeilen)}")
