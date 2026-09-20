# 🔬 Modul-Protokoll 7: Mehr math: Fakultät, ggT und Primzahlen

```python
import math

print(math.factorial(5))   # 5 · 4 · 3 · 2 · 1 = 120
print(math.gcd(24, 36))    # größter gemeinsamer Teiler: 12
print(math.lcm(12, 15))    # kleinstes gemeinsames Vielfaches: 60

winkel = math.radians(90)  # Grad in Bogenmaß umrechnen
print(math.sin(winkel))    # Sinus: 1.0
```

Winkelfunktionen (`sin`, `cos`, `tan`) rechnen im **Bogenmaß** – mit `math.radians(grad)` rechnest du Grad um.

**Primzahlen:** Eine Zahl ist eine **Primzahl**, wenn sie nur durch 1 und sich selbst teilbar ist. Mit `%` prüfst du die Teilbarkeit:

```python
def ist_primzahl(n):
    if n < 2:
        return False
    for teiler in range(2, n):
        if n % teiler == 0:
            return False    # gefunden: durch etwas anderes teilbar
    return True
```
