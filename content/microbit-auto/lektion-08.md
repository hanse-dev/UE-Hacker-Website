# Stufe 7: Hindernissen ausweichen

Stehenbleiben ist sicher, aber langweilig. Jetzt sucht sich das Auto selbst einen freien Weg, wie ein Staubsaugerroboter.

## Der Plan

1. Abstand messen.
2. Ist etwas näher als 15 cm: kurz zurücksetzen und ein Stück drehen.
3. Sonst: geradeaus fahren.
4. Wieder von vorn.

Schreibt so einen Plan immer zuerst in Worten auf. Dann ist der Code nur noch Übersetzen.

:::bloecke

```bloecke
[grundlagen] dauerhaft
  [variablen] setze abstand auf (Ultrasonic)
  [logik] wenn abstand > 0 und abstand < 15 dann
    [minicar] motor = A Direction = Backward speed = 70
    [minicar] motor = B Direction = Backward speed = 70
    [grundlagen] pausiere (ms) 300
    [minicar] motor = A Direction = Backward speed = 70
    [minicar] motor = B Direction = Forward speed = 70
    [grundlagen] pausiere (ms) 400
  [logik] ansonsten
    [minicar] motor = A Direction = Forward speed = 70
    [minicar] motor = B Direction = Forward speed = 70
```

:::

:::python

```python
from microbit import *
from keyes_MiniCar import *

auto = MiniCar()

while True:
    abstand = auto.get_distance()
    if 0 < abstand < 15:
        auto.Motor_L(0, 70)
        auto.Motor_R(0, 70)
        sleep(300)
        auto.Motor_L(0, 70)
        auto.Motor_R(1, 70)
        sleep(400)
    else:
        auto.Motor_L(1, 70)
        auto.Motor_R(1, 70)
    sleep(50)
```

:::

## Testen wie die Profis

Baut aus Büchern oder Kartons eine kleine Arena. Beobachtet das Auto eine Minute lang und notiert, wo es hängen bleibt. Ändert danach immer nur **eine** Zahl und testet neu. So merkt ihr, was die Änderung bewirkt hat. Die 15 bestimmt, wie früh das Auto ausweicht, die 300, wie weit es zurücksetzt, und die 400, wie weit es sich dreht. Bleibt es in Ecken hängen, probiert zum Beispiel eine längere Drehung.

Der Sensor sieht nur, was direkt vor ihm liegt. Schräge Wände, Stuhlbeine und weiche Stoffe erkennt er schlecht.

## Bonus: Mal links, mal rechts

Im Moment weicht euer Auto immer zur selben Seite aus. In einer Ecke kann es sich so festfahren. Lasst den Zufall entscheiden, ob es nach links oder nach rechts dreht.

<details>
<summary>Tipps anzeigen</summary>

Ihr braucht einen Würfel mit zwei Seiten:

:::bloecke

```bloecke
[mathematik] wähle eine zufällige Zahl von 0 bis 1
```

Den Block findet ihr unter **Mathematik**.

:::

:::python

```python
import random

zahl = random.randint(0, 1)
```

Die Zeile `import random` gehört ganz nach oben zu den anderen `import`-Zeilen.

:::

- Merkt euch die gewürfelte Zahl in einer Variable.
- Dann entscheidet eine Bedingung: Bei 0 dreht das Auto nach links, sonst nach rechts. Diese Bedingung (**wenn … dann … ansonsten** mit dem **=** aus **Logik**) steckt im oberen Teil eures wenn-Blocks, an der Stelle der Drehung. Ein wenn-Block darf in einem anderen stecken.
- Gewürfelt wird jedes Mal neu, wenn ein Hindernis auftaucht, nicht nur einmal am Anfang.

</details>
