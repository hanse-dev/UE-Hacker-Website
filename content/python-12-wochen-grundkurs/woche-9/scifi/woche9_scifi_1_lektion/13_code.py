# Beispiel 3: CSV mit DictReader/DictWriter
# Mit DictWriter schreiben
felder = ['name', 'rolle', 'alter', 'erfahrung']

with open('crew_daten_dict.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=felder)
    writer.writeheader()
    
    writer.writerow({'name': 'Captain Alex', 'rolle': 'Kommandant', 'alter': 35, 'erfahrung': 15})
    writer.writerow({'name': 'Dr. Zara', 'rolle': 'Wissenschaftlerin', 'alter': 28, 'erfahrung': 8})

# Mit DictReader lesen
with open('crew_daten_dict.csv', 'r') as f:
    reader = csv.DictReader(f)
    
    print('=== Crew-Statistik ===')
    for zeile in reader:
        print(f'{zeile["name"]} ({zeile["rolle"]}): {zeile["alter"]} Jahre')