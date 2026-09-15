import csv

# Schritt 1: CSV-Export
pferde = [
    {'name': 'Luna', 'rasse': 'Andalusier', 'alter': '7'},
    {'name': 'Spirit', 'rasse': 'Isländer', 'alter': '12'},
    {'name': 'Rocco', 'rasse': 'Isländer', 'alter': '5'},
    {'name': 'Bella', 'rasse': 'Shetlandpony', 'alter': '9'},
    {'name': 'Thunder', 'rasse': 'Andalusier', 'alter': '4'},
]

with open('pferde.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'rasse', 'alter'])
    writer.writeheader()
    writer.writerows(pferde)

print('Pferde in pferde.csv gespeichert!')

# Schritt 2: CSV-Import
gelesene_pferde = []
with open('pferde.csv', 'r') as f:
    reader = csv.DictReader(f)
    for zeile in reader:
        gelesene_pferde.append(zeile)

print(f'Anzahl gelesener Einträge: {len(gelesene_pferde)}')
print(f'Erster Eintrag: {gelesene_pferde[0]}')

# Schritt 3: Suchfunktion nach Rasse
def suche_nach_rasse(dateiname, rasse):
    ergebnisse = []
    with open(dateiname, 'r') as f:
        reader = csv.DictReader(f)
        for zeile in reader:
            if zeile['rasse'] == rasse:
                ergebnisse.append(zeile)
    return ergebnisse

islaender = suche_nach_rasse('pferde.csv', 'Isländer')
print(f'\nGefundene Isländer:')
for p in islaender:
    print(f'  {p["name"]} (Alter: {p["alter"]} Jahre)')

# Schritt 4: Kurzer Bericht
summe_alter = sum(int(p['alter']) for p in gelesene_pferde)
durchschnitt = summe_alter / len(gelesene_pferde)

rassen_zaehler = {}
for p in gelesene_pferde:
    r = p['rasse']
    rassen_zaehler[r] = rassen_zaehler.get(r, 0) + 1

print(f'\n=== Stall-Bericht ===')
print(f'Durchschnittsalter: {durchschnitt:.1f} Jahre')
print('Anzahl pro Rasse:')
for rasse, anzahl in rassen_zaehler.items():
    print(f'  {rasse}: {anzahl}')