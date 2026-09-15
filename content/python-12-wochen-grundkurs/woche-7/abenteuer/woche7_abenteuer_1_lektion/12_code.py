# Beispiel: Ein Warte-Ritual und die aktuelle Stunde
import time
from datetime import datetime

print("Ein Ritual beginnt zu wirken...")
time.sleep(1)
print("Das Ritual ist vollendet!")

jetzt = datetime.now()
print(f"\nAktuelle Uhrzeit: {jetzt.strftime('%H:%M:%S')}")

if 6 <= jetzt.hour < 18:
    print("Es ist Tag – die Sonnentore des Archivs stehen offen.")
else:
    print("Es ist Nacht – nur die Mondtore des Archivs sind geöffnet.")
