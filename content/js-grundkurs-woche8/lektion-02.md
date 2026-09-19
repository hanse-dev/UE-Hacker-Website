# Methoden in Klassen

Genau wie ein Objekt-Literal (Woche 6) kann eine Klasse Methoden haben – Funktionen, die über
`this` auf die Properties der jeweiligen Instanz zugreifen:

```js
class Rechteck {
  constructor(breite, hoehe) {
    this.breite = breite;
    this.hoehe = hoehe;
  }
  flaeche() {
    return this.breite * this.hoehe;
  }
}

let r = new Rechteck(5, 3);
console.log(r.flaeche());
```

`flaeche()` steht **einmal** in der Klasse, funktioniert aber für **jede** Instanz mit ihren
eigenen Werten – `this.breite`/`this.hoehe` beziehen sich immer auf die Instanz, über die die
Methode gerade aufgerufen wurde (`r` in diesem Beispiel).
