# Beispiel 1: CSV-Dateien schreiben
import csv

# Pferde-Daten
pferde_daten = [
    ['Name', 'Rasse', 'Alter', 'Größe', 'Besitzer'],
    ['Thunder', 'Hannoveraner', 8, 1.72, 'Anna'],
    ['Luna', 'Isländer', 6, 1.35, 'Tom'],
    ['Stormy', 'Quarter Horse', 10, 1.58, 'Maria']
]

# CSV schreiben
with open('pferde_daten.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(pferde_daten)

print('✅ CSV-Datei erstellt!')