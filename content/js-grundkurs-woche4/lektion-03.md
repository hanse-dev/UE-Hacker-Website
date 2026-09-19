# Warum Funktionen? Wiederverwendbarkeit

Der eigentliche Nutzen einer Funktion zeigt sich, wenn du sie mehrfach mit unterschiedlichen
Werten aufrufst – die Logik steht nur **einmal** im Code, wird aber beliebig oft verwendet:

```js
function istVolljaehrig(alter) {
  return alter >= 18;
}

console.log(istVolljaehrig(15));
console.log(istVolljaehrig(20));
console.log(istVolljaehrig(18));
```

Ohne Funktion müsstest du den Vergleich `alter >= 18` an jeder Stelle im Code neu hinschreiben, an
der du ihn brauchst – änderst du später die Regel (z.B. auf `alter >= 16`), müsstest du sie an
jeder einzelnen Stelle ändern. Mit einer Funktion genügt **eine** Änderung an **einer** Stelle.
