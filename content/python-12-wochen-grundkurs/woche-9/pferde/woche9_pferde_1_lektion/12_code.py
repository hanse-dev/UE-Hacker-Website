# Beispiel 2: CSV-Dateien lesen
with open('pferde_daten.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Überspringe Header
    
    print('=== Pferde-Analyse ===')
    for zeile in reader:
        name, rasse, alter, groesse, besitzer = zeile
        print(f'{name}: {rasse}, {alter} Jahre, {groesse}m, Besitzer: {besitzer}')