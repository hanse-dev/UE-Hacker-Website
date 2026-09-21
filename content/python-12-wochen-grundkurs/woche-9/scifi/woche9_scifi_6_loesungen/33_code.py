import csv
with open("crew.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "rang"])
    w.writerow(["Nova", 4])
    w.writerow(["Rex", 6])
    w.writerow(["Zara", 3])
summe = 0
with open("crew.csv", "r") as f:
    leser = csv.reader(f)
    next(leser)
    for zeile in leser:
        summe += int(zeile[1])
print(f"Summe: {summe}")
