# Das Primzahlen-Sieb

Jetzt willst du nicht nur eine einzelne Zahl prüfen, sondern **alle** Primzahlen bis zu einer Grenze finden. Dafür gehst du mit einer Schleife über jede Zahl bis zur Grenze und sammelst nur die Primzahlen ein:

```python
def primzahlen_bis(n):
    ergebnis = []
    for zahl in range(2, n + 1):
        if ist_primzahl(zahl):
            ergebnis.append(zahl)
    return ergebnis

print(primzahlen_bis(20))   # [2, 3, 5, 7, 11, 13, 17, 19]
```

Diese Technik – eine große Liste möglicher Zahlen durchgehen und nur die passenden behalten – nennt man ein **Sieb**: alles, was nicht passt, fällt durch, übrig bleiben nur die Primzahlen.
