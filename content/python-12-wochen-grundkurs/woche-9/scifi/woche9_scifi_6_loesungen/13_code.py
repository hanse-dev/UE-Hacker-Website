import json

# Schritt 1: Schiff-Daten als Dictionary
schiff = {
    'name': 'Nebula-7',
    'typ': 'Erkundungskreuzer',
    'crew': 42,
    'systeme': ['Lebenserhaltung', 'Antrieb', 'Waffensystem', 'Sensoren']
}
print('Schiff-Daten:', schiff)

# Schritt 2: JSON-Export
with open('schiff.json', 'w') as f:
    json.dump(schiff, f, indent=2)
print('Schiff-Daten in schiff.json gespeichert!')

# Schritt 3: JSON-Import
with open('schiff.json', 'r') as f:
    geladene_daten = json.load(f)

print(f'Geladenes Schiff: {geladene_daten["name"]}')
print('Alle Daten:', geladene_daten)

# Schritt 4: Statistik
print(f'\n=== Schiffs-Statistik ===')
print(f'Name: {geladene_daten["name"]}')
print(f'Typ: {geladene_daten["typ"]}')
print(f'Crew-Stärke: {geladene_daten["crew"]} Personen')
print(f'Aktive Systeme: {len(geladene_daten["systeme"])}')
for system in geladene_daten['systeme']:
    print(f'  - {system}')