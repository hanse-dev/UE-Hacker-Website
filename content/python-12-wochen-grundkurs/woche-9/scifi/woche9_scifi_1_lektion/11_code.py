# Beispiel 1: CSV-Dateien schreiben
import csv

# Crew-Daten
crew_daten = [
    ['Name', 'Rolle', 'Alter', 'Erfahrung'],
    ['Captain Alex', 'Kommandant', 35, 15],
    ['Dr. Zara', 'Wissenschaftlerin', 28, 8],
    ['Lt. Nova', 'Pilotin', 26, 6]
]

# CSV schreiben
with open('crew_daten.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(crew_daten)

print('✅ CSV-Datei erstellt!')