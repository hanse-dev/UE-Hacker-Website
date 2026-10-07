# Stufe 5: Figuren fahren

Ein Quadrat besteht aus vier gleichen Teilen: ein Stück geradeaus, dann eine Vierteldrehung. Statt das viermal hinzuschreiben, lasst ihr das Auto wiederholen.

## Eigene Befehle bauen

Für „geradeaus“ braucht ihr jedes Mal mehrere Zeilen. Packt sie in einen eigenen Befehl mit einem Namen. Dann wird das Programm kurz und lesbar.

:::bloecke

Öffnet in der Blockliste **Fortgeschritten** und dann **Funktionen**. Klickt auf **Erstelle eine Funktion** und nennt sie `vor`. Baut genauso `links` und `stopp`.

```bloecke
[funktionen] Funktion vor
  [minicar] motor = A Direction = Forward speed = 70
  [minicar] motor = B Direction = Forward speed = 70
[funktionen] Funktion links
  [minicar] motor = A Direction = Backward speed = 70
  [minicar] motor = B Direction = Forward speed = 70
[funktionen] Funktion stopp
  [minicar] motor = A Direction = Forward speed = 0
  [minicar] motor = B Direction = Forward speed = 0
```

:::

:::python

```python
from microbit import *
from keyes_MiniCar import *

auto = MiniCar()

def vor():
    auto.Motor_L(1, 70)
    auto.Motor_R(1, 70)

def links():
    auto.Motor_L(0, 70)
    auto.Motor_R(1, 70)

def stopp():
    auto.Motor_stop()
```

Mit `def` baut ihr einen eigenen Befehl. Aufgerufen wird er mit seinem Namen und Klammern, zum Beispiel `vor()`.

:::

## Das Quadrat

:::bloecke

```bloecke
[eingabe] wenn Knopf A geklickt
  [schleifen] 4-mal wiederholen
    [funktionen] Aufruf vor
    [grundlagen] pausiere (ms) 1000
    [funktionen] Aufruf links
    [grundlagen] pausiere (ms) 400
  [funktionen] Aufruf stopp
```

:::

:::python

Diese Zeilen kommen unter die Befehle von oben:

```python
while True:
    if button_a.was_pressed():
        for i in range(4):
            vor()
            sleep(1000)
            links()
            sleep(400)
        stopp()
```

`for i in range(4):` wiederholt die eingerückten Zeilen viermal.

:::

Setzt für die Drehung eure Zahl aus Stufe 4 ein. Das Quadrat ist gelungen, wenn das Auto ungefähr dort anhält, wo es gestartet ist.
