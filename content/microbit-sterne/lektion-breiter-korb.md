# Stufe 4: Der breite Korb

<img src="/microbit/sterne/breiter-korb.svg" alt="Drei Bilder mit einem Korb aus zwei Lampen bei x 2 und x 3: Ein Stern über der linken Lampe gibt einen Punkt, ein Stern über der rechten Lampe auch. Ein Stern bei x 4 fällt daneben">

Mit einem breiteren Korb fangt ihr mehr Sterne. Der Korb bekommt rechts eine zweite Lampe. `korb` bleibt die Spalte der linken Lampe, die rechte Lampe steht bei `korb + 1`.

Dafür ändert ihr drei Stellen im Programm: das Zeichnen, den rechten Rand und das Fangen.

## Zwei Lampen

:::bloecke

Überall, wo der Korb gezeichnet oder gelöscht wird, kommt ein zweiter Block für die rechte Lampe dazu. So sieht Knopf A dann aus:

```bloecke
[eingabe] wenn Knopf A geklickt
  [logik] wenn korb > 0 dann
    [led] lösche x korb y 4
    [led] lösche x korb + 1 y 4
    [variablen] ändere korb um -1
    [led] Zeichne x korb y 4
    [led] Zeichne x korb + 1 y 4
```

**`korb` + 1** baut ihr mit dem Block **0 + 0** unter **Mathematik**: `korb` kommt ins linke Feld, ins rechte tippt ihr 1.

Baut Knopf B genauso um. Auch in **beim Start** und in **dauerhaft** wird der Korb gezeichnet. Dort braucht er ebenfalls seine rechte Lampe.

:::

:::python

Der Korb wird nur an einer Stelle gezeichnet: unten in der Schleife. Schreibt darunter eine zweite Zeile für die rechte Lampe:

```python
    display.set_pixel(korb, 4, 9)
    display.set_pixel(korb + 1, 4, 9)
```

Löschen müsst ihr nichts, das macht `display.clear()` schon.

:::

:::javascript

Überall, wo der Korb gezeichnet oder gelöscht wird, kommt eine zweite Zeile für die rechte Lampe dazu. So sieht Knopf A dann aus:

```javascript
input.onButtonPressed(Button.A, function () {
    if (korb > 0) {
        led.unplot(korb, 4)
        led.unplot(korb + 1, 4)
        korb = korb - 1
        led.plot(korb, 4)
        led.plot(korb + 1, 4)
    }
})
```

Baut Knopf B genauso um. Auch ganz oben unter den Variablen und in `basic.forever` steht `led.plot(korb, 4)`. Dort braucht der Korb ebenfalls seine rechte Lampe.

:::

Probiert es aus. Fahrt dann mit Knopf B ganz nach rechts.

## Problem am rechten Rand

Steht der Korb ganz rechts, ist `korb` 4. Die rechte Lampe wäre dann bei x = 5, und die gibt es nicht.

:::bloecke

Die rechte Hälfte vom Korb verschwindet einfach.

:::

:::python

In Python läuft wieder eine Fehlermeldung über die Anzeige.

:::

:::javascript

Die rechte Hälfte vom Korb verschwindet einfach.

:::

Bis zu welcher Zahl darf `korb` jetzt nur noch fahren? Ändert die Grenze bei Knopf B. Am linken Rand bleibt alles, wie es ist: `korb` ist ja die linke Lampe.

## Gefangen mit beiden Hälften

Fällt der Stern auf die rechte Lampe, gibt es noch keinen Punkt. Euer Programm vergleicht `stern_x` nur mit `korb`. Gefangen ist der Stern jetzt, wenn `stern_x` gleich `korb` ist **oder** gleich `korb + 1`.

:::bloecke

Den Block **oder** findet ihr unter **Logik**. Er kommt in den inneren wenn-Block, an die Stelle von **`stern_x` = `korb`**. In jedes seiner zwei Felder steckt ihr einen Vergleich **=**:

```bloecke
[logik] wenn stern_x = korb oder stern_x = korb + 1 dann
  [variablen] ändere punkte um 1
```

:::

:::python

„Oder“ heißt in Python `or`. Ändert die Zeile `if stern_x == korb:` so:

```python
            if stern_x == korb or stern_x == korb + 1:
```

