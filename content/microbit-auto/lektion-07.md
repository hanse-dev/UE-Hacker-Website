# Stufe 6: Abstand messen

Die beiden „Augen“ vorn am Auto sind ein Ultraschallsensor. Ein Auge sendet einen Ton, den Menschen nicht hören. Das andere wartet auf das Echo. Aus der Wartezeit rechnet das Auto aus, wie weit das Hindernis entfernt ist, so wie eine Fledermaus.

## Den Abstand anzeigen

:::bloecke

```bloecke
[grundlagen] dauerhaft
  [grundlagen] zeige Zahl (Ultrasonic)
  [grundlagen] pausiere (ms) 500
```

Den Block **Ultrasonic** findet ihr bei **MiniCar**. Zieht ihn in das Zahlenfeld von **zeige Zahl**.

:::

:::python

```python
from microbit import *
from keyes_MiniCar import *

auto = MiniCar()

while True:
    abstand = auto.get_distance()
    display.scroll(abstand)
    sleep(500)
```

`abstand` ist eine Variable. Sie merkt sich die gemessene Zahl, damit ihr sie weiterverwenden könnt.

:::

Die Zahl ist der Abstand in Zentimetern. Haltet die Hand vor das Auto und bewegt sie. Eine **0** bedeutet: Es kam kein Echo zurück.

## Vor der Wand stoppen

Jetzt trifft das Auto zum ersten Mal selbst eine Entscheidung: Ist der Weg frei, fährt es. Ist etwas im Weg, bleibt es stehen.

:::bloecke

```bloecke
[grundlagen] dauerhaft
  [variablen] setze abstand auf (Ultrasonic)
  [logik] wenn abstand > 0 und abstand < 15 dann
    [minicar] motor = A Direction = Forward speed = 0
    [minicar] motor = B Direction = Forward speed = 0
  [logik] ansonsten
    [minicar] motor = A Direction = Forward speed = 70
    [minicar] motor = B Direction = Forward speed = 70
```

Die Variable `abstand` legt ihr unter **Variablen** an. Die Vergleiche und das **und** liegen unter **Logik**.

:::

:::python

```python
from microbit import *
from keyes_MiniCar import *

auto = MiniCar()

while True:
    abstand = auto.get_distance()
    if 0 < abstand < 15:
        auto.Motor_stop()
    else:
        auto.Motor_L(1, 70)
        auto.Motor_R(1, 70)
    sleep(50)
```

`if` prüft eine Bedingung. Stimmt sie, laufen die Zeilen darunter. Sonst laufen die Zeilen unter `else`.

:::

> Dieses Programm fährt ohne Startknopf los, sobald der Schalter auf ON steht. Haltet das Auto fest oder stellt es erst danach auf den Boden.
