import json

# Schritt 1: Missionen speichern
archiv = [
    {'name': 'Operation Sternenlicht', 'planet': 'Mars', 'ergebnis': 'In Bearbeitung', 'crew': ['Shepard', 'Hicks']},
    {'name': 'Expedition Kepler', 'planet': 'Kepler-452b', 'ergebnis': 'Offen', 'crew': ['Vasquez', 'Chen']},
    {'name': 'Basis Alpha Aufbau', 'planet': 'Mond', 'ergebnis': 'Offen', 'crew': ['Reyes', 'Hicks', 'Chen']},
]

with open('missionsarchiv.json', 'w') as f:
    json.dump(archiv, f, indent=2)

print('Missionsarchiv gespeichert!')

# Schritt 2: Archiv laden und anzeigen
with open('missionsarchiv.json', 'r') as f:
    geladenes_archiv = json.load(f)

print('\n=== Missionsarchiv ===')
for i, mission in enumerate(geladenes_archiv, 1):
    print(f'{i}. {mission["name"]}')
    print(f'   Planet: {mission["planet"]}')
    print(f'   Status: {mission["ergebnis"]}')
    print(f'   Crew: {', '.join(mission["crew"])}')

# Schritt 3: Mission aktualisieren
geladenes_archiv[0]['ergebnis'] = 'Erfolgreich abgeschlossen'

with open('missionsarchiv.json', 'w') as f:
    json.dump(geladenes_archiv, f, indent=2)

print('\n=== Finales Missionsarchiv ===')
for mission in geladenes_archiv:
    status_symbol = '✅' if mission['ergebnis'] == 'Erfolgreich abgeschlossen' else '⏳'
    print(f'{status_symbol} {mission["name"]} – {mission["ergebnis"]}')

# Bonus: Missionsbericht als Textdatei
abgeschlossene = [m for m in geladenes_archiv if m['ergebnis'] == 'Erfolgreich abgeschlossen']
with open('missionsbericht.txt', 'w') as f:
    f.write('=== Flotten-Missionsbericht ===\n')
    f.write(f'Gesamt-Missionen: {len(geladenes_archiv)}\n')
    f.write(f'Abgeschlossen: {len(abgeschlossene)}\n')
    f.write('\nAbgeschlossene Missionen:\n')
    for m in abgeschlossene:
        f.write(f'  - {m["name"]} (Planet: {m["planet"]})\n')

print('\nMissionsbericht in missionsbericht.txt gespeichert!')