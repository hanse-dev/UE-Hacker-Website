# Beispiel 3: Dateien anhängen und Fehlerbehandlung
# An existierende Datei anhängen
with open('mission_log.txt', 'a') as f:
    f.write('Update: Systeme nominal\n')

print('✅ Update hinzugefügt!')

# Mit Fehlerbehandlung
try:
    with open('nicht_existiert.txt', 'r') as f:
        inhalt = f.read()
except FileNotFoundError:
    print('❌ Datei nicht gefunden!')

# Prüfen ob Datei existiert
import os
if os.path.exists('mission_log.txt'):
    print('✅ Mission-Log existiert!')
else:
    print('❌ Mission-Log nicht gefunden!')