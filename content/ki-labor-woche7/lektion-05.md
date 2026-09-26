# ✅ Alles zusammen: Vorhersagen und Genauigkeit

Wie in Woche 4 prüfst du die Qualität eines Modells mit `ist_richtig()` und `genauigkeit()` – jetzt
angewendet auf das kleine Netz aus dieser Woche, im Vergleich zu einem einzelnen Neuron.

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

def ist_richtig(vorhersage, erwartet):
    return vorhersage == erwartet

def genauigkeit(vorhersagen, erwartete_werte):
    richtig = 0
    for i in range(len(vorhersagen)):
        if ist_richtig(vorhersagen[i], erwartete_werte[i]):
            richtig += 1
    return round(richtig / len(vorhersagen) * 100)

versteckte_gewichte = [[1, 1], [-1, -1]]
versteckte_bias = [-0.5, 1.5]
ausgabe_gewichte = [1, 1]
ausgabe_bias = -1.5

xor_tabelle = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0),
]

vorhersagen = [vorwaerts(e, versteckte_gewichte, versteckte_bias, ausgabe_gewichte, ausgabe_bias) for e, _ in xor_tabelle]
erwartete_werte = [erwartet for _, erwartet in xor_tabelle]
print(vorhersagen)
print(genauigkeit(vorhersagen, erwartete_werte))

baseline_vorhersagen = [neuron(e, [1, 1], -0.5) for e, _ in xor_tabelle]
print(baseline_vorhersagen)
print(genauigkeit(baseline_vorhersagen, erwartete_werte))
```

Das Netz mit versteckter Schicht erreicht **100%** – ein einzelnes Neuron (hier ein OR-Gatter als
`baseline`) schafft dagegen nur **75%**, genau wie in Lektion 2 gezeigt. Der Unterschied zwischen
einem und mehreren verbundenen Neuronen ist also kein Detail, sondern entscheidet, ob eine Aufgabe
überhaupt lösbar ist.
