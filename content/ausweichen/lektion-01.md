# Die Bühne

In diesem Projekt baust du ein eigenes Spiel: Unten fährt dein **Spieler** hin und her, von oben fallen **Steine**, und du musst ihnen ausweichen.

Oben kannst du wählen, ob du mit **Blöcken** oder mit **Python** programmierst. Beides baut dasselbe Spiel. Du kannst jederzeit wechseln.

## Wo ist was?

Dein Spiel läuft auf der **Bühne** rechts. Sie ist 400 Punkte breit und 400 Punkte hoch. Jeder Ort auf der Bühne hat zwei Zahlen:

- **x** sagt, wie weit rechts etwas ist: 0 ist ganz links, 400 ganz rechts.
- **y** sagt, wie weit unten etwas ist: 0 ist ganz oben, 400 ganz unten.

Achtung: y zählt nach **unten**, anders als in Mathe.

## Eine Figur

Alles in deinem Spiel ist eine **Figur**: ein Rechteck mit Ort, Größe und Farbe. x und y sind die **linke obere Ecke** der Figur.

:::bloecke

In der ersten Aufgabe steht schon dieses Programm:

```bloecke
[spiel] beim Start
  [variablen] setze spieler auf
    [figuren] neue Figur x 180 y 200 Breite 40 Höhe 20 Farbe blau
```

Alles im Block **beim Start** passiert einmal, wenn du auf ▶ Spielen klickst. Der Block **neue Figur** stellt ein Rechteck auf die Bühne. Mit **setze spieler auf** bekommt es einen Namen: Es ist jetzt die Variable **spieler**.

Eine Zahl änderst du, indem du in ihr weißes Feld klickst. Die Farbe wählst du im kleinen Menü.

Neue Blöcke findest du links in den Kategorien. **neue Figur** liegt unter **Figuren**, **setze … auf** unter **Variablen**. Dort legst du mit **Variable erstellen …** auch neue Namen an.

:::

:::python

In der ersten Aufgabe steht schon dieses Programm:

```python
from spiel import *

spieler = figur(180, 200, 40, 20, "blau")
```

Die erste Zeile holt die Spiel-Befehle. `figur(x, y, breite, hoehe, farbe)` stellt ein Rechteck auf die Bühne. Mit `spieler =` speicherst du es in der Variable `spieler`.

Mögliche Farben: `"blau"`, `"rot"`, `"gruen"`, `"gelb"`, `"orange"`, `"lila"`, `"pink"`, `"tuerkis"`, `"braun"`, `"grau"`, `"schwarz"` und `"weiss"`.

:::

> 💡 Probiere ruhig aus: Was passiert, wenn du x auf 0 setzt? Und wenn die Breite 200 ist?
