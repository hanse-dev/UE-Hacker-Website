import csv
import csv

with open("crew.csv", "w", newline="") as f:
    schreiber = csv.writer(f)
    schreiber.writerow(["name", "rang"])
    schreiber.writerow(["Nova", 4])
    schreiber.writerow(["Rex", 6])
    schreiber.writerow(["Zara", 3])
with open("crew.csv", "r") as f:
    leser = csv.reader(f)
    next(leser)
    zeilen = list(leser)
print(f"Zeilen: {len(zeilen)}")
