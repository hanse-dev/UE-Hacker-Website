# Boss-Quest 1: Das Missionstagebuch
# Hinweis: input() ist hier durch feste Beispielwerte ersetzt

# Schritt 1: Log-Eintrag schreiben
datum = '2324-03-15'
planet = 'Kepler-452b'
ereignis = 'Erste Bodenproben gesammelt – Lebenszeichen detected'

with open('missionstagebuch.txt', 'w') as f:
    f.write(f'[{datum}] Planet: {planet} | {ereignis}\n')

print('Log-Eintrag gespeichert!')

# Schritt 2: Log lesen
with open('missionstagebuch.txt', 'r') as f:
    print('\n=== Missionstagebuch ===')
    print(f.read())

# Schritt 3: 3 weitere Einträge anhängen
weitere_eintraege = [
    ('2324-03-16', 'Kepler-452b', 'Kontakt mit Außerirdischer Spezies hergestellt'),
    ('2324-03-17', 'Orbita', 'Notlandung nach Meteoriten-Treffer'),
    ('2324-03-20', 'Erde', 'Rückkehr zur Basis – Mission erfolgreich'),
]

with open('missionstagebuch.txt', 'a') as f:
    for d, p, e in weitere_eintraege:
        f.write(f'[{d}] Planet: {p} | {e}\n')

# Komplettes Log ausgeben
with open('missionstagebuch.txt', 'r') as f:
    zeilen = f.readlines()

print('=== Vollständiges Missionstagebuch ===')
for zeile in zeilen:
    print(zeile.strip())

# Bonus: Einträge zählen
print(f'\nGesamt-Log-Einträge: {len(zeilen)}')