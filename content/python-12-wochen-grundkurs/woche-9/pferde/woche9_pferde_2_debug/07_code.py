import csv
with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    for zeile in reader:
        print(zeile[0], zeile[1], zeile[2])