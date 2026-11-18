# Stufe 4: Punkte und Tempo

Euer Spiel funktioniert schon. Aber wer hat besser gespielt? Jetzt gibt es Punkte: einen für jede Sekunde, die ihr überlebt. Und damit es nicht langweilig wird, fallen die Steine mit der Zeit immer schneller.

## Ein Punkt pro Sekunde

:::bloecke

```bloecke
[spiel] wenn Spielupdate alle 1000 ms
  [info] ändere Punktzahl um 1
```

Nehmt einen zweiten Block **wenn Spielupdate alle 500 ms** unter **Spiel** und stellt 1000 ms ein (eine Sekunde). **ändere Punktzahl um 1** liegt unter **Info**.

:::

:::python

```python
def jede_sekunde():
    info.change_score_by(1)
game.on_update_interval(1000, jede_sekunde)
```

Eine zweite Funktion, diesmal jede Sekunde (1000 ms). Sie kommt ganz unten in euer Programm.

:::

:::javascript

```javascript
game.onUpdateInterval(1000, function () {
    info.changeScoreBy(1)
})
```

Ein zweites `game.onUpdateInterval`, diesmal jede Sekunde (1000 ms). Es kommt ganz unten in euer Programm.

:::

Oben rechts im Simulator zählen jetzt die Punkte. Ist das Spiel vorbei, zeigt Arcade eure Punkte und den bisherigen Rekord.

## Immer schneller

Bisher fallen alle Steine mit 50. Jetzt soll die Geschwindigkeit wachsen. Dafür braucht ihr eine **Variable**: einen Speicherplatz mit Namen, dessen Wert sich ändern kann. Sie heißt `tempo`, beginnt bei 50 und wird jede Sekunde um 5 größer. Jeder neue Stein fällt dann mit dem aktuellen `tempo`.

:::bloecke

```bloecke
[schleifen] beim Start
  [variablen] setze tempo auf 50
[spiel] wenn Spielupdate alle 1000 ms
  [info] ändere Punktzahl um 1
  [variablen] ändere tempo um 5
[spiel] wenn Spielupdate alle 500 ms
  [sprites] setze projectile auf Projektil [Bild] von der Seite mit vx 0 vy tempo
```

Unter **Variablen** klickt ihr auf **Erstelle eine Variable...** und nennt sie `tempo`. Danach liegen dort **setze tempo auf 0** und **ändere tempo um 1**. Den ersten steckt ihr in **beim Start** und tragt 50 ein, den zweiten in den Block für jede Sekunde und tragt 5 ein.

Zum Schluss zieht ihr den runden Block `tempo` aus **Variablen** in das Feld hinter **vy**, statt der 50. Steckt dort noch ein Zufallsblock aus dem Bonus von Stufe 2? Zieht ihn heraus und links auf die Kategorien, dann ist er gelöscht.

:::

:::python

```python
tempo = 50
```

Schreibt sie direkt unter `info.set_life(3)`. In `neuer_stein` ersetzt ihr die 50 hinter dem Bild durch `tempo`. Steht dort aus dem Bonus von Stufe 2 `randint(30, 90)`, ersetzt ihr das auch durch `tempo`.

Dann wächst `tempo` jede Sekunde. Schreibt `jede_sekunde` nicht noch einmal, sondern ergänzt eure Funktion von oben: Neu sind die Zeilen `global tempo` und `tempo = tempo + 5`.

```python
def jede_sekunde():
    global tempo
    info.change_score_by(1)
    tempo = tempo + 5
game.on_update_interval(1000, jede_sekunde)
```

Wichtig ist `global tempo`. Ohne diese Zeile würde Python in der Funktion eine neue, eigene Variable `tempo` anlegen, und euer `tempo` oben bliebe immer 50.

:::

:::javascript

```javascript
let tempo = 50
```

Schreibt sie direkt unter `info.setLife(3)`. Beim Stein ersetzt ihr die 50 hinter dem Bild durch `tempo`. Steht dort aus dem Bonus von Stufe 2 `randint(30, 90)`, ersetzt ihr das auch durch `tempo`.

Dann wächst `tempo` jede Sekunde. Schreibt keinen zweiten Sekunden-Teil, sondern ergänzt euren von oben: Neu ist nur die Zeile `tempo = tempo + 5`.

