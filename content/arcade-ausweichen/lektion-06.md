# Werkstatt: Euer Spiel, eure Regeln

Euer Ausweichspiel läuft. Jetzt macht ihr es zu eurem Spiel. Hier gibt es keine fertigen Programme mehr, nur Aufträge und Tipps. Die Sterne zeigen, wie knifflig ein Auftrag ist: ⭐ geht schnell, ⭐⭐⭐ braucht Ausdauer.

Ein gelöster Auftrag reicht für den Abschluss.

Kommt ihr nicht weiter, klappt den **Plan** unter einem Auftrag auf. Er sagt in Worten, was euer Programm Schritt für Schritt machen soll. In Blöcke oder Code übersetzt ihr ihn selbst.

## Auftrag 1: Feuer! ⭐

Trifft euch ein Stein, verschwindet er nicht einfach, sondern geht in Flammen auf.

:::bloecke

Klickt im Block **Zerstöre otherSprite** auf das **+**. Jetzt könnt ihr einen Effekt wählen, zum Beispiel **Feuer**, und wie lange er dauert.

:::

:::python

```python
    sprites.destroy(stein, effects.fire, 200)
```

Ersetzt damit die Zeile `sprites.destroy(stein)` in `getroffen`. 200 ist die Dauer in Millisekunden. Statt `fire` gehen auch `disintegrate`, `confetti` oder `hearts`.

:::

:::javascript

```javascript
    sprites.destroy(stein, effects.fire, 200)
```

Ersetzt damit die Zeile `sprites.destroy(stein)`. 200 ist die Dauer in Millisekunden. Statt `fire` gehen auch `disintegrate`, `confetti` oder `hearts`.

:::

## Auftrag 2: Herzen sammeln ⭐⭐

Ab und zu fällt statt eines Steins ein Herz. Wer es fängt, bekommt ein Leben dazu.

<details>
<summary>Plan anzeigen</summary>

1. Alle 3000 ms entsteht ein neues Projektil mit einem Herz-Bild, an einer zufälligen Stelle oben.
2. Dieses Projektil bekommt den Typ **Food** (Essen), damit es kein Stein ist.
3. Überlappt der Spieler ein Sprite vom Typ Food: ein Leben dazu und das Herz zerstören.

</details>

:::bloecke

Für Schritt 1 nehmt ihr einen neuen Block **wenn Spielupdate alle … ms** und baut darin wie beim Stein ein Projektil mit Herz-Bild und eine zufällige Position. Den Typ ändert ihr mit **setze Typ von mySprite auf Player** unter **Sprites**: Steckt ihn direkt unter das Herz-Projektil, klickt auf **mySprite** und wählt **projectile**, klickt auf **Player** und wählt **Food**. Für Schritt 3 braucht ihr einen zweiten Überlappen-Block, diesmal mit **Food** statt **Projectile**.

:::

:::python

Für Schritt 1 kopiert ihr eure Funktion `neuer_stein` samt der Zeile `game.on_update_interval` darunter. Nennt die Kopie `neues_herz`, schreibt überall `herz` statt `stein`, 3000 statt 500 und malt ein Herz (`2` ist rot). Den Typ ändert ihr mit `herz.set_kind(SpriteKind.food)` in derselben Funktion.

Für Schritt 3 baut ihr eine zweite Funktion wie `getroffen`, mit zwei Namen in der Klammer, zum Beispiel `def gefangen(sprite, herz):`. Darunter kommt ein zweites `sprites.on_overlap`, diesmal mit `SpriteKind.food`. Ein Leben dazu ist `info.change_life_by(1)`, und mit `sprites.destroy(herz)` verschwindet das Herz. Alles kommt ganz unten ins Programm.

:::

:::javascript

Für Schritt 1 kopiert ihr euer `game.onUpdateInterval` mit dem Stein. Schreibt in der Kopie überall `herz` statt `stein`, 3000 statt 500 und malt ein Herz (`2` ist rot). Den Typ ändert ihr mit `herz.setKind(SpriteKind.Food)` in derselben Funktion.

Für Schritt 3 braucht ihr ein zweites `sprites.onOverlap`, ganz unten im Programm: `sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, herz) { … })`. Ein Leben dazu ist `info.changeLifeBy(1)`, und mit `sprites.destroy(herz)` verschwindet das Herz.

:::

## Auftrag 3: Der Verfolger ⭐⭐

