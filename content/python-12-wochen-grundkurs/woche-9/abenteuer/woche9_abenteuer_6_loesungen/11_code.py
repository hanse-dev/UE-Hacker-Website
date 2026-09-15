from datetime import datetime

# Schritt 1: Quest-Log schreiben
with open('quest_log.txt', 'w') as f:
    f.write('[INFO] Quest gestartet: Drachen besiegen\n')
    f.write('[INFO] Held betritt die Drachenhöhle\n')
    f.write('[WARN] Gesundheit unter 50 XP\n')

print('Quest-Log erstellt!')

# Schritt 2: Zeitstempel hinzufügen
zeitstempel = datetime.now().strftime('%Y-%m-%d %H:%M')
neuer_eintrag = f'[INFO] {zeitstempel} - Held trinkt Heiltrank\n'

with open('quest_log.txt', 'a') as f:
    f.write(neuer_eintrag)

print(f'Neuer Eintrag: {neuer_eintrag.strip()}')

# Schritt 3: Log-Level – Datei komplett lesen und ausgeben
with open('quest_log.txt', 'r') as f:
    inhalt = f.read()

print('\n=== Quest-Log ===' )
print(inhalt)

# Schritt 4: Filter-Funktion
def filter_level(dateiname, level):
    ergebnisse = []
    with open(dateiname, 'r') as f:
        for zeile in f:
            if f'[{level}]' in zeile:
                ergebnisse.append(zeile.strip())
    return ergebnisse

warn_eintraege = filter_level('quest_log.txt', 'WARN')
print('=== Nur WARN-Einträge ===')
for eintrag in warn_eintraege:
    print(eintrag)