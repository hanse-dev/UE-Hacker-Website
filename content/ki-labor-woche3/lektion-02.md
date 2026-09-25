# 📐 Der Abstand zwischen zwei Beispielen

Ein Tier-Beispiel hat aber nicht nur ein Merkmal, sondern mehrere (`beine`, `gewicht`, ...). Der
gebräuchlichste Abstand für mehrere Merkmale ist die **euklidische Distanz**: für jedes Merkmal
die Differenz quadrieren, alle Quadrate addieren, und am Ende die Wurzel ziehen
(`math.sqrt()`).

```python
import math

a = {"beine": 4, "gewicht": 30}
b = {"beine": 4, "gewicht": 25}

abstand = math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)
print(abstand)
```

Als Funktion verpackt kannst du damit beliebige Paare von Beispielen vergleichen:

```python
import math

def abstand(a, b):
    return math.sqrt((a["beine"] - b["beine"]) ** 2 + (a["gewicht"] - b["gewicht"]) ** 2)

ziel = {"beine": 4, "gewicht": 28}
hund = {"beine": 4, "gewicht": 30}
spatz = {"beine": 2, "gewicht": 0.03}

print(abstand(ziel, hund))
print(abstand(ziel, spatz))
```

Der Hund ist dem Ziel viel ähnlicher als der Spatz – sein Abstand ist deutlich kleiner.

> 💡 Je mehr Merkmale zwei Beispiele gemeinsam haben, desto kleiner wird ihr Abstand – genau das
> nutzt du gleich, um den **nächsten** Nachbarn zu finden.
