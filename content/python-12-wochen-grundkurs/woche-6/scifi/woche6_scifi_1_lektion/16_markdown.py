"""## Daten-Sammlung 5: List Comprehension – Listen in einem Zug bauen

Oft willst du aus einer Liste eine **neue** Liste machen: alle Werte verändern oder nur bestimmte behalten. Mit einer Schleife und `append()` sind das mehrere Zeilen. Eine **List Comprehension** schafft es in einer:

```python
neue_liste = [ausdruck for element in liste]              # jedes Element umwandeln
neue_liste = [element for element in liste if bedingung]  # nur passende behalten
```

Lies sie von links nach rechts: *„Nimm `ausdruck` für jedes `element` in `liste` (wenn `bedingung` stimmt)."*

**Wichtig:** Die ursprüngliche Liste bleibt unverändert – du bekommst immer eine neue Liste."""