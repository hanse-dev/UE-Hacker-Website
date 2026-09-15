# Beispiel 2: CSV-Dateien lesen
with open('crew_daten.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Überspringe Header
    
    print('=== Crew-Analyse ===')
    for zeile in reader:
        name, rolle, alter, erfahrung = zeile
        print(f'{name}: {rolle}, {alter} Jahre, {erfahrung} J. Erfahrung')