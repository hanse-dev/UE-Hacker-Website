import json

# Schritt 1: Pferde-Daten als Dictionary
pferd = {
    'name': 'Luna',
    'rasse': 'Andalusier',
    'alter': 7,
    'besitzer': 'Maria Schneider'
}
print('Pferde-Daten:', pferd)

# Schritt 2: JSON-Export
with open('pferd.json', 'w') as f:
    json.dump(pferd, f, indent=2)
print('Pferd in pferd.json gespeichert!')

# Schritt 3: JSON-Import
with open('pferd.json', 'r') as f:
    geladene_daten = json.load(f)

print(f'Geladenes Pferd: {geladene_daten["name"]}')
print('Alle Daten:', geladene_daten)

# Schritt 4: Statistik
print(f'\n=== Pferde-Steckbrief ===')
print(f'Name: {geladene_daten["name"]}')
print(f'Rasse: {geladene_daten["rasse"]}')
print(f'Alter: {geladene_daten["alter"]} Jahre')
print(f'Besitzer: {geladene_daten["besitzer"]}')