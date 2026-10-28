# Werkstatt: Euer Spiel, eure Regeln

Euer Spiel mit dem breiten Korb läuft. Jetzt macht ihr es zu eurem Spiel. Hier gibt es keine fertigen Programme mehr, nur Aufträge und Tipps. Die Sterne zeigen, wie knifflig ein Auftrag ist: ⭐ geht schnell, ⭐⭐⭐ braucht Ausdauer.

Ein gelöster Auftrag reicht für den Abschluss.

Kommt ihr nicht weiter, klappt den **Plan** unter einem Auftrag auf. Er sagt in Worten, was euer Programm Schritt für Schritt machen soll. In Blöcke oder Code übersetzt ihr ihn selbst.

## Auftrag 1: Treffer-Ton ⭐

Fängt der Korb einen Stern, spielt der micro:bit einen kurzen Ton.

:::bloecke

Unter **Musik** nehmt ihr **spiele Note … für …**. Klickt auf die Note und wählt eine hohe, als Dauer passt 1/8 Takt. Der Ton kommt dorthin, wo `punkte` größer wird.

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

<details>
<summary>Plan anzeigen</summary>

**Wenn der Korb den Stern fängt:**

1. `punkte` wird um 1 größer. Das habt ihr schon.
2. Neu: Der micro:bit spielt einen kurzen, hohen Ton.

</details>

## Auftrag 2: Immer schneller ⭐⭐

<img src="/microbit/sterne/schneller.svg" alt="Dreimal dasselbe Bild vom Spiel, darunter die Pausen 400, 350 und 300 Millisekunden: Mit jeder Stufe fällt der Stern schneller">

Mit jedem Punkt fällt der Stern ein bisschen schneller. Wie viele Sterne schafft ihr dann noch?

:::bloecke

- Die Wartezeit wird eine Variable, zum Beispiel `tempo`. Setzt sie in **beim Start** auf 400.
- Bei jedem Punkt wird `tempo` um 50 kleiner, aber nur, **wenn** `tempo` noch größer als 100 ist. So wird es nie zu schnell.
- Nach „daneben“ setzt ihr `tempo` wieder auf 400.

Statt **pausiere (ms) 400** steht dann **pausiere (ms) tempo**.

:::

:::python

In Python ist das Tempo die 8 in `if takt == 8:`. Der Stern fällt nach 8 Runden der Schleife, 8 Runden mal 50 Millisekunden sind die 400 Millisekunden aus dem Bild. Mit weniger Runden fällt er schneller: 7 Runden sind 350 Millisekunden.

- Schreibt oben zu den anderen Variablen `tempo = 8`.
- Statt `if takt == 8:` steht dann `if takt >= tempo:`. `>=` heißt „größer oder gleich“. Mit `==` könnte der Stern hängen bleiben: Ist `takt` schon 7 und `tempo` wird 6, ist `takt` nie mehr genau 6.
- Bei jedem Punkt wird `tempo` um 1 kleiner, aber nur, **wenn** `tempo` noch größer als 2 ist. So wird es nie zu schnell. Das neue `if` steht direkt unter `punkte = punkte + 1`, genauso weit eingerückt. Die Zeile darin rückt ihr 4 Leerzeichen weiter ein.
- Nach „daneben“ setzt ihr `tempo` wieder auf 8.

:::

:::javascript

- Schreibt oben zu den anderen Variablen `let tempo = 400`.
- Statt `basic.pause(400)` steht dann `basic.pause(tempo)`.
- Bei jedem Punkt wird `tempo` um 50 kleiner, aber nur, **wenn** `tempo` noch größer als 100 ist. So wird es nie zu schnell.
- Nach „daneben“ setzt ihr `tempo` wieder auf 400.

:::

<details>
<summary>Plan anzeigen</summary>

**Am Anfang:**

1. `tempo` bekommt seinen Startwert.

**Beim Fallen:**

1. Wie schnell der Stern fällt, bestimmt jetzt `tempo` und nicht mehr eine feste Zahl.

