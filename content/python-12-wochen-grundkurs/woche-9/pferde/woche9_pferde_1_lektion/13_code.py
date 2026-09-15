# Beispiel 3: CSV mit DictReader/DictWriter
# Mit DictWriter schreiben
felder = ['name', 'rasse', 'alter', 'groesse', 'besitzer']

with open('pferde_daten_dict.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=felder)
    writer.writeheader()
    
    writer.writerow({'name': 'Thunder', 'rasse': 'Hannoveraner', 'alter': 8, 'groesse': 1.72, 'besitzer': 'Anna'})
    writer.writerow({'name': 'Luna', 'rasse': 'Isländer', 'alter': 6, 'groesse': 1.35, 'besitzer': 'Tom'})

# Mit DictReader lesen
with open('pferde_daten_dict.csv', 'r') as f:
    reader = csv.DictReader(f)
    
    print('=== Pferde-Statistik ===')
    for zeile in reader:
        print(f'{zeile['name']} ({zeile['rasse']}): {zeile['alter']} Jahre, {zeile['groesse']}m')