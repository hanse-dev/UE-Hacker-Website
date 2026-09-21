import csv
import csv

with open("heroes.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "level"])
    writer.writerow(["Aria", 15])
    writer.writerow(["Thorin", 18])
    writer.writerow(["Luna", 12])
with open("heroes.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    rows = list(reader)
print(f"Rows: {len(rows)}")
