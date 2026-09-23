import csv
import csv

with open("helden.csv", "w", newline="") as f:
    schreiber = csv.writer(f)
    schreiber.writerow(["name", "level"])
    schreiber.writerow(["Aria", 15])
    schreiber.writerow(["Thorin", 18])
    schreiber.writerow(["Luna", 12])
with open("helden.csv", "r") as f:
    leser = csv.reader(f)
    next(leser)
    zeilen = list(leser)
print(f"Zeilen: {len(zeilen)}")
