# 🐴 Woche 4: Der Rhythmus des Reitens

Willkommen auf dem **Trainingsplatz der Ausdauer**! Hier wiederholen sich Bewegungen, und Rhythmus führt zur Perfektion. In dieser Woche lernst du, wie Python Code **automatisch wiederholt** – mit **Schleifen**:

1. 🔁 Die **for-Schleife** mit `range()`
2. 🎯 `range()` mit Start und Ende
3. 🏇 Schrittweite und rückwärts zählen
4. 🔤 Schleifen über **Text**
5. ⏳ Die **while-Schleife**
6. 💪 while mit Bedingungen
7. 🌀 **Verschachtelte** Schleifen

## 🔁 Übung 1: Schleife – Der Dressur-Kreis

Eine **for-Schleife** wiederholt Code für jedes Element einer Folge.

```python
for i in range(5):
    print(f"Runde {i+1}: Das Pferd trabt elegant")
```

1. **`for`** startet die Wiederholung.
2. **`i`** ist ein Platzhalter, der bei jedem Durchlauf die aktuelle Zahl enthält.
3. **`in range(5)`** liefert die Zahlen 0, 1, 2, 3, 4 – also **5** Durchläufe.
4. Der **Doppelpunkt `:`** beendet die erste Zeile.
5. Alles **eingerückt** darunter wird bei jedem Durchlauf ausgeführt.

> 🐴 **Wichtig:** `range(5)` zählt ab **0** und endet **vor** der 5. Deshalb schreiben wir `i+1`, um von 1 bis 5 zu zählen.
