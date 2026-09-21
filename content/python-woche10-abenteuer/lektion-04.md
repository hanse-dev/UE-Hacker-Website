# ⚔️ Blaupausen-Zauber 4: Methoden mit Parametern und return

Methoden nehmen wie Funktionen **Parameter** entgegen und können mit **`return`** etwas zurückgeben:

```python
class Held:
    def __init__(self, name, energie=100):
        self.name = name
        self.energie = energie

    def kaempfe(self, kosten):
        self.energie -= kosten

    def ist_muede(self):
        return self.energie < 20

held = Held("Aria")
held.kaempfe(30)
print(held.energie)
print(held.ist_muede())
```

1. Nach `self` folgen die eigenen Parameter (hier `kosten`)
2. Die Methode **verändert** das Objekt: `self.energie -= kosten`
3. **`return`** liefert einen Wert zurück, z. B. `True` oder `False`
