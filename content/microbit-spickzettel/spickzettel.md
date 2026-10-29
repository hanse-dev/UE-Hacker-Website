# micro:bit-Spickzettel

Hier schlagt ihr nach, wenn euch in einem micro:bit-Kurs ein Wort neu ist. Oben wählt ihr, ob ihr die Beispiele als Blöcke, in Python oder in JavaScript sehen wollt.

Inhalt: [Knöpfe](#knoepfe) · [Warten](#warten) · [Variable](#variable) · [Schleife](#schleife) · [Bedingung](#bedingung) · [Ansonsten](#ansonsten) · [Mehrere Fälle](#mehrere-faelle) · [Vergleich](#vergleich) · [Und, oder](#und-oder) · [Zufall](#zufall) · [Funktion](#funktion) · [Parameter](#parameter) · [Pins](#pins) · [Funk](#funk) · [Kommentar](#kommentar) · [Einrückung](#einrueckung)

## Knöpfe

Euer Programm kann merken, wenn jemand Knopf A oder Knopf B drückt. Dann macht es etwas, zum Beispiel ein Herz zeigen.

:::bloecke

```bloecke
[eingabe] wenn Knopf A geklickt
  [grundlagen] zeige Symbol Herz
```

Den Block **wenn Knopf A geklickt** findet ihr unter **Eingabe**. Er steht frei auf der Fläche, nicht in **beim Start**. Alles darin passiert jedes Mal, wenn jemand den Knopf drückt. Für Knopf B klickt ihr auf das A und wählt B.

:::

:::python

```python
from microbit import *

while True:
    if button_a.was_pressed():
        display.show(Image.HEART)
```

`button_a.was_pressed()` fragt: Wurde Knopf A seit dem letzten Fragen gedrückt? Die Frage steht in der Schleife `while True:`, so wird immer wieder gefragt. Knopf B heißt `button_b`.

:::

:::javascript

```javascript
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Heart)
})
```

Alles in den geschweiften Klammern passiert jedes Mal, wenn jemand Knopf A drückt. Für Knopf B schreibt ihr `Button.B`.

:::

## Warten

Der micro:bit ist sehr schnell. Damit ihr etwas sehen könnt, lasst ihr ihn warten. Die Zeit gebt ihr in Millisekunden an: 1000 Millisekunden sind 1 Sekunde, 500 sind eine halbe.

:::bloecke

```bloecke
[grundlagen] pausiere (ms) 1000
```

Den Block **pausiere (ms)** findet ihr unter **Grundlagen**. Klickt auf die Zahl, um eine andere einzutippen.

:::

:::python

```python
sleep(1000)
```

`sleep(1000)` wartet 1000 Millisekunden, also eine Sekunde.

:::

:::javascript

```javascript
basic.pause(1000)
```

`basic.pause(1000)` wartet 1000 Millisekunden, also eine Sekunde.

:::

## Variable

Eine Variable ist wie eine beschriftete Schachtel. Unter ihrem Namen merkt sich das Programm einen Wert, zum Beispiel eine Zahl. Den Wert könnt ihr später ändern. Hier zählt die Variable `punkte`, wie oft Knopf A gedrückt wurde.

:::bloecke

```bloecke
[grundlagen] beim Start
  [variablen] setze punkte auf 0
[eingabe] wenn Knopf A geklickt
  [variablen] ändere punkte um 1
  [grundlagen] zeige Zahl punkte
```

Unter **Variablen** klickt ihr auf **Erstelle eine Variable** und gebt ihr einen Namen. Danach liegen dort **setze … auf** und **ändere … um**. Den runden Block mit dem Namen zieht ihr überall hin, wo sonst eine Zahl steht. Kleiner wird die Zahl mit einer Zahl mit Minus davor, zum Beispiel **ändere punkte um -1**.

:::

:::python

```python
from microbit import *

punkte = 0

while True:
    if button_a.was_pressed():
        punkte = punkte + 1
        display.scroll(punkte)
```

`punkte = 0` legt die Variable an und gibt ihr den Wert 0. `punkte = punkte + 1` heißt: Nimm den alten Wert, zähl 1 dazu und merk dir das Ergebnis.

:::

:::javascript

```javascript
let punkte = 0

input.onButtonPressed(Button.A, function () {
    punkte = punkte + 1
    basic.showNumber(punkte)
})
```

`let` legt die Variable an, nur beim ersten Mal. Danach schreibt ihr nur noch den Namen. `punkte = punkte + 1` heißt: Nimm den alten Wert, zähl 1 dazu und merk dir das Ergebnis.

:::

## Schleife

Eine Schleife wiederholt Befehle. Es gibt zwei Arten:

- Eine **Endlosschleife** hört nie auf. Ein Blinklicht blinkt zum Beispiel immer weiter.
- Eine **Zählschleife** läuft so oft, wie ihr sagt, zum Beispiel dreimal.

### Endlosschleife

:::bloecke

```bloecke
[grundlagen] dauerhaft
  [grundlagen] zeige Symbol Herz
  [grundlagen] pausiere (ms) 500
  [grundlagen] Bildschirminhalt löschen
  [grundlagen] pausiere (ms) 500
```

Alles im Block **dauerhaft** wiederholt sich immer wieder. Ihr findet ihn unter **Grundlagen**.

:::

:::python

```python
from microbit import *

while True:
    display.show(Image.HEART)
    sleep(500)
    display.clear()
    sleep(500)
```

Alles, was unter `while True:` eingerückt ist, wiederholt sich immer wieder.

:::

:::javascript

```javascript
basic.forever(function () {
    basic.showIcon(IconNames.Heart)
    basic.pause(500)
    basic.clearScreen()
    basic.pause(500)
})
```

Alles in den geschweiften Klammern von `basic.forever` wiederholt sich immer wieder.

:::

### Zählschleife

:::bloecke

```bloecke
[grundlagen] beim Start
  [schleifen] 3-mal wiederholen
    [grundlagen] zeige Symbol Herz
    [grundlagen] pausiere (ms) 500
    [grundlagen] Bildschirminhalt löschen
    [grundlagen] pausiere (ms) 500
```

Unter **Schleifen** gibt es den Block **4-mal wiederholen**. Klickt auf die Zahl, um sie zu ändern. Alles, was in ihm steckt, läuft so oft hintereinander, wie die Zahl sagt.

:::

:::python

```python
from microbit import *

for i in range(3):
    display.show(Image.HEART)
    sleep(500)
    display.clear()
    sleep(500)
```

Alles, was unter `for i in range(3):` eingerückt ist, passiert dreimal. Die 3 sagt, wie oft. `i` und `range` müsst ihr nicht verstehen.

:::

:::javascript

```javascript
for (let i = 0; i < 3; i++) {
    basic.showIcon(IconNames.Heart)
    basic.pause(500)
    basic.clearScreen()
    basic.pause(500)
}
```

Alles in den geschweiften Klammern passiert dreimal. Die 3 sagt, wie oft.

:::

## Bedingung

Mit einer Bedingung trifft euer Programm eine Entscheidung: Nur wenn etwas stimmt, laufen die Befehle darin. Sonst werden sie übersprungen. Hier zeigt der micro:bit erst ab 5 Punkten ein fröhliches Gesicht.

:::bloecke

```bloecke
[grundlagen] beim Start
  [variablen] setze punkte auf 0
[eingabe] wenn Knopf A geklickt
  [variablen] ändere punkte um 1
  [logik] wenn punkte > 4 dann
    [grundlagen] zeige Symbol Fröhlich
```

Den Block **wenn … dann** findet ihr unter **Logik**. In das Feld hinter **wenn** steckt ihr einen [Vergleich](#vergleich), zum Beispiel **punkte > 4**. Ein wenn-Block darf auch in einem anderen stecken.

:::

:::python

```python
from microbit import *

punkte = 0

while True:
    if button_a.was_pressed():
        punkte = punkte + 1
        if punkte > 4:
            display.show(Image.HAPPY)
```

`if` heißt „wenn“. Hinter die Bedingung kommt ein Doppelpunkt. Was darunter weiter eingerückt ist, läuft nur, wenn die Bedingung stimmt.

:::

:::javascript

```javascript
let punkte = 0

input.onButtonPressed(Button.A, function () {
    punkte = punkte + 1
    if (punkte > 4) {
        basic.showIcon(IconNames.Happy)
    }
})
```

`if` heißt „wenn“. Die Bedingung steht in runden Klammern, die Befehle dahinter in geschweiften.

:::

## Ansonsten

Mit „ansonsten“ bekommt eine Entscheidung einen zweiten Weg: Stimmt die Bedingung, läuft der erste Teil, sonst der zweite. Einer von beiden läuft also immer.

:::bloecke

```bloecke
[eingabe] wenn Knopf A geklickt
  [logik] wenn punkte > 4 dann
    [grundlagen] zeige Symbol Fröhlich
  [logik] ansonsten
    [grundlagen] zeige Symbol Traurig
```

Unter **Logik** gibt es den Block **wenn … dann … ansonsten**. Ihr könnt auch unten an einem wenn-Block auf das **Plus** klicken, dann kommt ein **ansonsten** dazu.

:::

:::python

```python
if punkte > 4:
    display.show(Image.HAPPY)
else:
    display.show(Image.SAD)
```

„Ansonsten“ heißt in Python `else:`. Es steht genauso weit eingerückt wie sein `if`.

:::

:::javascript

```javascript
if (punkte > 4) {
    basic.showIcon(IconNames.Happy)
} else {
    basic.showIcon(IconNames.Sad)
}
```

„Ansonsten“ heißt in JavaScript `else`. Es kommt direkt hinter die Klammer `}` vom `if`.

:::

## Mehrere Fälle

Manchmal gibt es mehr als zwei Wege. Dann prüft das Programm die Fälle von oben nach unten und nimmt den ersten, der stimmt. Passt keiner, läuft der letzte Teil.

:::bloecke

```bloecke
[eingabe] wenn Knopf A geklickt
  [logik] wenn punkte = 0 dann
    [grundlagen] zeige Symbol Traurig
  [logik] sonst wenn punkte < 5 dann
    [grundlagen] zeige Symbol Herz
  [logik] ansonsten
    [grundlagen] zeige Symbol Fröhlich
```

Mit dem **+** unten am wenn-Block fügt ihr weitere Fälle hinzu. Klickt so oft, bis ihr genug **sonst wenn** habt.

:::

:::python

```python
if punkte == 0:
    display.show(Image.SAD)
elif punkte < 5:
    display.show(Image.HEART)
else:
    display.show(Image.HAPPY)
```

`elif` heißt „sonst, wenn“. `elif` und `else` stehen genau unter dem `if`, genauso weit eingerückt, und enden mit einem Doppelpunkt.

:::

:::javascript

```javascript
if (punkte == 0) {
    basic.showIcon(IconNames.Sad)
} else if (punkte < 5) {
    basic.showIcon(IconNames.Heart)
} else {
    basic.showIcon(IconNames.Happy)
}
```

`else if` heißt „sonst, wenn“. Es kommt wie `else` direkt hinter die Klammer `}`.

:::

## Vergleich

Ein Vergleich prüft zwei Werte, zum Beispiel: Ist `punkte` größer als 4? Die Antwort ist ja oder nein. Darum steckt ein Vergleich meistens in einer [Bedingung](#bedingung).

:::bloecke

Die Vergleiche findet ihr unter **Logik**. In der Mitte des Blocks steht ein Zeichen. Klickt darauf, um ein anderes zu wählen:

| Zeichen | heißt |
|---|---|
| **=** | ist gleich |
| **≠** | ist nicht gleich |
| **<** | ist kleiner als |
| **>** | ist größer als |
| **≤** | ist kleiner oder gleich |
| **≥** | ist größer oder gleich |

In die beiden Felder links und rechts zieht ihr eine Variable oder tippt eine Zahl.

:::

:::python

| Zeichen | heißt |
|---|---|
| `==` | ist gleich |
| `!=` | ist nicht gleich |
| `<` | ist kleiner als |
| `>` | ist größer als |
| `<=` | ist kleiner oder gleich |
| `>=` | ist größer oder gleich |

Achtung: Vergleichen heißt `==`, mit zwei Gleichheitszeichen. Ein einzelnes `=` setzt eine Variable.

:::

:::javascript

| Zeichen | heißt |
|---|---|
| `==` | ist gleich |
| `!=` | ist nicht gleich |
| `<` | ist kleiner als |
| `>` | ist größer als |
| `<=` | ist kleiner oder gleich |
| `>=` | ist größer oder gleich |

Achtung: Vergleichen heißt `==`, mit zwei Gleichheitszeichen. Ein einzelnes `=` setzt eine Variable.

:::

## Und, oder

Manchmal hängt eine Entscheidung an zwei Vergleichen:

- **und:** Beide müssen stimmen. Zum Beispiel: Der Abstand ist größer als 0 und kleiner als 15.
- **oder:** Einer reicht. Zum Beispiel: Der Stern ist in der linken oder in der rechten Spalte vom Korb.

:::bloecke

```bloecke
[logik] wenn abstand > 0 und abstand < 15 dann
  [grundlagen] zeige Symbol Herz
```

Die Blöcke **und** und **oder** findet ihr unter **Logik**. Steckt einen davon in das Feld hinter **wenn** und dann in jede Seite einen Vergleich. Jede Seite braucht einen ganzen Vergleich, zum Beispiel `stern_x = korb` oder `stern_x = korb + 1`. Nur `korb + 1` allein ist kein Vergleich.

:::

:::python

```python
if abstand > 0 and abstand < 15:
    display.show(Image.HEART)
```

„Und“ heißt in Python `and`, „oder“ heißt `or`. Jede Seite braucht einen ganzen Vergleich: `stern_x == korb or stern_x == korb + 1`.

:::

:::javascript

```javascript
if (abstand > 0 && abstand < 15) {
    basic.showIcon(IconNames.Heart)
}
```

„Und“ heißt in JavaScript `&&`, „oder“ heißt `||`. Jede Seite braucht einen ganzen Vergleich: `stern_x == korb || stern_x == korb + 1`. Einen Strich `|` tippt ihr unter Windows mit **AltGr** und der Taste **< >** links unten, am Mac mit **alt** und **7**.

:::

## Zufall

Der micro:bit kann würfeln: Er wählt eine zufällige Zahl zwischen zwei Grenzen. Auch die Grenzen selbst können dabei herauskommen. Hier zeigt er nach dem Schütteln eine Zahl von 1 bis 6.

:::bloecke

```bloecke
[eingabe] wenn geschüttelt
  [grundlagen] zeige Zahl wähle eine zufällige Zahl von 1 bis 6
```

Den Block **wähle eine zufällige Zahl von 0 bis 10** findet ihr unter **Mathematik**. Klickt auf die Zahlen, um sie zu ändern.

:::

:::python

```python
from microbit import *
import random

while True:
    if accelerometer.was_gesture('shake'):
        display.show(random.randint(1, 6))
```

Für den Zufall schreibt ihr oben `import random`. Dann gibt `random.randint(1, 6)` eine Zahl von 1 bis 6.

:::

:::javascript

```javascript
input.onGesture(Gesture.Shake, function () {
    basic.showNumber(randint(1, 6))
})
```

`randint(1, 6)` gibt eine Zahl von 1 bis 6.

:::

## Funktion

Eine Funktion ist ein Ablauf mit Namen, also ein eigener Befehl. Ihr baut ihn einmal und startet ihn dann mit seinem Namen, so oft ihr wollt. Das Starten heißt **Aufruf**. Hier blinkt das Herz nach Knopf A zweimal.

:::bloecke

```bloecke
[funktionen] Funktion blinken
  [grundlagen] zeige Symbol Herz
  [grundlagen] pausiere (ms) 300
  [grundlagen] Bildschirminhalt löschen
  [grundlagen] pausiere (ms) 300
[eingabe] wenn Knopf A geklickt
  [funktionen] Aufruf blinken
  [funktionen] Aufruf blinken
```

Klickt in der Blockliste auf **Fortgeschritten**, dann auf **Funktionen** und auf **Erstelle eine Funktion**. Gebt ihr einen Namen. In den Block **Funktion …** kommt der Ablauf. Unter **Funktionen** liegt dann ein Block **Aufruf …**: Den zieht ihr in euer Programm, nicht den Funktionsblock selbst.

:::

:::python

```python
from microbit import *


def blinken():
    display.show(Image.HEART)
    sleep(300)
    display.clear()
    sleep(300)


while True:
    if button_a.was_pressed():
        blinken()
        blinken()
```

Eine Funktion beginnt mit `def`, dann kommen der Name, Klammern und ein Doppelpunkt. Was darunter eingerückt ist, gehört zur Funktion. `blinken()` ruft sie auf. Die Funktion steht über `while True:` und ohne Einrückung.

:::

:::javascript

```javascript
function blinken() {
    basic.showIcon(IconNames.Heart)
    basic.pause(300)
    basic.clearScreen()
    basic.pause(300)
}

input.onButtonPressed(Button.A, function () {
    blinken()
    blinken()
})
```

Eine Funktion beginnt mit `function`, dann kommen der Name und Klammern. Was in den geschweiften Klammern steht, gehört zur Funktion. `blinken()` ruft sie auf.

:::

## Parameter

Ein Parameter ist ein Platzhalter in einer [Funktion](#funktion). Beim Aufruf gebt ihr für ihn einen Wert mit. So macht dieselbe Funktion mal dies, mal das. Hier zeigt die Funktion `zeigen` die Zahl, die sie beim Aufruf bekommt: erst 3, dann 2, dann 1.

:::bloecke

```bloecke
[funktionen] Funktion zeigen zahl
  [grundlagen] zeige Zahl zahl
  [grundlagen] pausiere (ms) 1000
[eingabe] wenn Knopf A geklickt
  [funktionen] Aufruf zeigen 3
  [funktionen] Aufruf zeigen 2
  [funktionen] Aufruf zeigen 1
```

Beim Erstellen der Funktion fügt ihr einen Parameter vom Typ **Zahl** hinzu und gebt ihm einen Namen. Im Funktionsblock zieht ihr den Parameter heraus in ein Zahlenfeld. Beim **Aufruf** tippt ihr dann die Zahl ein.

:::

:::python

```python
from microbit import *


def zeigen(zahl):
    display.show(zahl)
    sleep(1000)


while True:
    if button_a.was_pressed():
        zeigen(3)
        zeigen(2)
        zeigen(1)
```

In den Klammern hinter dem Namen steht der Parameter. `zeigen(3)` ruft die Funktion auf. Dann ist darin `zahl` 3.

:::

:::javascript

```javascript
function zeigen(zahl: number) {
    basic.showNumber(zahl)
    basic.pause(1000)
}

input.onButtonPressed(Button.A, function () {
    zeigen(3)
    zeigen(2)
    zeigen(1)
})
```

In den Klammern hinter dem Namen steht der Parameter. `: number` heißt: Er ist eine Zahl. `zeigen(3)` ruft die Funktion auf. Dann ist darin `zahl` 3.

:::

## Pins

Pins sind die Anschlüsse am micro:bit. Über sie schaltet er Lampen und andere Teile, die ihr mit Kabeln anschließt. Ein Pin kann zwei Zustände haben: 1 heißt Strom an, 0 heißt Strom aus. Hier blinkt eine Lampe an Pin P13. Wie ihr Lampen ansteckt, zeigt der Kurs [Die Ampelanlage](/kurs/projekt-microbit-ampel).

:::bloecke

```bloecke
[grundlagen] dauerhaft
  [pins] schreibe digitalen Wert von Pin P13 auf 1
  [grundlagen] pausiere (ms) 500
  [pins] schreibe digitalen Wert von Pin P13 auf 0
  [grundlagen] pausiere (ms) 500
```

Die Pin-Blöcke findet ihr in der Blockliste unter **Fortgeschritten** und dann **Pins**. Klickt im Block auf den Pin, um einen anderen zu wählen. Mit **schreibe analogen Wert von Pin** geht auch etwas zwischen an und aus: 0 ist aus, 1023 ist ganz an.

:::

:::python

```python
from microbit import *

while True:
    pin13.write_digital(1)
    sleep(500)
    pin13.write_digital(0)
    sleep(500)
```

`pin13.write_digital(1)` schaltet P13 an, `pin13.write_digital(0)` schaltet ihn aus. Mit `pin14.write_analog(500)` geht auch etwas zwischen an und aus: 0 ist aus, 1023 ist ganz an.

:::

:::javascript

```javascript
basic.forever(function () {
    pins.digitalWritePin(DigitalPin.P13, 1)
    basic.pause(500)
    pins.digitalWritePin(DigitalPin.P13, 0)
    basic.pause(500)
})
```

`pins.digitalWritePin(DigitalPin.P13, 1)` schaltet P13 an, mit `0` statt `1` geht er aus. Mit `pins.analogWritePin(AnalogPin.P14, 500)` geht auch etwas zwischen an und aus: 0 ist aus, 1023 ist ganz an.

:::

## Funk

Zwei micro:bits können sich per Funk kurze Nachrichten schicken. Damit sich die Teams im Raum nicht stören, gibt es Funkgruppen: Ein micro:bit hört nur Nachrichten aus seiner eigenen Gruppe. Sender und Empfänger brauchen also dieselbe Gruppennummer. In den Beispielen steht dafür ein x. Statt x setzt ihr eure Nummer ein, sonst läuft das Programm nicht.

Beide micro:bits bekommen dieses Programm. Drückt ein Team Knopf B, zeigt der micro:bit des anderen Teams ein Herz. Aufträge mit Funk gibt es im Kurs [Die Ampelanlage](/kurs/projekt-microbit-ampel), in der Werkstatt 2.

:::bloecke

```bloecke
[grundlagen] beim Start
  [funk] setze Funkgruppe auf x
[eingabe] wenn Knopf B geklickt
  [funk] sende Zeichenkette "hallo" über Funk
[funk] wenn Text empfangen receivedString
  [logik] wenn receivedString = "hallo" dann
    [grundlagen] zeige Symbol Herz
```

Die Funk-Blöcke findet ihr unter **Funk**. Den Vergleich mit Text findet ihr unter **Logik**. **receivedString** zieht ihr aus dem Block **wenn Text empfangen** heraus in den Vergleich.

:::

:::python

```python
from microbit import *
import radio

radio.on()
radio.config(group=x)

while True:
    if button_b.was_pressed():
        radio.send("hallo")
    nachricht = radio.receive()
    if nachricht == "hallo":
        display.show(Image.HEART)
```

`radio.on()` schaltet den Funk ein, `radio.config(group=x)` stellt die Gruppe ein. `radio.receive()` holt die nächste Nachricht ab. Ist keine da, bekommt ihr `None`.

:::

:::javascript

```javascript
radio.setGroup(x)

input.onButtonPressed(Button.B, function () {
    radio.sendString("hallo")
})

radio.onReceivedString(function (receivedString) {
    if (receivedString == "hallo") {
        basic.showIcon(IconNames.Heart)
    }
})
```

`radio.setGroup(x)` stellt die Gruppe ein. Alles in den geschweiften Klammern von `radio.onReceivedString` passiert, sobald eine Nachricht ankommt. In `receivedString` steht, was angekommen ist.

:::

## Kommentar

Ein Kommentar ist eine Notiz für Menschen. Der micro:bit überspringt ihn. Er hilft euch, später noch zu wissen, was ein Teil des Programms macht.

:::bloecke

Bei den Blöcken braucht ihr meistens keinen Kommentar: Die Beschriftung sagt schon, was ein Block tut.

:::

:::python

```python
# Phase 1: Rot
pin16.write_digital(1)
```

Alles hinter `#` ist ein Kommentar.

:::

:::javascript

```javascript
// Phase 1: Rot
pins.digitalWritePin(DigitalPin.P16, 1)
```

Alles hinter `//` ist ein Kommentar.

:::

## Einrückung

Befehle können in anderen stecken, zum Beispiel in einer Schleife oder einer Bedingung. Dann gehören sie dazu und laufen nur dort.

:::bloecke

Bei den Blöcken seht ihr das sofort: Ein Block, der in einem anderen steckt, gehört dazu. In den Anleitungen ist er dafür ein Stück nach rechts gerückt.

:::

:::python

```python
while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
    sleep(100)
```

In Python zeigt die Einrückung, was wozu gehört. Eingerückt heißt: Die Zeile fängt vier Leerzeichen weiter rechts an. Nach einem Doppelpunkt macht der Editor das meist von selbst, sonst drückt ihr die Tab-Taste.

Hier gehört `display.show` zum `if`: Es läuft nur nach Knopf A. `sleep(100)` gehört nur zur Schleife: Es läuft jedes Mal.

:::

:::javascript

```javascript
basic.forever(function () {
    if (input.buttonIsPressed(Button.A)) {
        basic.showIcon(IconNames.Happy)
    }
    basic.pause(100)
})
```

In JavaScript zeigen die geschweiften Klammern `{ }`, was wozu gehört. Eingerückt wird, damit ihr es leichter lesen könnt. Die Klammern tippt ihr unter Windows mit **AltGr** und **7** bzw. **0**, am Mac mit **alt** und **8** bzw. **9**.

Hier gehört `basic.showIcon` zum `if`: Es läuft nur, wenn Knopf A gedrückt ist. `basic.pause(100)` gehört nur zur Schleife: Es läuft jedes Mal.

:::
