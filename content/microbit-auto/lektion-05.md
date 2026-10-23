# Stufe 4: Kurven

Ein Lenkrad hat das Auto nicht. Es lenkt, indem die beiden Räder sich unterschiedlich drehen.

| Linkes Rad | Rechtes Rad | Das Auto |
|---|---|---|
| vorwärts | vorwärts | fährt geradeaus |
| rückwärts | vorwärts | dreht sich auf der Stelle nach links |
| vorwärts | rückwärts | dreht sich auf der Stelle nach rechts |
| langsam vorwärts | schnell vorwärts | fährt einen Bogen nach links |

## Auf der Stelle nach links drehen

:::bloecke

```bloecke
[eingabe] wenn Knopf A geklickt
  [minicar] motor = A Direction = Backward speed = 70
  [minicar] motor = B Direction = Forward speed = 70
  [grundlagen] pausiere (ms) 400
  [minicar] motor = A Direction = Forward speed = 0
  [minicar] motor = B Direction = Forward speed = 0
```

:::

:::python

```python
from microbit import *
from keyes_MiniCar import *

auto = MiniCar()

while True:
    if button_a.was_pressed():
        auto.Motor_L(0, 70)
        auto.Motor_R(1, 70)
        sleep(400)
        auto.Motor_stop()
```

:::

## Die Vierteldrehung finden

Wie lange muss das Auto drehen, damit es genau nach links schaut? Das ist bei jedem Auto und jedem Boden anders. Ändert die Wartezeit in kleinen Schritten, bis es passt, und schreibt euch die Zahl auf. Ihr braucht sie in der nächsten Stufe.

## Zwei Knöpfe, zwei Richtungen

Knopf **B** ist noch frei. Baut für ihn dasselbe wie für Knopf A, nur mit vertauschten Richtungen: Motor A (linkes Rad) fährt `Forward`, Motor B (rechtes Rad) `Backward`. Die beiden Blöcke zum Anhalten bleiben gleich. Dann dreht A nach links und B nach rechts.

## Bonus: Der weite Bogen

Bisher dreht euer Auto auf der Stelle. Jetzt soll es wie auf einer Rennstrecke eine weite Kurve fahren. Wer schafft einen ganzen Kreis, der am Startpunkt endet?

<details>
<summary>Tipps anzeigen</summary>

- Schaut in die Tabelle oben, letzte Zeile: Bei einem Bogen drehen **beide** Räder vorwärts, nur unterschiedlich schnell.
- Das Auto biegt immer zu der Seite ab, auf der das langsamere Rad sitzt.
- Je größer der Unterschied zwischen den beiden Tempos, desto enger wird der Bogen. Probiert verschiedene Paare aus, zum Beispiel 50 und 100. Bleibt mit dem langsamen Rad über 40, sonst brummt es nur.
- Für den ganzen Kreis sucht ihr die passende Wartezeit, genau wie bei der Vierteldrehung. Markiert den Startpunkt mit einem Stück Klebeband.

</details>
