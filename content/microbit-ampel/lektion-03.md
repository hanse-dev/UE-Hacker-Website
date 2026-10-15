# Stufe 2: Die Autoampel

Eine Autoampel hat drei Lampen. In Deutschland schaltet sie immer in derselben Reihenfolge:

| Phase | Was leuchtet | Bedeutung | Dauer bei euch |
|---|---|---|---|
| 1 | Rot | Halt! | 5 Sekunden |
| 2 | Rot und Gelb | Gleich geht es los, macht euch bereit. | 1 Sekunde |
| 3 | Grün | Fahren. | 5 Sekunden |
| 4 | Gelb | Gleich wird es rot, haltet an, wenn es geht. | 2 Sekunden |

Danach beginnt alles wieder mit Phase 1.

## Die Autoampel stecken

Die Fußgängerampel bleibt stecken. Die Autoampel kommt oben auf das Breadboard: Rot oben, Gelb in der Mitte, Grün unten, wie an der Straße. Jede LED wird angeschlossen wie die erste, mit eigenem Widerstand und eigenem Kabel zu GND.

<img src="/microbit/ampel/stufe-2.svg" alt="Steckplan Autoampel: rote LED an P0 in Reihe 2 und 3, gelbe LED an P1 in Reihe 4 und 5, grüne LED an P2 in Reihe 6 und 7, darunter die Fußgängerampel in Reihe 10 bis 13">

| LED | Kabel vom Pin in | Widerstand über die Lücke in | langes Bein | kurzes Bein und GND-Kabel |
|---|---|---|---|---|
| Rot | **P0** → Reihe 2 links | Reihe 2 | Reihe 2 rechts | Reihe 3 rechts |
| Gelb | **P1** → Reihe 4 links | Reihe 4 | Reihe 4 rechts | Reihe 5 rechts |
| Grün | **P2** → Reihe 6 links | Reihe 6 | Reihe 6 rechts | Reihe 7 rechts |

Jetzt sind alle fünf Stifte mit **GND** belegt. Prüft zum Schluss jede LED mit dem Finger.

## Das Programm

Jede Phase hat dieselbe Form: Alle drei LEDs bekommen ihren Wert, dann wartet der micro:bit. Schreibt in jeder Phase **alle drei** LEDs, auch die, die aus sein sollen. Dann kann keine LED aus der vorigen Phase hängen bleiben.

Die ersten beiden Phasen sind fertig. Ergänzt Phase 3 und 4.

:::bloecke

```bloecke
[grundlagen] dauerhaft
  [pins] schreibe digitalen Wert von Pin P0 auf 1
  [pins] schreibe digitalen Wert von Pin P1 auf 0
  [pins] schreibe digitalen Wert von Pin P2 auf 0
  [grundlagen] pausiere (ms) 5000
  [pins] schreibe digitalen Wert von Pin P0 auf 1
  [pins] schreibe digitalen Wert von Pin P1 auf 1
  [pins] schreibe digitalen Wert von Pin P2 auf 0
  [grundlagen] pausiere (ms) 1000
```

Mit einem Rechtsklick auf einen Block und **Duplizieren** spart ihr euch viel Arbeit.

:::

:::python

```python
from microbit import *

while True:
    # Phase 1: Rot
    pin0.write_digital(1)
    pin1.write_digital(0)
    pin2.write_digital(0)
    sleep(5000)
    # Phase 2: Rot und Gelb
    pin0.write_digital(1)
    pin1.write_digital(1)
    pin2.write_digital(0)
    sleep(1000)
```

Alles hinter `#` ist ein Kommentar. Der micro:bit überspringt ihn, er hilft nur euch beim Lesen.

:::

<details>
<summary>Lösung anzeigen</summary>

:::bloecke

```bloecke
[grundlagen] dauerhaft
  [pins] schreibe digitalen Wert von Pin P0 auf 1
  [pins] schreibe digitalen Wert von Pin P1 auf 0
  [pins] schreibe digitalen Wert von Pin P2 auf 0
  [grundlagen] pausiere (ms) 5000
  [pins] schreibe digitalen Wert von Pin P0 auf 1
  [pins] schreibe digitalen Wert von Pin P1 auf 1
  [pins] schreibe digitalen Wert von Pin P2 auf 0
  [grundlagen] pausiere (ms) 1000
  [pins] schreibe digitalen Wert von Pin P0 auf 0
  [pins] schreibe digitalen Wert von Pin P1 auf 0
  [pins] schreibe digitalen Wert von Pin P2 auf 1
  [grundlagen] pausiere (ms) 5000
  [pins] schreibe digitalen Wert von Pin P0 auf 0
  [pins] schreibe digitalen Wert von Pin P1 auf 1
  [pins] schreibe digitalen Wert von Pin P2 auf 0
  [grundlagen] pausiere (ms) 2000
```

:::

:::python

```python
from microbit import *

while True:
    # Phase 1: Rot
    pin0.write_digital(1)
    pin1.write_digital(0)
    pin2.write_digital(0)
    sleep(5000)
    # Phase 2: Rot und Gelb
    pin0.write_digital(1)
    pin1.write_digital(1)
    pin2.write_digital(0)
    sleep(1000)
    # Phase 3: Grün
    pin0.write_digital(0)
    pin1.write_digital(0)
    pin2.write_digital(1)
    sleep(5000)
    # Phase 4: Gelb
    pin0.write_digital(0)
    pin1.write_digital(1)
    pin2.write_digital(0)
    sleep(2000)
```

:::

</details>

## Bonus: Eine Funktion für die Ampel

Euer Programm wiederholt sich ständig: drei Pins schreiben, warten. Baut eine eigene Funktion **autoampel**, die alle drei LEDs auf einmal schaltet. Danach braucht jede Phase nur noch eine Zeile für die LEDs und eine zum Warten.

<details>
<summary>Tipps anzeigen</summary>

:::bloecke

- Unter **Fortgeschritten** und dann **Funktionen** klickt ihr auf **Erstelle eine Funktion**.
- Gebt ihr den Namen `autoampel` und fügt drei Parameter vom Typ **Zahl** hinzu: `rot`, `gelb` und `gruen`.
- In der Funktion schreibt ihr jeden Pin auf seinen Parameter. Die Parameter zieht ihr aus dem Funktionsblock heraus in das Zahlenfeld.
- Aufrufen könnt ihr sie dann so: **Aufruf autoampel 1 1 0** für Rot und Gelb.

:::

:::python

- Eine Funktion beginnt mit `def`, dann der Name und in Klammern die Werte, die sie bekommt:

```python
def autoampel(rot, gelb, gruen):
    ...
```

- In der Funktion schreibt ihr jeden Pin auf seinen Wert, zum Beispiel `pin0.write_digital(rot)`.
- Aufrufen könnt ihr sie dann so: `autoampel(1, 1, 0)` für Rot und Gelb.

:::

</details>
