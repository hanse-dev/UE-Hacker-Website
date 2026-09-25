# 🔌 Logische Gatter von Hand nachbauen

Mit denselben Bausteinen (`gewichtete_summe()`, `aktivierung()`, `neuron()`) kannst du – nur durch
**andere Gewichte und einen anderen Schwellenwert** – ganz unterschiedliche logische Gatter
nachbauen. Bei gleichen Gewichten `[1, 1]` entscheidet allein der Schwellenwert, ob ein UND- oder
ein ODER-Gatter entsteht:

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
gewichte = [1, 1]
for e in alle_eingaben:
    print(neuron(e, gewichte, 2))
for e in alle_eingaben:
    print(neuron(e, gewichte, 1))
```

Schwelle `2` verlangt, dass **beide** Eingaben `1` sind (UND), Schwelle `1` reicht schon, wenn
**mindestens eine** Eingabe `1` ist (ODER). Mit **negativen** Gewichten kannst du sogar das
Gegenteil bauen – ein NAND-Gatter (UND, aber umgekehrt):

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
    print(neuron(e, [-1, -1], -1))
```

Negative Gewichte bedeuten: je größer diese Eingabe, desto **kleiner** die Summe – das Neuron
feuert also gerade dann, wenn die Eingaben **klein** (bzw. `0`) sind. Gewichte und Schwellenwert
zusammen legen fest, welches logische Gatter am Ende herauskommt.
