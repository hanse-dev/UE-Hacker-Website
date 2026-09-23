# 🚀 System-Protokoll 7: Objekte an Funktionen übergeben

Auch Funktionen können **Objekte** entgegennehmen. Dabei wird das Objekt **nicht kopiert** – die Funktion arbeitet mit **demselben** Objekt:

```python
class Roboter:
    def __init__(self, name, level):
        self.name = name
        self.level = level

a = Roboter("Nova", 1)
b = a          # zwei Namen, ein Objekt!
b.level = 10
print(a.level)

def befoerdere(figur):
    figur.level += 1

befoerdere(a)
print(a.level)
```

1. `b = a` erzeugt **kein** neues Objekt, nur einen zweiten Namen
2. Was über `b` geändert wird, sieht man auch bei `a`
3. Deshalb verändert `befoerdere(a)` das echte Objekt – ohne `return`
