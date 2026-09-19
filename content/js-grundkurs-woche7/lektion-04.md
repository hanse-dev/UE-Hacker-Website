# Einen Zähler bauen

Eine Variable, die **außerhalb** der Klick-Funktion angelegt wird, bleibt zwischen den Klicks
erhalten – so baust du einen Zähler:

```js
let zaehlerWert = 0;
let knopf = document.querySelector('#knopf');
knopf.addEventListener('click', () => {
  zaehlerWert++;
  document.querySelector('#anzeige').textContent = zaehlerWert;
});
```

Bei jedem Klick läuft die Funktion erneut – `zaehlerWert++` erhöht dabei **dieselbe** Variable von
vorhin, nicht eine neue. Deshalb zählt die Anzeige bei jedem Klick weiter, statt immer wieder bei
1 anzufangen.

> 💡 `textContent = zaehlerWert` funktioniert auch mit einer Zahl (nicht nur Text) – JavaScript
> wandelt sie automatisch in Text um.
