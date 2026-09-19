# Eine Frage auf der Übungsfläche anzeigen

Jetzt verbindest du das Fragen-Array mit der echten Übungsfläche (Woche 7) – statt die Frage nur
in der Konsole auszugeben, zeigst du sie direkt im Element `#text` an:

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

document.querySelector('#text').textContent = fragen[0].frage;
```

Nichts Neues hier – nur die Kombination aus Array-Zugriff (`fragen[0]`), Instanz-Property
(`.frage`) und DOM-Zuweisung (`.textContent = ...`), die du einzeln schon kennst.
