import csv
with open("heroes.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "level"])
    w.writerow(["Aria", 15])
    w.writerow(["Thorin", 18])
    w.writerow(["Luna", 12])
with open("heroes.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    first = next(reader)
print(f"Text: {first[1] + first[1]}")
print(f"Number: {int(first[1]) * 2}")
