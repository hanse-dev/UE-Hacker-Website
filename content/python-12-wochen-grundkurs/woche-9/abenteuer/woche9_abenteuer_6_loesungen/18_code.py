# Boss-Quest 1: Das Helden-Tagebuch
# Hinweis: input() ist hier durch feste Beispielwerte ersetzt

# Schritt 1: Eintrag schreiben (mit festem Datum statt input)
datum = '2024-06-17'
eintrag = 'Besiegte den Goblin-Hauptmann in der Höhle des Vergessens'

with open('helden_tagebuch.txt', 'w') as f:
    f.write(f'[{datum}] {eintrag}\n')

print('Eintrag gespeichert!')

# Schritt 2: Tagebuch lesen
with open('helden_tagebuch.txt', 'r') as f:
    print('\n=== Helden-Tagebuch ===')
    print(f.read())

# Schritt 3: 3 weitere Einträge anhängen
weitere_eintraege = [
    ('2024-06-18', 'Fand den magischen Beutel im alten Tempel'),
    ('2024-06-19', 'Rettete das Dorf vor dem wandelnden Totenberg'),
    ('2024-06-20', 'Erhielt die Gilde-Meister-Urkunde vom Rat der Weisen'),
]

with open('helden_tagebuch.txt', 'a') as f:
    for d, e in weitere_eintraege:
        f.write(f'[{d}] {e}\n')

# Komplettes Tagebuch ausgeben
with open('helden_tagebuch.txt', 'r') as f:
    zeilen = f.readlines()

print('=== Vollständiges Tagebuch ===')
for zeile in zeilen:
    print(zeile.strip())

# Bonus: Einträge zählen
print(f'\nGesamt-Einträge: {len(zeilen)}')