# 🚀 KI-Modul 3: super() und __init__

Braucht das Kind **zusätzliche** Attribute, schreibt es einen eigenen `__init__`. Dann muss es den `__init__` der Eltern **selbst aufrufen** – mit **`super()`**:

```python
class Roboter:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def arbeite(self):
        print(f"{self.name} läuft im Leerlauf.")

class Kampfroboter(Roboter):
    def __init__(self, name, panzer=30):
        super().__init__(name)
        self.panzer = panzer

k = Kampfroboter("Nova", 45)
print(k.name, k.panzer)
```

1. **`super().__init__(name)`** ruft den Konstruktor der Eltern auf (setzt `self.name`)
2. Danach kommen die **neuen** Attribute des Kindes
3. Mit `super().methode()` rufst du auch andere Methoden der Eltern auf, z. B. beim Überschreiben

> ⚠️ Ohne `super().__init__(...)` fehlen die Attribute der Eltern!
