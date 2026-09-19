# Zahlen, Text und Wahrheitswerte

Eine Variable kann ganz unterschiedliche **Arten** von Werten speichern. Die drei wichtigsten
heute:

| Datentyp | Beispiel | Bedeutung |
|---|---|---|
| Zahl (`number`) | `42` | Zahlen, mit denen du rechnen kannst |
| Text (`string`) | `'Katze'` | Text, immer in Anführungszeichen |
| Wahrheitswert (`boolean`) | `true` / `false` | Nur zwei mögliche Werte: wahr oder falsch |

Mit `typeof` kannst du herausfinden, welchen Datentyp ein Wert hat:

```js
console.log(typeof 42);
console.log(typeof 'Katze');
console.log(typeof true);
```

Das gibt `number`, `string` und `boolean` aus – genau die drei Zeilen der Tabelle oben.

Ein Text steht immer in Anführungszeichen (egal ob `'einfache'` oder `"doppelte"`) – ohne
Anführungszeichen sucht JavaScript nach einer **Variable** mit diesem Namen, nicht nach Text.
