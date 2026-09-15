# Beispiel 3: Schriftrollen anhängen und Fehlerbehandlung
# An existierende Schriftrolle anhängen
with open('quest_log.txt', 'a') as f:
    f.write('Update: Monster besiegt\n')

print('✅ Update hinzugefügt!')

# Mit Fehlerbehandlung
try:
    with open('nicht_existiert.txt', 'r') as f:
        inhalt = f.read()
except FileNotFoundError:
    print('❌ Schriftrolle nicht gefunden!')

# Prüfen ob Schriftrolle existiert
import os
if os.path.exists('quest_log.txt'):
    print('✅ Quest-Log existiert!')
else:
    print('❌ Quest-Log nicht gefunden!')