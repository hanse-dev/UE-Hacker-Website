# 🐴 Zuchtübung 7: Rechnen und zählen: __add__ und __len__

Auch Rechenzeichen und Funktionen wie `len()` lassen sich für eigene Klassen einrichten:

```python
class Vorrat:
    def __init__(self, menge):
        self.menge = menge

    def __add__(self, other):
        return Vorrat(self.menge + other.menge)

    def __str__(self):
        return f"Vorrat: {self.menge}"

a = Vorrat(10)
b = Vorrat(20)
print(a + b)

class Team:
    def __init__(self):
        self.mitglieder = []

    def __len__(self):
        return len(self.mitglieder)

t = Team()
t.mitglieder.append("Blitz")
t.mitglieder.append("Stella")
print(len(t))
```

1. **`__add__(self, other)`** wird bei `a + b` aufgerufen und gibt ein **neues** Objekt zurück
2. **`__len__(self)`** wird bei `len(objekt)` aufgerufen und gibt eine **Zahl** zurück
3. So verhalten sich deine Klassen fast wie eingebaute Typen
