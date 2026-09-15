# Beispiel 3: Dateien anhängen und Fehlerbehandlung
# An existierende Datei anhängen
with open('pferde_log.txt', 'a') as f:
    f.write('Update: Futterlieferung eingetroffen\n')

print('✅ Update hinzugefügt!')

# Mit Fehlerbehandlung
try:
    with open('nicht_existiert.txt', 'r') as f:
        inhalt = f.read()
except FileNotFoundError:
    print('❌ Datei nicht gefunden!')

# Prüfen ob Datei existiert
import os
if os.path.exists('pferde_log.txt'):
    print('✅ Pferde-Log existiert!')
else:
    print('❌ Pferde-Log nicht gefunden!')