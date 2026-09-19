# Mehrere Fälle mit else if

Manchmal reichen zwei Möglichkeiten nicht. Mit `else if` prüfst du beliebig viele Bedingungen
nacheinander – JavaScript nimmt den **ersten** Zweig, dessen Bedingung zutrifft, und ignoriert
den Rest:

```js
let punkte = 82;
if (punkte >= 90) {
  console.log('Note: Sehr gut');
} else if (punkte >= 75) {
  console.log('Note: Gut');
} else if (punkte >= 50) {
  console.log('Note: Befriedigend');
} else {
  console.log('Note: Nicht bestanden');
}
```

Bei `punkte = 82` schlägt die erste Bedingung (`>= 90`) fehl, die zweite (`>= 75`) passt – ab da
wird der Rest der Kette gar nicht mehr geprüft, selbst wenn `>= 50` auch zutreffen würde.

Die **Reihenfolge** ist deshalb wichtig: die spezifischste Bedingung sollte zuerst kommen.
