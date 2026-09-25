# Das Primzahlen-Sieb

Jetzt willst du nicht nur eine einzelne Zahl prüfen, sondern **alle** Primzahlen bis zu einer Grenze finden. Dafür gehst du mit einer Schleife über jede Zahl bis zur Grenze und sammelst nur die Primzahlen ein. So läuft das Prinzip ab:

```
def primzahlen_bis(n):
    ergebnis = []
    für jede zahl von 2 bis n:
        wenn ist_primzahl(zahl) wahr ist:
            hänge zahl an ergebnis an
    gib ergebnis zurück
```

Rufst du z.B. `primzahlen_bis(10)` auf, kommt `[2, 3, 5, 7]` heraus. Diese Technik – eine große Liste möglicher Zahlen durchgehen und nur die passenden behalten – nennt man ein **Sieb**: alles, was nicht passt, fällt durch, übrig bleiben nur die Primzahlen.
