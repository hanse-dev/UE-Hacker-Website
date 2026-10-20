# Stufe 3: Die Ampelanlage

Jetzt arbeiten beide Ampeln zusammen, wie an einem Zebrastreifen mit Ampel. Die Autos haben Grün, bis jemand auf den Knopf drückt. Dann hält die Autoampel die Autos an, und die Fußgänger dürfen gehen.

An der Schaltung ändert sich nichts. Alle fünf LEDs stecken schon.

## Die wichtigste Regel

> Autos und Fußgänger dürfen **nie gleichzeitig Grün** haben.

Echte Ampeln warten sogar nach jedem Rot noch einen Moment, bevor die anderen Grün bekommen. In dieser **Räumzeit** kommen alle, die noch unterwegs sind, sicher auf die andere Seite.

## Zuerst der Plan

Bevor ihr programmiert, schreibt ihr den Ablauf in Worten auf, auf Papier oder als Liste. Beginnt so:

1. Grundzustand: Die Autos haben Grün, die Fußgänger Rot.
2. Jemand drückt Knopf A.
3. ...

Überlegt: Welche Phasen der Autoampel aus Stufe 2 kommen vor? Wo braucht ihr eine Räumzeit? Wie kommt die Autoampel am Ende wieder auf Grün?

<details>
<summary>Plan anzeigen</summary>

1. Grundzustand: Autos Grün, Fußgänger Rot.
2. Jemand drückt Knopf A.
3. Autoampel Gelb, 2 Sekunden.
4. Autoampel Rot. Räumzeit: 1 Sekunde warten.
5. Fußgänger Grün, 5 Sekunden.
6. Fußgänger Rot. Räumzeit: 1 Sekunde warten.
7. Autoampel Rot und Gelb, 1 Sekunde.
8. Autoampel Grün. Jetzt ist wieder der Grundzustand erreicht.

</details>

## Der Grundzustand

Der Grundzustand wird beim Start hergestellt. Jetzt braucht ihr alle fünf Namen aus Stufe 1 und 2:

| Variable | Pin | LED |
|---|---|---|
| `auto_rot` / `auto_gelb` / `auto_gruen` | P16 / P15 / P14 | Autoampel Rot / Gelb / Grün |
| `fuss_rot` / `fuss_gruen` | P13 / P12 | Fußgängerampel Rot / Grün |

:::bloecke

```bloecke
[grundlagen] beim Start
  [variablen] setze auto_rot auf P16
  [variablen] setze auto_gelb auf P15
  [variablen] setze auto_gruen auf P14
  [variablen] setze fuss_rot auf P13
  [variablen] setze fuss_gruen auf P12
  [pins] schreibe digitalen Wert von Pin auto_gruen auf 1
  [pins] schreibe digitalen Wert von Pin fuss_rot auf 1
[eingabe] wenn Knopf A geklickt
  [pins] schreibe digitalen Wert von Pin auto_gruen auf 0
  [pins] schreibe digitalen Wert von Pin auto_gelb auf 1
  [grundlagen] pausiere (ms) 2000
```

:::

:::python

```python
from microbit import *

auto_rot = pin16
auto_gelb = pin15
auto_gruen = pin14
fuss_rot = pin13
fuss_gruen = pin12

auto_gruen.write_digital(1)
fuss_rot.write_digital(1)

while True:
    if button_a.was_pressed():
        auto_gruen.write_digital(0)
        auto_gelb.write_digital(1)
        sleep(2000)
```

:::

:::javascript

```javascript
let auto_rot = DigitalPin.P16
let auto_gelb = DigitalPin.P15
let auto_gruen = DigitalPin.P14
let fuss_rot = DigitalPin.P13
let fuss_gruen = DigitalPin.P12

pins.digitalWritePin(auto_gruen, 1)
pins.digitalWritePin(fuss_rot, 1)

input.onButtonPressed(Button.A, function () {
    pins.digitalWritePin(auto_gruen, 0)
    pins.digitalWritePin(auto_gelb, 1)
    basic.pause(2000)
})
```

:::

Der Anfang von Schritt 3 steht schon da: Grün aus, Gelb an, 2 Sekunden warten. Baut die übrigen Schritte eures Plans dazu. Achtet bei jedem Schritt darauf, welche LED aus- und welche angeht.

Testet zum Schluss genau: Drückt Knopf A und schaut auf beide Ampeln gleichzeitig. Leuchten irgendwann beide Grün? Dann stimmt etwas nicht.

<details>
<summary>Lösung anzeigen</summary>

:::bloecke

