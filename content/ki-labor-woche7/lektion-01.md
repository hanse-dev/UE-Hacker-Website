# 🔁 Wiederholung: Ein Neuron entscheidet

Letzte Woche hast du ein einzelnes **Neuron** von Hand gebaut: es multipliziert jede Eingabe mit
einem **Gewicht**, addiert alle Ergebnisse zu einer **gewichteten Summe**, addiert dazu noch einen
**Bias** (eine Art eingebauter Schwellenwert-Verschiebung) – und vergleicht das Ergebnis dann mit
einer **Aktivierungsfunktion**: liegt die Summe über der Schwelle, feuert das Neuron mit 1, sonst
mit 0.

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

print(neuron([0, 0], [1, 1], -1.5))
print(neuron([0, 1], [1, 1], -1.5))
print(neuron([1, 0], [1, 1], -1.5))
print(neuron([1, 1], [1, 1], -1.5))
```

Mit `gewichte=[1, 1]` und `bias=-1.5` verhält sich dieses eine Neuron wie ein **AND-Gatter**: nur
wenn *beide* Eingaben 1 sind, reicht die Summe (2 − 1.5 = 0.5), um über die Schwelle zu kommen.

Diese Woche baust du darauf auf: aus einem einzelnen Neuron wird ein kleines **Netz** aus mehreren
Neuronen – und du bringst ihm bei, seine Gewichte **selbst zu lernen**, statt sie von Hand
festzulegen.
