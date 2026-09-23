import csv
with open("crew.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "rank"])
    w.writerow(["Nova", 4])
    w.writerow(["Rex", 6])
    w.writerow(["Zara", 3])
total = 0
with open("crew.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        total += int(row[1])
print(f"Total: {total}")
