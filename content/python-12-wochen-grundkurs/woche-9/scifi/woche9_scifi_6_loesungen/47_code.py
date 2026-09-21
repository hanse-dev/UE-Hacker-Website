import csv
with open("test.csv", "w", newline="") as f:
    csv.writer(f).writerows([["name", "rang"], ["Nova", 4]])
with open("test.csv", "r") as f:
    zeilen = list(csv.reader(f))
print("Rang plus 1:", int(zeilen[1][1]) + 1)
