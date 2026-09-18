# Der Zahlenrater

Zum Abschluss baust du einen Computer, der eine Zahl zwischen 1 und 100 errät – und das erstaunlich schnell. Der Trick heißt **Bisektionssuche**: statt der Reihe nach zu raten (1, 2, 3, …), rätst du immer genau in der **Mitte** des noch möglichen Bereichs. Nach jedem Rateversuch halbiert sich der Bereich, der noch übrig bleibt:

```python
def rate_zahl(ziel, minimum=1, maximum=100):
    versuche = 0
    while minimum <= maximum:
        versuche += 1
        mitte = (minimum + maximum) // 2
        print(f"Versuch {versuche}: ist es {mitte}?")
        if mitte == ziel:
            print(f"Richtig! Ich habe {ziel} in {versuche} Versuchen erraten.")
            return versuche
        elif mitte < ziel:
            minimum = mitte + 1
        else:
            maximum = mitte - 1

rate_zahl(42)
```

Weil sich der Bereich jedes Mal halbiert, braucht der Computer selbst bei 100 möglichen Zahlen nur etwa 7 Versuche – viel schneller, als der Reihe nach durchzuzählen.
