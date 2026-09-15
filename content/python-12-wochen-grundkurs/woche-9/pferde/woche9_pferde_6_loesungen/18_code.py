# Boss-Quest 1: Das Trainingstagebuch
# Hinweis: input() ist hier durch feste Beispielwerte ersetzt

# Schritt 1: Trainingseintrag schreiben
datum = '2024-06-17'
pferd_name = 'Luna'
uebung = 'Trabübungen auf dem Außenplatz – 30 Minuten'

with open('trainingstagebuch.txt', 'w') as f:
    f.write(f'[{datum}] Pferd: {pferd_name} | Übung: {uebung}\n')

print('Trainingseintrag gespeichert!')

# Schritt 2: Tagebuch lesen
with open('trainingstagebuch.txt', 'r') as f:
    print('\n=== Trainingstagebuch ===')
    print(f.read())

# Schritt 3: 3 weitere Einträge anhängen
weitere_eintraege = [
    ('2024-06-18', 'Spirit', 'Galopparbeit im Gelände – 45 Minuten'),
    ('2024-06-19', 'Luna', 'Springtraining – 1 Stunde'),
    ('2024-06-20', 'Rocco', 'Longierarbeit zur Aufwärmung – 20 Minuten'),
]

with open('trainingstagebuch.txt', 'a') as f:
    for d, p, e in weitere_eintraege:
        f.write(f'[{d}] Pferd: {p} | Übung: {e}\n')

# Komplettes Tagebuch ausgeben
with open('trainingstagebuch.txt', 'r') as f:
    zeilen = f.readlines()

print('=== Vollständiges Trainingstagebuch ===')
for zeile in zeilen:
    print(zeile.strip())

# Bonus: Einträge zählen
print(f'\nGesamt-Trainingseinheiten: {len(zeilen)}')