# Dein Spiel, dein Stil

Fast fertig! Ein echtes Snake-Spiel braucht noch einen Punktestand und ein Gefühl für Schwierigkeit. `Math.floor()` rundet Kommazahlen ab – praktisch, wenn du z.B. aus Punkten eine ganze "Stufe" berechnen willst:

```js
console.log(Math.floor(9.7));   // 9
console.log(Math.floor(3.2));   // 3
```

Ein einfaches Punktesystem: Die Schlange startet mit 3 Segmenten, für jedes zusätzliche Segment gibt es 10 Punkte. So läuft das Prinzip ab:

```
function punkteFuerLaenge(laenge) {
  gib zurück: Math.max(0, (laenge minus 3) mal 10)
}
```

Jetzt ist dein Snake-Projekt komplett: Raster (Lektion 1), Segmente als Array (Lektion 2), Steuerung (Lektion 3), Bewegungsloop (Lektion 4) und Kollisionserkennung (Lektion 5) – bau daraus dein eigenes, vollständiges Spiel!

> 💡 Bau ruhig eigene Ideen ein: eine zweite Farbe für den Kopf, ein Hindernis, das die Schlange nicht berühren darf, oder ein Extra-Leben. Wichtig ist nur, dass sich am Ende wirklich etwas auf dem Spielfeld bewegt.
