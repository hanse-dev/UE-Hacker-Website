# Werkstatt 1: Licht und Anzeige

Eure Ampelanlage läuft. Jetzt macht ihr sie besser. Hier gibt es keine fertigen Programme mehr, nur Aufträge und Hinweise. Sucht euch aus, was euch reizt. Die Sterne zeigen, wie knifflig ein Auftrag ist: ⭐ geht schnell, ⭐⭐ braucht etwas mehr Nachdenken.

Ein gelöster Auftrag reicht für den Abschluss. Ist danach noch Zeit, nehmt ihr den nächsten.

## Auftrag 1: Der Countdown ⭐

Haben die Fußgänger Grün, zählt die LED-Anzeige die Sekunden herunter: 5, 4, 3, 2, 1. Danach wird die Anzeige dunkel und die Fußgängerampel rot.

Hinweis: Der Countdown ersetzt die 5 Sekunden Pause. Jede Zahl bleibt eine Sekunde stehen.

:::bloecke

Legt unter **Variablen** eine Variable `zeit` an. Diese Blöcke braucht ihr:

```bloecke
[variablen] setze zeit auf 5
[schleifen] 5-mal wiederholen
[grundlagen] zeige Zahl zeit
[variablen] ändere zeit um -1
```

:::

:::python

Eine Zählschleife kann auch rückwärts zählen. `range(5, 0, -1)` zählt 5, 4, 3, 2, 1:

```python
for zahl in range(5, 0, -1):
    display.show(zahl)
```

:::

:::javascript

Eine Zählschleife kann auch rückwärts zählen. Diese zählt 5, 4, 3, 2, 1:

```javascript
for (let zahl = 5; zahl > 0; zahl--) {
    basic.showNumber(zahl)
}
```

:::

## Auftrag 2: Das Ampelmännchen ⭐

Die LED-Anzeige wird zur zweiten Fußgängerampel: Bei Rot zeigt sie ein stehendes Männchen, bei Grün ein gehendes. Die Männchen malt ihr selbst.

Hinweis: Zeichnet beide Männchen zuerst auf kariertes Papier, 5 mal 5 Kästchen groß. Beim stehenden Männchen hängen die Arme herunter, beim gehenden sind die Beine gespreizt.

:::bloecke

Mit dem Block **zeige LEDs** aus **Grundlagen** malt ihr ein Bild: Ein Klick auf ein Kästchen schaltet die Lampe an oder aus.

:::

:::python

Ein eigenes Bild schreibt ihr als fünf Zeilen mit je fünf Ziffern. `0` ist aus, `9` ist ganz hell:

```python
stehend = Image("00900:"
                "09990:"
                "00900:"
                "00000:"
                "00000")
display.show(stehend)
```

Das ist erst der Kopf mit den Schultern. Den Rest malt ihr.

:::

:::javascript

Ein eigenes Bild malt ihr mit `basic.showLeds`. `#` ist an, `.` ist aus:

```javascript
basic.showLeds(`
    . . # . .
    . # # # .
    . . # . .
    . . . . .
    . . . . .
    `)
```

Das ist erst der Kopf mit den Schultern. Den Rest malt ihr.

:::

## Auftrag 3: Der Bahnübergang ⭐

Mit Knopf B meldet ihr: Ein Zug kommt! Die Autoampel schaltet über Gelb auf Rot. Dann blinken die beiden roten LEDs (Auto und Fußgänger) abwechselnd, zehnmal hin und her, wie das Warnlicht an einem Bahnübergang. Danach haben die Autos wieder Grün.

Hinweis: Abwechselnd heißt: Die eine geht an, wenn die andere ausgeht. Das passiert in einem einzigen Schritt, dann wird gewartet.

:::bloecke

Den Block **wenn Knopf A geklickt** könnt ihr ein zweites Mal hinlegen und dort **B** auswählen. Zum Wiederholen gibt es **4-mal wiederholen** unter **Schleifen**.

:::

:::python

Knopf B fragt ihr genauso ab wie Knopf A: `button_b.was_pressed()`. Zum Wiederholen gibt es `for i in range(10):`.

:::

:::javascript

