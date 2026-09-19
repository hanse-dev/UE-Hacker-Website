# Arrays und Bedingungen kombinieren

Genau wie bei Zahlenbereichen (Woche 3) zeigt sich die Stärke einer Schleife über ein Array, wenn
du sie mit einer Bedingung kombinierst – so wertest du nur bestimmte Elemente aus:

```js
let zahlen = [4, 9, 15, 22, 7];
let anzahlGerade = 0;
for (const zahl of zahlen) {
  if (zahl % 2 === 0) {
    anzahlGerade++;
  }
}
console.log(`Gerade Zahlen: ${anzahlGerade}`);
```

Die Schleife geht jedes Element durch, das `if` prüft bei **jedem** Durchlauf, ob es zur Bedingung
passt – nur dann wird gezählt (oder summiert, oder etwas anderes gemacht). Elemente, die nicht
passen, werden einfach übersprungen.
