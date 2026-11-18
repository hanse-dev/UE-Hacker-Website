# Startklar: Editor und Spieler

Euer Spiel entsteht in **MakeCode Arcade**. Das ist ein kostenloser Editor, der im Browser läuft. Links im Editor sitzt ein kleiner Spiele-Bildschirm, der **Simulator**. Dort läuft euer Spiel, sobald ihr etwas ändert.

## Editor öffnen

1. Öffnet <a href="https://arcade.makecode.com" target="_blank" rel="noopener">arcade.makecode.com</a> in einem neuen Tab.
2. Ist alles auf Englisch? Klickt oben rechts auf das Zahnrad, dann auf **Language** und wählt **Deutsch**.
3. Klickt auf **Neues Projekt**, nennt es „Ausweichen“ und klickt auf **Erstelle**.

:::bloecke

Ihr seht jetzt die **Blöcke**. Wenn oben in der Mitte nicht **Blöcke** ausgewählt ist, klickt darauf. Links stehen die Kategorien wie **Sprites** oder **Schleifen**, in der Mitte baut ihr euer Programm.

:::

:::python

Oben in der Mitte schaltet ihr die Ansicht um. Neben **JavaScript** ist ein kleiner Pfeil, dort findet ihr **Python**. Im Code steht danach noch nichts, das ist richtig so.

:::

:::javascript

Oben in der Mitte schaltet ihr die Ansicht um: Klickt auf **JavaScript**. Im Code steht danach noch nichts, das ist richtig so.

:::

**Speichern müsst ihr meistens nicht.** Der Editor merkt sich euer Projekt im Browser. Auf der Startseite (das Haus oben links) findet ihr es unter **Meine Projekte** wieder. An einem anderen Computer ist es aber nicht da. Was ihr an einem Schulcomputer tut, steht unten bei **Plan B**.

## Der Bildschirm

<img src="/arcade/ausweichen/bildschirm.svg" alt="Der Arcade-Bildschirm ist 160 Punkte breit und 120 hoch. Links oben ist x 0 und y 0. Der Spieler steht unten in der Mitte bei x 80 und y 108. Ein Stein fällt nach unten, dabei wird y größer">

Jeder Punkt auf dem Bildschirm hat zwei Zahlen: **x** sagt, wie weit rechts er liegt, **y**, wie weit unten. Ganz links oben ist x 0 und y 0. Der Bildschirm ist 160 Punkte breit und 120 hoch. Unten in der Mitte liegt also ungefähr bei x 80 und y 108.

## Der Spieler

Euer Spieler ist ein **Sprite**, so heißen in Arcade alle Figuren. Ein Sprite hat ein Bild und eine Position.

:::bloecke

```bloecke
[schleifen] beim Start
  [sprites] setze mySprite auf Sprite [Bild] vom Typ Player
  [sprites] setze Position von mySprite auf x 80 y 108
```

**beim Start** steht schon da. Unter **Sprites** findet ihr **setze mySprite auf Sprite … vom Typ Player**. Zieht ihn in **beim Start**. Klickt dann auf das graue Feld im Block: Es öffnet sich der Bild-Editor. Malt euren Spieler (ein Raumschiff, ein Auto, ein Tier …) und klickt auf **Fertig**.

**setze Position von mySprite auf x … y …** findet ihr auch unter **Sprites**. Tragt 80 und 108 ein.

:::

:::python

```python
spieler = sprites.create(img("""
    . . . 8 8 . . .
    . . 8 9 9 8 . .
    . . 8 9 9 8 . .
    . 8 8 8 8 8 8 .
    8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8
    . 2 . . . . 2 .
    . 2 . . . . 2 .
"""), SpriteKind.player)
spieler.set_position(80, 108)
```

Schreibt den Code in das leere Feld. Eine `import`-Zeile braucht ihr in Arcade nicht.

