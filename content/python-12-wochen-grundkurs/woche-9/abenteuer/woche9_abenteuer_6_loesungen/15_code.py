import csv

# Schritt 1: CSV-Export
helden = [
    {'name': 'Lyra', 'klasse': 'Bogenschützin', 'level': '8'},
    {'name': 'Gorund', 'klasse': 'Krieger', 'level': '12'},
    {'name': 'Selene', 'klasse': 'Magierin', 'level': '10'},
    {'name': 'Finn', 'klasse': 'Bogenschütze', 'level': '5'},
    {'name': 'Mira', 'klasse': 'Magierin', 'level': '7'},
]

with open('helden.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'klasse', 'level'])
    writer.writeheader()
    writer.writerows(helden)

print('Helden in helden.csv gespeichert!')

# Schritt 2: CSV-Import
gelesene_helden = []
with open('helden.csv', 'r') as f:
    reader = csv.DictReader(f)
    for zeile in reader:
        gelesene_helden.append(zeile)

print(f'Anzahl gelesener Einträge: {len(gelesene_helden)}')
print(f'Erster Eintrag: {gelesene_helden[0]}')

# Schritt 3: Suchfunktion
def suche_nach_klasse(dateiname, klasse):
    ergebnisse = []
    with open(dateiname, 'r') as f:
        reader = csv.DictReader(f)
        for zeile in reader:
            if zeile['klasse'] == klasse:
                ergebnisse.append(zeile)
    return ergebnisse

magierinnen = suche_nach_klasse('helden.csv', 'Magierin')
print(f'\nGefundene Magierinnen:')
for m in magierinnen:
    print(f'  {m["name"]} (Level {m["level"]})')

# Schritt 4: Kurzer Bericht
summe_level = sum(int(h['level']) for h in gelesene_helden)
durchschnitt = summe_level / len(gelesene_helden)

klassen_zaehler = {}
for h in gelesene_helden:
    k = h['klasse']
    klassen_zaehler[k] = klassen_zaehler.get(k, 0) + 1

print(f'\n=== Gilde-Bericht ===')
print(f'Durchschnittslevel: {durchschnitt:.1f}')
print('Anzahl pro Klasse:')
for klasse, anzahl in klassen_zaehler.items():
    print(f'  {klasse}: {anzahl}')