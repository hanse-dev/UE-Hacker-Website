# Beispiel 1: CSV-Schriftrollen schreiben
import csv

# Helden-Daten
helden_daten = [
    ['Name', 'Klasse', 'Level', 'Erfahrung'],
    ['Aria', 'Magierin', 15, 2500],
    ['Thorin', 'Krieger', 18, 3200],
    ['Luna', 'Schurkin', 12, 1800]
]

# CSV schreiben
with open('helden_daten.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(helden_daten)

print('✅ CSV-Schriftrolle erstellt!')