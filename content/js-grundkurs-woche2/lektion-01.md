# Vergleichen mit ===, <, >

Bisher hast du Werte nur gespeichert und ausgegeben. Jetzt lässt du deinen Code **vergleichen** –
das Ergebnis ist immer ein Wahrheitswert (`true` oder `false`):

| Operator | Bedeutung |
|---|---|
| `===` | gleich |
| `!==` | ungleich |
| `<` / `>` | kleiner als / größer als |
| `<=` / `>=` | kleiner-gleich / größer-gleich |

```js
let a = 7;
let b = 3;
console.log(a > b);
console.log(a === b);
console.log(a !== b);
```

> 💡 Nutze für "gleich" immer drei Gleichheitszeichen (`===`), nicht nur zwei (`==`). `===`
> vergleicht auch den **Datentyp** mit – `5 === '5'` ist deshalb `false`, obwohl beide "wie 5
> aussehen". Das schützt dich vor überraschenden Fehlern.

Das Ergebnis eines Vergleichs kannst du wie jeden anderen Wert in einer Variable speichern:

```js
let alter = 20;
let istVolljaehrig = alter >= 18;
console.log(istVolljaehrig);
```
