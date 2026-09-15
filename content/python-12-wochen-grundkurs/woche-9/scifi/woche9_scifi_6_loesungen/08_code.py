# Problem: Zugriff auf nicht existierende Spalten
import csv
with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    for zeile in reader:
        if len(zeile) >= 3:  # Prüfen ob genug Spalten
            print(zeile[0], zeile[1], zeile[2])
        else:
            print(f'Zeile hat nur {len(zeile)} Spalten: {zeile}')