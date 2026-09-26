# Listen – viele Werte auf einmal 📋

Bisher konnte eine Variable immer nur einen Wert speichern. Eine Liste ist eine Truhe, in der mehrere Werte hintereinander liegen – perfekt, wenn du z.B. alle deine Haustiere auf einmal speichern willst. Der erste Eintrag hat den Index 0, nicht 1!

```python
tiere = ["Hund", "Katze", "Maus"]
print(tiere[0])   # gibt "Hund" aus – der erste Eintrag!
print(tiere[-1])  # gibt "Maus" aus (letztes Element!)
```

Der negative Index `-1` ist ein praktischer Trick: er zeigt immer auf das **letzte** Element, egal wie lang die Liste ist – du musst also nicht erst zählen, wie viele Einträge drin sind.

Mit `len()` findest du heraus, wie viele Einträge eine Liste hat, und mit `.append()` fügst du am Ende einen neuen hinzu:

```python
tiere.append("Papagei")
print(len(tiere))   # gibt 4 aus
print(tiere)        # gibt ["Hund", "Katze", "Maus", "Papagei"] aus
```

Listen können alles enthalten: Texte, Zahlen, ja sogar andere Listen! Und du kannst sie mit `for` (aus der letzten Lektion) der Reihe nach durchgehen.
