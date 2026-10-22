# Stufe 2: Der Stern fällt

<img src="/microbit/sterne/stufe-2.svg" alt="Sechs Bilder: Der Stern fällt in Spalte 3 von y 0 bis y 4 nach unten, der Korb steht unten. Danach erscheint oben links ein neuer Stern">

Der Stern braucht zwei Variablen: `stern_x` für die Spalte und `stern_y` für die Reihe. Fallen heißt: `stern_y` wird immer wieder um 1 größer.

## Der Stern fällt

Euer Programm aus Stufe 1 bleibt. Neu dazu kommt:

:::bloecke

```bloecke
[grundlagen] beim Start
  [variablen] setze korb auf 2
  [variablen] setze stern_x auf 2
  [variablen] setze stern_y auf 0
  [led] Zeichne x korb y 4
[grundlagen] dauerhaft
  [led] lösche x stern_x y stern_y
  [variablen] ändere stern_y um 1
  [led] Zeichne x stern_x y stern_y
  [led] Zeichne x korb y 4
  [grundlagen] pausiere (ms) 400
```

Fällt der Stern in den Korb, löscht **lösche** auch den Korb. Darum wird der Korb danach neu gezeichnet.

:::

:::python

```python
from microbit import *

korb = 2
stern_x = 2
stern_y = 0
takt = 0

while True:
    if button_a.was_pressed() and korb > 0:
        korb = korb - 1
    if button_b.was_pressed() and korb < 4:
        korb = korb + 1

    takt = takt + 1
    if takt == 8:
        takt = 0
        stern_y = stern_y + 1

    display.clear()
    display.set_pixel(stern_x, stern_y, 9)
    display.set_pixel(korb, 4, 9)
    sleep(50)
```

Die Schleife läuft alle 50 Millisekunden, damit der Korb schnell reagiert. Der Stern fällt nur bei jedem 8. Mal: Dafür zählt `takt` mit.

:::

:::javascript

```javascript
let stern_x = 2
let stern_y = 0

basic.forever(function () {
    led.unplot(stern_x, stern_y)
    stern_y = stern_y + 1
    led.plot(stern_x, stern_y)
    led.plot(korb, 4)
    basic.pause(400)
})
```

Fällt der Stern in den Korb, löscht `led.unplot` auch den Korb. Darum wird der Korb danach neu gezeichnet.

:::

Probiert es aus. Der Stern fällt, aber nur einmal. Unten bei y = 5 gibt es keine Lampe mehr.

## Der nächste Stern

Ist `stern_y` größer als 4, fängt der Stern wieder oben an: `stern_y` wird 0. Baut das selbst ein. Wo im Programm muss es stehen: vor oder nach dem Zeichnen?

Danach soll jeder neue Stern in einer **zufälligen** Spalte starten.

:::bloecke

Den Zufall findet ihr unter **Mathematik**:

```bloecke
[mathematik] wähle eine zufällige Zahl von 0 bis 4
```

:::

:::python

Für den Zufall schreibt ihr oben `import random`. Dann gibt `random.randint(0, 4)` eine zufällige Zahl von 0 bis 4.

:::

:::javascript

`randint(0, 4)` gibt eine zufällige Zahl von 0 bis 4.

:::

<details>
<summary>Lösung anzeigen</summary>

:::bloecke

```bloecke
[grundlagen] dauerhaft
  [led] lösche x stern_x y stern_y
  [variablen] ändere stern_y um 1
  [logik] wenn stern_y > 4 dann
    [variablen] setze stern_y auf 0
    [variablen] setze stern_x auf wähle eine zufällige Zahl von 0 bis 4
  [led] Zeichne x stern_x y stern_y
  [led] Zeichne x korb y 4
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

    display.clear()
    display.set_pixel(stern_x, stern_y, 9)
    display.set_pixel(korb, 4, 9)
    sleep(50)
```

:::

:::javascript

```javascript
basic.forever(function () {
    led.unplot(stern_x, stern_y)
    stern_y = stern_y + 1
    if (stern_y > 4) {
        stern_y = 0
        stern_x = randint(0, 4)
    }
    led.plot(stern_x, stern_y)
    led.plot(korb, 4)
    basic.pause(400)
})
```

:::

</details>

## Bonus: Sternschnuppe

Der Stern zieht einen schwachen Schweif hinter sich her: Über dem Stern leuchtet eine Lampe nur ein bisschen.

<details>
<summary>Tipps anzeigen</summary>

- Der Schweif sitzt eine Reihe über dem Stern, also bei `stern_y - 1`. Ganz oben (y = 0) gibt es keinen Schweif.
- Am einfachsten: Bei jedem Schritt erst die ganze Anzeige löschen, dann Schweif, Stern und Korb neu zeichnen.

:::bloecke

Unter **LED** gibt es **Zeichne x y Helligkeit**. 255 ist ganz hell, 30 nur ein Glimmen. Die ganze Anzeige löscht **Bildschirminhalt löschen** unter **Grundlagen** (unter **… mehr**).

:::

:::python

Die letzte Zahl von `display.set_pixel` ist die Helligkeit: 9 ist ganz hell, 2 nur ein Glimmen.

:::

:::javascript

`led.plotBrightness(x, y, 30)` zeichnet einen Punkt mit wenig Helligkeit. 255 ist ganz hell. `basic.clearScreen()` löscht die ganze Anzeige.

:::

</details>
