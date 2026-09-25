# ➕ Die gewichtete Summe

Der erste Baustein eines Neurons ist die **gewichtete Summe**: jede Eingabe mit ihrem Gewicht
multiplizieren und alles zusammenzählen. Statt mit `range(len(...))` zu arbeiten, kannst du dafür
`zip()` nutzen – es fasst zwei Listen paarweise zusammen:

```python
def gewichtete_summe(eingaben, gewichte):
    summe = 0
    for e, g in zip(eingaben, gewichte):
        summe += e * g
    return summe

print(gewichtete_summe([1, 0, 1], [2, 5, 3]))
print(gewichtete_summe([0, 1, 1], [2, 5, 3]))
```

`zip(eingaben, gewichte)` liefert bei jedem Schleifendurchlauf ein Paar `(e, g)` – eine Eingabe und
ihr passendes Gewicht. Das funktioniert für beliebig viele Eingaben, nicht nur für zwei oder drei:

```python
def gewichtete_summe(eingaben, gewichte):
    summe = 0
    for e, g in zip(eingaben, gewichte):
        summe += e * g
    return summe

sensor_messungen = [[1, 0, 1], [0, 0, 0], [1, 1, 1]]
gewichte = [2, 5, 3]
for m in sensor_messungen:
    print(gewichtete_summe(m, gewichte))
```

Egal wie viele Sensoren `eingaben` und `gewichte` enthalten – `gewichtete_summe()` funktioniert
unverändert. Das macht sie zum Baustein, den du in den nächsten Lektionen immer wieder brauchst.
