# Beispiel 3: CSV mit DictReader/DictWriter
# Mit DictWriter schreiben
felder = ['name', 'klasse', 'level', 'erfahrung']

with open('helden_daten_dict.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=felder)
    writer.writeheader()
    
    writer.writerow({'name': 'Aria', 'klasse': 'Magierin', 'level': 15, 'erfahrung': 2500})
    writer.writerow({'name': 'Thorin', 'klasse': 'Krieger', 'level': 18, 'erfahrung': 3200})

# Mit DictReader lesen
with open('helden_daten_dict.csv', 'r') as f:
    reader = csv.DictReader(f)
    
    print('=== Helden-Statistik ===')
    for zeile in reader:
        print(f'{zeile['name']} ({zeile['klasse']}): Level {zeile['level']}')