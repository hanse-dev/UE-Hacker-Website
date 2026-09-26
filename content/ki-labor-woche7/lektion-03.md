# 🧠 Eine versteckte Schicht: mehrere Neuronen kombinieren

Die Lösung: statt einem Neuron nimmst du **mehrere Neuronen in einer versteckten Schicht** – und
ein weiteres Neuron, das deren Ergebnisse kombiniert. "Versteckt" heißt nur: es liegt zwischen der
Eingabe und der Ausgabe, du siehst seine Werte normalerweise nicht direkt.

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

def vorwaerts(eingaben, versteckte_gewichte, versteckte_bias, ausgabe_gewichte, ausgabe_bias):
    versteckte_ausgaben = []
    for i in range(len(versteckte_gewichte)):
        versteckte_ausgaben.append(neuron(eingaben, versteckte_gewichte[i], versteckte_bias[i]))
    return neuron(versteckte_ausgaben, ausgabe_gewichte, ausgabe_bias)

versteckte_gewichte = [[1, 1], [-1, -1]]
versteckte_bias = [-0.5, 1.5]
ausgabe_gewichte = [1, 1]
ausgabe_bias = -1.5

print(vorwaerts([0, 0], versteckte_gewichte, versteckte_bias, ausgabe_gewichte, ausgabe_bias))
print(vorwaerts([0, 1], versteckte_gewichte, versteckte_bias, ausgabe_gewichte, ausgabe_bias))
print(vorwaerts([1, 0], versteckte_gewichte, versteckte_bias, ausgabe_gewichte, ausgabe_bias))
print(vorwaerts([1, 1], versteckte_gewichte, versteckte_bias, ausgabe_gewichte, ausgabe_bias))
```

`vorwaerts()` schickt die Eingabe zuerst durch **zwei versteckte Neuronen** (das erste ist ein
OR-Gatter, das zweite ein NAND-Gatter), sammelt deren beide Ausgaben in einer Liste – und schickt
diese Liste dann als Eingabe in ein **drittes Neuron** (ein AND-Gatter). Das Ergebnis: `0 1 1 0` –
genau XOR! Ein einzelnes Neuron konnte das nicht, aber drei kombinierte Neuronen schon.
