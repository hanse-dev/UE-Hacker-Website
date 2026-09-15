import csv

# Schritt 1: CSV-Export
crew = [
    {'name': 'Commander Shepard', 'rang': 'Kommandant', 'alter': '35'},
    {'name': 'Dr. Vasquez', 'rang': 'Ärztin', 'alter': '29'},
    {'name': 'Hicks', 'rang': 'Sergeant', 'alter': '31'},
    {'name': 'Reyes', 'rang': 'Pilot', 'alter': '27'},
    {'name': 'Chen', 'rang': 'Pilot', 'alter': '33'},
]

with open('crew.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'rang', 'alter'])
    writer.writeheader()
    writer.writerows(crew)

print('Crew-Daten in crew.csv gespeichert!')

# Schritt 2: CSV-Import
gelesene_crew = []
with open('crew.csv', 'r') as f:
    reader = csv.DictReader(f)
    for zeile in reader:
        gelesene_crew.append(zeile)

print(f'Anzahl gelesener Einträge: {len(gelesene_crew)}')
print(f'Erster Eintrag: {gelesene_crew[0]}')

# Schritt 3: Suchfunktion nach Rang
def suche_nach_rang(dateiname, rang):
    ergebnisse = []
    with open(dateiname, 'r') as f:
        reader = csv.DictReader(f)
        for zeile in reader:
            if zeile['rang'] == rang:
                ergebnisse.append(zeile)
    return ergebnisse

piloten = suche_nach_rang('crew.csv', 'Pilot')
print(f'\nGefundene Piloten:')
for p in piloten:
    print(f'  {p["name"]} (Alter: {p["alter"]})')

# Schritt 4: Kurzer Bericht
summe_alter = sum(int(m['alter']) for m in gelesene_crew)
durchschnitt = summe_alter / len(gelesene_crew)

rang_zaehler = {}
for m in gelesene_crew:
    r = m['rang']
    rang_zaehler[r] = rang_zaehler.get(r, 0) + 1

print(f'\n=== Crew-Bericht ===')
print(f'Durchschnittsalter: {durchschnitt:.1f} Jahre')
print('Anzahl pro Rang:')
for rang, anzahl in rang_zaehler.items():
    print(f'  {rang}: {anzahl}')