# Stufe 2: Steine fallen

Jetzt kommt die Gefahr von oben: Alle halbe Sekunde fällt ein Stein. Dafür gibt es in Arcade **Projektile**. Das sind Sprites, die von selbst fliegen und verschwinden, sobald sie den Bildschirm verlassen.

## Ein Stein alle halbe Sekunde

Eine halbe Sekunde sind 500 **Millisekunden** (ms), eine ganze Sekunde sind 1000.

:::bloecke

```bloecke
[spiel] wenn Spielupdate alle 500 ms
  [sprites] setze projectile auf Projektil [Bild] von der Seite mit vx 0 vy 50
```

**wenn Spielupdate alle 500 ms** findet ihr unter **Spiel**. Zieht ihn frei auf die Fläche, nicht in **beim Start**. Alles darin passiert jetzt immer wieder, alle 500 ms.

Unter **Sprites** liegt **setze projectile auf Projektil … von der Seite mit vx … vy …**. Malt im grauen Feld einen Stein. **vy 50** heißt: Der Stein fliegt 50 Punkte pro Sekunde nach unten. Nach links oder rechts soll er nicht, also **vx 0**. Lasst euch von „von der Seite“ nicht stören: Mit vx 0 und vy 50 kommt der Stein von oben.

:::

:::python

```python
def neuer_stein():
    stein = sprites.create_projectile_from_side(img("""
        . e e e e .
        e e c e e e
        e e e e c e
        e c e e e e
        e e e c e e
        . e e e e .
    """), 0, 50)
game.on_update_interval(500, neuer_stein)
```

Schreibt den Code ganz unten unter alles, was schon da ist. `def neuer_stein():` legt eine **Funktion** an: eine Liste von Befehlen mit einem Namen. Was eingerückt darunter steht, gehört dazu. Die letzte Zeile sagt dem Spiel: Rufe `neuer_stein` alle 500 ms auf.

Die beiden Zahlen hinter dem Bild sind die Geschwindigkeit: 0 nach links und rechts, 50 Punkte pro Sekunde nach unten. `e` ist braun, `c` dunkelviolett.

:::

:::javascript

```javascript
game.onUpdateInterval(500, function () {
    let stein = sprites.createProjectileFromSide(img`
        . e e e e .
        e e c e e e
        e e e e c e
        e c e e e e
        e e e c e e
        . e e e e .
    `, 0, 50)
})
```

Schreibt den Code ganz unten unter alles, was schon da ist. `function () { … }` ist eine **Funktion**: eine Liste von Befehlen. `game.onUpdateInterval` ruft sie alle 500 ms auf.

Die beiden Zahlen hinter dem Bild sind die Geschwindigkeit: 0 nach links und rechts, 50 Punkte pro Sekunde nach unten. `e` ist braun, `c` dunkelviolett.

:::

Startet das Spiel. Die Steine fallen, aber immer an derselben Stelle in der Mitte. Da muss man ja nie ausweichen!

## Zufall

Jeder Stein soll an einer anderen Stelle oben starten. Dafür lasst ihr den Computer eine Zahl für x **würfeln**: irgendwo zwischen 0 (ganz links) und 160 (ganz rechts).

:::bloecke

```bloecke
[spiel] wenn Spielupdate alle 500 ms
  [sprites] setze projectile auf Projektil [Bild] von der Seite mit vx 0 vy 50
  [sprites] setze Position von projectile auf x (wähle eine zufällige Zahl von 0 bis 160) y 0
```

**setze Position von mySprite auf x … y …** kennt ihr schon. Steckt einen neuen davon in **wenn Spielupdate**, direkt unter den Projektil-Block. Klickt darin auf **mySprite** und wählt **projectile**. Unter **Mathematik** findet ihr **wähle eine zufällige Zahl von 0 bis 10**. Steckt ihn in das Feld hinter **x** und tragt 160 statt 10 ein. Bei **y** kommt 0 hin, also ganz oben.

:::

:::python

```python
    stein.set_position(randint(0, 160), 0)
```

`randint(0, 160)` würfelt eine ganze Zahl von 0 bis 160. Die Zeile kommt ganz unten in die Funktion, unter die Zeile mit `0, 50)`. Rückt sie genauso weit ein wie `stein = …`, damit sie zur Funktion gehört.

:::

:::javascript

```javascript
    stein.setPosition(randint(0, 160), 0)
```

`randint(0, 160)` würfelt eine ganze Zahl von 0 bis 160. Die Zeile kommt vor die schließende Klammer `})`, damit sie zur Funktion gehört.

:::

Jetzt regnet es Steine. Versucht schon mal auszuweichen. Noch passiert nichts, wenn ein Stein euch trifft. Das kommt in der nächsten Stufe.

<details>
<summary>Lösung anzeigen</summary>

:::bloecke

```bloecke
[schleifen] beim Start
  [sprites] setze mySprite auf Sprite [Bild] vom Typ Player
  [sprites] setze Position von mySprite auf x 80 y 108
  [controller] bewege mySprite mit Knöpfen vx 100 vy 0
  [sprites] setze mySprite bleibe auf dem Display an
[spiel] wenn Spielupdate alle 500 ms
  [sprites] setze projectile auf Projektil [Bild] von der Seite mit vx 0 vy 50
  [sprites] setze Position von projectile auf x (wähle eine zufällige Zahl von 0 bis 160) y 0
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
```

:::

</details>

## Bonus: Schnelle und langsame Steine

Nicht jeder Stein ist gleich schnell: Manche fallen gemütlich, andere sausen.

:::bloecke

Ihr kennt schon **wähle eine zufällige Zahl von … bis …**. Steckt so einen Block auch in das Feld hinter **vy**, statt der 50. Zum Beispiel von 30 bis 90.

:::

:::python

Ihr kennt schon `randint`. Ersetzt die 50 hinter dem Bild durch `randint(30, 90)`.

:::

:::javascript

Ihr kennt schon `randint`. Ersetzt die 50 hinter dem Bild durch `randint(30, 90)`.

:::
