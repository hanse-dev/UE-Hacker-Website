# Game Over: Kollision mit sich selbst und dem Rand

Achtung, eine Falle: Zwei Objekte mit denselben Werten sind in JavaScript trotzdem **nicht gleich**, wenn du sie mit `===` vergleichst – `===` prüft bei Objekten, ob es dieselbe Stelle im Speicher ist, nicht ob die Werte gleich sind.

```js
const a = { x: 1, y: 1 };
const b = { x: 1, y: 1 };
console.log(a === b);                     // false – zwei verschiedene Objekte!
console.log(a.x === b.x && a.y === b.y);  // true – aber ihre Werte stimmen überein
```

Deshalb vergleichst du bei der Kollisionserkennung immer `x` und `y` einzeln, nie das ganze Objekt auf einmal. Für die Selbstkollision prüfst du, ob der Kopf dieselbe Position wie irgendein Körper-Segment hat. So läuft das Prinzip ab:

```
function istSelbstKollision(kopf, koerper) {
  für jedes segment in koerper:
    wenn segment.x gleich kopf.x UND segment.y gleich kopf.y ist:
      gib true zurück
  gib false zurück
}
```

Für die Randkollision reicht ein einfacher Bereichs-Check: Ist der Kopf negativ oder größer/gleich der Anzahl Spalten bzw. Zeilen, ist er über den Rand hinaus.

```
function istRandKollision(kopf, spaltenAnzahl, zeilenAnzahl) {
  gib zurück: kopf.x kleiner 0 ODER kopf.x mindestens spaltenAnzahl ODER kopf.y kleiner 0 ODER kopf.y mindestens zeilenAnzahl
}
```

> 💡 Das Grundgerüst dieser Kollisionsprüfung kennst du aus [Lektion 4 der JS-Spielewerkstatt](/kurs/projekt-js-spielewerkstatt) (`istTreffer`) – dort ging es um Ball und Schläger, hier prüfst du den Kopf gegen den eigenen Körper und gegen die Spielfeldgrenzen.
