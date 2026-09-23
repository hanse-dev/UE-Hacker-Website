# ⚔️ Blaupausen-Zauber 3: Methoden und self

Eine **Methode** ist eine Funktion **in** einer Klasse. Sie kann das Objekt über **`self`** benutzen:

```python
class Held:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level

    def stelle_vor(self):
        print(f"Ich bin {self.name}, Level {self.level}.")

held = Held("Aria")
held.stelle_vor()
```

1. Die Methode steht **eingerückt** in der Klasse und hat **`self`** als ersten Parameter
2. Beim Aufruf schreibst du **`held.stelle_vor()`** – das `self` setzt Python selbst ein
3. Mit **`self.name`** greift die Methode auf die Attribute **dieses** Objekts zu

> 💡 Python übersetzt `held.stelle_vor()` in `Held.stelle_vor(held)`.
