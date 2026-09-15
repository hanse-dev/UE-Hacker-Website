# Beispiel 2: CSV-Schriftrollen lesen
with open('helden_daten.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # Überspringe Header
    
    print('=== Helden-Analyse ===')
    for zeile in reader:
        name, klasse, level, erfahrung = zeile
        print(f'{name}: {klasse}, Level {level}, {erfahrung} XP')