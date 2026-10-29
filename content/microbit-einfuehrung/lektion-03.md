# Die Knöpfe

<img src="/microbit/einfuehrung/knoepfe.svg" alt="Zwei Bilder: Nach Knopf A zeigt der micro:bit ein fröhliches Gesicht, nach Knopf B ein trauriges">

Bisher macht euer Programm immer dasselbe. Jetzt reagiert es: Drückt jemand Knopf A, zeigt der micro:bit ein fröhliches Gesicht.

## Knopf A

:::bloecke

```bloecke
[eingabe] wenn Knopf A geklickt
  [grundlagen] zeige Symbol Fröhlich
```

Den Block **wenn Knopf A geklickt** findet ihr unter **Eingabe**. Er steht frei auf der Fläche, nicht in **beim Start**. Alles darin passiert jedes Mal, wenn jemand Knopf A drückt. Im Block **zeige Symbol** klickt ihr auf das Herz und wählt das Bild „Fröhlich“ aus.

:::

:::python

```python
from microbit import *

while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
```

`while True:` wiederholt alles darunter ohne Ende. `button_a.was_pressed()` fragt jedes Mal: Wurde Knopf A gedrückt? Achtet auf die Einrückung: Sie zeigt, was wozu gehört. Eingerückt heißt, die Zeile fängt weiter rechts an. Nach einem Doppelpunkt macht der Editor das meist von selbst, sonst drückt ihr die Tab-Taste.

:::

:::javascript

```javascript
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
})
```

Alles in den geschweiften Klammern passiert jedes Mal, wenn jemand Knopf A drückt.

:::

Probiert es aus: Beim micro:bit auf dem Bildschirm klickt ihr auf A. Für den echten micro:bit klickt ihr wieder auf **Herunterladen**. Dann baut ihr Knopf B selbst: Er zeigt ein trauriges Gesicht.

:::bloecke

Holt einen zweiten Block **wenn Knopf A geklickt** und stellt darin A auf B um. Das traurige Gesicht heißt in **zeige Symbol** „Traurig“.

:::

:::python

Das traurige Gesicht heißt `Image.SAD`. Die neuen zwei Zeilen stehen genauso weit eingerückt wie das erste `if`.

:::

:::javascript

Kopiert den Teil mit Knopf A und schreibt ihn unter die letzte Klammer `})`. Ändert dann `A` in `B` und `Happy` in `Sad` (traurig).

:::

<details>
<summary>Lösung anzeigen</summary>

:::bloecke

```bloecke
[eingabe] wenn Knopf A geklickt
  [grundlagen] zeige Symbol Fröhlich
[eingabe] wenn Knopf B geklickt
  [grundlagen] zeige Symbol Traurig
```

Im Block **wenn Knopf A geklickt** könnt ihr A in B umstellen.

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

:::

:::javascript

```javascript
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
})

input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Sad)
})
```

:::

</details>

## Geschafft!

Ihr kennt jetzt alles, was ihr für den Start braucht. Sucht euch einen Kurs aus:

- [Fang den Stern](/kurs/projekt-microbit-sterne): ein Spiel auf der LED-Anzeige. Ihr braucht nur den micro:bit.
- [Die Ampelanlage](/kurs/projekt-microbit-ampel): Lampen auf einem Steckbrett.
- [Das Roboterauto](/kurs/projekt-microbit-auto): ein kleines Auto, das fährt und Hindernisse erkennt.

Ist euch in einem Kurs ein Wort neu? Dann schlagt es im [micro:bit-Spickzettel](/microbit/spickzettel) nach. Wörter mit einem kleinen Pfeil ↗ führen direkt dorthin.

## Bonus: Der Würfel

Schüttelt den micro:bit, und er zeigt eine zufällige Zahl von 1 bis 6.

<details>
<summary>Tipps anzeigen</summary>

:::bloecke

Unter **Eingabe** gibt es **wenn geschüttelt**. Eine zufällige Zahl findet ihr unter **Mathematik**: **wähle eine zufällige Zahl von 0 bis 10**. Den Block **zeige Zahl** findet ihr unter **Grundlagen**. Zieht den Zufalls-Block auf die 0 in **zeige Zahl**. Ändert dann im Zufalls-Block die 0 in 1 und die 10 in 6.

:::

:::python

`accelerometer.was_gesture('shake')` fragt: Wurde der micro:bit geschüttelt? Für den Zufall schreibt ihr unter die erste Zeile `import random`. Dann gibt `random.randint(1, 6)` eine Zahl von 1 bis 6, und `display.show()` zeigt sie, so wie das Gesicht bei Knopf A. Die Frage nach dem Schütteln kommt wie die Knöpfe in die Schleife `while True:`.

:::

:::javascript

`input.onGesture(Gesture.Shake, function () { ... })` reagiert auf Schütteln. Statt `...` kommt hinein, was dann passieren soll. `randint(1, 6)` gibt eine Zahl von 1 bis 6. `basic.showNumber()` zeigt eine Zahl: Steckt `randint(1, 6)` in die Klammern.

:::

Im Simulator rechts könnt ihr auch ohne echten micro:bit schütteln. Wo der Knopf dafür ist, zeigt euch eure Kursleitung.

</details>

<details>
<summary>Lösung anzeigen</summary>

:::bloecke

```bloecke
[eingabe] wenn geschüttelt
  [grundlagen] zeige Zahl wähle eine zufällige Zahl von 1 bis 6
```

:::

:::python

```python
from microbit import *
import random

while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
    if button_b.was_pressed():
        display.show(Image.SAD)
    if accelerometer.was_gesture('shake'):
        display.show(random.randint(1, 6))
```

:::

:::javascript

```javascript
input.onGesture(Gesture.Shake, function () {
    basic.showNumber(randint(1, 6))
})
```

:::

</details>
