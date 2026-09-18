# Dein Spiel, dein Stil

Du hast jetzt alle Bausteine für „Fang den Ball" selbst gebaut: ein Spielfeld, einen steuerbaren Schläger, eine Animationsschleife, Kollisionserkennung und einen Punktestand. Zeit, das Spiel schwerer – und zu deinem eigenen zu machen.

Ein einfacher Trick für eine Schwierigkeitskurve: das Tempo des Balls mit dem Punktestand steigen lassen.

```js
function tempoFuer(punkte) {
  return 3 + Math.floor(punkte / 5);
}
```

`Math.floor(zahl)` rundet immer nach unten ab – so bleibt das Tempo lange genug gleich, bevor es den nächsten Sprung macht (bei 5, 10, 15 Punkten, …).

Ab hier bist du dran! Ein paar Ideen, falls du noch mehr willst:

- eine zweite Ballfarbe, die zufällig gewählt wird (`Math.random()`)
- ein Hindernis, das der Schläger nicht berühren darf
- ein Extra-Leben, das gelegentlich auftaucht
- ein Highscore, den du dir merkst

Bau dein Spiel in der letzten Aufgabe komplett zusammen – aus den Teilen der letzten fünf Lektionen. Es muss nicht perfekt sein. Hauptsache, es ist **dein** Spiel.

Viel Spaß beim Spielen! 🎮
