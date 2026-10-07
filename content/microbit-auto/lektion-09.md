# Stufe 8: Die Linie sehen

Unter dem Auto sitzen zwei Liniensensoren, einer links und einer rechts. Jeder leuchtet mit unsichtbarem Licht auf den Boden. Weißes Papier wirft das Licht zurück, eine schwarze Linie schluckt es. So erkennt der Sensor, ob er über Hell oder Dunkel steht.

Ihr braucht ein weißes Blatt mit einer schwarzen Linie, etwa 2 cm breit. Schwarzes Klebeband eignet sich gut.

## Was meldet der Sensor?

:::bloecke

```bloecke
[grundlagen] dauerhaft
  [grundlagen] zeige Zahl (Line Tracking)
```

Der Block **Line Tracking** meldet eine Zahl von 0 bis 3. Sie verrät, welcher Sensor Schwarz sieht.

:::

:::python

```python
from microbit import *

pin12.set_pull(pin12.PULL_UP)
pin13.set_pull(pin13.PULL_UP)

while True:
    links = pin13.read_digital()
    rechts = pin12.read_digital()
    display.show(links * 2 + rechts)
    sleep(100)
```

Der linke Sensor hängt an `pin13`, der rechte an `pin12`. Jeder meldet `1` für Schwarz und `0` für Weiß. Die Rechnung `links * 2 + rechts` macht daraus eine einzige Zahl von 0 bis 3.

:::

## Forschen

Das Auto bleibt in der Hand, der Schalter steht auf ON. Schiebt es langsam quer über die Linie und füllt die Tabelle aus. Zeichnet sie auf ein Blatt.

| Wo steht das Auto? | Angezeigte Zahl |
|---|---|
| beide Sensoren über Weiß | ? |
| nur der linke Sensor über der Linie | ? |
| nur der rechte Sensor über der Linie | ? |
| beide Sensoren über der Linie | ? |

Hebt die Tabelle gut auf. In der nächsten Stufe baut ihr damit den Linienfolger.

## Wenn die Zahl sich nicht ändert

Neben jedem Sensor sitzt eine kleine Stellschraube. Dreht sie vorsichtig mit dem Schraubendreher, bis die kleine Lampe daneben über Weiß leuchtet und über Schwarz ausgeht. Helles Sonnenlicht stört die Sensoren.
