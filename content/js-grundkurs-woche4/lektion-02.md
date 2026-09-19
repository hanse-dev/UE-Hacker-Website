# Mehrere Parameter

Eine Funktion kann mehrere Parameter entgegennehmen, getrennt durch Kommas – beim Aufruf gibst du
die Werte in genau dieser Reihenfolge mit:

```js
function addiere(a, b) {
  return a + b;
}

console.log(addiere(4, 5));
```

`addiere(4, 5)` heißt: `a` wird `4`, `b` wird `5`. Die Reihenfolge beim Aufruf muss zur
Reihenfolge der Parameter in der Funktions-Deklaration passen – `addiere(5, 4)` würde hier
zufällig dasselbe Ergebnis liefern (Addition ist symmetrisch), bei Subtraktion oder Division wäre
das Ergebnis dagegen komplett anders.
