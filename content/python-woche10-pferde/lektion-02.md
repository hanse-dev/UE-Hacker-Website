# 🐴 Übung 2: Der Konstruktor __init__

Jedes Attribut einzeln zu setzen ist mühsam. Der **Konstruktor `__init__`** läuft **automatisch**, sobald ein Objekt entsteht, und nimmt gleich alle Startwerte entgegen:

```python
class Pferd:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

a = Pferd("Blitz")
b = Pferd("Stella", 5)
print(a.name, a.level)
print(b.name, b.level)
```

1. **`self`** ist immer der erste Parameter – es ist das Objekt, das gerade entsteht
2. **`self.name = name`** speichert den Wert **im Objekt**
3. **`level=1`** ist ein **Standardwert** (wie bei Funktionen in Woche 5)

> ⚠️ Zwei Unterstriche vor und nach `init`: `__init__`.
