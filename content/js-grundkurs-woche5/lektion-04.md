# Schleife über ein Array

Genau wie bei einem Text (Woche 3) kannst du mit `for...of` jedes Element eines Arrays einzeln
durchgehen:

```js
let punkte = [12, 7, 19, 3];
for (const punkt of punkte) {
  console.log(punkt);
}
```

Bei jedem Durchlauf steht in `punkt` das **nächste** Element des Arrays – erst `12`, dann `7`,
dann `19`, dann `3`. Du musst dich dafür nicht um Indizes kümmern; `for...of` übernimmt das
Durchzählen für dich.

Das ist der übliche Weg, um jedes Element eines Arrays zu verarbeiten – egal ob du sie ausgeben,
verändern oder auswerten willst.
