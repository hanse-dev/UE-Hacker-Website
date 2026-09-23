# ⚔️ Archiv-Zauber 1: Steckbriefe erstellen und lesen

Willkommen im **Gildenarchiv von Pyralia**! Hier führt der Archivar für jeden Helden, jedes Monster und jeden Schatz einen **Steckbrief**. Er sagt: *"Wer nur Listen kennt, sucht ewig – wer Steckbriefe führt, findet jeden Helden mit einem Wort."*

Ein **Dictionary** speichert Werte unter **Namen** (Schlüssel) statt unter Nummern wie eine Liste. Du schreibst es mit geschweiften Klammern:

```python
held = {"name": "Aria", "klasse": "Magierin", "level": 15}

print(held["name"])    # Zugriff über den Schlüssel: Aria
print(len(held))       # Anzahl der Einträge: 3
leer = {}                 # ein leeres Dictionary
```

**Schritt für Schritt:**
1. **`{}`** – geschweifte Klammern umschließen das Dictionary
2. **`schlüssel: wert`** – der Doppelpunkt verbindet Schlüssel und Wert, Kommas trennen die Einträge
3. **`dict[schlüssel]`** – in eckigen Klammern holst du den Wert

> ⚠️ Ein Schlüssel, den es nicht gibt, löst einen **KeyError** aus. Achte auch auf Groß- und Kleinschreibung!
