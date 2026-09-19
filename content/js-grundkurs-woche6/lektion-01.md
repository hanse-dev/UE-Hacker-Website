# Objekte: zusammengehörige Werte bündeln

Ein Array ordnet Werte nach **Position** (Index 0, 1, 2, …). Ein **Objekt** ordnet Werte stattdessen
nach **Namen** – praktisch, wenn ein Wert eine eigene Bedeutung hat, statt nur "der Wert an
Stelle 2" zu sein:

```js
let person = { name: 'Alex', alter: 12 };
console.log(person.name);
console.log(person.alter);
```

Ein Objekt-Literal steht in geschweiften Klammern `{ }`, mit `eigenschaft: wert`-Paaren, getrennt
durch Kommas. Mit der **Punkt-Notation** (`person.name`) liest du eine Eigenschaft (auch
**Property** genannt) aus.

> 💡 Anders als bei einem Array musst du dir bei einem Objekt keine Reihenfolge merken –
> `person.alter` funktioniert unabhängig davon, an welcher Stelle `alter` im Objekt steht.