**Wenn der Korb den Stern fängt:**

1. `punkte` wird um 1 größer.
2. Ist `tempo` noch größer als die Grenze? Dann wird `tempo` um einen Schritt kleiner. Sonst bleibt es, wie es ist.

**Wenn der Stern daneben fällt:**

1. Der micro:bit zeigt die Punkte, und `punkte` wird 0. Das habt ihr schon.
2. `tempo` bekommt wieder seinen Startwert.

Habt ihr drei Leben eingebaut? Dann bekommt `tempo` erst wieder seinen Startwert, wenn das letzte Leben weg ist.

Startwert, Schritt und Grenze stehen oben bei den Tipps.

</details>

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

Ein Symbol zeigt zum Beispiel `display.show(Image.HAPPY)`. Schreibt danach `sleep(1000)`, sonst läuft sofort die Zahl durch, und ihr seht das Symbol kaum.

:::

:::javascript

Ein Symbol zeigt zum Beispiel `basic.showIcon(IconNames.Happy)`.

:::

<details>
<summary>Plan anzeigen</summary>

**Am Anfang:**

1. `rekord` wird 0.

**Wenn der Stern daneben fällt:**

1. Ist `punkte` größer als `rekord`? Dann:
   - Der micro:bit zeigt das Symbol.
   - `rekord` wird so groß wie `punkte`.
2. Der micro:bit zeigt die Punkte.
3. `punkte` wird 0.

Habt ihr drei Leben eingebaut? Dann passiert das alles erst, wenn das letzte Leben weg ist.

</details>

## Auftrag 4: Steuern durch Neigen ⭐⭐

<img src="/microbit/sterne/neigen.svg" alt="Ein schräg gehaltener micro:bit: Wird er nach links geneigt, fährt der Korb nach links">

Statt mit den Knöpfen steuert ihr den Korb, indem ihr den micro:bit nach links oder rechts neigt. Jedes Neigen schiebt den Korb um ein Feld. Haltet den micro:bit danach wieder gerade.

- Am Rand darf der Korb auch jetzt nicht verschwinden.

:::bloecke

Unter **Eingabe** gibt es **wenn geschüttelt**. Im Feld könnt ihr statt „geschüttelt“ auch **nach links neigen** und **nach rechts neigen** wählen. Den Inhalt von Knopf A müsst ihr nicht neu bauen: Rechtsklick auf den wenn-Block darin, dann **Duplizieren**, und die Kopie in den Neigen-Block ziehen.

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

<details>
<summary>Plan anzeigen</summary>

**Wenn der micro:bit nach links geneigt wird:**

1. Ist `korb` größer als 0? Dann fährt der Korb ein Feld nach links, genau wie bei Knopf A.

**Wenn der micro:bit nach rechts geneigt wird:**

1. Ist `korb` kleiner als 3? Dann fährt der Korb ein Feld nach rechts, genau wie bei Knopf B.

</details>

## Auftrag 5: Achtung, Bombe! ⭐⭐⭐

<img src="/microbit/sterne/bombe.svg" alt="Neben dem hellen Stern fällt eine schwach leuchtende Bombe. Lenkt man den Korb unter die Bombe und fängt sie, ist das Spiel vorbei">

Neben dem Stern fällt eine Bombe. Sie leuchtet nur schwach. Fängt der Korb die Bombe, ist das Spiel vorbei.

- Die Bombe braucht eigene Variablen: `bombe_x` und `bombe_y`.
- Gefangen ist die Bombe, wenn `bombe_y` 4 ist und `bombe_x` gleich `korb` oder `korb + 1`. „Spiel vorbei“ heißt: Der micro:bit zeigt die Punkte, und alles fängt von vorn an – wie bei „daneben“.
- Fällt die Bombe daneben, passiert nichts. Kopiert also nicht den Teil für „daneben“ vom Stern.
- Startet die Bombe ein paar Reihen über dem Spielfeld, zum Beispiel bei y = -3. Dann fallen Stern und Bombe nicht im Gleichschritt. Unten angekommen, fängt sie wie der Stern wieder bei y = 0 an.

