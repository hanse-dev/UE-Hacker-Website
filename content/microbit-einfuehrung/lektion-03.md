# Die Knöpfe

<img src="/microbit/einfuehrung/knoepfe.svg" alt="Zwei Bilder: Nach Knopf A zeigt der micro:bit ein fröhliches Gesicht, nach Knopf B ein trauriges">

Bisher macht euer Programm immer dasselbe. Jetzt reagiert es: Drückt jemand Knopf A, zeigt der micro:bit ein fröhliches Gesicht.

## Knopf A

:::bloecke

```bloecke
[eingabe] wenn Knopf A geklickt
  [grundlagen] zeige Symbol Fröhlich
```

Den Block **wenn Knopf A geklickt** findet ihr unter **Eingabe**. Er steht frei auf der Fläche, nicht in **beim Start**. Alles darin passiert jedes Mal, wenn jemand Knopf A drückt.

:::

:::python

```python
from microbit import *

while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
```

`while True:` wiederholt alles darunter ohne Ende. `button_a.was_pressed()` fragt jedes Mal: Wurde Knopf A gedrückt? Achtet auf die Einrückung: Sie zeigt, was wozu gehört.

:::

:::javascript

```javascript
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
})
```

Alles in den geschweiften Klammern passiert jedes Mal, wenn jemand Knopf A drückt.

:::

Probiert es aus. Dann baut ihr Knopf B selbst: Er zeigt ein trauriges Gesicht.

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

## Bonus: Der Würfel

Schüttelt den micro:bit, und er zeigt eine zufällige Zahl von 1 bis 6.

<details>
<summary>Tipps anzeigen</summary>

:::bloecke

Unter **Eingabe** gibt es **wenn geschüttelt**. Eine zufällige Zahl findet ihr unter **Mathematik**: **wähle eine zufällige Zahl von 0 bis 10**. Steckt sie in **zeige Zahl** und stellt sie auf 1 bis 6 um.

:::

:::python

`accelerometer.was_gesture('shake')` fragt: Wurde der micro:bit geschüttelt? Für den Zufall schreibt ihr oben `import random`. Dann gibt `random.randint(1, 6)` eine Zahl von 1 bis 6.

:::

:::javascript

`input.onGesture(Gesture.Shake, function () { ... })` reagiert auf Schütteln. `randint(1, 6)` gibt eine Zahl von 1 bis 6, `basic.showNumber()` zeigt sie.

:::

</details>
