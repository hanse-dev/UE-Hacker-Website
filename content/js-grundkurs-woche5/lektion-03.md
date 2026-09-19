# Die Länge eines Arrays: length

Mit `.length` bekommst du, wie viele Elemente ein Array hat:

```js
let tiere = ['Hund', 'Katze', 'Maus', 'Vogel'];
console.log(tiere.length);
console.log(tiere[tiere.length - 1]);
```

`tiere.length` ist hier `4` – aber der **letzte gültige Index** ist `3` (nicht `4`, da bei 0
gezählt wird). `tiere[tiere.length - 1]` ist deshalb der zuverlässige Weg, an das letzte Element
zu kommen, egal wie lang das Array gerade ist.

> ⚠️ `tiere[tiere.length]` (ohne das `- 1`) liegt **außerhalb** des Arrays – JavaScript wirft dabei
> keinen Fehler, sondern gibt einfach `undefined` zurück.
