# 🚧 Warum XOR nicht geht

UND, ODER und NAND lassen sich mit einem einzigen Neuron nachbauen – aber nicht jedes logische
Gatter! Das **XOR**-Gatter ("entweder-oder", englisch: *exclusive or*) feuert nur, wenn sich die
beiden Eingaben **unterscheiden**: `[0,1]` und `[1,0]` ergeben `1`, `[0,0]` und `[1,1]` ergeben `0`.

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

def anzahl_fehler(vorhersagen, erwartete_werte):
    fehler = 0
    for i in range(len(vorhersagen)):
        if vorhersagen[i] != erwartete_werte[i]:
            fehler += 1
    return fehler

alle_eingaben = [[0, 0], [0, 1], [1, 0], [1, 1]]
xor_erwartet = [0, 1, 1, 0]

vorhersagen1 = [neuron(e, [1, 1], 1) for e in alle_eingaben]
print(vorhersagen1)
print(anzahl_fehler(vorhersagen1, xor_erwartet))

vorhersagen2 = [neuron(e, [1, 1], 2) for e in alle_eingaben]
print(vorhersagen2)
print(anzahl_fehler(vorhersagen2, xor_erwartet))
```

Egal welche Gewichte und welchen Schwellenwert du ausprobierst – ein einzelnes Neuron bleibt bei
**mindestens einem** Fehler stecken. Der Grund: die gewichtete Summe kann Eingaben nur entlang
einer einzigen "Trennlinie" aufteilen, aber XOR bräuchte zwei davon (die beiden "wahren" Fälle
`[0,1]` und `[1,0]` liegen sich diagonal gegenüber). Diese Grenze eines einzelnen Neurons war
historisch einer der Gründe, warum Forscher anfingen, **mehrere Neuronen zu kombinieren** –
genau das baust du nächste Woche.
