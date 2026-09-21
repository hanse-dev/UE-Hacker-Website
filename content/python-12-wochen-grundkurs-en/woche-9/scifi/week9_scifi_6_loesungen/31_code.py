import csv
import csv

with open("crew.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "rank"])
    writer.writerow(["Nova", 4])
    writer.writerow(["Rex", 6])
    writer.writerow(["Zara", 3])
with open("crew.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    rows = list(reader)
print(f"Rows: {len(rows)}")
