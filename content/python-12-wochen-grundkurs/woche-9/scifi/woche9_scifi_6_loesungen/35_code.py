import csv
with open("crew.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "rang"])
    w.writerow(["Nova", 4])
    w.writerow(["Rex", 6])
    w.writerow(["Zara", 3])
with open("crew.csv", "r") as f:
    leser = csv.reader(f)
    next(leser)
    erste = next(leser)
print(f"Text: {erste[1] + erste[1]}")
print(f"Zahl: {int(erste[1]) * 2}")
