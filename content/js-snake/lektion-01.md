# Das Spielfeld als Raster

Willkommen bei deinem Snake-Projekt! Anders als beim Ball-Spiel aus der JS-Spielewerkstatt bewegt sich hier alles auf einem unsichtbaren **Raster**: Statt an beliebigen Pixel-Positionen zu zeichnen, denkst du in Kästchen.

Dein Spielfeld ist 400×300 Pixel groß. Teilst du es in Kästchen von 20×20 Pixeln ein, bekommst du 20 Spalten und 15 Zeilen. Eine Rasterposition wie `(5, 5)` rechnest du für `fillRect` in Pixel um, indem du sie mit der Kästchengröße multiplizierst:

```js
const canvas = document.getElementById('spielfeld');
const ctx = canvas.getContext('2d');

const groesse = 20;
const gitterX = 5;
const gitterY = 5;

ctx.fillStyle = 'limegreen';
ctx.fillRect(gitterX * groesse, gitterY * groesse, groesse, groesse);
```

`gitterX * groesse` und `gitterY * groesse` sind die tatsächlichen Pixel-Koordinaten. Später wird `gitterX`/`gitterY` einfach eine Zahl, die du bei jeder Bewegung um genau 1 veränderst – kein krummes Pixel-Rechnen mehr.

> 💡 `ctx.fillRect()` kennst du schon aus [Lektion 1 der JS-Spielewerkstatt](/kurs/projekt-js-spielewerkstatt) – neu ist nur die Umrechnung von Gitter- in Pixel-Koordinaten.
