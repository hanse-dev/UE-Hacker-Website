# Stufe 1: Die Fußgängerampel

Eine Fußgängerampel hat zwei Lampen: Rot heißt stehen, Grün heißt gehen. Meistens ist sie rot. Erst wenn jemand auf den Knopf drückt, wird sie für eine Weile grün. Euer Knopf ist Knopf **A** am micro:bit.

## Die grüne LED stecken

Die rote LED aus der ersten Stufe bleibt stecken. Die grüne LED kommt direkt darunter und wird genauso angeschlossen, nur zwei Reihen tiefer und an **P14**.

<img src="/microbit/ampel/stufe-1.svg" alt="Steckplan Fußgängerampel: rote LED an P13 in Reihe 10 und 11, grüne LED an P14 in Reihe 12 und 13, jede mit Widerstand über der Lücke und eigenem Kabel zu GND">

1. Zieht das USB-Kabel ab.
2. **Widerstand** über die Lücke in Reihe 12.
3. **Grüne LED:** langes Bein in Reihe 12 rechts, kurzes Bein in Reihe 13 rechts.
4. **Kabel von P14** in Reihe 12 links.
5. **Kabel von GND** in Reihe 13 rechts.

Prüft mit dem Finger: Hat auch die grüne LED einen geschlossenen Kreis?

## Rot nach dem Start

Nach dem Start soll nur Rot leuchten. Alles, was nur einmal am Anfang passieren soll, kommt in den Start-Block.

:::bloecke

```bloecke
[grundlagen] beim Start
  [pins] schreibe digitalen Wert von Pin P13 auf 1
  [pins] schreibe digitalen Wert von Pin P14 auf 0
```

:::

:::python

```python
from microbit import *

pin13.write_digital(1)
pin14.write_digital(0)
```

Was ganz oben ohne Einrückung steht, passiert genau einmal nach dem Start.

:::

## Auf den Knopf reagieren

Jetzt kommt der Knopf dazu. Wird Knopf A gedrückt, geht Rot aus und Grün an. Das Gerüst zeigt euch den Anfang.

:::bloecke

```bloecke
[eingabe] wenn Knopf A geklickt
  [pins] schreibe digitalen Wert von Pin P13 auf 0
  [pins] schreibe digitalen Wert von Pin P14 auf 1
```

Den Block **wenn Knopf A geklickt** findet ihr unter **Eingabe**. Er steht frei neben **beim Start**, nicht darin.

:::

:::python

```python
from microbit import *

pin13.write_digital(1)
pin14.write_digital(0)

while True:
    if button_a.was_pressed():
        pin13.write_digital(0)
        pin14.write_digital(1)
```

`button_a.was_pressed()` fragt: Wurde Knopf A seit dem letzten Fragen gedrückt? Die Schleife fragt das ohne Ende immer wieder.

:::

Probiert es aus. Grün geht an, aber nie wieder aus. Ergänzt das Programm so, dass die Ampel nach 5 Sekunden wieder auf Rot schaltet.

<details>
<summary>Lösung anzeigen</summary>

:::bloecke

```bloecke
[grundlagen] beim Start
  [pins] schreibe digitalen Wert von Pin P13 auf 1
  [pins] schreibe digitalen Wert von Pin P14 auf 0
[eingabe] wenn Knopf A geklickt
  [pins] schreibe digitalen Wert von Pin P13 auf 0
  [pins] schreibe digitalen Wert von Pin P14 auf 1
  [grundlagen] pausiere (ms) 5000
  [pins] schreibe digitalen Wert von Pin P14 auf 0
  [pins] schreibe digitalen Wert von Pin P13 auf 1
```

:::

:::python

```python
from microbit import *

pin13.write_digital(1)
pin14.write_digital(0)

while True:
    if button_a.was_pressed():
        pin13.write_digital(0)
        pin14.write_digital(1)
        sleep(5000)
        pin14.write_digital(0)
        pin13.write_digital(1)
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

</details>
