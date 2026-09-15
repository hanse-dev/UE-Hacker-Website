# Beispiel 1: Einfache Schriftrollen-Operationen
# Schriftrolle schreiben
with open('quest_log.txt', 'w') as f:
    f.write('Pyralia Quest Log\n')
    f.write('Datum: 15. März 1257\n')
    f.write('Status: Aktiv\n')

print('✅ Quest-Log erstellt!')

# Schriftrolle lesen
with open('quest_log.txt', 'r') as f:
    inhalt = f.read()
    print('=== Quest-Log ===')
    print(inhalt)