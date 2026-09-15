import json

# Schritt 1: Quests speichern
questbuch = [
    {'name': 'Das verlorene Schwert', 'schwierigkeit': 'leicht', 'status': 'Offen'},
    {'name': 'Die Oger-Bedrohung', 'schwierigkeit': 'mittel', 'status': 'In Bearbeitung'},
    {'name': 'Der alte Drachenfürst', 'schwierigkeit': 'episch', 'status': 'Offen'},
]

with open('questbuch.json', 'w') as f:
    json.dump(questbuch, f, indent=2)

print('Questbuch gespeichert!')

# Schritt 2: Quests laden und anzeigen
with open('questbuch.json', 'r') as f:
    geladenes_buch = json.load(f)

print('\n=== Questbuch ===')
for i, quest in enumerate(geladenes_buch, 1):
    print(f'{i}. {quest["name"]}')
    print(f'   Schwierigkeit: {quest["schwierigkeit"]}')
    print(f'   Status: {quest["status"]}')

# Schritt 3: Quest abschließen
geladenes_buch[1]['status'] = 'Abgeschlossen'

with open('questbuch.json', 'w') as f:
    json.dump(geladenes_buch, f, indent=2)

print('\n=== Aktualisiertes Questbuch ===')
for quest in geladenes_buch:
    status_symbol = '✅' if quest['status'] == 'Abgeschlossen' else '⏳'
    print(f'{status_symbol} {quest["name"]} – {quest["status"]}')

# Bonus: Abschlussbericht als Textdatei
abgeschlossene = [q for q in geladenes_buch if q['status'] == 'Abgeschlossen']
with open('abschlussbericht.txt', 'w') as f:
    f.write('=== Gilde-Abschlussbericht ===\n')
    f.write(f'Abgeschlossene Quests: {len(abgeschlossene)}\n')
    for q in abgeschlossene:
        f.write(f'  - {q["name"]} (Schwierigkeit: {q["schwierigkeit"]})\n')

print('\nAbschlussbericht in abschlussbericht.txt gespeichert!')