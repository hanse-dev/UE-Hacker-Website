import json

# Schritt 1: Sternenkarte anlegen
sternenkarte = {
    'Alpha Centauri': {'koordinaten': [4.37, 0.0, 0.0], 'status': 'Erkundet', 'entfernung_lj': 4.37},
    'Proxima Centauri': {'koordinaten': [4.24, 0.1, 0.3], 'status': 'Erkundet', 'entfernung_lj': 4.24},
    'Tau Ceti': {'koordinaten': [11.9, 2.1, -1.5], 'status': 'Unbekannt', 'entfernung_lj': 11.9},
}

with open('sternenkarte.json', 'w') as f:
    json.dump(sternenkarte, f, indent=2)

print('Sternenkarte gespeichert!')

# Schritt 2: Karte laden und ausgeben
with open('sternenkarte.json', 'r') as f:
    geladene_karte = json.load(f)

print('\n=== Sternenkarte ===')
for name, info in geladene_karte.items():
    print(f'  System: {name}')
    print(f'    Koordinaten: {info["koordinaten"]}')
    print(f'    Status: {info["status"]}')
    print(f'    Entfernung: {info["entfernung_lj"]} Lichtjahre')

# Schritt 3: Neues System hinzufügen
geladene_karte['Kepler-452'] = {
    'koordinaten': [1400.0, 55.2, -12.7],
    'status': 'Unbekannt',
    'entfernung_lj': 1400.0
}

with open('sternenkarte.json', 'w') as f:
    json.dump(geladene_karte, f, indent=2)

print('\n=== Aktualisierte Sternenkarte ===')
for name, info in geladene_karte.items():
    print(f'  {name}: {info["entfernung_lj"]} Lichtjahre – {info["status"]}')

# Bonus: Entferntestes System finden
entferntestes = max(geladene_karte, key=lambda s: geladene_karte[s]['entfernung_lj'])
print(f'\n*** Entferntestes System: {entferntestes} ({geladene_karte[entferntestes]["entfernung_lj"]} Lichtjahre) ***')