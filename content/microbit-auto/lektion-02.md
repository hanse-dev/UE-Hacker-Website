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

## Eure Namen

Statt Bildern können die Knöpfe auch Text zeigen. Ändert das Programm so, dass Knopf A den Namen des einen von euch zeigt und Knopf B den des anderen. Den Text-Befehl kennt ihr von oben. Die Bilder dürfen dafür weg.

## Tipp

Ein Programm startet neu, wenn ihr den kleinen Knopf auf der Rückseite des micro:bit drückt.

## Bonus: Der Countdown

Vor jedem Start wird gezählt. Nach Knopf **A** soll der micro:bit **3**, dann **2**, dann **1** zeigen und danach ein Bild eurer Wahl. Jede Zahl bleibt etwa eine Sekunde stehen.

<details>
<summary>Tipps anzeigen</summary>

Ihr braucht zwei neue Bausteine: einen, der eine Zahl zeigt, und einen, der wartet.

:::bloecke

```bloecke
[grundlagen] zeige Zahl 3
[grundlagen] pausiere (ms) 1000
```

1000 Millisekunden sind eine Sekunde.

:::

:::python

```python
display.show(3)
sleep(1000)
```

`sleep(1000)` wartet 1000 Millisekunden, also eine Sekunde.

:::

- Überlegt zuerst in Worten: Was passiert nacheinander, sobald Knopf A gedrückt wird?
- Probiert aus, was ohne das Warten passiert. Könnt ihr die Zahlen dann noch lesen?
- Für Profis: Dreimal fast dasselbe hinschreiben ist mühsam. In Stufe 5 lernt ihr Wiederholungen kennen. Kommt danach zurück und baut den Countdown kürzer.

</details>
