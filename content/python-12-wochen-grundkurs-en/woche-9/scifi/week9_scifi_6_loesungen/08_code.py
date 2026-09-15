# Problem: access to non-existent columns
import csv
with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) >= 3:  # check if enough columns
            print(row[0], row[1], row[2])
        else:
            print(f'Row has only {len(row)} columns: {row}')