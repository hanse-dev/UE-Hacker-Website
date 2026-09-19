# Methoden: Funktionen in Objekten

Eine Property kann auch eine **Funktion** sein – dann heißt sie **Methode**. Innerhalb einer
Methode zeigt `this` auf das Objekt selbst, über das die Methode aufgerufen wurde:

```js
let rechner = {
  wert: 10,
  verdoppeln() {
    return this.wert * 2;
  }
};

console.log(rechner.verdoppeln());
```

`this.wert` greift auf die `wert`-Property **desselben** Objekts zu, in dem die Methode steht.
Ohne `this.` würde JavaScript nach einer eigenständigen Variable namens `wert` suchen – die es
hier gar nicht gibt.

> 💡 Vergiss beim Aufruf einer Methode nicht die runden Klammern: `rechner.verdoppeln()` **ruft**
> die Methode auf, `rechner.verdoppeln` (ohne Klammern) verweist nur auf die Funktion selbst,
> ohne sie auszuführen.