```javascript
game.onUpdateInterval(1000, function () {
    info.changeScoreBy(1)
    tempo = tempo + 5
})
```

:::

Spielt eine Runde. Am Anfang ist es leicht, nach einer halben Minute wird es richtig hektisch. Wie viele Punkte schafft ihr?

<details>
<summary>Lösung anzeigen</summary>

:::bloecke

```bloecke
[schleifen] beim Start
  [sprites] setze mySprite auf Sprite [Bild] vom Typ Player
  [sprites] setze Position von mySprite auf x 80 y 108
  [controller] bewege mySprite mit Knöpfen vx 100 vy 0
  [sprites] setze mySprite bleibe auf dem Display an
  [info] setze Anzahl Leben auf 3
  [variablen] setze tempo auf 50
[spiel] wenn Spielupdate alle 500 ms
  [sprites] setze projectile auf Projektil [Bild] von der Seite mit vx 0 vy tempo
  [sprites] setze Position von projectile auf x (wähle eine zufällige Zahl von 0 bis 160) y 0
[spiel] wenn Spielupdate alle 1000 ms
  [info] ändere Punktzahl um 1
  [variablen] ändere tempo um 5
[sprites] wenn sprite der Art Player überlappt otherSprite der Art Projectile
  [info] ändere Leben um -1
  [sprites] Zerstöre otherSprite
```

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
controller.move_sprite(spieler, 100, 0)
spieler.set_stay_in_screen(True)
info.set_life(3)
tempo = 50

def neuer_stein():
    stein = sprites.create_projectile_from_side(img("""
        . e e e e .
        e e c e e e
        e e e e c e
        e c e e e e
        e e e c e e
        . e e e e .
    """), 0, tempo)
    stein.set_position(randint(0, 160), 0)
game.on_update_interval(500, neuer_stein)

def getroffen(sprite, stein):
    info.change_life_by(-1)
    sprites.destroy(stein)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, getroffen)

def jede_sekunde():
    global tempo
    info.change_score_by(1)
    tempo = tempo + 5
game.on_update_interval(1000, jede_sekunde)
```

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
controller.moveSprite(spieler, 100, 0)
spieler.setStayInScreen(true)
info.setLife(3)
let tempo = 50

game.onUpdateInterval(500, function () {
    let stein = sprites.createProjectileFromSide(img`
        . e e e e .
        e e c e e e
        e e e e c e
        e c e e e e
        e e e c e e
        . e e e e .
    `, 0, tempo)
    stein.setPosition(randint(0, 160), 0)
})

sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, stein) {
    info.changeLifeBy(-1)
    sprites.destroy(stein)
})

game.onUpdateInterval(1000, function () {
    info.changeScoreBy(1)
    tempo = tempo + 5
})
```

:::

</details>

## Bonus: Tempolimit

Nach zwei Minuten sind die Steine so schnell, dass niemand mehr ausweichen kann. Baut eine Grenze ein: Ab `tempo` 150 werden die Steine nicht mehr schneller.

:::bloecke

Ihr braucht **wenn … dann** aus **Logik**. Steckt es in den Block für jede Sekunde und zieht **ändere tempo um 5** hinein. **ändere Punktzahl um 1** bleibt draußen. Dann holt ihr den Vergleich **0 < 0**, auch aus **Logik**, und steckt ihn in das Feld hinter **wenn**. Zieht `tempo` auf die linke 0 und tragt rechts 150 ein. **<** heißt „kleiner als“.

:::

:::python

Ihr braucht `if` mit einem Vergleich. Es kommt in `jede_sekunde`, `info.change_score_by(1)` bleibt draußen. Steht `tempo = tempo + 5` noch weiter eingerückt unter `if tempo < 150:`, wächst `tempo` nur, solange es kleiner als 150 ist. `<` heißt „kleiner als“.

:::

:::javascript

Ihr braucht `if` mit einem Vergleich. Es kommt in euren Sekunden-Teil, `info.changeScoreBy(1)` bleibt draußen. Steht `tempo = tempo + 5` in den geschweiften Klammern von `if (tempo < 150) { … }`, wächst `tempo` nur, solange es kleiner als 150 ist. `<` heißt „kleiner als“.

:::