:::

:::javascript

„Oder“ heißt in JavaScript `||`. Ändert die Zeile `if (stern_x == korb) {` so:

```javascript
        if (stern_x == korb || stern_x == korb + 1) {
```

:::

Habt ihr in Stufe 3 drei Leben eingebaut? Dann bleibt euer Teil für „daneben“, wie er ist.

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
  [led] Zeichne x korb + 1 y 4
[eingabe] wenn Knopf A geklickt
  [logik] wenn korb > 0 dann
    [led] lösche x korb y 4
    [led] lösche x korb + 1 y 4
    [variablen] ändere korb um -1
    [led] Zeichne x korb y 4
    [led] Zeichne x korb + 1 y 4
[eingabe] wenn Knopf B geklickt
  [logik] wenn korb < 3 dann
    [led] lösche x korb y 4
    [led] lösche x korb + 1 y 4
    [variablen] ändere korb um 1
    [led] Zeichne x korb y 4
    [led] Zeichne x korb + 1 y 4
[grundlagen] dauerhaft
  [led] lösche x stern_x y stern_y
  [variablen] ändere stern_y um 1
  [logik] wenn stern_y > 4 dann
    [variablen] setze stern_y auf 0
    [variablen] setze stern_x auf wähle eine zufällige Zahl von 0 bis 4
  [led] Zeichne x stern_x y stern_y
  [led] Zeichne x korb y 4
  [led] Zeichne x korb + 1 y 4
  [logik] wenn stern_y = 4 dann
    [logik] wenn stern_x = korb oder stern_x = korb + 1 dann
      [variablen] ändere punkte um 1
    [logik] ansonsten
      [grundlagen] zeige Zahl punkte
      [variablen] setze punkte auf 0
      [grundlagen] Bildschirminhalt löschen
  [grundlagen] pausiere (ms) 400
```

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
    if button_b.was_pressed() and korb < 3:
        korb = korb + 1

    takt = takt + 1
    if takt == 8:
        takt = 0
        stern_y = stern_y + 1
        if stern_y > 4:
            stern_y = 0
            stern_x = random.randint(0, 4)
        if stern_y == 4:
            if stern_x == korb or stern_x == korb + 1:
                punkte = punkte + 1
            else:
                display.scroll(punkte)
                punkte = 0

    display.clear()
    display.set_pixel(stern_x, stern_y, 9)
    display.set_pixel(korb, 4, 9)
    display.set_pixel(korb + 1, 4, 9)
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
led.plot(korb + 1, 4)

input.onButtonPressed(Button.A, function () {
    if (korb > 0) {
        led.unplot(korb, 4)
        led.unplot(korb + 1, 4)
        korb = korb - 1
        led.plot(korb, 4)
        led.plot(korb + 1, 4)
    }
})

input.onButtonPressed(Button.B, function () {
    if (korb < 3) {
        led.unplot(korb, 4)
        led.unplot(korb + 1, 4)
        korb = korb + 1
        led.plot(korb, 4)
        led.plot(korb + 1, 4)
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
    led.plot(korb + 1, 4)
    if (stern_y == 4) {
        if (stern_x == korb || stern_x == korb + 1) {
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

Ist das Spiel jetzt zu leicht? In der Werkstatt macht ihr es wieder schwerer.

## Bonus: Riesenkorb

Der Korb wird drei Lampen breit. Fahren, Rand und Fangen funktionieren weiter.

<details>
<summary>Tipps anzeigen</summary>

- Die dritte Lampe steht bei `korb + 2`.
- Ihr ändert wieder dieselben drei Stellen: das Zeichnen, den rechten Rand und das Fangen.
- Am rechten Rand darf die äußerste Lampe höchstens bei x = 4 stehen. Wie groß darf `korb` dann sein?

:::bloecke

- Beim Fangen braucht ihr drei Vergleiche. Ein **oder**-Block passt in ein Feld eines anderen **oder**-Blocks.

:::

:::python

- Beim Fangen braucht ihr drei Vergleiche. `or` dürft ihr mehrmals in eine Zeile schreiben.

:::

:::javascript

- Beim Fangen braucht ihr drei Vergleiche. `||` dürft ihr mehrmals in eine Zeile schreiben.

:::

</details>