Das Bild steht zwischen den drei Anführungszeichen. Jedes Zeichen ist ein Punkt: `.` ist durchsichtig, die Ziffern und Buchstaben sind Farben (`8` blau, `9` hellblau, `2` rot). Tippt es genau so ab, mit den Leerzeichen. Danach könnt ihr Zeichen austauschen und so eigene Farben nehmen. Bequemer geht es mit dem Bild-Editor: Klickt im Code auf das kleine Bild-Symbol neben `img`.

Alle Farben: `1` weiß, `2` rot, `3` rosa, `4` orange, `5` gelb, `6` türkis, `7` grün, `8` blau, `9` hellblau, `a` lila, `b` grau, `c` dunkelviolett, `d` beige, `e` braun, `f` schwarz.

:::

:::javascript

```javascript
let spieler = sprites.create(img`
    . . . 8 8 . . .
    . . 8 9 9 8 . .
    . . 8 9 9 8 . .
    . 8 8 8 8 8 8 .
    8 8 8 8 8 8 8 8
    8 8 8 8 8 8 8 8
    . 2 . . . . 2 .
    . 2 . . . . 2 .
`, SpriteKind.Player)
spieler.setPosition(80, 108)
```

Schreibt den Code in das leere Feld.

Das Bild steht zwischen den beiden Backticks ` hinter `img`. Das ist kein normaler Schrägstrich, sondern ein eigenes Zeichen. Jedes Zeichen ist ein Punkt: `.` ist durchsichtig, die Ziffern und Buchstaben sind Farben (`8` blau, `9` hellblau, `2` rot). Tippt es genau so ab, mit den Leerzeichen. Danach könnt ihr Zeichen austauschen und so eigene Farben nehmen. Bequemer geht es mit dem Bild-Editor: Klickt im Code auf das kleine Bild-Symbol neben `img`. Den Backtick ` bekommt ihr so: Umschalttaste festhalten, die Taste rechts neben ß drücken, dann die Leertaste.

Alle Farben: `1` weiß, `2` rot, `3` rosa, `4` orange, `5` gelb, `6` türkis, `7` grün, `8` blau, `9` hellblau, `a` lila, `b` grau, `c` dunkelviolett, `d` beige, `e` braun, `f` schwarz.

:::

Schaut in den Simulator: Steht euer Spieler unten in der Mitte? Probiert auch andere Zahlen für x und y aus und beobachtet, wohin er wandert.

## Bonus: Hintergrund

Der Bildschirm bekommt eine eigene Farbe, zum Beispiel einen hellblauen Himmel.

:::bloecke

```bloecke
[szene] setze Hintergrundfarbe auf [Farbe]
```

Der Block liegt unter **Szene**. Steckt ihn in **beim Start** und klickt auf das Farbfeld.

:::

:::python

```python
scene.set_background_color(9)
```

Schreibt die Zeile ganz unten dazu. Die Zahl ist eine Farbe, wie bei den Bildern: `9` ist hellblau. Probiert auch andere Zahlen von 1 bis 15.

:::

:::javascript

```javascript
scene.setBackgroundColor(9)
```

Schreibt die Zeile ganz unten dazu. Die Zahl ist eine Farbe, wie bei den Bildern: `9` ist hellblau. Probiert auch andere Zahlen von 1 bis 15.

:::

## Plan B: Das Projekt ist weg

Manche Schulcomputer löschen beim Abmelden alles, was der Browser sich gemerkt hat. Dann ist auch euer Projekt weg. Am Schulcomputer sichert ihr es deshalb am Ende jeder Stunde: Klickt unten neben dem Projektnamen auf das Disketten-Symbol (**Speichern**). Ihr bekommt eine Datei, die wie ein Bild aussieht. In ihr steckt euer ganzes Programm. Sie landet im Ordner **Downloads**; nehmt sie zum Beispiel auf einem USB-Stick mit. Nächstes Mal zieht ihr diese Datei mit der Maus in das Fenster des Editors, und euer Projekt ist wieder da.
