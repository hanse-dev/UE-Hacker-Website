# Ein Stein fällt

Jetzt kommt die Gefahr: ein roter Stein, der von oben herunterfällt.

Fallen heißt: Der Stein kommt in jedem Bild ein Stück weiter nach unten. Sein **y** wird also in jedem Bild ein bisschen größer.

:::bloecke

Dafür brauchst du wieder den Block **ändere … von … um** aus **Figuren**. Im ersten kleinen Menü wählst du **y**, im zweiten den **stein**.

:::

:::python

Dafür brauchst du wieder `+=`, diesmal mit `stein.y`.

:::

## Wieder von vorn

Ein Stein reicht für das ganze Spiel, wenn er wiederkommt. Ist er unten aus der Bühne raus (y größer als 400), setzt du ihn wieder nach oben:

- y wird -40. Das ist knapp **über** der Bühne. Dann taucht er langsam auf, statt plötzlich da zu sein.
- Damit es spannend bleibt, kommt er jedes Mal an einer anderen Stelle: x wird eine **Zufallszahl** von 0 bis 360.

Wie prüft man „größer als“? Das kennst du schon vom Rand aus der letzten Lektion.

:::bloecke

Die **Zufallszahl von … bis …** findest du unter **Spiel**. So würfelt man zum Beispiel eine Zahl von 1 bis 6:

```bloecke
[variablen] setze wurf auf
  [aktion] Zufallszahl von 1 bis 6
```

In einem **wenn … dann** dürfen mehrere Blöcke untereinander stehen. Sie laufen dann alle, wenn die Bedingung stimmt.

:::

:::python

`zufall(von, bis)` gibt dir eine zufällige ganze Zahl. So würfelt man zum Beispiel:

```python
wurf = zufall(1, 6)
```

In einem `if` können mehrere Zeilen stehen, wenn sie alle gleich weit eingerückt sind.

:::

> 💡 Warum bis 360 und nicht bis 400? Der Stein ist 40 breit. Bei x = 400 wäre er schon rechts aus der Bühne heraus.
