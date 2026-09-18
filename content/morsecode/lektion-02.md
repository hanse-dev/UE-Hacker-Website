# Ein ganzes Wort verschlüsseln

Ein einzelner Buchstabe ist schön und gut – aber du willst ganze Wörter übersetzen. Dafür gehst du mit einer Schleife über jeden Buchstaben im Text, holst dir dessen Morsezeichen und reihst alles hintereinander auf. Zwischen den Morsezeichen kommt jeweils ein Leerzeichen, damit man die einzelnen Buchstaben wieder auseinanderhalten kann:

```python
def in_morse(text):
    ergebnis = []
    for zeichen in text:
        ergebnis.append(MORSE[zeichen])
    return " ".join(ergebnis)

print(in_morse('hi'))   # .... ..
```

`" ".join(ergebnis)` fügt alle Morsezeichen aus der Liste `ergebnis` zusammen und setzt dabei ein Leerzeichen dazwischen.

> 💡 Falls dir Schleifen über Strings noch nicht so vertraut sind, wirf einen Blick in [Woche 4 – Der Kreislauf der Macht](/kurs/python-12-wochen-grundkurs?week=4&tab=lektion#woche-4) des 12-Wochen-Kurses.
