# Werkstatt: Euer Spiel, eure Regeln

Euer Spiel läuft. Jetzt macht ihr es zu eurem Spiel. Hier gibt es keine fertigen Programme mehr, nur Aufträge und Tipps. Die Sterne zeigen, wie knifflig ein Auftrag ist: ⭐ geht schnell, ⭐⭐⭐ braucht Ausdauer.

Ein gelöster Auftrag reicht für den Abschluss.

## Auftrag 1: Treffer-Ton ⭐

Fängt der Korb einen Stern, spielt der micro:bit einen kurzen Ton.

:::bloecke

Töne findet ihr unter **Musik**. Der Ton kommt dorthin, wo `punkte` größer wird.

:::

:::python

```python
import music

music.pitch(880, 100)
```

`music.pitch(880, 100)` spielt einen hohen Ton für 100 Millisekunden.

:::

:::javascript

```javascript
music.playTone(880, music.beat(BeatFraction.Eighth))
```

Das spielt einen hohen, kurzen Ton.

:::

## Auftrag 2: Immer schneller ⭐⭐

<img src="/microbit/sterne/schneller.svg" alt="Dreimal dasselbe Bild vom Spiel, darunter die Pausen 400, 300 und 200 Millisekunden: Mit jeder Stufe fällt der Stern schneller">

Mit jedem Punkt fällt der Stern ein bisschen schneller. Wie viele Sterne schafft ihr dann noch?

- Die Wartezeit wird eine Variable, zum Beispiel `tempo`. Setzt sie in **beim Start** auf 400.
- Bei jedem Punkt wird `tempo` um 50 kleiner, aber nur, **wenn** `tempo` noch größer als 100 ist. So wird es nie zu schnell.
- Nach „daneben“ setzt ihr `tempo` wieder auf 400.

:::bloecke

Statt **pausiere (ms) 400** steht dann **pausiere (ms) tempo**.

:::

:::python

In Python ist das Tempo die 8 in `if takt == 8:`. Mit `if takt >= tempo:` und einer Variable `tempo` wird der Stern schneller, wenn `tempo` kleiner wird.

:::

:::javascript

Statt `basic.pause(400)` steht dann `basic.pause(tempo)`.

:::

## Auftrag 3: Rekord ⭐⭐

Der micro:bit merkt sich die meisten Punkte, die jemand geschafft hat. Ist eine Runde besser, zeigt er zuerst ein Symbol und dann den neuen Rekord.

- Ihr braucht eine Variable `rekord`, die am Anfang 0 ist.
- Bei „daneben“ vergleicht ihr: Ist `punkte` größer als `rekord`? Dann zeigt ihr das Symbol und setzt `rekord` auf `punkte`.
- Vergleicht, **bevor** `punkte` wieder auf 0 gesetzt wird. Sonst ist `punkte` schon 0, und es gibt nie einen Rekord.

:::bloecke

Ein Symbol zeigt **zeige Symbol** unter **Grundlagen**.

:::

:::python

Ein Symbol zeigt zum Beispiel `display.show(Image.HAPPY)`.

:::

:::javascript

Ein Symbol zeigt zum Beispiel `basic.showIcon(IconNames.Happy)`.

:::

## Auftrag 4: Steuern durch Neigen ⭐⭐

<img src="/microbit/sterne/neigen.svg" alt="Ein schräg gehaltener micro:bit: Wird er nach links geneigt, fährt der Korb nach links">

Statt mit den Knöpfen steuert ihr den Korb, indem ihr den micro:bit nach links oder rechts neigt.

- Am Rand darf der Korb auch jetzt nicht verschwinden.

:::bloecke

Unter **Eingabe** gibt es **wenn geschüttelt**. Im Feld könnt ihr statt „geschüttelt“ auch **nach links neigen** und **nach rechts neigen** wählen.

:::

:::python

`accelerometer.was_gesture('left')` fragt: Wurde der micro:bit seit dem letzten Fragen nach links geneigt? Für rechts heißt es `'right'`.

:::

:::javascript

```javascript
input.onGesture(Gesture.TiltLeft, function () {
    // ...
})
```

Für rechts heißt es `Gesture.TiltRight`.

:::

## Auftrag 5: Achtung, Bombe! ⭐⭐⭐

<img src="/microbit/sterne/bombe.svg" alt="Neben dem hellen Stern fällt eine schwach leuchtende Bombe. Lenkt man den Korb unter die Bombe und fängt sie, ist das Spiel vorbei">

Neben dem Stern fällt eine Bombe. Sie leuchtet nur schwach. Fängt der Korb die Bombe, ist das Spiel vorbei.

- Die Bombe braucht eigene Variablen: `bombe_x` und `bombe_y`.
- Sie fällt genauso wie der Stern. Kopiert vom Stern: das Setzen am Anfang, das Löschen der alten Bombe, das Fallen (`bombe_y` um 1 größer, über 4 wieder oben mit zufälligem `bombe_x`) und das Zeichnen. Ändert dabei die Namen. Bei Blöcken kopiert ihr mit einem Rechtsklick auf einen Block und **Duplizieren**.
- Gefangen ist die Bombe, wenn `bombe_y` 4 ist und `bombe_x` gleich `korb`. „Spiel vorbei“ heißt: Der micro:bit zeigt die Punkte, und alles fängt von vorn an – wie bei „daneben“.
- Startet die Bombe ein paar Reihen über dem Spielfeld (zum Beispiel bei y = -3), fallen Stern und Bombe nicht im Gleichschritt. Mit Blöcken und JavaScript zeigt der micro:bit oberhalb des Spielfelds einfach nichts an, in Python zeichnet ihr nur, wenn y von 0 bis 4 geht (siehe unten).

:::bloecke

Schwach zeichnet ihr mit **Zeichne x y Helligkeit** unter **LED**, zum Beispiel mit Helligkeit 30.

:::

:::python

Schwach zeichnet ihr mit einer kleinen Helligkeit: `display.set_pixel(bombe_x, bombe_y, 2)`. Aber Achtung: Python zeichnet nur, wenn y von 0 bis 4 geht.

:::

:::javascript

Schwach zeichnet ihr mit `led.plotBrightness(bombe_x, bombe_y, 30)`.

:::

## Auftrag 6: Eure eigene Idee

Zwei Sterne gleichzeitig? Ein goldener Stern, der drei Punkte bringt? Ein Duell mit zwei micro:bits per Funk? Schreibt eure Idee zuerst als Plan in Worten auf und zeigt sie eurer Kursleitung.

## Bonus: Zwei Aufträge in einem Programm

Verbindet zwei Aufträge zu einem Spiel, zum Beispiel „Immer schneller“ mit „Rekord“. Lasst ein anderes Team spielen: Wer knackt den Rekord?

<details>
<summary>Tipps anzeigen</summary>

- Speichert zuerst das Programm mit dem ersten Auftrag, damit ihr zu ihm zurückkehren könnt. In MakeCode klickt ihr unten neben dem Projektnamen auf das Speichern-Symbol, dann liegt eine .hex-Datei in **Downloads**. In Python klickt ihr auf **Speichern**.
- Baut den zweiten Auftrag dann Schritt für Schritt dazu und probiert nach jedem Schritt aus.

</details>
