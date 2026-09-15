# Beispiel 1: Einfache Dateioperationen
# Datei schreiben
with open('pferde_log.txt', 'w') as f:
    f.write('Sonnental Pferde-Log\n')
    f.write('Datum: 15.03.2025\n')
    f.write('Status: Alle Pferde gesund\n')

print('✅ Pferde-Log erstellt!')

# Datei lesen
with open('pferde_log.txt', 'r') as f:
    inhalt = f.read()
    print('=== Pferde-Log ===')
    print(inhalt)