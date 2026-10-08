# Stufe 2: Scheinwerfer

Vorn am Auto sitzen zwei Scheinwerfer, die jede Farbe können. Ab jetzt braucht das Auto Strom aus den Batterien: Nach dem Übertragen stellt ihr den Schalter **POWER** auf **ON**.

## Scheinwerfer einschalten

:::bloecke

```bloecke
[grundlagen] beim Start
  [minicar] RGB = LED_L color = red
  [minicar] RGB = LED_R color = red
  [grundlagen] pausiere (ms) 2000
  [minicar] LED OFF
```

`LED_L` ist der linke Scheinwerfer, `LED_R` der rechte. **pausiere (ms) 2000** wartet 2000 Millisekunden, das sind 2 Sekunden.

:::

:::python

```python
from microbit import *
from keyes_MiniCar import *

auto = MiniCar()

auto.left_red(0)
auto.right_red(0)
sleep(2000)
auto.led_off()
```

`auto = MiniCar()` stellt die Verbindung zum Auto her. Diese drei Zeilen am Anfang braucht ab jetzt jedes Programm.

Die Zahl bestimmt die Helligkeit, und zwar andersherum als erwartet: **0 ist ganz hell, 255 ist aus.** Für jede Seite gibt es `red`, `green` und `blue`, zum Beispiel `auto.left_green(0)`.

`sleep(2000)` wartet 2000 Millisekunden, das sind 2 Sekunden.

:::

## Blinken

Soll etwas immer wieder passieren, kommt es in eine Endlosschleife.

:::bloecke

```bloecke
[grundlagen] dauerhaft
  [minicar] RGB = LED_L color = yellow
  [grundlagen] pausiere (ms) 500
  [minicar] LED OFF
  [grundlagen] pausiere (ms) 500
```

:::

:::python

```python
from microbit import *
from keyes_MiniCar import *

auto = MiniCar()

while True:
    auto.left_red(0)
    auto.left_green(0)
    sleep(500)
    auto.led_off()
    sleep(500)
```

Rot und Grün zusammen ergeben Gelb.

:::

## Bonus: Das Polizeilicht

Die Scheinwerfer sollen wie bei einem Einsatzfahrzeug flackern: erst links blau und rechts rot, dann sofort umgekehrt, und das schnell und ohne Ende.

<details>
<summary>Tipps anzeigen</summary>

- Das Polizeilicht hat genau zwei Zustände, die sich abwechseln. Schreibt beide in Worten auf, bevor ihr baut.
- Zwischen den Zuständen steht eine kurze Pause. Probiert Werte zwischen 100 und 300 Millisekunden und sucht, was am echtesten aussieht.
- Alles zusammen gehört in die Endlosschleife, wie beim Blinken.

:::bloecke

Im Block **RGB** wählt ihr die Farbe `blue` genauso aus wie vorher `red`.

:::

:::python

Für Blau gibt es `auto.left_blue(0)` und `auto.right_blue(0)`.

Achtung, Farben mischen sich: Leuchtet ein Scheinwerfer rot und ihr schaltet Blau dazu, wird er lila. Schaltet vor jedem Wechsel alles aus.

:::

</details>
