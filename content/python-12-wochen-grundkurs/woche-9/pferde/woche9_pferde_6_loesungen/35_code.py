import csv
with open("pferde.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "alter"])
    w.writerow(["Blitz", 8])
    w.writerow(["Sturm", 12])
    w.writerow(["Luna", 6])
with open("pferde.csv", "r") as f:
    leser = csv.reader(f)
    next(leser)
    erste = next(leser)
print(f"Text: {erste[1] + erste[1]}")
print(f"Zahl: {int(erste[1]) * 2}")
