import csv
with open("helden.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "level"])
    w.writerow(["Aria", 15])
    w.writerow(["Thorin", 18])
    w.writerow(["Luna", 12])
with open("helden.csv", "r") as f:
    leser = csv.reader(f)
    next(leser)
    erste = next(leser)
print(f"Text: {erste[1] + erste[1]}")
print(f"Zahl: {int(erste[1]) * 2}")
