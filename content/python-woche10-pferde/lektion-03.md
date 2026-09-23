# 🐴 Übung 3: Methoden und self

Eine **Methode** ist eine Funktion **in** einer Klasse. Sie kann das Objekt über **`self`** benutzen:

```python
class Pferd:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    def stelle_vor(self):
        print(f"Ich bin {self.name}, Level {self.level}.")

pferd = Pferd("Blitz")
pferd.stelle_vor()
```

1. Die Methode steht **eingerückt** in der Klasse und hat **`self`** als ersten Parameter
2. Beim Aufruf schreibst du **`pferd.stelle_vor()`** – das `self` setzt Python selbst ein
3. Mit **`self.name`** greift die Methode auf die Attribute **dieses** Objekts zu

> 💡 Python übersetzt `pferd.stelle_vor()` in `Pferd.stelle_vor(pferd)`.
