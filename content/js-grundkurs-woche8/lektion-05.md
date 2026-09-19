# Instanzen, Schleifen und Bedingungen kombinieren

Wie bei jedem anderen Array aus Objekten (Woche 6) zeigt sich die Stärke erst richtig, wenn du ein
Array aus Instanzen mit einer Bedingung auswertest:

```js
class Spieler {
  constructor(name, punkte) {
    this.name = name;
    this.punkte = punkte;
  }
}

let spieler = [
  new Spieler('Mia', 45),
  new Spieler('Jonas', 82),
  new Spieler('Zoe', 30),
];

let anzahlGut = 0;
for (const s of spieler) {
  if (s.punkte >= 50) {
    anzahlGut++;
  }
}
console.log(`Bestanden: ${anzahlGut}`);
```

Ob die Instanzen aus `new Spieler(...)` oder aus einem einfachen Objekt-Literal `{ name, punkte }`
stammen, spielt für die Schleife und die Bedingung keine Rolle – beide lassen sich mit
`s.punkte` gleich auswerten. Klassen sind vor allem dann nützlich, wenn die Objekte zusätzlich
**Methoden** (Woche 8, Lektion 2) haben sollen, die einfache Objekt-Literale nicht so
übersichtlich anbieten.
