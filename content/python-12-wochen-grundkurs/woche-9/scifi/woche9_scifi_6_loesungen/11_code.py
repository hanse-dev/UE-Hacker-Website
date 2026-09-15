from datetime import datetime

# Schritt 1: Log-Datei schreiben
with open('log.txt', 'w') as f:
    f.write('[INFO] Raumstation Nebula-7 gestartet\n')
    f.write('[INFO] Alle Systeme nominal\n')
    f.write('[WARN] Sauerstoff-Level auf Deck 3 leicht erhöht\n')

print('Log-Datei erstellt!')

# Schritt 2: Zeitstempel hinzufügen
zeitstempel = datetime.now().strftime('%Y-%m-%d %H:%M')
neuer_eintrag = f'[INFO] {zeitstempel} - Hyperantrieb aktiviert\n'

with open('log.txt', 'a') as f:
    f.write(neuer_eintrag)

print(f'Neuer Eintrag: {neuer_eintrag.strip()}')

# Schritt 3: Log-Level – Datei komplett lesen und ausgeben
with open('log.txt', 'r') as f:
    inhalt = f.read()

print('\n=== System-Log ===')
print(inhalt)

# Schritt 4: Filter-Funktion
def filter_level(dateiname, level):
    ergebnisse = []
    with open(dateiname, 'r') as f:
        for zeile in f:
            if f'[{level}]' in zeile:
                ergebnisse.append(zeile.strip())
    return ergebnisse

warn_eintraege = filter_level('log.txt', 'WARN')
print('=== Nur WARN-Einträge ===')
for eintrag in warn_eintraege:
    print(eintrag)