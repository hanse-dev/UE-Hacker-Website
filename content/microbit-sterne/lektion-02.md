# Stufe 1: Der Korb

<img src="/microbit/sterne/stufe-1.svg" alt="Vier Bilder: Der Korb startet unten bei x 2. Nach Knopf A steht er bei x 1, nach noch einmal A bei x 0, nach Knopf B wieder bei x 1">

Der Korb merkt sich seine Spalte in einer **Variable** namens `korb`. Am Anfang ist `korb` 2, also die Mitte. Knopf A macht `korb` um 1 kleiner, Knopf B um 1 größer.

## Knopf A

:::bloecke

```bloecke
[grundlagen] beim Start
  [variablen] setze korb auf 2
  [led] Zeichne x korb y 4
[eingabe] wenn Knopf A geklickt
  [led] lösche x korb y 4
  [variablen] ändere korb um -1
  [led] Zeichne x korb y 4
```

Die Variable legt ihr unter **Variablen** mit **Erstelle eine Variable** an. Danach liegt dort ein runder Block `korb`: Zieht ihn in das Feld hinter **x**, statt eine Zahl zu tippen. **ändere `korb` um** findet ihr auch unter **Variablen**, für -1 tippt ihr ins Zahlenfeld -1. **lösche** macht den alten Punkt aus, bevor der Korb weiterfährt.

:::

:::python

```python
from microbit import *

korb = 2

while True:
    if button_a.was_pressed():
        korb = korb - 1
    display.clear()
    display.set_pixel(korb, 4, 9)
    sleep(50)
```

Die Schleife fragt immer wieder: Wurde Knopf A gedrückt? Dann löscht sie die Anzeige und zeichnet den Korb neu.

:::

:::javascript

```javascript
let korb = 2
led.plot(korb, 4)

input.onButtonPressed(Button.A, function () {
    led.unplot(korb, 4)
    korb = korb - 1
    led.plot(korb, 4)
})
```

`led.unplot` macht den alten Punkt aus, bevor der Korb weiterfährt.

:::

Probiert es aus. Dann baut ihr Knopf B selbst: Er schiebt den Korb nach rechts.

## Problem am Rand

<img src="/microbit/sterne/rand.svg" alt="Der Korb steht ganz links bei x 0. Nach Knopf A wäre x minus 1: Der Korb ist weg. Richtig wäre: Der Korb bleibt bei x 0 stehen">

Drückt ein paar Mal A. Der Korb verschwindet, denn x = -1 gibt es nicht.

:::bloecke

Der Korb darf nur fahren, **wenn** noch Platz ist. Den Block **wenn … dann** findet ihr unter **Logik**, den Vergleich **0 < 0** auch. Steckt den Vergleich in das Feld hinter **wenn**, zieht `korb` in das linke Feld, klickt auf **<** und wählt **>**. Ins rechte Feld kommt 0.

```bloecke
[eingabe] wenn Knopf A geklickt
  [logik] wenn korb > 0 dann
    [led] lösche x korb y 4
    [variablen] ändere korb um -1
    [led] Zeichne x korb y 4
```

:::

:::python

In Python läuft sogar eine Fehlermeldung über die Anzeige. Der Korb darf nur fahren, wenn noch Platz ist:

```python
    if button_a.was_pressed() and korb > 0:
        korb = korb - 1
```

:::

:::javascript

Der Korb darf nur fahren, wenn noch Platz ist:

```javascript
input.onButtonPressed(Button.A, function () {
    if (korb > 0) {
        led.unplot(korb, 4)
        korb = korb - 1
        led.plot(korb, 4)
    }
})
```

:::

Und am rechten Rand? Welche Zahl ist dort die Grenze?

<details>
<summary>Lösung anzeigen</summary>

:::bloecke

```bloecke
[grundlagen] beim Start
  [variablen] setze korb auf 2
  [led] Zeichne x korb y 4
[eingabe] wenn Knopf A geklickt
  [logik] wenn korb > 0 dann
    [led] lösche x korb y 4
    [variablen] ändere korb um -1
    [led] Zeichne x korb y 4
[eingabe] wenn Knopf B geklickt
  [logik] wenn korb < 4 dann
    [led] lösche x korb y 4
    [variablen] ändere korb um 1
    [led] Zeichne x korb y 4
```

:::

:::python

```python
from microbit import *

korb = 2

while True:
    if button_a.was_pressed() and korb > 0:
        korb = korb - 1
    if button_b.was_pressed() and korb < 4:
        korb = korb + 1
    display.clear()
    display.set_pixel(korb, 4, 9)
    sleep(50)
```

:::

:::javascript

```javascript
let korb = 2
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
```

:::

</details>

## Bonus: Durch die Wand

Fährt der Korb links hinaus, kommt er rechts wieder herein. Und umgekehrt.

<details>
<summary>Tipps anzeigen</summary>

- Statt stehen zu bleiben, springt der Korb: Bei x = 0 und Knopf A wird `korb` zu 4.
- Ihr braucht dafür ein **ansonsten**: Wenn noch Platz ist, fährt der Korb, ansonsten springt er. Unter **Logik** gibt es den Block **wenn … dann … ansonsten**.
- In den ansonsten-Teil kommen drei Blöcke: den Korb löschen, `korb` auf 4 setzen, den Korb neu zeichnen.

</details>
