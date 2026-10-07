# Stufe 3: Losfahren und stoppen

Das Auto hat zwei Motoren, einen für jedes Rad. Drehen beide gleich schnell vorwärts, fährt das Auto geradeaus.

## Der Startknopf

Ein Auto, das sofort losfährt, reißt am Kabel. Deshalb startet die Fahrt erst, wenn ihr Knopf **A** drückt.

So läuft jeder Test ab:

1. Schalter auf **OFF**, Programm übertragen.
2. Kabel abziehen, Auto auf den Boden stellen.
3. Schalter auf **ON**, dann Knopf **A** drücken.

## Eine Sekunde geradeaus

:::bloecke

```bloecke
[eingabe] wenn Knopf A geklickt
  [minicar] motor = A Direction = Forward speed = 70
  [minicar] motor = B Direction = Forward speed = 70
  [grundlagen] pausiere (ms) 1000
  [minicar] motor = A Direction = Forward speed = 0
  [minicar] motor = B Direction = Forward speed = 0
```

Motor **A** ist das linke Rad, Motor **B** das rechte. `speed` geht von 0 (steht) bis 255 (volle Kraft). Einen eigenen Stopp-Block gibt es nicht: Zum Anhalten stellt ihr beide Motoren auf `speed = 0`.

:::

:::python

```python
from microbit import *
from keyes_MiniCar import *

auto = MiniCar()

while True:
    if button_a.was_pressed():
        auto.Motor_L(1, 70)
        auto.Motor_R(1, 70)
        sleep(1000)
        auto.Motor_stop()
```

`Motor_L` ist das linke Rad, `Motor_R` das rechte. Die erste Zahl ist die Richtung: `1` vorwärts, `0` rückwärts. Die zweite Zahl ist das Tempo von 0 (steht) bis 255 (volle Kraft).

:::

## So denkt das Auto

Das Auto misst keine Strecke. Es schaltet die Motoren ein, wartet und schaltet sie wieder aus. Wie weit es kommt, hängt von Tempo und Wartezeit ab. Die passenden Zahlen findet ihr nur durch Ausprobieren.

## Wenn etwas nicht klappt

- **Nichts bewegt sich:** Steht der Schalter auf ON? Sind die Batterien voll?
- **Das Auto fährt eine Kurve statt geradeaus:** Die Motoren sind nie ganz gleich stark. Gebt dem schwächeren Rad ein paar Punkte mehr Tempo.
- **Es brummt nur:** Das Tempo ist zu klein. Unter etwa 40 kommt das Auto kaum los.
