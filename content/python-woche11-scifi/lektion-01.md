# 🚀 KI-Modul 1: Vererbung

Willkommen im **KI-Labor der Raumstation Nebula-7**! Neue Roboter-Modelle erben die Fähigkeiten ihrer Vorgänger – genau das macht **Vererbung** in Python.

Eine **Kind-Klasse** erbt alle Methoden und Attribute ihrer **Eltern-Klasse**. Die Eltern stehen in Klammern hinter dem Namen:

```python
class Roboter:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def arbeite(self):
        print(f"{self.name} läuft im Leerlauf.")

class Kampfroboter(Roboter):
    pass

k = Kampfroboter("Nova")
k.stelle_vor()
print(isinstance(k, Roboter))
```

1. **`class Kampfroboter(Roboter):`** – Kampfroboter erbt alles von Roboter
2. `k.stelle_vor()` funktioniert, obwohl Kampfroboter sie **nicht selbst** schreibt
3. Eine Kind-Klasse kann **neue** Methoden dazubekommen
4. **`isinstance(objekt, Klasse)`** fragt: „Gehört das Objekt zu dieser Klasse (oder ihren Eltern)?“
