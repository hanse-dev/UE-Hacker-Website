# Alles bewegt sich: die Animationsschleife

Bisher hast du nur ein einzelnes, unbewegtes Bild gezeichnet. Ein Spiel braucht aber Bewegung – und die entsteht, indem du **immer wieder** ein neues Bild zeichnest: erst löschen, dann neu zeichnen, an leicht veränderter Position. Wiederholt man das schnell genug (60 Mal pro Sekunde), sieht es aus wie eine flüssige Bewegung.

Der Browser stellt dafür `requestAnimationFrame` bereit:

```js
function frame() {
  ctx.clearRect(0, 0, canvas.width, canvas.height); // altes Bild löschen
  // ... hier neu zeichnen ...
  requestAnimationFrame(frame); // den nächsten Frame anfordern
}

frame(); // die Schleife anstoßen
```

`clearRect(x, y, breite, hoehe)` löscht einen Bereich des Canvas – ohne das würde sich jeder neue Ball über die alten legen und eine Spur hinterlassen.

Einen Kreis (unseren Ball) zeichnest du mit `arc`:

```js
ctx.beginPath();
ctx.arc(200, ballY, 10, 0, Math.PI * 2); // Mittelpunkt x/y, Radius, Start-/Endwinkel
ctx.fill();
```

Damit der Ball wirklich fällt, musst du seine y-Position bei jedem Frame ein Stück erhöhen – genau das rechnet deine Funktion `naechstePosition(y, tempo)` aus der ersten Aufgabe.

> 💡 `requestAnimationFrame` läuft so lange weiter, bis die Seite neu geladen wird oder der Sandbox-Bereich neu gestartet wird (z.B. durch „Neu starten" oder einen neuen Lauf) – dann verschwindet die alte Schleife automatisch.
