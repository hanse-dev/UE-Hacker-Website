# Viele Steine

Ein einzelner Stein ist auf Dauer langweilig. Jetzt fallen gleich mehrere!

Für jeden Stein eine eigene Variable (stein1, stein2, stein3 …) wäre mühsam. Besser: Alle Steine kommen in eine **Liste**. Die Liste heißt `steine`.

:::bloecke

In der Vorlage steht schon, wie die Liste entsteht:

```bloecke
[variablen] setze steine auf
  [listen] erzeuge eine leere Liste
[schleifen] wiederhole 3-mal
  [listen] hänge … an die Liste steine an
    [figuren] neue Figur x (Zufallszahl) y (Zufallszahl) Breite 40 Höhe 40 Farbe rot
```

Erst ist die Liste leer, dann kommt dreimal ein neuer Stein dazu.

In **jedes Bild** steht eine Schleife **für jeden Wert stein aus der Liste** `steine` (unter **Schleifen**). Die Blöcke darin laufen einmal für jeden Stein der Liste. Beim ersten Mal ist **stein** der erste Stein, dann der zweite, dann der dritte.

Bisher bewegt die Schleife die Steine nur nach unten. Ergänze **in** der Schleife, was du für den einzelnen Stein gebaut hast: unten raus wieder nach oben (mit Punkt), und das Erwischt. Dann gilt alles für jeden Stein.

:::

:::python

In der Vorlage steht schon, wie die Liste entsteht:

```python
steine = []
for i in range(3):
    steine.append(figur(zufall(0, 360), zufall(-400, -40), 40, 40, "rot"))
```

Erst ist die Liste leer (`[]`), dann hängt `append` dreimal einen neuen Stein an.

In `jedes_bild` steht eine Schleife `for stein in steine:`. Alles, was darunter eingerückt ist, läuft einmal für jeden Stein der Liste. Beim ersten Mal ist `stein` der erste Stein, dann der zweite, dann der dritte.

Bisher bewegt die Schleife die Steine nur nach unten. Ergänze **in** der Schleife, was du für den einzelnen Stein geschrieben hast: unten raus wieder nach oben (mit Punkt), und das Erwischt. Dann gilt alles für jeden Stein. Achte auf die Einrückung: Diese Zeilen stehen eine Stufe tiefer als `for`.

:::

## Bonus: Ein Stern

Sterne fangen statt ausweichen: Ein gelber Stern **stern** fällt langsam herunter. Fängst du ihn, gibt es 5 Punkte und er startet wieder oben.

<details><summary>Tipps anzeigen</summary>

- Lege den Stern beim Start an, so wie früher den einzelnen Stein, aber gelb und etwas kleiner (30 × 30).
- Er fällt langsamer als die Steine, zum Beispiel um 3.
- Unten raus: wieder nach oben, wie beim Stein, aber ohne Punkt.
- Berührt der Spieler ihn: 5 Punkte dazu und den Stern wieder nach oben setzen.

</details>

## Ideen zum Weiterbauen

Dein Spiel ist fertig! Wenn du magst, bau es weiter aus:

- **Leben:** Statt sofort vorbei zieht ein Treffer ein Leben ab. Erst bei 0 Leben ist Schluss.
- **Turbo:** Solange die Leertaste gedrückt ist, fährt der Spieler doppelt so schnell.
- **Verschiedene Steine:** Manche Steine sind breiter oder schneller als andere.
