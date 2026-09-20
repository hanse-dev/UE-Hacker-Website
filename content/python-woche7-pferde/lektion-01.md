# 🐴 Übung 1: Module importieren

Willkommen bei den **Werkzeugkisten des Reiterhofs**! Im Stall liegen fertige Werkzeuge für jede Aufgabe – Striegel, Hufkratzer, Bürsten. Die Stallmeisterin sagt: *"Wer jedes Werkzeug selbst schmiedet, kommt nie zum Reiten. Wer sich die richtigen Kisten leiht, hat mehr Zeit für die Pferde."*

Nicht alles musst du selbst schreiben. Python bringt viele fertige **Module** mit – Sammlungen von Funktionen, die du dir mit `import` holst:

```python
import math                 # ganzes Modul laden
print(math.sqrt(16))        # Funktion mit Modulname davor: 4.0

import math as m            # mit Spitzname
print(m.sqrt(25))           # 5.0

from math import sqrt       # nur eine Funktion holen
print(sqrt(36))             # 6.0 – ohne Modulname davor
```

**Schritt für Schritt:**
1. **`import modul`** lädt das Modul – benutzt wird es mit **`modul.funktion()`**
2. **`import modul as kurz`** gibt ihm einen kurzen **Spitznamen**
3. **`from modul import funktion`** holt eine einzelne Funktion – dann schreibst du **keinen** Modulnamen mehr davor

> ⚠️ Ohne `import` kennt Python das Modul nicht: `math.sqrt(16)` gibt einen **NameError**.
