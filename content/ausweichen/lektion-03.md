# Am Rand stoppen

Fahr mal ganz nach links: Dein Spieler verschwindet einfach von der Bühne! Das soll nicht passieren.

Die Idee: In jedem Bild prüfst du, ob der Spieler zu weit draußen ist. Wenn ja, stellst du ihn zurück an den Rand.

So sieht das für den **oberen** Rand aus (falls dein Spieler auch nach oben fahren kann):

:::bloecke

```bloecke
[logik] wenn
  [logik] y von spieler < 0
[logik] dann
  [figuren] setze y von spieler auf 0
```

Den Vergleich **… < …** findest du unter **Logik**. Mit dem kleinen Menü in der Mitte wählst du, ob er auf `=`, `<` oder `>` prüft. **y von spieler** liegt unter **Figuren**, das kleine Menü darin stellst du auf **x** oder **y**.

Solche Blöcke kommen in **jedes Bild**, und zwar **unter** die Blöcke, die den Spieler bewegen.

:::

:::python

```python
    if spieler.y < 0:
        spieler.y = 0
```

`<` heißt „kleiner als“, `>` heißt „größer als“. Solche Zeilen kommen in `jedes_bild`, und zwar **unter** die Zeilen, die den Spieler bewegen. Achte auf die Einrückung: `if` steht genauso weit eingerückt wie die anderen `if`-Zeilen.

:::

Für den linken Rand brauchst du dasselbe mit **x**.

## Und rechts?

Rechts ist es etwas kniffliger: x ist ja die **linke** Ecke des Spielers. Steht der Spieler ganz rechts, ist seine linke Ecke bei 400 minus seiner Breite.
