# Stufe 9: Der Linie folgen

Jetzt fährt das Auto allein eine Strecke ab. Der Trick: Es schaut ständig nach, wo die Linie liegt, und lenkt sofort dagegen.

## Der Plan

| Was sehen die Sensoren? | Was tut das Auto? |
|---|---|
| beide Schwarz | geradeaus, die Linie liegt genau darunter |
| nur links Schwarz | nach links drehen, die Linie wandert nach links weg |
| nur rechts Schwarz | nach rechts drehen |
| beide Weiß | anhalten, die Linie ist verloren |

Vergleicht den Plan mit eurer Tabelle aus Stufe 8. Dort steht, welche Zahl zu welcher Zeile gehört.

:::bloecke

```bloecke
[grundlagen] dauerhaft
  [variablen] setze linie auf (Line Tracking)
  [logik] wenn linie = 3 dann
    [minicar] motor = A Direction = Forward speed = 60
    [minicar] motor = B Direction = Forward speed = 60
  [logik] sonst wenn linie = 2 dann
    [minicar] motor = A Direction = Backward speed = 60
    [minicar] motor = B Direction = Forward speed = 60
  [logik] sonst wenn linie = 1 dann
    [minicar] motor = A Direction = Forward speed = 60
    [minicar] motor = B Direction = Backward speed = 60
  [logik] ansonsten
    [minicar] motor = A Direction = Forward speed = 0
    [minicar] motor = B Direction = Forward speed = 0
```

Mit dem kleinen **+** unten am **wenn**-Block fügt ihr weitere Fälle hinzu.

Hier steht 2 für „nur links Schwarz“ und 1 für „nur rechts Schwarz“. Zeigt eure Tabelle es andersherum, tauscht ihr die beiden Zahlen.

:::

:::python

```python
from microbit import *
from keyes_MiniCar import *

auto = MiniCar()
pin12.set_pull(pin12.PULL_UP)
pin13.set_pull(pin13.PULL_UP)

while True:
    links = pin13.read_digital()
    rechts = pin12.read_digital()
    if links == 1 and rechts == 1:
        auto.Motor_L(1, 60)
        auto.Motor_R(1, 60)
    elif links == 1 and rechts == 0:
        auto.Motor_L(0, 60)
        auto.Motor_R(1, 60)
    elif links == 0 and rechts == 1:
        auto.Motor_L(1, 60)
        auto.Motor_R(0, 60)
    else:
        auto.Motor_stop()
```

`elif` heißt „sonst, wenn“. Python prüft die Fälle von oben nach unten und nimmt den ersten, der stimmt. Ein `==` vergleicht zwei Werte.

:::

## Die Strecke

Fangt mit einer geraden Linie an, dann eine weite Kurve, dann ein geschlossenes Oval. Enge Ecken sind schwer.

## Wenn das Auto die Linie verliert

- **Es schießt in der Kurve hinaus:** Tempo senken.
- **Es dreht in die falsche Richtung:** Links und rechts sind vertauscht. Seht in eurer Tabelle aus Stufe 8 nach.
- **Es bleibt sofort stehen:** Stellt es so auf, dass beide Sensoren über der Linie liegen. Ist die Linie breit genug?

## Bonus: Das Tempolimit

Wie schnell kann euer Auto fahren, ohne aus der Kurve zu fliegen? Findet das höchste Tempo, bei dem es drei Runden hintereinander auf der Linie bleibt.

<details>
<summary>Tipps anzeigen</summary>

- Im Moment steht das Tempo an vielen Stellen im Programm. Legt ganz oben eine Variable `tempo` an und benutzt sie überall. Dann ändert ihr für jeden Versuch nur noch eine einzige Zahl.
- Erhöht das Tempo in kleinen Schritten, zum Beispiel immer um 10, und führt eine Liste: Tempo, geschafft oder nicht.
- Eine Runde reicht nicht als Beweis. Erst drei Runden ohne Fehler zählen.
- Für Profis: Muss das Auto beim Drehen genauso schnell sein wie auf gerader Strecke? Probiert zwei verschiedene Tempos.

</details>
