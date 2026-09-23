import csv
with open("horses.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "age"])
    w.writerow(["Blitz", 8])
    w.writerow(["Storm", 12])
    w.writerow(["Luna", 6])
with open("horses.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    first = next(reader)
print(f"Text: {first[1] + first[1]}")
print(f"Number: {int(first[1]) * 2}")
