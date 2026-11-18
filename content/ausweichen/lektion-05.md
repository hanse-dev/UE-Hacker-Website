# Erwischt!

Noch fällt der Stein einfach durch deinen Spieler hindurch. Jetzt wird es ernst: Trifft der Stein den Spieler, ist das Spiel vorbei.

Dafür brauchst du zwei neue Bausteine.

:::bloecke

**spieler berührt stein** (unter **Figuren**) ist eine Bedingung wie **Taste … gedrückt**. Sie stimmt, sobald sich die beiden Rechtecke überlappen. Mit den kleinen Menüs wählst du, welche Figuren gemeint sind.

**Spiel vorbei** (unter **Spiel**) hält das Spiel an und schreibt einen Text groß in die Mitte der Bühne. Den Text tippst du in das Feld daneben.

Setze beide zusammen mit einem **wenn … dann** in **jedes Bild**.

:::

:::python

`spieler.beruehrt(stein)` ist eine Bedingung wie `taste("links")`. Sie ist `True`, sobald sich die beiden Rechtecke überlappen.

`spiel_ende("Text")` hält das Spiel an und schreibt den Text groß in die Mitte der Bühne.

Setze beide zusammen mit einem `if` in `jedes_bild`.

:::

Jetzt kannst du richtig spielen. Wie lange hältst du durch? Mit ▶ Spielen geht es wieder von vorn los.

## Bonus: Deine Farben

Dein Spiel, deine Farben! Gib dem Spieler eine andere Farbe und färbe den Hintergrund ein.

<details><summary>Tipps anzeigen</summary>

:::bloecke

Der Block **Hintergrund** liegt unter **Spiel**. Er gehört in **beim Start**, denn die Farbe muss nur einmal gesetzt werden.

:::

:::python

`hintergrund("lila")` färbt die Bühne ein. Die Zeile gehört an den Anfang, nicht in `jedes_bild`, denn die Farbe muss nur einmal gesetzt werden.

:::

</details>
