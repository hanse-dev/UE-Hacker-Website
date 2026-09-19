# Eigene Funktionen schreiben

Eine **Funktion** ist ein benannter Codeblock, den du beliebig oft aufrufen kannst, ohne ihn
erneut abzutippen. Mit `function` deklarierst du eine, mit `return` gibst du ein Ergebnis zurück:

```js
function verdoppleZahl(zahl) {
  return zahl * 2;
}

console.log(verdoppleZahl(3));
console.log(verdoppleZahl(10));
```

`zahl` in den runden Klammern ist ein **Parameter** – ein Platzhalter für den Wert, den du beim
Aufruf mitgibst (`verdoppleZahl(3)` übergibt `3`). `return` beendet die Funktion sofort und gibt
den dahinterstehenden Wert an die Stelle zurück, an der die Funktion aufgerufen wurde – deshalb
kannst du `verdoppleZahl(3)` direkt in `console.log(...)` einsetzen, so wie jeden anderen Wert.

> 💡 Ohne `return` gibt eine Funktion `undefined` zurück, selbst wenn sie intern etwas berechnet
> hat – ein sehr häufiger Anfängerfehler.
