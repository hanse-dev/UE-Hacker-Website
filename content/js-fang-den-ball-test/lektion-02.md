# Der Ball fällt

Ein stehendes Bild ist noch kein Spiel. Damit sich etwas bewegt, braucht dein Code eine
**Animationsschleife**: eine Funktion, die sich mit `requestAnimationFrame` selbst immer wieder
neu aufruft – etwa 60 Mal pro Sekunde.

```js
function frame() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);  // altes Bild löschen
  // ... neu zeichnen ...
  requestAnimationFrame(frame);                       // sich selbst erneut aufrufen
}
frame();   // einmal anstoßen, danach läuft es von allein
```

In jedem Frame rufst du `zeichneSchlaeger(ctx, schlaegerX)` und `zeichneBall(ctx, 200, ballY)` aus
Lektion 1 auf – nur dass sich `ballY` zwischendrin verändert, bevor der nächste Frame gezeichnet
wird. Schau dir das komplette Beispiel unten an: Schläger steht fest, Ball fällt.
