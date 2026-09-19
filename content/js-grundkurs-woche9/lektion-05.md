# Den Punktestand auswerten

Zum Schluss kombinierst du eine Funktion (Woche 4), die ein Array aus Objekten auswertet
(Woche 5/6), mit einem Klick, der das Ergebnis anzeigt (Woche 7):

```js
let antworten = [
  { richtig: true },
  { richtig: false },
  { richtig: true },
];

function zaehleRichtige(liste) {
  let anzahl = 0;
  for (const a of liste) {
    if (a.richtig) {
      anzahl++;
    }
  }
  return anzahl;
}

let knopf = document.querySelector('#knopf');
knopf.addEventListener('click', () => {
  document.querySelector('#anzeige').textContent = zaehleRichtige(antworten);
});
```

`zaehleRichtige` zählt mit einer Schleife (Woche 3) und einer Bedingung (Woche 2), wie viele
Objekte im Array eine `richtig`-Property mit dem Wert `true` haben – der Klick-Listener ruft die
Funktion auf und zeigt das Ergebnis an. Sieben Wochen JavaScript in sieben Zeilen Code.
