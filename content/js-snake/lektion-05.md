# Game Over: Kollision mit sich selbst und dem Rand

Achtung, eine Falle: Zwei Objekte mit denselben Werten sind in JavaScript trotzdem **nicht gleich**, wenn du sie mit `===` vergleichst – `===` prüft bei Objekten, ob es dieselbe Stelle im Speicher ist, nicht ob die Werte gleich sind.

```js
const a = { x: 1, y: 1 };
const b = { x: 1, y: 1 };
console.log(a === b);                     // false – zwei verschiedene Objekte!
console.log(a.x === b.x && a.y === b.y);  // true – aber ihre Werte stimmen überein
```

Deshalb vergleichst du bei der Kollisionserkennung immer `x` und `y` einzeln, nie das ganze Objekt auf einmal. Für die Selbstkollision prüfst du, ob der Kopf dieselbe Position wie irgendein Körper-Segment hat:

```js
function istSelbstKollision(kopf, koerper) {
  for (const segment of koerper) {
    if (segment.x === kopf.x && segment.y === kopf.y) return true;
  }
  return false;
}
```

Für die Randkollision reicht ein einfacher Bereichs-Check: Ist der Kopf negativ oder größer/gleich der Anzahl Spalten bzw. Zeilen, ist er über den Rand hinaus.

```js
function istRandKollision(kopf, spaltenAnzahl, zeilenAnzahl) {
  return kopf.x < 0 || kopf.x >= spaltenAnzahl || kopf.y < 0 || kopf.y >= zeilenAnzahl;
}
```

> 💡 Das Grundgerüst dieser Kollisionsprüfung kennst du aus [Lektion 4 der JS-Spielewerkstatt](/kurs/projekt-js-spielewerkstatt) (`istTreffer`) – dort ging es um Ball und Schläger, hier prüfst du den Kopf gegen den eigenen Körper und gegen die Spielfeldgrenzen.
