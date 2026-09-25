# 🚦 Die Sprungfunktion

Der zweite Baustein entscheidet, ob das Neuron "feuert": die **Sprungfunktion** (englisch:
*step function*) vergleicht die gewichtete Summe mit dem Schwellenwert und springt zwischen zwei
Werten – `0` oder `1`, nichts dazwischen:

```python
def aktivierung(summe, schwelle):
    if summe >= schwelle:
        return 1
    else:
        return 0

print(aktivierung(5, 5))
print(aktivierung(4, 5))
```

Erreicht die Summe den Schwellenwert genau (`5 >= 5`), zählt das schon als "aktiviert" – deshalb
`>=` und nicht nur `>`. Mit `gewichtete_summe()` aus der letzten Lektion und `aktivierung()` kannst
du jetzt ein komplettes Neuron zusammensetzen:

```python
def gewichtete_summe(eingaben, gewichte):
    summe = 0
    for e, g in zip(eingaben, gewichte):
        summe += e * g
    return summe

def aktivierung(summe, schwelle):
    if summe >= schwelle:
        return 1
    else:
        return 0

def neuron(eingaben, gewichte, schwelle):
    summe = gewichtete_summe(eingaben, gewichte)
    return aktivierung(summe, schwelle)

alle_eingaben = [[0, 0], [0, 1], [1, 0], [1, 1]]
for e in alle_eingaben:
    print(neuron(e, [1, 1], 2))
```

`neuron()` ruft einfach `gewichtete_summe()` und `aktivierung()` nacheinander auf – zwei kleine,
für sich verständliche Bausteine statt einer langen Funktion. Bei den Gewichten `[1, 1]` und
Schwelle `2` feuert das Neuron nur, wenn **beide** Eingaben `1` sind: ein logisches UND-Gatter!
