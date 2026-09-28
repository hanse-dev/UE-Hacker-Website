# Treffer! Kollision erkennen und Punkte zählen

Wie erkennt dein Code, ob der Ball wirklich auf dem Schläger gelandet ist? Das nennt man
**Kollisionserkennung**. Der Schläger ist 80 Pixel breit, seine linke Kante ist `schlaegerX`,
seine rechte Kante also `schlaegerX + 80`. Ein Treffer liegt vor, wenn

- der Ball unten genug angekommen ist (`ballY >= 270`), **und**
- die x-Position des Balls zwischen der linken und der rechten Kante des Schlägers liegt.

Beide Bedingungen müssen gleichzeitig gelten – das ist eine `&&`-Verknüpfung:

```js
function istTreffer(ballX, ballY, schlaegerX) {
  return ballY >= 270 && ballX >= schlaegerX && ballX <= schlaegerX + 80;
}
```

Auch diese Funktion wird im Beispiel unten sofort im Spiel verwendet: Bei jedem Frame prüft die
Schleife `istTreffer(...)` – trifft der Schläger, gibt es einen Punkt und der Ball startet wieder
oben, sonst fällt er weiter. Der Punktestand wird mit `ctx.fillText(text, x, y)` direkt aufs
Spielfeld geschrieben, du siehst ihn also live oben links mitzählen.
