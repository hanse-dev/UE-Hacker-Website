# Ein Array aus Objekten

Arrays und Objekte lassen sich kombinieren – besonders nützlich ist ein **Array aus Objekten**,
zum Beispiel eine Liste von Personen mit mehreren Eigenschaften pro Person:

```js
let schueler = [
  { name: 'Mia', note: 2 },
  { name: 'Jonas', note: 1 },
];

for (const person of schueler) {
  console.log(`${person.name}: ${person.note}`);
}
```

`for...of` funktioniert hier genau wie bei einem Array aus Zahlen (Woche 5) – nur dass `person`
bei jedem Durchlauf ein ganzes Objekt ist, aus dem du dir mit `person.name`/`person.note` einzelne
Werte herausholst.

Dieses Muster – ein Array aus Objekten, jedes mit denselben Properties – begegnet dir sehr häufig,
sobald du mit echten Datenlisten arbeitest (Spieler:innen, Produkte, Nachrichten, …).
