import csv
with open("heroes.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "level"])
    w.writerow(["Aria", 15])
    w.writerow(["Thorin", 18])
    w.writerow(["Luna", 12])
total = 0
with open("heroes.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        total += int(row[1])
print(f"Total: {total}")
