import json

# Schritt 1: Helden-Daten als Dictionary
held = {
    'name': 'Thorin Eichenschild',
    'klasse': 'Krieger',
    'level': 12,
    'lebenspunkte': 250
}
print('Helden-Daten:', held)

# Schritt 2: JSON-Export
with open('held.json', 'w') as f:
    json.dump(held, f, indent=2)
print('Held in held.json gespeichert!')

# Schritt 3: JSON-Import
with open('held.json', 'r') as f:
    geladene_daten = json.load(f)

print(f'Geladener Held: {geladene_daten["name"]}')
print('Alle Daten:', geladene_daten)

# Schritt 4: Statistik
print(f'\n=== Helden-Statistik ===')
print(f'Name: {geladene_daten["name"]}')
print(f'Klasse: {geladene_daten["klasse"]}')
print(f'Level: {geladene_daten["level"]}')
print(f'Lebenspunkte: {geladene_daten["lebenspunkte"]}')