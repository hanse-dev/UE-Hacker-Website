# Arrays: mehrere Werte in einer Variable

Ein **Array** speichert eine ganze Liste von Werten in einer einzigen Variable, in eckigen
Klammern `[ ]` durch Kommas getrennt:

```js
let farben = ['rot', 'gruen', 'blau'];
console.log(farben[0]);
console.log(farben[2]);
```

Auf ein einzelnes Element greifst du mit dem **Index** in eckigen Klammern zu – `farben[0]` ist
das **erste** Element, nicht das zweite. JavaScript zählt Indizes ab **0**:

| Index | 0 | 1 | 2 |
|---|---|---|---|
| Wert | `'rot'` | `'gruen'` | `'blau'` |

> ⚠️ `farben[1]` ist deshalb `'gruen'` (das **zweite** Element), nicht `'rot'` – ein sehr
> häufiger Anfängerfehler.
