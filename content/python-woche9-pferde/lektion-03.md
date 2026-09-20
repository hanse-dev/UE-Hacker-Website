# 🐴 Übung 3: Wenn die Datei fehlt

Wer eine Datei lesen will, die es nicht gibt, bekommt einen **FileNotFoundError**. Den kennst du schon aus Woche 8: mit `try`/`except` fängst du ihn ab.

```python
try:
    with open("fehlt.txt", "r") as f:
        text = f.read()
except FileNotFoundError:
    print("Datei fehlt")

import os
print(os.path.exists("stallbuch.txt"))   # True oder False
os.remove("stallbuch.txt")               # Datei löschen
```

Mit **`os.path.exists(name)`** fragst du vorher, ob es die Datei gibt. Das Modul **`os`** kommt wie `math` und `random` aus Woche 7 fertig mit.
