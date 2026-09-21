import csv
with open("crew.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "rank"])
    w.writerow(["Nova", 4])
    w.writerow(["Rex", 6])
    w.writerow(["Zara", 3])
with open("crew.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    first = next(reader)
print(f"Text: {first[1] + first[1]}")
print(f"Number: {int(first[1]) * 2}")
