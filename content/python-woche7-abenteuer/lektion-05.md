# ⏳ Archiv-Zauber 5: Zeit mit time und datetime

```python
import time
from datetime import datetime

start = time.time()        # aktueller Zeitstempel (Sekunden)
time.sleep(0.2)            # 0,2 Sekunden warten
ende = time.time()
print(ende - start)        # etwa 0.2

jetzt = datetime.now()     # aktuelles Datum und Uhrzeit
print(jetzt.hour)          # nur die Stunde (0–23)
print(jetzt.strftime("%Y-%m-%d"))   # Datum als Text formatieren
```

- **`time.sleep(sekunden)`** pausiert das Programm
- **`time.time()`** liefert einen Zeitstempel – die **Differenz** zweier Zeitstempel ist die vergangene Zeit
- **`datetime.now()`** liefert Datum und Uhrzeit; `.hour`, `.minute`, `.year` … holen einzelne Teile
- **`strftime("...")`** formatiert die Zeit als Text: `%Y` Jahr, `%m` Monat, `%d` Tag, `%H:%M` Uhrzeit

> 💡 Halte Wartezeiten hier kurz (unter einer Sekunde) – die Aufgaben sollen schnell laufen.
