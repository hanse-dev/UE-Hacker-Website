# 🚧 Warum ein einzelnes Neuron nicht reicht

Manche Aufgaben lassen sich mit einem einzigen Neuron einfach nicht lösen – egal, welche Gewichte
und welchen Bias du ausprobierst. Das berühmteste Beispiel ist **XOR** ("entweder – oder, aber
nicht beides"):

| Eingabe 1 | Eingabe 2 | XOR |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

```python
def step(x):
    if x >= 0:
        return 1
    else:
        return 0

def neuron(eingaben, gewichte, bias):
    gewichtete_summe = 0
    for i in range(len(eingaben)):
        gewichtete_summe += eingaben[i] * gewichte[i]
    gewichtete_summe += bias
    return step(gewichtete_summe)

def anzahl_richtig(gewichte, bias, tabelle):
    richtig = 0
    for eingaben, erwartet in tabelle:
        if neuron(eingaben, gewichte, bias) == erwartet:
            richtig += 1
    return richtig

xor_tabelle = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0),
]

print(anzahl_richtig([1, 1], -0.5, xor_tabelle))
print(anzahl_richtig([1, 1], -1.5, xor_tabelle))
print(anzahl_richtig([-1, -1], 1.5, xor_tabelle))
```

Egal welches Gewichts-Paar du probierst: **nie werden alle 4 Fälle richtig**. Das liegt daran, dass
ein einzelnes Neuron die Welt nur mit einer einzigen geraden Linie in zwei Bereiche teilen kann –
und bei XOR liegen die "richtigen" Fälle (0,1) und (1,0) diagonal gegenüber den "falschen" Fällen
(0,0) und (1,1). Keine gerade Linie trennt das sauber. Das nennt man **nicht linear trennbar**.