```bloecke
[grundlagen] beim Start
  [variablen] setze auto_rot auf P16
  [variablen] setze auto_gelb auf P15
  [variablen] setze auto_gruen auf P14
  [variablen] setze fuss_rot auf P13
  [variablen] setze fuss_gruen auf P12
  [pins] schreibe digitalen Wert von Pin auto_gruen auf 1
  [pins] schreibe digitalen Wert von Pin fuss_rot auf 1
[eingabe] wenn Knopf A geklickt
  [pins] schreibe digitalen Wert von Pin auto_gruen auf 0
  [pins] schreibe digitalen Wert von Pin auto_gelb auf 1
  [grundlagen] pausiere (ms) 2000
  [pins] schreibe digitalen Wert von Pin auto_gelb auf 0
  [pins] schreibe digitalen Wert von Pin auto_rot auf 1
  [grundlagen] pausiere (ms) 1000
  [pins] schreibe digitalen Wert von Pin fuss_rot auf 0
  [pins] schreibe digitalen Wert von Pin fuss_gruen auf 1
  [grundlagen] pausiere (ms) 5000
  [pins] schreibe digitalen Wert von Pin fuss_gruen auf 0
  [pins] schreibe digitalen Wert von Pin fuss_rot auf 1
  [grundlagen] pausiere (ms) 1000
  [pins] schreibe digitalen Wert von Pin auto_gelb auf 1
  [grundlagen] pausiere (ms) 1000
  [pins] schreibe digitalen Wert von Pin auto_rot auf 0
  [pins] schreibe digitalen Wert von Pin auto_gelb auf 0
  [pins] schreibe digitalen Wert von Pin auto_gruen auf 1
```

:::

:::python

```python
from microbit import *

auto_rot = pin16
auto_gelb = pin15
auto_gruen = pin14
fuss_rot = pin13
fuss_gruen = pin12

auto_gruen.write_digital(1)
fuss_rot.write_digital(1)

while True:
    if button_a.was_pressed():
        # Autos: Gelb, dann Rot
        auto_gruen.write_digital(0)
        auto_gelb.write_digital(1)
        sleep(2000)
        auto_gelb.write_digital(0)
        auto_rot.write_digital(1)
        sleep(1000)
        # Fußgänger: Grün, dann Rot
        fuss_rot.write_digital(0)
        fuss_gruen.write_digital(1)
        sleep(5000)
        fuss_gruen.write_digital(0)
        fuss_rot.write_digital(1)
        sleep(1000)
        # Autos: Rot und Gelb, dann Grün
        auto_gelb.write_digital(1)
        sleep(1000)
        auto_rot.write_digital(0)
        auto_gelb.write_digital(0)
        auto_gruen.write_digital(1)
```

:::

:::javascript

```javascript
let auto_rot = DigitalPin.P16
let auto_gelb = DigitalPin.P15
let auto_gruen = DigitalPin.P14
let fuss_rot = DigitalPin.P13
let fuss_gruen = DigitalPin.P12

pins.digitalWritePin(auto_gruen, 1)
pins.digitalWritePin(fuss_rot, 1)

input.onButtonPressed(Button.A, function () {
    // Autos: Gelb, dann Rot
    pins.digitalWritePin(auto_gruen, 0)
    pins.digitalWritePin(auto_gelb, 1)
    basic.pause(2000)
    pins.digitalWritePin(auto_gelb, 0)
    pins.digitalWritePin(auto_rot, 1)
    basic.pause(1000)
    // Fußgänger: Grün, dann Rot
    pins.digitalWritePin(fuss_rot, 0)
    pins.digitalWritePin(fuss_gruen, 1)
    basic.pause(5000)
    pins.digitalWritePin(fuss_gruen, 0)
    pins.digitalWritePin(fuss_rot, 1)
    basic.pause(1000)
    // Autos: Rot und Gelb, dann Grün
    pins.digitalWritePin(auto_gelb, 1)
    basic.pause(1000)
    pins.digitalWritePin(auto_rot, 0)
    pins.digitalWritePin(auto_gelb, 0)
    pins.digitalWritePin(auto_gruen, 1)
})
```

:::

</details>

## Bonus: Signal kommt

An vielen Fußgängerampeln leuchtet nach dem Drücken ein Schild: **Signal kommt**. So wissen alle, dass der Knopf funktioniert hat. Lasst die LED-Anzeige des micro:bit nach Knopf A ein Symbol zeigen, bis die Fußgänger Grün bekommen. Danach wird die Anzeige wieder dunkel.

<details>
<summary>Tipps anzeigen</summary>

- Das Symbol muss gleich am Anfang kommen, noch bevor die Autoampel umschaltet.
- Überlegt, an welcher Stelle eures Ablaufs die Fußgänger Grün bekommen. Dort löscht ihr die Anzeige.

:::bloecke

Unter **Grundlagen** gibt es **zeige Symbol**. **Bildschirminhalt löschen** findet ihr dort, wenn ihr auf **mehr** klickt. Das Symbol **Ja** (ein Haken) passt gut.

:::

:::python

`display.show(Image.YES)` zeigt einen Haken, `display.clear()` macht die Anzeige wieder dunkel.

:::

:::javascript

`basic.showIcon(IconNames.Yes)` zeigt einen Haken, `basic.clearScreen()` macht die Anzeige wieder dunkel.

:::

</details>