Knopf B fragt ihr genauso ab wie Knopf A: `input.onButtonPressed(Button.B, function () { ... })`. Zum Wiederholen gibt es `for (let i = 0; i < 10; i++) { ... }`.

:::

## Auftrag 4: Der Nachtmodus ⭐⭐

Nachts sind kaum Autos unterwegs. Viele Ampeln schalten dann ab, nur das gelbe Licht der Autoampel blinkt. Eure Ampel soll selbst merken, wann es dunkel ist.

Der micro:bit kann Helligkeit messen, und zwar mit seiner LED-Anzeige. Er liefert eine Zahl von 0 (ganz dunkel) bis 255 (ganz hell).

Hinweis: Lasst euch die Helligkeit zuerst ein paar Sekunden lang anzeigen. Haltet dann eine Hand über die Anzeige. Welche Zahl ist bei euch normal, welche bei Nacht? Dazwischen liegt eure Grenze.

:::bloecke

```bloecke
[grundlagen] dauerhaft
  [grundlagen] zeige Zahl Lichtstärke
```

**Lichtstärke** findet ihr unter **Eingabe**. Für die Entscheidung braucht ihr **wenn … dann … ansonsten** aus **Logik** und den Vergleich **<**.

:::

:::python

```python
while True:
    display.scroll(display.read_light_level())
```

Für die Entscheidung braucht ihr `if`, `else` und den Vergleich `<`.

:::

:::javascript

```javascript
basic.forever(function () {
    basic.showNumber(input.lightLevel())
})
```

Für die Entscheidung braucht ihr `if`, `else` und den Vergleich `<`.

:::

Fangt mit einem neuen, kleinen Programm an, das nur Tag und Nacht kennt: Am Tag haben die Autos Grün, nachts blinkt Gelb. Wer mag, baut den Nachtmodus danach in die Ampelanlage ein.

## Auftrag 5: Die Glühlampen-Ampel ⭐⭐

Alte Ampeln hatten Glühlampen. Die gingen nicht schlagartig an, sondern wurden in einem kurzen Moment heller und beim Ausschalten langsam dunkel. Baut eure Autoampel aus Stufe 2 so um, dass jede Lampe sanft auf- und abblendet.

Bisher konnte ein Pin nur 0 oder 1. Mit einem **analogen Wert** von 0 bis 1023 bestimmt ihr die Helligkeit. Dabei schaltet der micro:bit die LED in Wirklichkeit tausende Male pro Sekunde an und aus. Ist sie länger an als aus, sieht sie für euer Auge heller aus.

Hinweis: Ein sanftes Aufblenden sind viele kleine Schritte: etwas heller, kurz warten, etwas heller, kurz warten. Probiert 20 Schritte mit je 50 mehr und 20 Millisekunden Pause.

:::bloecke

```bloecke
[pins] schreibe analogen Wert von Pin P14 auf 500
```

P14 ist die grüne LED der Autoampel. Für analoge Werte wählt ihr den Pin direkt aus, die Variable `auto_gruen` passt in diesen Block nicht. Statt 500 könnt ihr eine Variable einsetzen, zum Beispiel `hell`. Mit **ändere hell um 50** aus **Variablen** wird sie Schritt für Schritt größer.

:::

:::python

```python
auto_gruen.write_analog(500)
```

Mit `range` könnt ihr in Schritten zählen: `range(0, 1024, 50)` zählt 0, 50, 100 und so weiter bis 1000.

:::

:::javascript

```javascript
pins.analogWritePin(AnalogPin.P14, 500)
```

P14 ist die grüne LED der Autoampel. Für analoge Werte schreibt ihr den Pin direkt hin, die Variable `auto_gruen` passt hier nicht. In Schritten zählt ihr so: `for (let hell = 0; hell <= 1000; hell += 50)`.

:::

## Auftrag 6: Der echte Ampeldrücker ⭐⭐

An einer echten Ampel drückt man einen dicken Knopf, nicht einen winzigen am micro:bit. Baut einen Taster auf das Breadboard, der die Ampelanlage startet. Fragt eure Kursleitung nach einem Taster.