:::bloecke

- Die Bombe fällt genauso wie der Stern. Kopiert vom Stern: das Setzen in **beim Start**, das Löschen der alten Bombe, das Fallen (`bombe_y` um 1 größer, über 4 wieder oben mit zufälligem `bombe_x`) und das Zeichnen. Ändert dabei die Namen. Ihr kopiert mit einem Rechtsklick auf einen Block und **Duplizieren**.
- Oberhalb des Spielfelds (y kleiner als 0) zeigt der micro:bit einfach nichts an. Das ist in Ordnung.
- Schwach zeichnet ihr mit **Zeichne x y Helligkeit** unter **LED**, zum Beispiel mit Helligkeit 30.
- Die Bombe zeichnet ihr nur, wenn `bombe_y` ≥ 0 ist. ≥ heißt „größer oder gleich“, ihr wählt es im Vergleich aus.

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

`>=` heißt „größer oder gleich“. Die 2 ist eine kleine Helligkeit, so leuchtet die Bombe nur schwach. Löschen müsst ihr die alte Bombe nicht, das macht `display.clear()` schon.

:::

:::javascript

- Die Bombe fällt genauso wie der Stern. Kopiert vom Stern: `let bombe_x` und `let bombe_y` oben, `led.unplot` für die alte Bombe, das Fallen (`bombe_y` um 1 größer, über 4 wieder oben mit zufälligem `bombe_x`) und das Zeichnen. Ändert dabei die Namen.
- Oberhalb des Spielfelds (y kleiner als 0) zeigt der micro:bit einfach nichts an. Das ist in Ordnung.
- Schwach zeichnet ihr mit `led.plotBrightness(bombe_x, bombe_y, 30)`.
- „0 oder größer“ schreibt ihr `bombe_y >= 0`. `>=` heißt „größer oder gleich“.

:::

<details>
<summary>Plan anzeigen</summary>

**Am Anfang:**

1. `bombe_x` wird eine zufällige Zahl von 0 bis 4.
2. `bombe_y` wird -3.

Die Bomben-Teile kommen jeweils direkt unter die passenden Teile vom Stern: Löschen unter Löschen, Fallen unter Fallen, Zeichnen unter Zeichnen. Der Korb wird zuletzt gezeichnet.

**Beim Fallen, an derselben Stelle wie beim Stern:**

1. Löscht euer Programm den alten Stern einzeln? Dann löscht es die Bombe genauso an ihrer alten Stelle.
2. `bombe_y` wird um 1 größer.
3. Ist `bombe_y` größer als 4? Dann wird `bombe_y` 0, und `bombe_x` wird eine neue zufällige Zahl von 0 bis 4.

**Beim Prüfen, direkt unter der Prüfung, ob der Stern gefangen ist:**

1. Ist `bombe_y` 4? Dann:
   - Ist `bombe_x` gleich `korb` oder gleich `korb + 1`? Dann ist das Spiel vorbei. Es passiert dasselbe wie bei „daneben“: Der micro:bit zeigt die Punkte, `punkte` wird 0, und die Anzeige wird wieder leer.
   - Fällt die Bombe daneben, passiert nichts. Für die Bombe gibt es keinen Teil „daneben“.

Habt ihr drei Leben eingebaut? Bei der Bombe ist sofort Schluss, und `leben` wird wieder 3.

**Beim Zeichnen:**

1. Ist `bombe_y` 0 oder größer? Dann wird die Bombe schwach gezeichnet.

</details>

## Auftrag 6: Eure eigene Idee

Zwei Sterne gleichzeitig? Ein goldener Stern, der drei Punkte bringt? Ein Duell mit zwei micro:bits per Funk? Schreibt eure Idee zuerst als Plan in Worten auf, so wie die Pläne oben, und zeigt sie eurer Kursleitung.

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
