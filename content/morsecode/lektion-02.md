# Ein ganzes Wort verschlüsseln

Ein einzelner Buchstabe ist schön und gut – aber du willst ganze Wörter übersetzen. Dafür gehst du mit einer Schleife über jeden Buchstaben im Text, holst dir dessen Morsezeichen und reihst alles hintereinander auf. Zwischen den Morsezeichen kommt jeweils ein Leerzeichen, damit man die einzelnen Buchstaben wieder auseinanderhalten kann. So läuft das Prinzip ab:

```
def in_morse(text):
    ergebnis = []
    für jedes zeichen in text:
        hänge MORSE[zeichen] an ergebnis an
    gib " ".join(ergebnis) zurück
```

`" ".join(ergebnis)` fügt alle Morsezeichen aus der Liste `ergebnis` zusammen und setzt dabei ein Leerzeichen dazwischen. Rufst du z.B. `in_morse('ok')` auf, kommt `"--- -.-"` heraus.

> 💡 Falls dir Schleifen über Strings noch nicht so vertraut sind, wirf einen Blick in [Woche 4 – Der Kreislauf der Macht](/kurs/python-12-wochen-grundkurs?week=4&tab=lektion#woche-4) des 12-Wochen-Kurses.
