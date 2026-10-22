# Stufe 3: Fangen und Punkte

<img src="/microbit/sterne/stufe-3.svg" alt="Oben: Der Stern fällt genau in den Korb, das gibt einen Punkt, und der nächste Stern kommt. Unten: Der Stern landet neben dem Korb, daneben, und der micro:bit zeigt die Punkte, hier eine 3">

Jetzt wird es ein Spiel. Kommt der Stern unten an (`stern_y` ist 4), gibt es zwei Möglichkeiten:

- **Gefangen:** Stern und Korb stehen in derselben Spalte. Dann gibt es einen Punkt.
- **Daneben:** Der micro:bit zeigt die Punkte, und es geht mit 0 Punkten weiter.

## Gefangen?

Legt eine neue Variable `punkte` an, die am Anfang 0 ist. Dann kommt diese Prüfung in die Schleife, direkt nach dem Zeichnen:

:::bloecke

```bloecke
[logik] wenn stern_y = 4 dann
  [logik] wenn stern_x = korb dann
    [variablen] ändere punkte um 1
```

Den Vergleich mit **=** findet ihr unter **Logik**.

:::

:::python

```python
        if stern_y == 4:
            if stern_x == korb:
                punkte = punkte + 1
```

In Python gehört die Prüfung in den Teil, in dem der Stern fällt: direkt nach dem Block `if stern_y > 4:` und genauso weit eingerückt wie dieses `if`. Achtung: Vergleichen heißt `==`, ein einzelnes `=` setzt eine Variable.

:::

:::javascript

```javascript
    if (stern_y == 4) {
        if (stern_x == korb) {
            punkte = punkte + 1
        }
    }
```

Achtung: Vergleichen heißt `==`, ein einzelnes `=` setzt eine Variable.

:::

Probiert es aus. Ihr seht die Punkte noch nicht. Das kommt jetzt.

## Daneben!

Fällt der Stern daneben, zeigt der micro:bit die Punkte. Danach fängt `punkte` wieder bei 0 an. Baut das selbst ein: Es ist das **sonst** zu „gefangen“.

<details>
<summary>Lösung anzeigen</summary>

:::bloecke

```bloecke
[grundlagen] beim Start
  [variablen] setze korb auf 2
  [variablen] setze stern_x auf wähle eine zufällige Zahl von 0 bis 4
  [variablen] setze stern_y auf 0
  [variablen] setze punkte auf 0
  [led] Zeichne x korb y 4
[grundlagen] dauerhaft
  [led] lösche x stern_x y stern_y
  [variablen] ändere stern_y um 1
  [logik] wenn stern_y > 4 dann
    [variablen] setze stern_y auf 0
    [variablen] setze stern_x auf wähle eine zufällige Zahl von 0 bis 4
  [led] Zeichne x stern_x y stern_y
  [led] Zeichne x korb y 4
  [logik] wenn stern_y = 4 dann
    [logik] wenn stern_x = korb dann
      [variablen] ändere punkte um 1
    [logik] ansonsten
      [grundlagen] zeige Zahl punkte
      [variablen] setze punkte auf 0
      [grundlagen] Bildschirminhalt löschen
  [grundlagen] pausiere (ms) 400
```

Die Knopf-Blöcke aus Stufe 1 bleiben, wie sie sind.

:::

:::python

```python
from microbit import *
import random

korb = 2
stern_x = random.randint(0, 4)
stern_y = 0
takt = 0
punkte = 0

while True:
    if button_a.was_pressed() and korb > 0:
        korb = korb - 1
    if button_b.was_pressed() and korb < 4:
        korb = korb + 1

    takt = takt + 1
    if takt == 8:
        takt = 0
        stern_y = stern_y + 1
        if stern_y > 4:
            stern_y = 0
            stern_x = random.randint(0, 4)
        if stern_y == 4:
            if stern_x == korb:
                punkte = punkte + 1
            else:
                display.scroll(punkte)
                punkte = 0

    display.clear()
    display.set_pixel(stern_x, stern_y, 9)
    display.set_pixel(korb, 4, 9)
    sleep(50)
```

:::

:::javascript

```javascript
let korb = 2
let stern_x = randint(0, 4)
let stern_y = 0
let punkte = 0
led.plot(korb, 4)

input.onButtonPressed(Button.A, function () {
    if (korb > 0) {
        led.unplot(korb, 4)
        korb = korb - 1
        led.plot(korb, 4)
    }
})

input.onButtonPressed(Button.B, function () {
    if (korb < 4) {
        led.unplot(korb, 4)
        korb = korb + 1
        led.plot(korb, 4)
    }
})

basic.forever(function () {
    led.unplot(stern_x, stern_y)
    stern_y = stern_y + 1
    if (stern_y > 4) {
        stern_y = 0
        stern_x = randint(0, 4)
    }
    led.plot(stern_x, stern_y)
    led.plot(korb, 4)
    if (stern_y == 4) {
        if (stern_x == korb) {
            punkte = punkte + 1
        } else {
            basic.showNumber(punkte)
            punkte = 0
            basic.clearScreen()
        }
    }
    basic.pause(400)
})
```

:::

</details>

Fertig! Spielt eine Runde gegeneinander: Wer fängt mehr Sterne?

## Bonus: Drei Leben

Ein Stern daneben ist noch nicht das Ende. Ihr habt drei Leben. Erst wenn alle drei weg sind, zeigt der micro:bit die Punkte, und alles beginnt von vorn.

<details>
<summary>Tipps anzeigen</summary>

- Ihr braucht eine neue Variable `leben`, die am Anfang 3 ist.
- Daneben heißt jetzt: `leben` wird um 1 kleiner. Erst wenn `leben` 0 ist, kommen die Punkte.
- Beim Neustart bekommen `punkte` und `leben` wieder ihre Anfangswerte.

</details>
