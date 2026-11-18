# Stufe 1: Steuern

Jetzt soll sich euer Spieler bewegen. Im Simulator steuert ihr mit den **Pfeiltasten** der Tastatur oder mit dem Steuerkreuz unter dem Bildschirm.

## Bewegen mit den Pfeiltasten

:::bloecke

```bloecke
[schleifen] beim Start
  [sprites] setze mySprite auf Sprite [Bild] vom Typ Player
  [sprites] setze Position von mySprite auf x 80 y 108
  [controller] bewege mySprite mit Knöpfen
```

**bewege mySprite mit Knöpfen** liegt unter **Controller**. Steckt ihn unter die anderen Blöcke in **beim Start**.

:::

:::python

```python
controller.move_sprite(spieler, 100, 100)
```

Schreibt die Zeile unter euren Spieler. `controller` sind die Pfeiltasten. Die beiden Zahlen sagen, wie schnell der Spieler fährt: erst nach links und rechts, dann nach oben und unten.

:::

:::javascript

```javascript
controller.moveSprite(spieler, 100, 100)
```

Schreibt die Zeile unter euren Spieler. `controller` sind die Pfeiltasten. Die beiden Zahlen sagen, wie schnell der Spieler fährt: erst nach links und rechts, dann nach oben und unten.

:::

Probiert es im Simulator aus. Klickt vorher einmal hinein, damit er die Tasten bekommt.

## Nur nach links und rechts

Der Spieler kann noch nach oben fahren, mitten in die Steine. Er soll aber unten bleiben. Er hat zwei Geschwindigkeiten: eine nach links und rechts, eine nach oben und unten. Die zweite setzt ihr auf 0.

:::bloecke

Klickt im Block **bewege mySprite mit Knöpfen** auf das kleine **+**. Jetzt seht ihr **vx 100 vy 100**. **vx** ist links und rechts, **vy** oben und unten. Tragt bei **vy** eine 0 ein.

:::

:::python

Ändert die zweite Zahl: `controller.move_sprite(spieler, 100, 0)`.

:::

:::javascript

Ändert die zweite Zahl: `controller.moveSprite(spieler, 100, 0)`.

:::

## Problem am Rand

Fahrt ganz nach links. Der Spieler verschwindet einfach aus dem Bild. Er soll am Rand stehen bleiben.

:::bloecke

```bloecke
[sprites] setze mySprite bleibe auf dem Display an
```

Den Block findet ihr unter **Sprites**. Er kommt auch in **beim Start**.

:::

:::python

```python
spieler.set_stay_in_screen(True)
```

Schreibt die Zeile ganz unten dazu. `True` heißt „ja“: Der Spieler bleibt auf dem Bildschirm.

:::

:::javascript

```javascript
spieler.setStayInScreen(true)
```

Schreibt die Zeile ganz unten dazu. `true` heißt „ja“: Der Spieler bleibt auf dem Bildschirm.

:::

<details>
<summary>Lösung anzeigen</summary>

:::bloecke

```bloecke
[schleifen] beim Start
  [sprites] setze mySprite auf Sprite [Bild] vom Typ Player
  [sprites] setze Position von mySprite auf x 80 y 108
  [controller] bewege mySprite mit Knöpfen vx 100 vy 0
  [sprites] setze mySprite bleibe auf dem Display an
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
```

:::

</details>

## Bonus: Los!

Beim Start sagt euer Spieler kurz „Los!“ in einer Sprechblase.

:::bloecke

Unter **Sprites** gibt es **mySprite sagt :)**. Steckt ihn ganz unten in **beim Start**, unter die anderen Blöcke. Schreibt euren Text in das Feld und klickt auf **+**: Dort stellt ihr ein, wie lange die Sprechblase bleibt, zum Beispiel 2000 ms (zwei Sekunden).

:::

:::python

```python
spieler.say_text("Los!", 2000, False)
```

Schreibt die Zeile ganz unten dazu. 2000 heißt zwei Sekunden. `False` schaltet die Animation der Sprechblase aus.

:::

:::javascript

```javascript
spieler.sayText("Los!", 2000, false)
```

Schreibt die Zeile ganz unten dazu. 2000 heißt zwei Sekunden. `false` schaltet die Animation der Sprechblase aus.

:::
