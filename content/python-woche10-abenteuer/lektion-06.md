# ⚔️ Blaupausen-Zauber 6: Objekte in Listen

Objekte lassen sich wie Zahlen oder Texte in **Listen** sammeln (Woche 6) und mit **`for`** durchlaufen:

```python
class Held:
    def __init__(self, name, level):
        self.name = name
        self.level = level

gruppe = [Held("Aria", 3), Held("Thorin", 8), Held("Luna", 5)]
for h in gruppe:
    print(h.name, h.level)

starke = [h.name for h in gruppe if h.level >= 5]
print(starke)
```

1. Die Liste enthält **Objekte**, keine Texte
2. Die Schleifenvariable `h` ist jeweils ein Objekt – `h.name` liest sein Attribut
3. Auch die List Comprehension aus Woche 6 funktioniert mit Attributen
