# Dein erstes Bild auf dem Canvas

Willkommen in der JS-Spielewerkstatt! Du baust hier Schritt für Schritt dein eigenes Browserspiel: „Fang den Ball". Die Sprache dafür ist **JavaScript** – die Sprache, in der (fast) jede Webseite und jedes Browserspiel geschrieben ist.

Auf dieser Seite hast du unten ein eigenes **Spielfeld** (ein `<canvas>`-Element mit der ID `spielfeld`). Dein Code läuft in einem abgeschotteten Bereich und zeichnet direkt darauf.

So holst du dir das Spielfeld und bereitest es zum Zeichnen vor:

```js
const canvas = document.getElementById('spielfeld');
const ctx = canvas.getContext('2d');
```

`ctx` ist dein Zeichenstift – der „2D-Kontext" des Canvas. Damit zeichnest du Rechtecke:

```js
ctx.fillStyle = 'yellow';       // welche Farbe
ctx.fillRect(50, 50, 100, 80);  // x, y, Breite, Höhe
```

`fillRect(x, y, breite, hoehe)` zeichnet ein gefülltes Rechteck. `(0, 0)` ist oben links im Spielfeld, x wächst nach rechts, y wächst nach unten.

> 💡 Jeder Klick auf „Ausführen" oder „Prüfen" startet deinen Code in einem frischen, leeren Spielfeld – frühere Zeichnungen sind dann weg. Das ist Absicht: so fängt jede Aufgabe sauber von vorne an.
