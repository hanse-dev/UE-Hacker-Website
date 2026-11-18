# Mit Pfeiltasten steuern

Bisher passiert alles nur einmal, beim Start. In einem Spiel muss sich aber etwas bewegen. Dafür gibt es **jedes Bild**: Was darin steht, passiert immer wieder, 60-mal in jeder Sekunde.

:::bloecke

```bloecke
[spiel] jedes Bild
  [logik] wenn
    [aktion] Taste ← links gedrückt
  [logik] dann
    [figuren] ändere x von spieler um -5
```

- **jedes Bild** findest du unter **Spiel**.
- **wenn … dann** liegt unter **Logik**. Die Blöcke darin laufen nur, wenn die Bedingung stimmt.
- **Taste … gedrückt** liegt unter **Spiel**. Die Bedingung stimmt, solange du die Taste festhältst.
- **ändere x von spieler um -5** liegt unter **Figuren**. Minus 5 macht x kleiner, also fährt der Spieler nach links.

:::

:::python

```python
def jedes_bild():
    if taste("links"):
        spieler.x -= 5
```

- `def jedes_bild():` ist eine **Funktion**. Das Spiel ruft sie 60-mal pro Sekunde auf. Alles, was darunter eingerückt ist, gehört dazu.
- `taste("links")` ist `True`, solange du die Taste ← festhältst.
- `spieler.x -= 5` zieht 5 von x ab. Das ist kurz für `spieler.x = spieler.x - 5`. Mit `+= 5` zählst du 5 dazu.

:::

Klicke nach ▶ Spielen einmal auf die Bühne, damit sie die Tasten bekommt. Mit ■ Stopp hältst du das Spiel an. Auf einem Tablet tippst du auf die Pfeile unter der Bühne.

## Die Pfeiltasten

Die vier Pfeiltasten heißen **links**, **rechts**, **oben** und **unten**.
