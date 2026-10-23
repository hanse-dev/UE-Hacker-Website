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

Die Fußgängerampel bleibt stecken. Die Autoampel kommt oben auf das Breadboard: Rot oben, Gelb in der Mitte, Grün unten, wie an der Straße. Jede LED wird angeschlossen wie die erste, mit eigenem Widerstand. Die Autoampel bekommt ihre eigene **GND-Reihe 8**, mit einem Kabel vom zweiten GND-Stift.

<img src="/microbit/ampel/stufe-2.svg" alt="Steckplan Autoampel: rote LED an P16 in Reihe 2 und 3, gelbe LED an P15 in Reihe 4 und 5, grüne LED an P14 in Reihe 6 und 7, jede mit einer Brücke in die GND-Reihe 8 und dort ein Kabel zu GND, darunter die Fußgängerampel in Reihe 10 bis 14">

| LED | Kabel vom Pin in | Widerstand über die Lücke in | langes Bein | kurzes Bein und Brücke |
|---|---|---|---|---|
| Rot | **P16** → Reihe 2 links | Reihe 2 | Reihe 2 rechts | Reihe 3 rechts → Reihe 8 |
| Gelb | **P15** → Reihe 4 links | Reihe 4 | Reihe 4 rechts | Reihe 5 rechts → Reihe 8 |
| Grün | **P14** → Reihe 6 links | Reihe 6 | Reihe 6 rechts | Reihe 7 rechts → Reihe 8 |

Zum Schluss das Kabel vom zweiten **GND**-Stift in Reihe 8 rechts, direkt an der Lücke. Jetzt sind beide GND-Stifte belegt. Prüft jede LED mit dem Finger.

## Die neuen Pins bekommen Namen

| Variable | Pin | LED |
|---|---|---|
| `auto_rot` | P16 | Autoampel Rot |
| `auto_gelb` | P15 | Autoampel Gelb |
| `auto_gruen` | P14 | Autoampel Grün |

## Das Programm

Jede Phase hat dieselbe Form: Alle drei LEDs bekommen ihren Wert, dann wartet der micro:bit. Schreibt in jeder Phase **alle drei** LEDs, auch die, die aus sein sollen. Dann kann keine LED aus der vorigen Phase hängen bleiben.

Fangt dafür ein **neues Projekt** an. Die Fußgängerampel bleibt gesteckt, bleibt in dieser Stufe aber dunkel – das ist richtig so.

Die ersten beiden Phasen sind fertig. Ergänzt Phase 3 und 4.

:::bloecke

```bloecke
[grundlagen] beim Start
  [variablen] setze auto_rot auf P16
  [variablen] setze auto_gelb auf P15
  [variablen] setze auto_gruen auf P14
[grundlagen] dauerhaft
  [pins] schreibe digitalen Wert von Pin auto_rot auf 1
  [pins] schreibe digitalen Wert von Pin auto_gelb auf 0
  [pins] schreibe digitalen Wert von Pin auto_gruen auf 0
  [grundlagen] pausiere (ms) 5000
  [pins] schreibe digitalen Wert von Pin auto_rot auf 1
  [pins] schreibe digitalen Wert von Pin auto_gelb auf 1
  [pins] schreibe digitalen Wert von Pin auto_gruen auf 0
  [grundlagen] pausiere (ms) 1000
```

Mit einem Rechtsklick auf den obersten Block einer Phase und **Duplizieren** spart ihr euch viel Arbeit: Alle Blöcke darunter kommen mit. Hängt die Kopie unten an und ändert die Zahlen.

:::

:::python

```python
from microbit import *

auto_rot = pin16
auto_gelb = pin15
auto_gruen = pin14

while True:
    # Phase 1: Rot
    auto_rot.write_digital(1)
    auto_gelb.write_digital(0)
    auto_gruen.write_digital(0)
    sleep(5000)
    # Phase 2: Rot und Gelb
    auto_rot.write_digital(1)
    auto_gelb.write_digital(1)
    auto_gruen.write_digital(0)
    sleep(1000)
```

Alles hinter `#` ist ein Kommentar. Der micro:bit überspringt ihn, er hilft nur euch beim Lesen.

:::

:::javascript

```javascript
let auto_rot = DigitalPin.P16
let auto_gelb = DigitalPin.P15
let auto_gruen = DigitalPin.P14

basic.forever(function () {
    // Phase 1: Rot
    pins.digitalWritePin(auto_rot, 1)
    pins.digitalWritePin(auto_gelb, 0)
    pins.digitalWritePin(auto_gruen, 0)
    basic.pause(5000)
    // Phase 2: Rot und Gelb
    pins.digitalWritePin(auto_rot, 1)
    pins.digitalWritePin(auto_gelb, 1)
    pins.digitalWritePin(auto_gruen, 0)
    basic.pause(1000)
})
```

Alles hinter `//` ist ein Kommentar. Der micro:bit überspringt ihn, er hilft nur euch beim Lesen.

:::

<details>
<summary>Lösung anzeigen</summary>

:::bloecke

