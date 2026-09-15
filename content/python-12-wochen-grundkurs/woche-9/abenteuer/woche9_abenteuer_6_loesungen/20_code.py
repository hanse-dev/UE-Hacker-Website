import json

# Schritt 1: Schatzkarte anlegen
schatzkarte = {
    'Drachenhöhle': {'koordinaten': [42, 17], 'wert': 1500, 'beschreibung': 'Tief in den Bergen'},
    'Versunkener Tempel': {'koordinaten': [88, 55], 'wert': 3200, 'beschreibung': 'Unter dem alten See'},
    'Goblin-Festung': {'koordinaten': [23, 91], 'wert': 800, 'beschreibung': 'Im dunklen Wald'},
}

with open('schatzkarte.json', 'w') as f:
    json.dump(schatzkarte, f, indent=2)

print('Schatzkarte gespeichert!')

# Schritt 2: Karte laden und ausgeben
with open('schatzkarte.json', 'r') as f:
    geladene_karte = json.load(f)

print('\n=== Schatzkarte ===')
for ort, info in geladene_karte.items():
    print(f'  Ort: {ort}')
    print(f'    Koordinaten: {info["koordinaten"]}')
    print(f'    Wert: {info["wert"]} Gold')
    print(f'    Beschreibung: {info["beschreibung"]}')

# Schritt 3: Neuen Eintrag hinzufügen
geladene_karte['Elfenwald-Lichtung'] = {
    'koordinaten': [66, 33],
    'wert': 2100,
    'beschreibung': 'Versteckt im silbernen Elfenwald'
}

with open('schatzkarte.json', 'w') as f:
    json.dump(geladene_karte, f, indent=2)

print('\n=== Aktualisierte Schatzkarte ===')
for ort, info in geladene_karte.items():
    print(f'  {ort}: {info["wert"]} Gold')

# Bonus: Wertvollsten Schatz finden
wertvollster_ort = max(geladene_karte, key=lambda o: geladene_karte[o]['wert'])
print(f'\n*** Wertvollster Schatz: {wertvollster_ort} ({geladene_karte[wertvollster_ort]["wert"]} Gold) ***')