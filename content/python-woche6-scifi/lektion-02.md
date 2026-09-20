# 🔢 Datenprotokoll 2: Auf Einträge zugreifen

Jeder Eintrag hat eine Nummer, den **Index**. Wichtig: Das Zählen beginnt bei **0**!

```python
module = ["Antrieb", "Sensor", "Schild", "Radar", "Funk"]
print(module[0])    # erster Eintrag
print(module[1])    # zweiter Eintrag
print(module[-1])   # letzter Eintrag
module[0] = "Kern"   # Eintrag ersetzen
```

**Merke:**
- `liste[0]` ist der **erste**, `liste[-1]` der **letzte** Eintrag, `liste[-2]` der vorletzte
- Ein Index, den es nicht gibt (z. B. `liste[5]` bei 5 Einträgen), gibt einen **IndexError**
- Mit `liste[1] = "neu"` **ersetzt** du einen Eintrag

**Listen in Listen:** Ein Eintrag darf selbst eine Liste sein. Mit zwei Indizes greifst du hinein: `party[1][0]` ist der erste Eintrag der zweiten Teilliste.
