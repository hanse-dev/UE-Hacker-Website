# Stufe 1: Die Fußgängerampel

Eine Fußgängerampel hat zwei Lampen: Rot heißt stehen, Grün heißt gehen. Meistens ist sie rot. Erst wenn jemand auf den Knopf drückt, wird sie für eine Weile grün. Euer Knopf ist Knopf **A** am micro:bit.

## Die grüne LED stecken

Die rote LED aus der ersten Stufe bleibt stecken. Die grüne LED kommt direkt darunter und wird genauso angeschlossen, nur zwei Reihen tiefer und an **P12**. Auch sie bekommt eine Brücke in die GND-Reihe 14.

<img src="/microbit/ampel/stufe-1.svg" alt="Steckplan Fußgängerampel: rote LED an P13 in Reihe 10 und 11, grüne LED an P12 in Reihe 12 und 13, jede mit Widerstand über der Lücke und einer Brücke in die GND-Reihe 14, dort ein Kabel zu GND">

1. Zieht das USB-Kabel ab.
2. **Widerstand** über die Lücke in Reihe 12.
3. **Grüne LED:** langes Bein in Reihe 12 rechts, kurzes Bein in Reihe 13 rechts.
4. **Kabel von P12** in Reihe 12 links.
5. **Brücke** von Reihe 13 rechts in die GND-Reihe 14.

Prüft mit dem Finger: Hat auch die grüne LED einen geschlossenen Kreis?

## Die Pins bekommen Namen

Ab jetzt gibt es zwei LEDs, bald fünf. Damit ihr nicht nachschlagen müsst, welche Nummer welche Lampe ist, gebt ihr jedem Pin einen Namen: eine **Variable**. Die Variable `fuss_rot` steht dann für den Pin P13, `fuss_gruen` für P12. Steckt eine LED später an einem anderen Pin, ändert ihr nur eine Zeile.

| Variable | Pin | LED |
|---|---|---|
| `fuss_rot` | P13 | Fußgängerampel Rot |
| `fuss_gruen` | P12 | Fußgängerampel Grün |

## Rot nach dem Start

Nach dem Start soll nur Rot leuchten. Alles, was nur einmal am Anfang passieren soll, kommt in den Start-Block. Zuerst bekommen die Pins ihre Namen, dann werden die LEDs geschaltet.

:::bloecke

```bloecke
[grundlagen] beim Start
  [variablen] setze fuss_rot auf P13
  [variablen] setze fuss_gruen auf P12
  [pins] schreibe digitalen Wert von Pin fuss_rot auf 1
  [pins] schreibe digitalen Wert von Pin fuss_gruen auf 0
```

Die Variablen legt ihr unter **Variablen** mit **Erstelle eine Variable** an. Im Block **setze … auf** klickt ihr auf den Namen und wählt die richtige Variable aus. Den Pin bekommt sie mit dem Block **Digital-Pin**: Klickt in der Blockliste auf **Fortgeschritten**, dann auf **Pins** und darunter auf **… mehr**. Zieht den Block in das Feld hinter **auf** und wählt darin **P13** bzw. **P12**. In den Pin-Block zieht ihr statt der Nummer die Variable.

:::

:::python

```python
from microbit import *

fuss_rot = pin13
fuss_gruen = pin12

fuss_rot.write_digital(1)
fuss_gruen.write_digital(0)
```

Was ganz oben ohne Einrückung steht, passiert genau einmal nach dem Start. `fuss_rot = pin13` gibt dem Pin 13 den Namen `fuss_rot`.

:::

:::javascript

```javascript
let fuss_rot = DigitalPin.P13
let fuss_gruen = DigitalPin.P12

pins.digitalWritePin(fuss_rot, 1)
pins.digitalWritePin(fuss_gruen, 0)
```

Was außerhalb von Klammern wie `basic.forever` steht, passiert genau einmal nach dem Start. `let fuss_rot = DigitalPin.P13` gibt dem Pin 13 den Namen `fuss_rot`.

:::

## Auf den Knopf reagieren

Jetzt kommt der Knopf dazu. Wird Knopf A gedrückt, geht Rot aus und Grün an. Das Gerüst zeigt euch den Anfang.

:::bloecke

