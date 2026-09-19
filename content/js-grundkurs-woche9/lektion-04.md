# Durch alle Fragen klicken

Jetzt soll jeder Klick zur **nächsten** Frage weiterschalten – dafür brauchst du eine Variable
`index`, die sich zwischen den Klicks merkt, wo du gerade stehst (Woche 7), und eine Bedingung
(Woche 2), die prüft, ob noch eine weitere Frage übrig ist:

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
  new Frage('Farbe des Himmels?', 'blau'),
];

let index = 0;
let knopf = document.querySelector('#knopf');
knopf.addEventListener('click', () => {
  if (index < fragen.length) {
    document.querySelector('#text').textContent = fragen[index].frage;
    index++;
  } else {
    document.querySelector('#text').textContent = 'Fertig!';
  }
});
```

Solange `index` kleiner als `fragen.length` ist, zeigt der Klick die nächste Frage und zählt
`index` hoch. Ist das Array einmal komplett durchgeklickt, greift der `else`-Zweig und zeigt
stattdessen `'Fertig!'` – egal wie oft danach noch geklickt wird.
