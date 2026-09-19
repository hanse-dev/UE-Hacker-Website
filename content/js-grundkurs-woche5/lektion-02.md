# Elemente hinzufügen und entfernen: push und pop

Mit `.push(wert)` fügst du ein Element **hinten** an ein Array an, mit `.pop()` entfernst du das
**letzte** Element wieder:

```js
let einkaufsliste = ['Brot', 'Milch'];
einkaufsliste.push('Eier');
console.log(einkaufsliste);

einkaufsliste.pop();
console.log(einkaufsliste);
```

Beide Methoden verändern das Array **direkt** (kein neues Array, keine Zuweisung mit `=` nötig).

> 💡 `.push(wert)` gibt selbst die **neue Länge** des Arrays zurück, nicht das Array – wenn du das
> Ergebnis von `.push()` in einer Variable speicherst, bekommst du dort also eine Zahl, kein
> Array.
