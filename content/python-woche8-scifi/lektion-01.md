# 🚀 Daten-Log 1: Steckbriefe erstellen und lesen

Willkommen im **Daten-Archiv der Raumstation Nebula-7**! Die Bordintelligenz speichert jede Person, jedes Bauteil und jeden Fund als **Datensatz**. Sie meldet: *"Wer nur Listen kennt, sucht Sekunden – wer Datensätze mit Namen führt, findet alles sofort."*

Ein **Dictionary** speichert Werte unter **Namen** (Schlüssel) statt unter Nummern wie eine Liste. Du schreibst es mit geschweiften Klammern:

```python
mitglied = {"name": "Nova", "rolle": "Pilotin", "rang": 4}

print(mitglied["name"])    # Zugriff über den Schlüssel: Nova
print(len(mitglied))       # Anzahl der Einträge: 3
leer = {}                 # ein leeres Dictionary
```

**Schritt für Schritt:**
1. **`{}`** – geschweifte Klammern umschließen das Dictionary
2. **`schlüssel: wert`** – der Doppelpunkt verbindet Schlüssel und Wert, Kommas trennen die Einträge
3. **`dict[schlüssel]`** – in eckigen Klammern holst du den Wert

> ⚠️ Ein Schlüssel, den es nicht gibt, löst einen **KeyError** aus. Achte auch auf Groß- und Kleinschreibung!
