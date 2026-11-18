# Stufe 3: Getroffen!

Bisher fliegen die Steine einfach durch euren Spieler hindurch. Jetzt wird es ernst: Ihr habt drei Leben. Jeder Treffer kostet eins, und ohne Leben ist das Spiel vorbei.

## Drei Leben

:::bloecke

```bloecke
[schleifen] beim Start
  [info] setze Anzahl Leben auf 3
```

Den Block findet ihr unter **Info**. Steckt ihn zu den anderen in **beim Start**.

:::

:::python

```python
info.set_life(3)
```

Schreibt die Zeile direkt unter `spieler.set_stay_in_screen(True)`, nicht in die Funktion.

:::

:::javascript

```javascript
info.setLife(3)
```

Schreibt die Zeile direkt unter `spieler.setStayInScreen(true)`, nicht in die Funktion.

:::

Oben links im Simulator erscheinen drei Herzen.

## Wenn ein Stein trifft

Das Spiel soll merken, wenn sich zwei Sprites berühren: euer Spieler und ein Stein. Das nennt man **Überlappen**. Damit es weiß, welche Sprites gemeint sind, hat jedes Sprite einen **Typ**: Euer Spieler ist vom Typ **Player** (Spieler), die Steine sind vom Typ **Projectile** (Projektil).

:::bloecke

```bloecke
[sprites] wenn sprite der Art Player überlappt otherSprite der Art Projectile
  [info] ändere Leben um -1
  [sprites] Zerstöre otherSprite
```

Der große Block **wenn sprite der Art Player überlappt otherSprite der Art Player** liegt unter **Sprites**. Zieht ihn frei auf die Fläche. Klickt auf das zweite **Player** und wählt **Projectile**. Im Block heißt der Typ **Art**.

**ändere Leben um -1** findet ihr unter **Info**. Den Block **Zerstöre mySprite** findet ihr wieder unter **Sprites**. Packt dann oben im großen Block das Wort **otherSprite** mit der Maus: Ihr bekommt eine Kopie davon. Die zieht ihr auf **mySprite** im Block **Zerstöre**. So verschwindet der Stein, der euch getroffen hat, und nicht euer Spieler.

:::

:::python

```python
def getroffen(sprite, stein):
    info.change_life_by(-1)
    sprites.destroy(stein)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, getroffen)
```

Schreibt die Zeilen ganz unten unter alles andere, nicht in die Funktion `neuer_stein`. `def` und die letzte Zeile fangen ganz links an.

Die letzte Zeile sagt: Wenn ein Sprite vom Typ `player` einen vom Typ `projectile` berührt, rufe `getroffen` auf. Die Funktion bekommt die beiden Sprites mitgeliefert, das zweite ist der Stein. `sprites.destroy(stein)` nimmt ihn vom Bildschirm.

:::

:::javascript

```javascript
sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, stein) {
    info.changeLifeBy(-1)
    sprites.destroy(stein)
})
```

Schreibt den Block ganz unten unter alles andere, nicht in die Funktion für die Steine. Wenn ein Sprite vom Typ `Player` einen vom Typ `Projectile` berührt, läuft die Funktion. Sie bekommt die beiden Sprites mitgeliefert, das zweite ist der Stein. `sprites.destroy(stein)` nimmt ihn vom Bildschirm.

:::

Lasst euch absichtlich treffen. Ein Herz verschwindet und der Stein mit ihm. Sind alle Herzen weg, beendet Arcade das Spiel von selbst. Mit einem Klick oder einer Taste geht es von vorn los.

Warum muss der Stein verschwinden? Probiert es aus: Nehmt das Zerstören kurz heraus (den Block herausziehen oder die Zeile löschen), spielt eine Runde und baut es danach wieder ein. Ein Stein, der langsam durch euren Spieler rutscht, berührt ihn viele Male hintereinander, und alle Leben sind auf einmal weg.

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
[spiel] wenn Spielupdate alle 500 ms
  [sprites] setze projectile auf Projektil [Bild] von der Seite mit vx 0 vy 50
  [sprites] setze Position von projectile auf x (wähle eine zufällige Zahl von 0 bis 160) y 0
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

def neuer_stein():
    stein = sprites.create_projectile_from_side(img("""
        . e e e e .
        e e c e e e
        e e e e c e
        e c e e e e
        e e e c e e
        . e e e e .
    """), 0, 50)
    stein.set_position(randint(0, 160), 0)
game.on_update_interval(500, neuer_stein)

def getroffen(sprite, stein):
    info.change_life_by(-1)
    sprites.destroy(stein)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, getroffen)
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

game.onUpdateInterval(500, function () {
    let stein = sprites.createProjectileFromSide(img`
        . e e e e .
        e e c e e e
        e e e e c e
        e c e e e e
        e e e c e e
        . e e e e .
    `, 0, 50)
    stein.setPosition(randint(0, 160), 0)
})

sprites.onOverlap(SpriteKind.Player, SpriteKind.Projectile, function (sprite, stein) {
    info.changeLifeBy(-1)
    sprites.destroy(stein)
})
```

:::

</details>

## Bonus: Das hat gesessen

Bei jedem Treffer wackelt der Bildschirm kurz.

:::bloecke

Unter **Szene** findet ihr **Kamera schütteln um 4 Pixel für 500 ms**. Steckt ihn in den Überlappen-Block.

:::

:::python

```python
    scene.camera_shake(4, 500)
```

Die Zeile kommt eingerückt in `getroffen`. 4 ist die Stärke, 500 die Dauer in Millisekunden.

:::

:::javascript

```javascript
    scene.cameraShake(4, 500)
```

Die Zeile kommt in die Funktion bei `sprites.onOverlap`. 4 ist die Stärke, 500 die Dauer in Millisekunden.

:::
