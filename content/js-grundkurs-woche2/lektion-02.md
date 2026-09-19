# Entscheidungen mit if und else

Mit `if` lässt du Code nur dann laufen, wenn eine Bedingung `true` ist. Mit `else` gibst du an,
was stattdessen passieren soll, wenn sie `false` ist:

```js
let zahl = 8;
if (zahl % 2 === 0) {
  console.log(`${zahl} ist gerade`);
} else {
  console.log(`${zahl} ist ungerade`);
}
```

Der Operator `%` (Modulo) gibt den **Rest** einer Division zurück – `zahl % 2` ist `0`, wenn
`zahl` durch 2 teilbar ist, also gerade.

Die geschweiften Klammern `{ }` fassen zusammen, was zu einem Zweig gehört. Auch wenn dort nur
eine einzige Zeile steht, lohnt es sich, sie immer zu schreiben – ohne sie gehört nur die
**nächste** Zeile zum `if`, was schnell zu Überraschungen führt.
