import json

# Schritt 1: Turnierergebnisse speichern
turnierbuch = [
    {'reiter': 'Lisa Müller', 'pferd': 'Luna', 'platzierung': 1, 'disziplin': 'Dressur'},
    {'reiter': 'Tom Becker', 'pferd': 'Spirit', 'platzierung': 3, 'disziplin': 'Springen'},
    {'reiter': 'Sarah Klein', 'pferd': 'Rocco', 'platzierung': 2, 'disziplin': 'Dressur'},
]

with open('turnierbuch.json', 'w') as f:
    json.dump(turnierbuch, f, indent=2)

print('Turnierbuch gespeichert!')

# Schritt 2: Ergebnisse laden und anzeigen
with open('turnierbuch.json', 'r') as f:
    geladenes_buch = json.load(f)

print('\n=== Turnierbuch ===')
for eintrag in geladenes_buch:
    platz_symbol = '🥇' if eintrag['platzierung'] == 1 else ('🥈' if eintrag['platzierung'] == 2 else '🥉')
    print(f'{platz_symbol} Platz {eintrag["platzierung"]}: {eintrag["reiter"]} mit {eintrag["pferd"]} ({eintrag["disziplin"]})')

# Schritt 3: Champions ermitteln und Champion-Eintrag hinzufügen
champions = [e for e in geladenes_buch if e['platzierung'] == 1]

for champ in champions:
    champ['titel'] = 'Champion'

with open('turnierbuch.json', 'w') as f:
    json.dump(geladenes_buch, f, indent=2)

print('\n=== Finales Turnierbuch ===')
for eintrag in geladenes_buch:
    titel = eintrag.get('titel', '')
    print(f'  Platz {eintrag["platzierung"]}: {eintrag["reiter"]} {titel}')

# Bonus: Kurzer Turnierbericht als Textdatei
with open('turnierbericht.txt', 'w') as f:
    f.write('=== Reiterhof-Turnierbericht ===\n')
    f.write(f'Teilnehmer: {len(geladenes_buch)}\n')
    f.write('\nErgebnisse:\n')
    for eintrag in sorted(geladenes_buch, key=lambda e: e['platzierung']):
        f.write(f'  Platz {eintrag["platzierung"]}: {eintrag["reiter"]} mit {eintrag["pferd"]}\n')
    f.write(f'\nChampion: {champions[0]["reiter"]} mit {champions[0]["pferd"]}!\n')

print('\nTurnierbericht in turnierbericht.txt gespeichert!')