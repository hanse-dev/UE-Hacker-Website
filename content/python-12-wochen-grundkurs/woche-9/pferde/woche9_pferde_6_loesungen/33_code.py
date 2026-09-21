import csv
with open("pferde.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "alter"])
    w.writerow(["Blitz", 8])
    w.writerow(["Sturm", 12])
    w.writerow(["Luna", 6])
summe = 0
with open("pferde.csv", "r") as f:
    leser = csv.reader(f)
    next(leser)
    for zeile in leser:
        summe += int(zeile[1])
print(f"Summe: {summe}")
