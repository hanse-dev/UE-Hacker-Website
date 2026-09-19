# Bedingungen verknüpfen: &&, || und !

Mit den logischen Operatoren kombinierst du mehrere Bedingungen zu einer einzigen:

| Operator | Bedeutung |
|---|---|
| `&&` | UND – nur `true`, wenn **beide** Seiten `true` sind |
| `\|\|` | ODER – `true`, wenn **mindestens eine** Seite `true` ist |
| `!` | NICHT – dreht einen Wahrheitswert um |

```js
let sonne = true;
let warm = false;
console.log(`Beides: ${sonne && warm}`);
console.log(`Mindestens eins: ${sonne || warm}`);
console.log(`Nicht warm: ${!warm}`);
```

Das lässt sich direkt in einer `if`-Bedingung verwenden, ohne den Vergleich vorher in einer
eigenen Variable zu speichern:

```js
let alter = 14;
let groesse = 150;
if (alter >= 12 && groesse >= 140) {
  console.log('Fahrt frei!');
}
```
