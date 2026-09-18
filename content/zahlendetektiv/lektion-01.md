# Ist diese Zahl eine Primzahl?

Eine **Primzahl** ist eine Zahl größer als 1, die sich nur durch 1 und sich selbst teilen lässt. 7 ist eine Primzahl (nur 1 und 7 teilen sie glatt), 8 nicht (auch 2 und 4 teilen sie).

Um das zu prüfen, probierst du der Reihe nach alle möglichen Teiler von 2 bis zur Zahl minus 1 durch. Findest du einen Teiler, ist es keine Primzahl:

```python
def ist_primzahl(zahl):
    if zahl < 2:
        return False
    for teiler in range(2, zahl):
        if zahl % teiler == 0:
            return False
    return True

print(ist_primzahl(17))   # True
```

`zahl % teiler == 0` prüft, ob die Division ohne Rest aufgeht – also ob `teiler` die Zahl glatt teilt.

> 💡 Falls dir `%` (Modulo) und Schleifen noch nicht so vertraut sind, wirf einen Blick in [Woche 4 – Der Kreislauf der Macht](/kurs/python-12-wochen-grundkurs?week=4&tab=lektion#woche-4) des 12-Wochen-Kurses.
