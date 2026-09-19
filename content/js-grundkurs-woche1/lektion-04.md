# Rechnen und Text verbinden

Mit Zahlen kannst du ganz normal rechnen: `+`, `-`, `*` (mal) und `/` (geteilt):

```js
let a = 4;
let b = 3;
console.log(a + b);
console.log(a * b);
```

Willst du eine Zahl mitten in einem Text ausgeben, gibt es einen praktischen Trick: eine
**Template-Literal** – ein Text in **Backticks** (`` ` ``, nicht die normalen Anführungszeichen)
mit `${...}` für eingebaute Werte:

```js
let a = 4;
let b = 3;
console.log(`Die Summe von ${a} und ${b} ist ${a + b}`);
```

Alles, was zwischen `${` und `}` steht, wird ausgerechnet und ins Ergebnis eingesetzt. Das ist viel
übersichtlicher als Texte mit `+` zusammenzukleben (`'Summe: ' + (a + b)` funktioniert zwar auch,
aber Template-Literals lesen sich meist einfacher).
