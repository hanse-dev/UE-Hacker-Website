# Die Schlange bewegt sich wirklich

Jetzt bringst du alles zusammen: eine Animationsschleife mit `requestAnimationFrame`, die bei jedem Frame den Kopf einen Schritt weiterbewegt und neu zeichnet.

```js
const canvas = document.getElementById('spielfeld');
const ctx = canvas.getContext('2d');
const groesse = 20;
let kopf = { x: 0, y: 5 };

function frame() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = 'limegreen';
  ctx.fillRect(kopf.x * groesse, kopf.y * groesse, groesse, groesse);

  kopf = { x: kopf.x + 1, y: kopf.y };

  requestAnimationFrame(frame);
}

frame();
```

`ctx.clearRect()` löscht das ganze Spielfeld vor jedem Frame – sonst würden die alten Positionen als Spur stehen bleiben. Wächst die Schlange später um ein Segment, musst du außerdem ihre Länge im Blick behalten:

```js
function gibNeueLaenge(laenge, gewachsen) {
  return gewachsen ? laenge + 1 : laenge;
}
```

> 💡 `requestAnimationFrame` und `clearRect` kennst du aus [Lektion 3 der JS-Spielewerkstatt](/kurs/projekt-js-spielewerkstatt) – dort ist ein Ball gefallen, hier bewegt sich stattdessen dein Schlangenkopf über das Raster.
