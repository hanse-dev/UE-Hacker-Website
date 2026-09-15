# Beispiel 1: Einfache Dateioperationen
# Datei schreiben
with open('mission_log.txt', 'w') as f:
    f.write('Nebula-7 Mission Log\n')
    f.write('Datum: 2157.03.15\n')
    f.write('Status: Aktiv\n')

print('✅ Mission-Log erstellt!')

# Datei lesen
with open('mission_log.txt', 'r') as f:
    inhalt = f.read()
    print('=== Mission-Log ===')
    print(inhalt)