Ein Gegner taucht auf und jagt euren Spieler langsam über den Bildschirm. Berührt er euch, kostet das ein Leben.

<details>
<summary>Plan anzeigen</summary>

1. Beim Start entsteht ein zweites Sprite vom Typ **Enemy** (Gegner) mit eigenem Bild, oben in einer Ecke.
2. Der Gegner folgt dem Spieler, aber langsam, zum Beispiel mit Geschwindigkeit 20.
3. Überlappt der Spieler den Gegner: ein Leben weniger, und der Gegner springt zurück in seine Ecke.

</details>

:::bloecke

Legt unter **Variablen** mit **Erstelle eine Variable...** eine neue Variable `gegner` an. Für den Gegner nehmt ihr noch einmal **setze mySprite auf Sprite … vom Typ Player**: Klickt auf **mySprite** und wählt `gegner`, klickt auf **Player** und wählt **Enemy**. Unter **Sprites** gibt es **setze myEnemy folgend mySprite**: Klickt auf **myEnemy** und wählt `gegner`. Mit **+** stellt ihr die Geschwindigkeit ein. Diese Blöcke kommen in **beim Start**. Zurück in die Ecke springt der Gegner mit **setze Position von … auf x 0 y 0**, das ist oben links: Er kommt in einen neuen Überlappen-Block mit **Enemy**, zusammen mit **ändere Leben um -1**. Wählt darin **otherSprite**, das ist der Gegner.

:::

:::python

Der Gegner ist ein Sprite wie euer Spieler: `gegner = sprites.create(img(""" … """), SpriteKind.enemy)`. Folgen geht mit `gegner.follow(spieler, 20)`. Diese Zeilen kommen oben unter euren Spieler, nicht in eine Funktion. Zurück in die Ecke oben links geht es mit `gegner.set_position(0, 0)`. Die Überlappen-Funktion baut ihr wie `getroffen`, mit `SpriteKind.enemy`, ganz unten im Programm.

:::

:::javascript

Der Gegner ist ein Sprite wie euer Spieler: `` let gegner = sprites.create(img` … `, SpriteKind.Enemy) ``. Folgen geht mit `gegner.follow(spieler, 20)`. Diese Zeilen kommen oben unter euren Spieler, nicht in eine Funktion. Zurück in die Ecke oben links geht es mit `gegner.setPosition(0, 0)`. Das Überlappen baut ihr wie bei den Steinen, mit `SpriteKind.Enemy`, ganz unten im Programm.

:::

## Auftrag 4: Gewonnen! ⭐⭐⭐

Bisher kann man nur verlieren. Wer 60 Punkte schafft, also eine ganze Minute überlebt, gewinnt.

<details>
<summary>Plan anzeigen</summary>

1. Erreicht die Punktzahl 60, ist das Spiel vorbei.
2. Diesmal endet es nicht mit „verloren“, sondern mit „gewonnen“.
3. Probiert es erst mit 5 Punkten aus, sonst müsst ihr zum Testen jedes Mal eine Minute spielen.

</details>

:::bloecke

Unter **Info** gibt es den Block **bei Punktzahl …**. Tragt dort 60 ein. Unter **Spiel** findet ihr **Game over**. Ein Klick auf den Schalter darin wählt, ob das Spiel gewonnen oder verloren ist.

:::

:::python

`info.on_score(60, gewonnen)` ruft die Funktion `gewonnen` auf (`def gewonnen():`, mit leerer Klammer), sobald ihr 60 Punkte habt. Die Funktion und diese Zeile kommen ganz unten ins Programm, in die Funktion schreibt ihr `game.over(True)`. `game.over(True)` beendet das Spiel als Sieg, `game.over(False)` als Niederlage.

:::

:::javascript

`info.onScore(60, function () { … })` läuft, sobald ihr 60 Punkte habt. Es kommt ganz unten ins Programm, in die geschweiften Klammern schreibt ihr `game.over(true)`. `game.over(true)` beendet das Spiel als Sieg, `game.over(false)` als Niederlage.

:::

## Bonus: Vorspielen

Lasst jemanden euer Spiel spielen, der es noch nicht kennt: eure Eltern, Geschwister oder ein anderes Team. Schaut zu, ohne zu helfen. Wo kommt die Person nicht weiter? Was macht ihr am meisten Spaß? Vielleicht findet ihr dabei schon die Idee für euren nächsten Auftrag.
