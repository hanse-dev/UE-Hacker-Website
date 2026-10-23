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

Die Zahl ist der Abstand in Zentimetern. Haltet die Hand vor das Auto und bewegt sie. Eine **0** bedeutet: Es kam kein Echo zurück. Zeigt der micro:bit immer nur 0, stellt den Schalter auf **ON** und probiert es noch einmal.

## Vor der Wand stoppen

Jetzt trifft das Auto zum ersten Mal selbst eine Entscheidung: Ist der Weg frei, fährt es. Ist etwas im Weg, bleibt es stehen. Das neue Programm ersetzt das Anzeigen: Löscht das alte Programm vorher (bei Blöcken den ersten **dauerhaft**-Block, in Python die Schleife `while True:` mit allem darunter).

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

Der rote Block gehört zu einer **Variable**. Eine Variable ist wie eine beschriftete Schachtel, in der sich das Programm eine Zahl merkt. So baut ihr sie:

1. Klickt in der Blockliste auf **Variablen** und dann auf **Erstelle eine Variable**. Nennt sie `abstand`.
2. Jetzt gibt es dort neue rote Blöcke. Zieht **setze abstand auf 0** in den Block **dauerhaft**.
3. Zieht den Block **Ultrasonic** aus **MiniCar** auf die `0`. Damit legt das Programm in jeder Runde den frisch gemessenen Abstand in die Schachtel.

Der Block **wenn … dann … ansonsten** liegt unter **Logik**, genauso wie die Vergleiche `<` und `>` und das **und**. Steckt zuerst das **und** in das Feld hinter **wenn** und dann in jede Seite einen Vergleich. Auf dem Vergleich-Block steht zuerst ein **=**: Klickt auf das Zeichen und wählt **>** bzw. **<**. Den kleinen runden Block `abstand` holt ihr aus **Variablen** und zieht ihn in beide Vergleiche.

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

`if` prüft eine Bedingung. Stimmt sie, laufen die Zeilen darunter. Sonst laufen die Zeilen unter `else`. `0 < abstand < 15` heißt: `abstand` ist größer als 0 und kleiner als 15.

:::

Warum „größer als 0“? Eine 0 heißt: Es kam kein Echo zurück. Ohne diese Bedingung würde das Auto dann grundlos anhalten.

> Dieses Programm fährt ohne Startknopf los, sobald der Schalter auf ON steht. Haltet das Auto fest oder stellt es erst danach auf den Boden.

## Bonus: Die Ampel

Das Auto zeigt mit den Scheinwerfern, was es gerade sieht: **Grün** bei freier Fahrt, **Rot**, sobald etwas im Weg ist.

<details>
<summary>Tipps anzeigen</summary>

- Euer Programm unterscheidet schon zwei Fälle: Hindernis oder freie Fahrt. In jeden der beiden Fälle kommt zusätzlich ein Befehl für die Scheinwerfer.
- Die Befehle für die Scheinwerfer kennt ihr aus Stufe 2.

:::bloecke

Im Block **RGB** gibt es die Farbe `green`. Ihr braucht den Block für beide Scheinwerfer, `LED_L` und `LED_R`.

:::

:::python

Denkt an das Mischen der Farben: Leuchtet Grün noch, wenn Rot dazukommt, wird es gelb. Schaltet deshalb vor der neuen Farbe alles aus. Und nicht vergessen: 0 ist hell, 255 ist aus.

```python
    if 0 < abstand < 15:
        auto.Motor_stop()
        auto.led_off()
        auto.left_red(0)
        auto.right_red(0)
    else:
        # wie bisher fahren, dazu: alles aus, dann Grün an
```

:::

- Für Profis: Baut eine dritte Stufe ein. Zwischen 15 und 30 cm leuchtet die Ampel gelb, und das Auto fährt langsamer.

</details>
