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

`music.pitch(880, 100)` spielt einen hohen Ton für 100 Millisekunden. `import music` kommt oben zu den anderen `import`-Zeilen, der Ton direkt unter `punkte = punkte + 1`.

:::

:::javascript

```javascript
music.playTone(880, music.beat(BeatFraction.Eighth))
```

Das spielt einen hohen, kurzen Ton. Schreibt die Zeile direkt unter `punkte = punkte + 1`.

:::

## Auftrag 2: Immer schneller ⭐⭐

<img src="/microbit/sterne/schneller.svg" alt="Dreimal dasselbe Bild vom Spiel, darunter die Pausen 400, 300 und 200 Millisekunden: Mit jeder Stufe fällt der Stern schneller">

Mit jedem Punkt fällt der Stern ein bisschen schneller. Wie viele Sterne schafft ihr dann noch?

:::bloecke

- Die Wartezeit wird eine Variable, zum Beispiel `tempo`. Setzt sie in **beim Start** auf 400.
- Bei jedem Punkt wird `tempo` um 50 kleiner, aber nur, **wenn** `tempo` noch größer als 100 ist. So wird es nie zu schnell.
- Nach „daneben“ setzt ihr `tempo` wieder auf 400.

Statt **pausiere (ms) 400** steht dann **pausiere (ms) tempo**.

:::

:::python

In Python ist das Tempo die 8 in `if takt == 8:`. Der Stern fällt nach 8 Runden der Schleife. Mit weniger Runden fällt er schneller.

- Schreibt oben zu den anderen Variablen `tempo = 8`.
- Statt `if takt == 8:` steht dann `if takt >= tempo:`.
- Bei jedem Punkt wird `tempo` um 1 kleiner, aber nur, **wenn** `tempo` noch größer als 2 ist. So wird es nie zu schnell.
- Nach „daneben“ setzt ihr `tempo` wieder auf 8.

:::

:::javascript

- Schreibt oben zu den anderen Variablen `let tempo = 400`.
- Statt `basic.pause(400)` steht dann `basic.pause(tempo)`.
- Bei jedem Punkt wird `tempo` um 50 kleiner, aber nur, **wenn** `tempo` noch größer als 100 ist. So wird es nie zu schnell.
- Nach „daneben“ setzt ihr `tempo` wieder auf 400.

:::

## Auftrag 3: Rekord ⭐⭐

Der micro:bit merkt sich die meisten Punkte, die jemand geschafft hat. Ist eine Runde besser, zeigt er zuerst ein Symbol und dann den neuen Rekord.

- Ihr braucht eine Variable `rekord`, die am Anfang 0 ist.
- Bei „daneben“ passiert dann der Reihe nach:
  1. Ist `punkte` größer als `rekord`? Dann zeigt ihr das Symbol und setzt `rekord` auf `punkte`.
  2. Der micro:bit zeigt die Punkte, wie bisher.
  3. `punkte` wird wieder 0.
- Vergleicht also, **bevor** `punkte` wieder auf 0 gesetzt wird. Sonst ist `punkte` schon 0, und es gibt nie einen Rekord.

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

`accelerometer.was_gesture('left')` fragt: Wurde der micro:bit seit dem letzten Fragen nach links geneigt? Für rechts heißt es `'right'`. Nehmt es statt `button_a.was_pressed()` und `button_b.was_pressed()`.

:::

:::javascript

```javascript
input.onGesture(Gesture.TiltLeft, function () {
    // ...
})
```

Für rechts heißt es `Gesture.TiltRight`. Kopiert den Inhalt von Knopf A an die Stelle von `// ...`, für rechts den von Knopf B. Die Knopf-Teile dürfen bleiben, dann geht beides.

:::

## Auftrag 5: Achtung, Bombe! ⭐⭐⭐

<img src="/microbit/sterne/bombe.svg" alt="Neben dem hellen Stern fällt eine schwach leuchtende Bombe. Lenkt man den Korb unter die Bombe und fängt sie, ist das Spiel vorbei">

Neben dem Stern fällt eine Bombe. Sie leuchtet nur schwach. Fängt der Korb die Bombe, ist das Spiel vorbei.

