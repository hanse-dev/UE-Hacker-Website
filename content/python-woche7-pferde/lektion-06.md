# 🧮 Übung 6: math und Rechenoperatoren

Das Modul **`math`** hat Zahlen-Werkzeuge:

```python
import math

print(math.pi)          # 3.141592653589793
print(math.sqrt(16))    # Wurzel: 4.0
print(math.ceil(3.2))   # aufrunden: 4
print(math.floor(3.8))  # abrunden: 3
print(round(3.14159, 2))  # auf 2 Stellen runden: 3.14
print(abs(-5.5))        # Betrag: 5.5
```

Dazu drei **Operatoren**, für die du kein Modul brauchst:

```python
print(2 ** 3)    # Potenz: 8
print(17 // 5)   # ganzzahlige Division: 3
print(17 % 5)    # Rest (Modulo): 2
```

**`%`** ist besonders nützlich: `zahl % 2 == 0` heißt „`zahl` ist **gerade**", und `zahl % 5 == 0` heißt „durch 5 teilbar".
