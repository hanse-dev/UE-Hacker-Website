# Funktionen mit allem kombinieren

Eine Funktion kann alles enthalten, was du bisher gelernt hast – Variablen, Bedingungen und
Schleifen. Das macht Funktionen besonders mächtig: du verpackst eine ganze Berechnung in einen
einzigen, wiederverwendbaren Aufruf.

```js
function summeBis(n) {
  let summe = 0;
  for (let i = 1; i <= n; i++) {
    summe += i;
  }
  return summe;
}

console.log(summeBis(5));
```

`summeBis` nutzt intern eine `for`-Schleife (Woche 3), um die Summe aller Zahlen von 1 bis `n` zu
berechnen – von außen betrachtet ist das nur ein einziger Aufruf `summeBis(5)`, der komplexe
Schleifen-Code bleibt innerhalb der Funktion versteckt.
