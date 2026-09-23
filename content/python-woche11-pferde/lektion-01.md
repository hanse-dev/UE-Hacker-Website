# 🐴 Zuchtübung 1: Vererbung

Willkommen im **Zuchtzentrum Sonnental**! Edle Pferdelinien vererben ihre Fähigkeiten an die Fohlen – genau das macht **Vererbung** in Python.

Eine **Kind-Klasse** erbt alle Methoden und Attribute ihrer **Eltern-Klasse**. Die Eltern stehen in Klammern hinter dem Namen:

```python
class Pferd:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def laufe(self):
        print(f"{self.name} trabt gemütlich.")

class Rennpferd(Pferd):
    pass

k = Rennpferd("Blitz")
k.stelle_vor()
print(isinstance(k, Pferd))
```

1. **`class Rennpferd(Pferd):`** – Rennpferd erbt alles von Pferd
2. `k.stelle_vor()` funktioniert, obwohl Rennpferd sie **nicht selbst** schreibt
3. Eine Kind-Klasse kann **neue** Methoden dazubekommen
4. **`isinstance(objekt, Klasse)`** fragt: „Gehört das Objekt zu dieser Klasse (oder ihren Eltern)?“
