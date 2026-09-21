import csv
import csv

with open("horses.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])
    writer.writerow(["Blitz", 8])
    writer.writerow(["Storm", 12])
    writer.writerow(["Luna", 6])
with open("horses.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    rows = list(reader)
print(f"Rows: {len(rows)}")
