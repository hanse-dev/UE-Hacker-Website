# Stufe 5: Figuren fahren

Ein Quadrat besteht aus vier gleichen Teilen: ein Stück geradeaus, dann eine Vierteldrehung. Statt das viermal hinzuschreiben, lasst ihr das Auto wiederholen.

## Eigene Befehle bauen

Für „geradeaus“ braucht ihr jedes Mal mehrere Zeilen. Packt sie in einen eigenen Befehl mit einem Namen. Dann wird das Programm kurz und lesbar.

:::bloecke

Öffnet in der Blockliste **Fortgeschritten** und dann **Funktionen**. Klickt auf **Erstelle eine Funktion** und nennt sie `vor`. Auf der Fläche erscheint der Block **Funktion vor**: Da hinein kommen die Motor-Blöcke. Baut genauso `links` und `stopp`. Unter **Funktionen** liegen jetzt Blöcke wie **Aufruf vor**. Die zieht ihr in euer Programm, nicht den Funktionsblock selbst.

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

Der grüne Block **4-mal wiederholen** liegt unter **Schleifen**. Alles, was in ihm steckt, läuft so oft hintereinander, wie die Zahl vorn sagt. Die Zahl könnt ihr anklicken und ändern. Der Aufruf von `stopp` hängt unter der Schleife, nicht in ihr: Das Auto hält erst an, wenn alle vier Runden fertig sind.

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

## Ein vierter Befehl

Baut selbst einen vierten Befehl, zum Beispiel `rechts` oder `zurueck`.

:::bloecke

`rechts` ist wie `links`, nur fährt Motor A `Forward` und Motor B `Backward`. Bei `zurueck` fahren beide Motoren `Backward`.

:::

:::python

`rechts` ist wie `links`, nur bekommt `Motor_L` eine `1` und `Motor_R` eine `0`. Bei `zurueck` bekommen beide Motoren eine `0`.

:::
 Denkt euch damit eine eigene Figur aus, zum Beispiel einen Zickzack oder ein Rechteck mit Rückwärtsfahrt.

## Bonus: Dreieck oder Acht

Sucht euch eine Figur aus:

- **Dreieck:** drei gleich lange Seiten, am Ende steht das Auto wieder am Start.
- **Acht:** zwei Kreise nebeneinander, einer links herum und einer rechts herum.

<details>
<summary>Tipps anzeigen</summary>

**Dreieck**

- Wie oft muss die Wiederholung laufen?
- An jeder Ecke dreht das Auto weiter als beim Quadrat. Nach drei Ecken hat es sich genau einmal ganz herumgedreht, beim Quadrat erst nach vier. Die Wartezeit für die Drehung muss also länger sein als eure Zahl aus Stufe 4. Rechnet so: Teilt eure Zahl durch 3 und zählt das Ergebnis zu eurer Zahl dazu. Ein Beispiel: 400 geteilt durch 3 sind etwa 130. 400 plus 130 sind 530.

**Acht**

- Eine Acht besteht aus zwei Bögen wie im Bonus von Stufe 4.
- Baut euch dafür zwei eigene Befehle, einen für den Bogen nach links und einen für den Bogen nach rechts.

:::bloecke

- Im Bogen nach links fährt Motor A langsamer als Motor B, zum Beispiel mit `speed = 35` statt 70. Beide fahren `Forward`.

:::

:::python

- Ein Bogen-Befehl sieht so aus wie `vor()`, nur mit zwei verschiedenen Tempos:

```python
def bogen_links():
    auto.Motor_L(1, 35)
    auto.Motor_R(1, 70)
```

- Die Wartezeit steht nicht im Befehl, sondern dort, wo ihr ihn aufruft: `bogen_links()` und darunter `sleep(…)`.

:::
- Findet zuerst die Wartezeit für einen ganzen Kreis. Dieselbe Zeit braucht ihr dann für den zweiten Kreis.

</details>