- Die Bombe braucht eigene Variablen: `bombe_x` und `bombe_y`.
- Gefangen ist die Bombe, wenn `bombe_y` 4 ist und `bombe_x` gleich `korb`. „Spiel vorbei“ heißt: Der micro:bit zeigt die Punkte, und alles fängt von vorn an – wie bei „daneben“.
- Startet die Bombe ein paar Reihen über dem Spielfeld, zum Beispiel bei y = -3. Dann fallen Stern und Bombe nicht im Gleichschritt. Unten angekommen, fängt sie wie der Stern wieder bei y = 0 an.

:::bloecke

- Die Bombe fällt genauso wie der Stern. Kopiert vom Stern: das Setzen in **beim Start**, das Löschen der alten Bombe, das Fallen (`bombe_y` um 1 größer, über 4 wieder oben mit zufälligem `bombe_x`) und das Zeichnen. Ändert dabei die Namen. Ihr kopiert mit einem Rechtsklick auf einen Block und **Duplizieren**.
- Oberhalb des Spielfelds (y kleiner als 0) zeigt der micro:bit einfach nichts an. Das ist in Ordnung.
- Schwach zeichnet ihr mit **Zeichne x y Helligkeit** unter **LED**, zum Beispiel mit Helligkeit 30.

:::

:::python

Die Bombe fällt genauso wie der Stern. Kopiert die Zeilen vom Stern und ändert die Namen:

- Oben bei den Variablen: `bombe_x = random.randint(0, 4)` und `bombe_y = -3`.
- Im Teil, in dem der Stern fällt: `bombe_y` wird um 1 größer, und über 4 fängt sie mit zufälligem `bombe_x` wieder oben an.
- Beim Zeichnen, unter `display.clear()`: Python zeichnet nur, wenn y von 0 bis 4 geht. Darum fragt ihr vorher:

```python
    if bombe_y >= 0:
        display.set_pixel(bombe_x, bombe_y, 2)
```

Die 2 ist eine kleine Helligkeit, so leuchtet die Bombe nur schwach.

:::

:::javascript

- Die Bombe fällt genauso wie der Stern. Kopiert vom Stern: `let bombe_x` und `let bombe_y` oben, `led.unplot` für die alte Bombe, das Fallen (`bombe_y` um 1 größer, über 4 wieder oben mit zufälligem `bombe_x`) und das Zeichnen. Ändert dabei die Namen.
- Oberhalb des Spielfelds (y kleiner als 0) zeigt der micro:bit einfach nichts an. Das ist in Ordnung.
- Schwach zeichnet ihr mit `led.plotBrightness(bombe_x, bombe_y, 30)`.

:::

## Auftrag 6: Eure eigene Idee

Zwei Sterne gleichzeitig? Ein goldener Stern, der drei Punkte bringt? Ein Duell mit zwei micro:bits per Funk? Schreibt eure Idee zuerst als Plan in Worten auf und zeigt sie eurer Kursleitung.

## Bonus: Zwei Aufträge in einem Programm

Verbindet zwei Aufträge zu einem Spiel, zum Beispiel „Immer schneller“ mit „Rekord“. Lasst ein anderes Team spielen: Wer knackt den Rekord?

<details>
<summary>Tipps anzeigen</summary>

- Speichert zuerst das Programm mit dem ersten Auftrag, damit ihr zu ihm zurückkehren könnt.

:::bloecke

- Klickt unten neben dem Projektnamen auf das Speichern-Symbol, dann liegt eine .hex-Datei in **Downloads**. Wieder öffnen könnt ihr sie, indem ihr sie auf den Editor zieht.

:::

:::python

- Klickt auf **Speichern**, dann liegt eine .hex-Datei in **Downloads**. Wieder öffnen könnt ihr sie mit **Öffnen** neben **Speichern**.

:::

:::javascript

- Klickt unten neben dem Projektnamen auf das Speichern-Symbol, dann liegt eine .hex-Datei in **Downloads**. Wieder öffnen könnt ihr sie, indem ihr sie auf den Editor zieht.

:::

- Baut den zweiten Auftrag dann Schritt für Schritt dazu und probiert nach jedem Schritt aus.

</details>