```bloecke
[grundlagen] beim Start
  [variablen] setze auto_rot auf P16
  [variablen] setze auto_gelb auf P15
  [variablen] setze auto_gruen auf P14
[grundlagen] dauerhaft
  [pins] schreibe digitalen Wert von Pin auto_rot auf 1
  [pins] schreibe digitalen Wert von Pin auto_gelb auf 0
  [pins] schreibe digitalen Wert von Pin auto_gruen auf 0
  [grundlagen] pausiere (ms) 5000
  [pins] schreibe digitalen Wert von Pin auto_rot auf 1
  [pins] schreibe digitalen Wert von Pin auto_gelb auf 1
  [pins] schreibe digitalen Wert von Pin auto_gruen auf 0
  [grundlagen] pausiere (ms) 1000
  [pins] schreibe digitalen Wert von Pin auto_rot auf 0
  [pins] schreibe digitalen Wert von Pin auto_gelb auf 0
  [pins] schreibe digitalen Wert von Pin auto_gruen auf 1
  [grundlagen] pausiere (ms) 5000
  [pins] schreibe digitalen Wert von Pin auto_rot auf 0
  [pins] schreibe digitalen Wert von Pin auto_gelb auf 1
  [pins] schreibe digitalen Wert von Pin auto_gruen auf 0
  [grundlagen] pausiere (ms) 2000
```

:::

:::python

```python
from microbit import *

auto_rot = pin16
auto_gelb = pin15
auto_gruen = pin14

while True:
    # Phase 1: Rot
    auto_rot.write_digital(1)
    auto_gelb.write_digital(0)
    auto_gruen.write_digital(0)
    sleep(5000)
    # Phase 2: Rot und Gelb
    auto_rot.write_digital(1)
    auto_gelb.write_digital(1)
    auto_gruen.write_digital(0)
    sleep(1000)
    # Phase 3: Grün
    auto_rot.write_digital(0)
    auto_gelb.write_digital(0)
    auto_gruen.write_digital(1)
    sleep(5000)
    # Phase 4: Gelb
    auto_rot.write_digital(0)
    auto_gelb.write_digital(1)
    auto_gruen.write_digital(0)
    sleep(2000)
```

:::

:::javascript

```javascript
let auto_rot = DigitalPin.P16
let auto_gelb = DigitalPin.P15
let auto_gruen = DigitalPin.P14

basic.forever(function () {
    // Phase 1: Rot
    pins.digitalWritePin(auto_rot, 1)
    pins.digitalWritePin(auto_gelb, 0)
    pins.digitalWritePin(auto_gruen, 0)
    basic.pause(5000)
    // Phase 2: Rot und Gelb
    pins.digitalWritePin(auto_rot, 1)
    pins.digitalWritePin(auto_gelb, 1)
    pins.digitalWritePin(auto_gruen, 0)
    basic.pause(1000)
    // Phase 3: Grün
    pins.digitalWritePin(auto_rot, 0)
    pins.digitalWritePin(auto_gelb, 0)
    pins.digitalWritePin(auto_gruen, 1)
    basic.pause(5000)
    // Phase 4: Gelb
    pins.digitalWritePin(auto_rot, 0)
    pins.digitalWritePin(auto_gelb, 1)
    pins.digitalWritePin(auto_gruen, 0)
    basic.pause(2000)
})
```

:::

</details>

## Bonus: Eine Funktion für die Ampel

Euer Programm wiederholt sich ständig: drei Pins schreiben, warten. Baut eine eigene Funktion **autoampel**, die alle drei LEDs auf einmal schaltet. Danach braucht jede Phase nur noch eine Zeile für die LEDs und eine zum Warten.

<details>
<summary>Tipps anzeigen</summary>

:::bloecke

- Unter **Fortgeschritten** und dann **Funktionen** klickt ihr auf **Erstelle eine Funktion**.
- Gebt ihr den Namen `autoampel` und fügt drei Parameter vom Typ **Zahl** hinzu: `rot`, `gelb` und `gruen`. Ein **Parameter** ist ein Platzhalter: Beim Benutzen der Funktion (dem **Aufruf**) gebt ihr für jeden eine Zahl mit, 1 für an oder 0 für aus.
- In der Funktion schreibt ihr jeden Pin auf seinen Parameter, zum Beispiel **schreibe digitalen Wert von Pin auto_rot auf rot**. Die Parameter zieht ihr aus dem Funktionsblock heraus in das Zahlenfeld.
- Aufrufen könnt ihr sie dann so: **Aufruf autoampel 1 1 0** für Rot und Gelb.

:::

:::python

- Eine Funktion beginnt mit `def`, dann der Name und in Klammern die Werte, die sie bekommt:

```python
def autoampel(rot, gelb, gruen):
    ...
```

- In der Funktion schreibt ihr jeden Pin auf seinen Wert, zum Beispiel `auto_rot.write_digital(rot)`.
- Aufrufen könnt ihr sie dann so: `autoampel(1, 1, 0)` für Rot und Gelb.

:::

:::javascript

- Eine Funktion beginnt mit `function`, dann der Name und in Klammern die Werte, die sie bekommt. Hinter jedem Wert steht, dass er eine Zahl ist:

```javascript
function autoampel(rot: number, gelb: number, gruen: number) {
    // ...
}
```

- In der Funktion schreibt ihr jeden Pin auf seinen Wert, zum Beispiel `pins.digitalWritePin(auto_rot, rot)`.
- Aufrufen könnt ihr sie dann so: `autoampel(1, 1, 0)` für Rot und Gelb.

:::

</details>
