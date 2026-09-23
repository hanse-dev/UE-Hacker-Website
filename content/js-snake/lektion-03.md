# Steuerung: Pfeiltaste wird Richtung

Die Schlange bewegt sich immer in eine **Richtung** – nach oben, unten, links oder rechts. Eine Richtung lässt sich super als Objekt mit `x` und `y` darstellen: `{x: 1, y: 0}` bedeutet "ein Kästchen nach rechts", `{x: 0, y: -1}` bedeutet "ein Kästchen nach oben" (nach oben wird `y` kleiner, nicht größer!).

```js
function richtungFuerTaste(taste) {
  if (taste === 'ArrowUp') return { x: 0, y: -1 };
  if (taste === 'ArrowDown') return { x: 0, y: 1 };
  if (taste === 'ArrowLeft') return { x: -1, y: 0 };
  if (taste === 'ArrowRight') return { x: 1, y: 0 };
  return { x: 0, y: 0 };
}

console.log(richtungFuerTaste('ArrowRight'));
```

Hast du die aktuelle Richtung, berechnest du die neue Kopf-Position ganz einfach durch Addition:

```js
function naechsterKopf(kopf, richtung) {
  return { x: kopf.x + richtung.x, y: kopf.y + richtung.y };
}

console.log(naechsterKopf({ x: 5, y: 5 }, { x: 1, y: 0 }));   // { x: 6, y: 5 }
```

> 💡 Das Muster "Taste → neuer Wert" kennst du schon aus [Lektion 2 der JS-Spielewerkstatt](/kurs/projekt-js-spielewerkstatt) (`bewegeSchlaeger`) – dort war das Ergebnis eine einzelne Zahl, hier ist es ein ganzes Richtungs-Objekt.
