# 🐴 Übung 1: Steckbriefe erstellen und lesen

Willkommen im **Stallarchiv des Reiterhofs**! Für jedes Pferd gibt es eine **Stallkarte** mit allen Angaben. Die Stallmeisterin sagt: *"Wer alle Angaben in einer langen Liste sucht, verliert Zeit. Wer Stallkarten führt, findet jedes Pferd sofort."*

Ein **Dictionary** speichert Werte unter **Namen** (Schlüssel) statt unter Nummern wie eine Liste. Du schreibst es mit geschweiften Klammern:

```python
pferd = {"name": "Blitz", "rasse": "Hannoveraner", "alter": 8}

print(pferd["name"])    # Zugriff über den Schlüssel: Blitz
print(len(pferd))       # Anzahl der Einträge: 3
leer = {}                 # ein leeres Dictionary
```

**Schritt für Schritt:**
1. **`{}`** – geschweifte Klammern umschließen das Dictionary
2. **`schlüssel: wert`** – der Doppelpunkt verbindet Schlüssel und Wert, Kommas trennen die Einträge
3. **`dict[schlüssel]`** – in eckigen Klammern holst du den Wert

> ⚠️ Ein Schlüssel, den es nicht gibt, löst einen **KeyError** aus. Achte auch auf Groß- und Kleinschreibung!
