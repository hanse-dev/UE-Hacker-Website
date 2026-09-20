# 🔢 Übung 2: Auf Einträge zugreifen

Jeder Eintrag hat eine Nummer, den **Index**. Wichtig: Das Zählen beginnt bei **0**!

```python
pferde = ["Sturmwind", "Blitz", "Luna", "Fuchs", "Balu"]
print(pferde[0])    # erster Eintrag
print(pferde[1])    # zweiter Eintrag
print(pferde[-1])   # letzter Eintrag
pferde[0] = "Stella"   # Eintrag ersetzen
```

**Merke:**
- `liste[0]` ist der **erste**, `liste[-1]` der **letzte** Eintrag, `liste[-2]` der vorletzte
- Ein Index, den es nicht gibt (z. B. `liste[5]` bei 5 Einträgen), gibt einen **IndexError**
- Mit `liste[1] = "neu"` **ersetzt** du einen Eintrag

**Listen in Listen:** Ein Eintrag darf selbst eine Liste sein. Mit zwei Indizes greifst du hinein: `party[1][0]` ist der erste Eintrag der zweiten Teilliste.

**Ausschnitte (Slicing):** Mit `liste[von:bis]` holst du einen **Teil** der Liste – der Endindex gehört **nicht** mehr dazu:

```python
print(pferde[0:3])    # Index 0, 1, 2
print(pferde[-2:])    # die letzten zwei
print(pferde[1::2])   # jeder zweite Eintrag, ab Index 1
```
