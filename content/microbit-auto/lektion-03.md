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
