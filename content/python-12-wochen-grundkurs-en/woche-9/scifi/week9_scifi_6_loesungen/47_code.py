import csv
with open("test.csv", "w", newline="") as f:
    csv.writer(f).writerows([["name", "rank"], ["Nova", 4]])
with open("test.csv", "r") as f:
    rows = list(csv.reader(f))
print("Rank plus 1:", int(rows[1][1]) + 1)
