import json

# Schritt 1: Stallkarte anlegen
stallkarte = {
    'Luna': {'rasse': 'Andalusier', 'box': 3, 'futterration': 6.5},
    'Spirit': {'rasse': 'Isländer', 'box': 7, 'futterration': 5.0},
    'Rocco': {'rasse': 'Isländer', 'box': 1, 'futterration': 4.5},
}

with open('stallkarte.json', 'w') as f:
    json.dump(stallkarte, f, indent=2)

print('Stallkarte gespeichert!')

# Schritt 2: Karte laden und ausgeben
with open('stallkarte.json', 'r') as f:
    geladene_karte = json.load(f)

print('\n=== Stallkarte ===')
for name, info in geladene_karte.items():
    print(f'  Pferd: {name}')
    print(f'    Rasse: {info["rasse"]}')
    print(f'    Box: {info["box"]}')
    print(f'    Futterration: {info["futterration"]} kg/Tag')

# Schritt 3: Neues Pferd hinzufügen
geladene_karte['Bella'] = {
    'rasse': 'Shetlandpony',
    'box': 12,
    'futterration': 3.0
}

with open('stallkarte.json', 'w') as f:
    json.dump(geladene_karte, f, indent=2)

print('\n=== Aktualisierte Stallkarte ===')
for name, info in geladene_karte.items():
    print(f'  {name} (Box {info["box"]}): {info["futterration"]} kg Futter/Tag')

# Bonus: Gesamt-Futterration berechnen
gesamt_futter = sum(info['futterration'] for info in geladene_karte.values())
print(f'\nGesamt-Futterration pro Tag: {gesamt_futter:.1f} kg')