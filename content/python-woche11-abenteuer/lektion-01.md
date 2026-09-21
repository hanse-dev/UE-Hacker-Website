# ⚔️ Evolutions-Zauber 1: Vererbung

Willkommen in den **Meistergilden von Pyralia**! Große Helden-Linien vererben ihre Fähigkeiten an die nächste Generation – genau das macht **Vererbung** in Python.

Eine **Kind-Klasse** erbt alle Methoden und Attribute ihrer **Eltern-Klasse**. Die Eltern stehen in Klammern hinter dem Namen:

```python
class Held:
    def __init__(self, name):
        self.name = name

    def stelle_vor(self):
        print(f"Ich bin {self.name}.")

    def kaempfe(self):
        print(f"{self.name} kämpft mit bloßen Händen.")

class Krieger(Held):
    pass

k = Krieger("Aria")
k.stelle_vor()
print(isinstance(k, Held))
```

1. **`class Krieger(Held):`** – Krieger erbt alles von Held
2. `k.stelle_vor()` funktioniert, obwohl Krieger sie **nicht selbst** schreibt
3. Eine Kind-Klasse kann **neue** Methoden dazubekommen
4. **`isinstance(objekt, Klasse)`** fragt: „Gehört das Objekt zu dieser Klasse (oder ihren Eltern)?“