<img src="/microbit/ampel/taster.svg" alt="Steckplan Taster: Taster mit Beinchen in Reihe 15 und 17 rechts, Kabel von P20 in Reihe 15, Brücke von Reihe 17 in die GND-Reihe 14">

1. Zieht das USB-Kabel ab.
2. Steckt den Taster rechts von der Lücke ein: zwei Beinchen in Reihe 15, zwei in Reihe 17.
3. **Kabel von P20** in Reihe 15 rechts. P20 ist der Stift direkt neben den beiden GND-Stiften.
4. **Brücke** von Reihe 17 rechts in die GND-Reihe 14.

Drückt ihr den Taster, verbindet er den Pin mit GND. Das liest der micro:bit als 0. Lasst ihr los, hängt der Pin in der Luft und könnte zufällige Werte lesen. Darum stellt ihr den Pin so ein, dass er ohne Druck sicher 1 liest. Das nennt man **Pull-up**. Bei diesem Taster heißt also: **0 = gedrückt, 1 = nicht gedrückt.**

Testet den Taster zuerst mit diesem Programm. Ohne Druck muss die Anzeige 1 zeigen, mit Druck 0.

:::bloecke

```bloecke
[grundlagen] beim Start
  [pins] ziehe den Pin P20 auf nach oben
[grundlagen] dauerhaft
  [grundlagen] zeige Zahl digitale Werte von Pin P20
```

:::

:::python

```python
from microbit import *

pin20.set_pull(pin20.PULL_UP)

while True:
    display.show(pin20.read_digital())
```

:::

:::javascript

```javascript
pins.setPull(DigitalPin.P20, PinPullMode.PullUp)

basic.forever(function () {
    basic.showNumber(pins.digitalReadPin(DigitalPin.P20))
})
```

:::

Zeigt die Anzeige immer 0, auch ohne Druck? Dann sind die Beinchen innen schon verbunden. Zieht das USB-Kabel ab und dreht den Taster um eine Vierteldrehung. Die Kabel kommen dann in die neuen Reihen der Beinchen, eines oben, eines unten.

Hinweis: In der Ampelanlage prüft ihr den Taster immer wieder. Ist er gedrückt, läuft derselbe Ablauf wie bei Knopf A.

:::bloecke

Ihr braucht **dauerhaft**, **wenn … dann** aus **Logik** und den Vergleich **=**. Denkt daran: gedrückt ist **0**.

:::

:::python

Ihr fragt in der Schleife zusätzlich `pin20.read_digital() == 0` ab. Mit `or` klappen Knopf A und Taster gleichzeitig.

:::

:::javascript

Steckt den Ablauf in `basic.forever` und fragt dort `input.buttonIsPressed(Button.A) || pins.digitalReadPin(DigitalPin.P20) == 0` ab. `||` heißt oder, damit klappen Knopf A und Taster gleichzeitig.

:::

## Bonus: Zwei Aufträge in einem Programm

Verbindet zwei Aufträge zu einer Ampelanlage, zum Beispiel Countdown und Ampelmännchen oder Nachtmodus und Taster.

<details>
<summary>Tipps anzeigen</summary>

- Schreibt zuerst auf, was eure Anlage am Ende alles können soll, und in welcher Reihenfolge.
- Baut nicht alles auf einmal ein. Fügt einen Auftrag hinzu, testet, und erst dann den nächsten.

:::bloecke

Laufen zwei Blöcke gleichzeitig, zum Beispiel **dauerhaft** und **wenn Knopf A geklickt**, können sie sich die LEDs gegenseitig umschalten. Steckt dann alles in einen einzigen **dauerhaft**-Block und fragt den Knopf mit **Knopf A ist geklickt** aus **Eingabe** ab.

:::

:::python

In Python läuft alles in einer Schleife nacheinander. Achtet darauf, dass jeder Teil eurer Anlage in dieser einen Schleife drankommt.

:::

:::javascript

Laufen `basic.forever` und `input.onButtonPressed` gleichzeitig, können sie sich die LEDs gegenseitig umschalten. Steckt dann alles in ein einziges `basic.forever` und fragt den Knopf mit `input.buttonIsPressed(Button.A)` ab.

:::

</details>
