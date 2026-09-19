# Die Antwort per Klick aufdecken

Jetzt kommt die Interaktivität dazu: ein Klick auf den Knopf soll die passende Antwort anzeigen –
genau das Klick-Muster aus Woche 7, nur mit Daten aus dem Fragen-Array:

```js
class Frage {
  constructor(frage, antwort) {
    this.frage = frage;
    this.antwort = antwort;
  }
}

let fragen = [
  new Frage('Hauptstadt von Frankreich?', 'Paris'),
  new Frage('2 + 2?', '4'),
];

let knopf = document.querySelector('#knopf');
knopf.addEventListener('click', () => {
  document.querySelector('#anzeige').textContent = fragen[0].antwort;
});
```

So ein kleiner Baustein – Array aus Instanzen + Klick-Listener – ist schon die Grundlage für
ziemlich viele interaktive Web-Anwendungen, nicht nur für Quizze.
