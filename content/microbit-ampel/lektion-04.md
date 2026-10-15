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

Der Grundzustand wird beim Start hergestellt. Die Pins sind dieselben wie bisher:

| Pin | LED |
|---|---|
| P0 / P1 / P2 | Autoampel Rot / Gelb / Grün |
| P13 / P14 | Fußgängerampel Rot / Grün |

:::bloecke

```bloecke
[grundlagen] beim Start
  [pins] schreibe digitalen Wert von Pin P2 auf 1
  [pins] schreibe digitalen Wert von Pin P13 auf 1
[eingabe] wenn Knopf A geklickt
  [pins] schreibe digitalen Wert von Pin P2 auf 0
  [pins] schreibe digitalen Wert von Pin P1 auf 1
  [grundlagen] pausiere (ms) 2000
```

:::

:::python

```python
from microbit import *

pin2.write_digital(1)
pin13.write_digital(1)

while True:
    if button_a.was_pressed():
        pin2.write_digital(0)
        pin1.write_digital(1)
        sleep(2000)
```

:::

Der Anfang von Schritt 3 steht schon da: Grün aus, Gelb an, 2 Sekunden warten. Baut die übrigen Schritte eures Plans dazu. Achtet bei jedem Schritt darauf, welche LED aus- und welche angeht.

Testet zum Schluss genau: Drückt Knopf A und schaut auf beide Ampeln gleichzeitig. Leuchten irgendwann beide Grün? Dann stimmt etwas nicht.

<details>
<summary>Lösung anzeigen</summary>

:::bloecke

```bloecke
[grundlagen] beim Start
  [pins] schreibe digitalen Wert von Pin P2 auf 1
  [pins] schreibe digitalen Wert von Pin P13 auf 1
[eingabe] wenn Knopf A geklickt
  [pins] schreibe digitalen Wert von Pin P2 auf 0
  [pins] schreibe digitalen Wert von Pin P1 auf 1
  [grundlagen] pausiere (ms) 2000
  [pins] schreibe digitalen Wert von Pin P1 auf 0
  [pins] schreibe digitalen Wert von Pin P0 auf 1
  [grundlagen] pausiere (ms) 1000
  [pins] schreibe digitalen Wert von Pin P13 auf 0
  [pins] schreibe digitalen Wert von Pin P14 auf 1
  [grundlagen] pausiere (ms) 5000
  [pins] schreibe digitalen Wert von Pin P14 auf 0
  [pins] schreibe digitalen Wert von Pin P13 auf 1
  [grundlagen] pausiere (ms) 1000
  [pins] schreibe digitalen Wert von Pin P1 auf 1
  [grundlagen] pausiere (ms) 1000
  [pins] schreibe digitalen Wert von Pin P0 auf 0
  [pins] schreibe digitalen Wert von Pin P1 auf 0
  [pins] schreibe digitalen Wert von Pin P2 auf 1
```

:::

:::python

```python
from microbit import *

pin2.write_digital(1)
pin13.write_digital(1)

while True:
    if button_a.was_pressed():
        # Autos: Gelb, dann Rot
        pin2.write_digital(0)
        pin1.write_digital(1)
        sleep(2000)
        pin1.write_digital(0)
        pin0.write_digital(1)
        sleep(1000)
        # Fußgänger: Grün, dann Rot
        pin13.write_digital(0)
        pin14.write_digital(1)
        sleep(5000)
        pin14.write_digital(0)
        pin13.write_digital(1)
        sleep(1000)
        # Autos: Rot und Gelb, dann Grün
        pin1.write_digital(1)
        sleep(1000)
        pin0.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(1)
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

</details>
