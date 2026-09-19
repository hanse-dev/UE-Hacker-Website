# Schleife über einen Text: for...of

Ein Text (`string`) lässt sich wie eine Reihe einzelner Zeichen durchlaufen – mit `for...of`
bekommst du bei jedem Durchlauf das nächste Zeichen:

```js
let wort = 'Katze';
for (const zeichen of wort) {
  console.log(zeichen);
}
```

Das gibt `K`, `a`, `t`, `z`, `e` aus – jeweils ein Zeichen pro Zeile.

`for...of` eignet sich perfekt, um einen Text Zeichen für Zeichen auszuwerten – zum Beispiel, um
zu zählen, wie oft ein bestimmter Buchstabe vorkommt:

```js
let wort = 'Ananas';
let anzahlN = 0;
for (const zeichen of wort) {
  if (zeichen === 'n') {
    anzahlN++;
  }
}
console.log(anzahlN);
```

> 💡 Achte auf Groß-/Kleinschreibung: `'n' === 'N'` ist `false` – ein großes N wird bei diesem
> Vergleich nicht mitgezählt.
