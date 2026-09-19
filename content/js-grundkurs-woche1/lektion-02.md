# Werte merken mit Variablen

Mit `console.log()` kannst du Text ausgeben – aber ein Programm muss sich auch Dinge **merken**
können, zum Beispiel einen Punktestand oder einen Namen. Dafür gibt es **Variablen**.

Eine Variable erstellst du mit `let`, gibst ihr einen Namen und einen Startwert:

```js
let punkte = 0;
console.log(punkte);

punkte = 5;
console.log(punkte);
```

`let` erlaubt es, den Wert später zu **ändern** (siehst du oben: erst `0`, dann `5`). Es gibt auch
`const` – für Werte, die sich nie ändern sollen:

```js
const geburtsjahr = 2012;
console.log(geburtsjahr);
```

Versuchst du, eine `const`-Variable neu zu beschreiben, meldet JavaScript einen Fehler – das ist
Absicht, nicht kaputt! So schützt du Werte, die konstant bleiben sollen.

> 💡 Variablennamen dürfen keine Leerzeichen enthalten. Für Namen aus mehreren Wörtern schreibt man
> in JavaScript meist so: `meinPunktestand` (erstes Wort klein, jedes weitere Wort mit großem
> Anfangsbuchstaben – „camelCase").