```bloecke
[eingabe] wenn Knopf A geklickt
  [pins] schreibe digitalen Wert von Pin fuss_rot auf 0
  [pins] schreibe digitalen Wert von Pin fuss_gruen auf 1
```

Den Block **wenn Knopf A geklickt** findet ihr unter **Eingabe**. Er steht frei neben **beim Start**, nicht darin.

:::

:::python

```python
from microbit import *

fuss_rot = pin13
fuss_gruen = pin12

fuss_rot.write_digital(1)
fuss_gruen.write_digital(0)

while True:
    if button_a.was_pressed():
        fuss_rot.write_digital(0)
        fuss_gruen.write_digital(1)
```

`button_a.was_pressed()` fragt: Wurde Knopf A seit dem letzten Fragen gedrückt? Die Schleife fragt das ohne Ende immer wieder.

:::

:::javascript

```javascript
input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(fuss_rot, 0)
    pins.digitalWritePin(fuss_gruen, 1)
})
```

Alles in den geschweiften Klammern von `input.onButtonPressed` passiert, sobald jemand Knopf A drückt. Es kommt unter die Zeilen vom Start.

:::

Probiert es aus. Grün geht an, aber nie wieder aus. Ergänzt das Programm so, dass die Ampel nach 5 Sekunden wieder auf Rot schaltet. 5 Sekunden sind 5000 Millisekunden.

<details>
<summary>Lösung anzeigen</summary>

:::bloecke

```bloecke
[grundlagen] beim Start
  [variablen] setze fuss_rot auf P13
  [variablen] setze fuss_gruen auf P12
  [pins] schreibe digitalen Wert von Pin fuss_rot auf 1
  [pins] schreibe digitalen Wert von Pin fuss_gruen auf 0
[eingabe] wenn Knopf A geklickt
  [pins] schreibe digitalen Wert von Pin fuss_rot auf 0
  [pins] schreibe digitalen Wert von Pin fuss_gruen auf 1
  [grundlagen] pausiere (ms) 5000
  [pins] schreibe digitalen Wert von Pin fuss_gruen auf 0
  [pins] schreibe digitalen Wert von Pin fuss_rot auf 1
```

:::

:::python

```python
from microbit import *

fuss_rot = pin13
fuss_gruen = pin12

fuss_rot.write_digital(1)
fuss_gruen.write_digital(0)

while True:
    if button_a.was_pressed():
        fuss_rot.write_digital(0)
        fuss_gruen.write_digital(1)
        sleep(5000)
        fuss_gruen.write_digital(0)
        fuss_rot.write_digital(1)
```

:::

:::javascript

```javascript
let fuss_rot = DigitalPin.P13
let fuss_gruen = DigitalPin.P12

pins.digitalWritePin(fuss_rot, 1)
pins.digitalWritePin(fuss_gruen, 0)

input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(fuss_rot, 0)
    pins.digitalWritePin(fuss_gruen, 1)
    basic.pause(5000)
    pins.digitalWritePin(fuss_gruen, 0)
    pins.digitalWritePin(fuss_rot, 1)
})
```

:::

</details>

## Bonus: Grün blinkt zum Abschied

In manchen Ländern blinkt das grüne Licht, kurz bevor die Ampel auf Rot schaltet. So wissen alle: Jetzt nicht mehr losgehen! Lasst Grün dreimal blinken, bevor Rot kommt.

<details>
<summary>Tipps anzeigen</summary>

- Einmal blinken heißt: aus, kurz warten, an, kurz warten. Probiert 300 Millisekunden.
- Das Blinken kommt zwischen die 5 Sekunden Grün und das Umschalten auf Rot.

:::bloecke

Damit ihr das Blinken nicht dreimal bauen müsst, gibt es unter **Schleifen** den Block **4-mal wiederholen**. Die Zahl könnt ihr ändern.

:::

:::python

Damit ihr das Blinken nicht dreimal schreiben müsst, gibt es die Zählschleife. Alles, was darunter eingerückt ist, passiert dreimal:

```python
for i in range(3):
    ...
```

:::

:::javascript

Damit ihr das Blinken nicht dreimal schreiben müsst, gibt es die Zählschleife. Alles in den geschweiften Klammern passiert dreimal:

```javascript
for (let i = 0; i < 3; i++) {
    // ...
}
```

:::

</details>
