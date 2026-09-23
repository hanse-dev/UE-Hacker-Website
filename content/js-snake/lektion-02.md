# Die Schlange als Liste von Segmenten

Eine Schlange besteht aus mehreren Segmenten – Kopf und Körper. Genau dafür ist ein **Array aus Objekten** gemacht: jedes Segment ist ein Objekt mit `x` und `y`, alle Segmente zusammen bilden die Schlange.

```js
const schlange = [
  { x: 5, y: 5 },  // Kopf
  { x: 4, y: 5 },
  { x: 3, y: 5 },  // Schwanz
];
```

Um die ganze Schlange zu zeichnen, läufst du mit `for...of` durch alle Segmente und zeichnest jedes einzeln – genau wie ein einzelnes Segment aus Lektion 1, nur wiederholt:

```js
const canvas = document.getElementById('spielfeld');
const ctx = canvas.getContext('2d');
const groesse = 20;

for (const segment of schlange) {
  ctx.fillRect(segment.x * groesse, segment.y * groesse, groesse, groesse);
}
```

Um später zu prüfen, ob an einer bestimmten Position schon ein Segment liegt (wichtig für die Kollisionserkennung in einer späteren Lektion), durchsuchst du das Array mit einer Schleife:

```js
function istSegmentAn(schlange, x, y) {
  for (const segment of schlange) {
    if (segment.x === x && segment.y === y) return true;
  }
  return false;
}
```

> 💡 Arrays kennst du aus [Woche 5](/kurs/js-grundkurs?week=5) und `for...of`-Schleifen über Objekte aus [Woche 6 des JS-Grundkurses](/kurs/js-grundkurs?week=6) – hier kombinierst du beides zum ersten Mal in einem Array aus Objekten.
