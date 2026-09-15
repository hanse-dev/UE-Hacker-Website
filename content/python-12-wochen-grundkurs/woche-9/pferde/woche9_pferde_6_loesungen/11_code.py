from datetime import datetime

# Schritt 1: Stall-Log schreiben
with open('stall_log.txt', 'w') as f:
    f.write('[INFO] Luna: Morgenfütterung abgeschlossen\n')
    f.write('[INFO] Spirit: Hufe gereinigt\n')
    f.write('[WARN] Rocco: Huf-Verletzung festgestellt – Tierarzt benachrichtigen\n')

print('Stall-Log erstellt!')

# Schritt 2: Zeitstempel hinzufügen
zeitstempel = datetime.now().strftime('%Y-%m-%d %H:%M')
neuer_eintrag = f'[INFO] {zeitstempel} - Luna: Abendtraining absolviert\n'

with open('stall_log.txt', 'a') as f:
    f.write(neuer_eintrag)

print(f'Neuer Eintrag: {neuer_eintrag.strip()}')

# Schritt 3: Log-Level – Datei komplett lesen und ausgeben
with open('stall_log.txt', 'r') as f:
    inhalt = f.read()

print('\n=== Stall-Log ===')
print(inhalt)

# Schritt 4: Filter-Funktion
def filter_level(dateiname, level):
    ergebnisse = []
    with open(dateiname, 'r') as f:
        for zeile in f:
            if f'[{level}]' in zeile:
                ergebnisse.append(zeile.strip())
    return ergebnisse

warn_eintraege = filter_level('stall_log.txt', 'WARN')
print('=== Nur WARN-Einträge ===')
for eintrag in warn_eintraege:
    print(eintrag)