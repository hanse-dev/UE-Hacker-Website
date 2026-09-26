# Zahlen und Rechnen

Python unterstützt alle gängigen Rechenoperationen. `//` ist ganzzahlige Division, `%` der Rest (Modulo), `**` Potenz.

```python
preis = 29.99
rabatt = 0.1
endpreis = preis * (1 - rabatt)
print(endpreis)
```

Die Rechenreihenfolge folgt der aus der Mathematik bekannten Regel Punkt-vor-Strich, `**` bindet dabei sogar stärker als `*`. Bei komplexeren Ausdrücken lohnen sich Klammern, um Missverständnisse zu vermeiden:

```python
ergebnis = (2 + 3) * 4  # 20, nicht 14
```

`//` und `%` gehören zusammen und sind besonders bei ganzzahligen Aufteilungen nützlich – z.B. wenn du wissen willst, wie viele volle Gruppen zu je 4 Personen sich aus 22 Personen bilden lassen, und wie viele übrig bleiben:

```python
personen = 22
gruppen = personen // 4   # 5 volle Gruppen
rest = personen % 4       # 2 übrige Personen
print(gruppen, rest)
```

Ein wichtiger Unterschied zu manchen anderen Sprachen: `/` liefert in Python **immer** ein Ergebnis vom Typ `float`, selbst wenn die Division glatt aufgeht (`10 / 2` ergibt `5.0`, nicht `5`). Willst du eine ganze Zahl als Ergebnis, brauchst du `//`.
