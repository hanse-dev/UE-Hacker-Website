import csv
with open("helden.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "level"])
    w.writerow(["Aria", 15])
    w.writerow(["Thorin", 18])
    w.writerow(["Luna", 12])
summe = 0
with open("helden.csv", "r") as f:
    leser = csv.reader(f)
    next(leser)
    for zeile in leser:
        summe += int(zeile[1])
print(f"Summe: {summe}")
