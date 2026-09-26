# 🎲 Gewichte lernen lassen

In Lektion 3 hast du die Gewichte für XOR **von Hand** bekommen. In echt sucht ein neuronales Netz
seine Gewichte selbst – hier mit einer einfachen Methode: **zufällig ein bisschen verändern, und
nur behalten, was nicht schlechter wird.**

```python
import random

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

def bewertung(parameter, tabelle):
    versteckte_gewichte = [[parameter[0], parameter[1]], [parameter[3], parameter[4]]]
    versteckte_bias = [parameter[2], parameter[5]]
    ausgabe_gewichte = [parameter[6], parameter[7]]
    ausgabe_bias = parameter[8]
    richtig = 0
    for eingaben, erwartet in tabelle:
        vorhersage = vorwaerts(eingaben, versteckte_gewichte, versteckte_bias, ausgabe_gewichte, ausgabe_bias)
        if vorhersage == erwartet:
            richtig += 1
    return richtig / len(tabelle) * 100

def trainiere(tabelle, neustarts, schritte):
    beste_parameter = None
    beste_bewertung = -1
    for _ in range(neustarts):
        parameter = [random.uniform(-1, 1) for _ in range(9)]
        aktuelle_bewertung = bewertung(parameter, tabelle)
        for _ in range(schritte):
            index = random.randrange(len(parameter))
            alter_wert = parameter[index]
            parameter[index] = alter_wert + random.uniform(-1, 1)
            neue_bewertung = bewertung(parameter, tabelle)
            if neue_bewertung >= aktuelle_bewertung:
                aktuelle_bewertung = neue_bewertung
            else:
                parameter[index] = alter_wert
        if aktuelle_bewertung > beste_bewertung:
            beste_bewertung = aktuelle_bewertung
            beste_parameter = parameter
        if beste_bewertung == 100:
            break
    return beste_parameter, beste_bewertung

xor_tabelle = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0),
]

random.seed(0)
beste_parameter, beste_bewertung = trainiere(xor_tabelle, 40, 60)
print(beste_bewertung)
```

Die 9 Zahlen in `parameter` sind alle Gewichte und Biase des Netzes aus Lektion 3 (2 Gewichte + 1
Bias je verstecktem Neuron, plus 2 Gewichte + 1 Bias für das Ausgabe-Neuron) – als eine einzige
Liste. `trainiere()` startet mehrmals mit zufälligen Werten (**Neustarts**) und probiert bei jedem
Start viele kleine zufällige Änderungen aus (**Schritte**) – eine Änderung bleibt nur, wenn sie
nicht schlechter wird. `random.seed(0)` sorgt dafür, dass die "zufälligen" Zahlen bei jedem Lauf
gleich sind, damit das Ergebnis reproduzierbar ist. Nach genug Versuchen findet das Training
Gewichte, mit denen das Netz XOR zu 100% löst – ganz ohne dass ihm jemand die richtigen Gewichte
verraten hat.
