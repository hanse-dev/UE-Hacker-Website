import csv
with open("horses.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "age"])
    w.writerow(["Blitz", 8])
    w.writerow(["Storm", 12])
    w.writerow(["Luna", 6])
total = 0
with open("horses.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        total += int(row[1])
print(f"Total: {total}")
