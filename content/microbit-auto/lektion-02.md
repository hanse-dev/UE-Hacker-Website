# Stufe 1: Display und Knöpfe

Bevor das Auto fährt, lernt ihr den micro:bit kennen. Er kann Bilder und Text zeigen und hat zwei Knöpfe: **A** links und **B** rechts.

## Text und Bilder zeigen

:::bloecke

```bloecke
[grundlagen] beim Start
  [grundlagen] zeige Text "Los"
  [grundlagen] zeige Symbol Fröhlich
```

Alles in **beim Start** läuft genau einmal, von oben nach unten.

:::

:::python

```python
from microbit import *

display.scroll("Los")
display.show(Image.HAPPY)
```

Python arbeitet die Zeilen von oben nach unten ab. `display.scroll` lässt Text durchlaufen, `display.show` zeigt ein Bild.

:::

## Auf Knöpfe reagieren

:::bloecke

```bloecke
[eingabe] wenn Knopf A geklickt
  [grundlagen] zeige Symbol Fröhlich
[eingabe] wenn Knopf B geklickt
  [grundlagen] zeige Symbol Traurig
```

Die beiden Blöcke stehen einzeln auf der Fläche. Jeder wartet auf seinen Knopf.

:::

:::python

```python
from microbit import *

while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
    if button_b.was_pressed():
        display.show(Image.SAD)
```

`while True:` wiederholt die eingerückten Zeilen ohne Ende. So prüft der micro:bit immer wieder, ob ein Knopf gedrückt wurde. Achtet auf die Einrückung: vier Leerzeichen pro Stufe.

:::

## Tipp

Ein Programm startet neu, wenn ihr den kleinen Knopf auf der Rückseite des micro:bit drückt.
