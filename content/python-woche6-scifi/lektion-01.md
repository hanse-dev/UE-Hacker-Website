# 🚀 Datenprotokoll 1: Listen erstellen

Willkommen in den **Daten-Bänken der Raumstation Nebula-7**! Sensoren, Module, Crewmitglieder – die Bordintelligenz speichert alles in Listen. Sie meldet: *"Wer Daten sammelt, ohne sie zu ordnen, sammelt nur Rauschen."*

Bisher hat jede Variable **einen** Wert gehalten. Mit einer **Liste** speicherst du **viele** Werte in einer einzigen Variable:

```python
module = ["Antrieb", "Sensor", "Schild", "Radar", "Funk"]
print(module)
print(len(module))
```

**Schritt für Schritt:**
1. **`[ ]`** – eckige Klammern legen eine Liste an
2. **`,`** – Kommas trennen die Einträge
3. Text steht in Anführungszeichen, Zahlen nicht: `[1, 5, 10]`
4. **`len(liste)`** gibt die **Anzahl** der Einträge zurück
5. **`[]`** allein ist eine **leere** Liste

> 💡 Eine Liste darf auch Text und Zahlen mischen – meist sammelst du aber Dinge derselben Art.
