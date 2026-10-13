# Stufe 9: Der Linie folgen

Jetzt fährt das Auto allein eine Strecke ab. Der Trick: Es schaut ständig nach, wo die Linie liegt, und lenkt sofort dagegen.

## Der Plan

Bevor ihr programmiert, macht ihr einen Plan in Worten. Die Sensoren können vier verschiedene Dinge sehen. Was soll das Auto jeweils tun? Zeichnet die Tabelle ab und füllt die rechte Spalte aus.

| Was sehen die Sensoren? | Was tut das Auto? |
|---|---|
| beide Schwarz | ? |
| nur links Schwarz | ? |
| nur rechts Schwarz | ? |
| beide Weiß | ? |

Zwei Fragen helfen euch:

- Sieht nur der linke Sensor Schwarz: Auf welcher Seite des Autos liegt die Linie dann? Wohin muss das Auto drehen, damit sie wieder genau unter ihm liegt?
- Was ist am sichersten, wenn das Auto gar keine Linie mehr sieht?

Kommt ihr nicht weiter, hilft der fertige Plan. Versucht es aber zuerst allein.

<details>
<summary>Plan anzeigen</summary>

| Was sehen die Sensoren? | Was tut das Auto? |
|---|---|
| beide Schwarz | geradeaus, die Linie liegt genau darunter |
| nur links Schwarz | nach links drehen, die Linie wandert nach links weg |
| nur rechts Schwarz | nach rechts drehen |
| beide Weiß | anhalten, die Linie ist verloren |

</details>

## Vom Plan zum Programm

Jede Zeile eures Plans wird im Programm zu einem Fall. An welcher Zahl ihr einen Fall erkennt, steht in eurer Tabelle aus Stufe 8. Wie das Auto fährt, dreht und anhält, wisst ihr aus Stufe 3 und 4.

Der erste Fall ist schon fertig. Die anderen drei baut ihr selbst.

:::bloecke

```bloecke
[grundlagen] dauerhaft
  [variablen] setze linie auf (Line Tracking)
  [logik] wenn linie = 3 dann
    [minicar] motor = A Direction = Forward speed = 60
    [minicar] motor = B Direction = Forward speed = 60
  [logik] sonst wenn … dann
  [logik] ansonsten
```

Mit dem kleinen **+** unten am **wenn**-Block fügt ihr weitere Fälle hinzu. Den Vergleich mit **=** findet ihr unter **Logik**.

Die 3 steht hier für „beide Schwarz“. Zeigt eure Tabelle dafür eine andere Zahl, nehmt ihr eure.

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
    # Hier kommen eure drei weiteren Fälle hin.
```

Weitere Fälle hängt ihr mit `elif` an, das heißt „sonst, wenn“. Der letzte Fall bekommt ein `else`. Python prüft die Fälle von oben nach unten und nimmt den ersten, der stimmt. Ein `==` vergleicht zwei Werte.

:::

Das Auto fährt nicht so, wie ihr wollt? Lest zuerst weiter unten bei „Wenn das Auto die Linie verliert“ nach. Erst wenn gar nichts mehr hilft, schaut ihr in die Lösung.

<details>
<summary>Lösung anzeigen</summary>

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

:::

</details>

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
