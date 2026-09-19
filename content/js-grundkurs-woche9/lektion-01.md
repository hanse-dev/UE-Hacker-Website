# Abschlussprojekt: Ein Mini-Quiz

Diese Woche bringst du alles zusammen, was du seit Woche 2 gelernt hast – Bedingungen, Schleifen,
Funktionen, Arrays, Objekte, Klassen und DOM-Interaktivität. Kein neues Konzept, nur die bekannten
Bausteine kombiniert zu einem kleinen, echten Programm: einem Quiz.

Die Fragen speicherst du als Array aus Instanzen einer eigenen Klasse `Frage` – genau wie in
Woche 8:

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

function gibFrage(index) {
  return fragen[index].frage;
}

console.log(gibFrage(0));
```

`gibFrage` (Woche 4) greift auf das Array `fragen` (Woche 5) zu und liest daraus die
`frage`-Property der `Frage`-Instanz an der gewünschten Stelle (Woche 8) – genauso, wie du es von
einem Objekt-Literal (Woche 6) kennst, nur diesmal über `new Frage(...)` erzeugt.
