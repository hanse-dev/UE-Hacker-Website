# Mehrere Instanzen derselben Klasse

Der eigentliche Sinn einer Blaupause zeigt sich, wenn du mehrere Instanzen erzeugst – jede hat
ihre **eigenen** Property-Werte, völlig unabhängig von den anderen:

```js
class Spieler {
  constructor(name, punkte) {
    this.name = name;
    this.punkte = punkte;
  }
}

let spieler1 = new Spieler('Mia', 10);
let spieler2 = new Spieler('Jonas', 25);
console.log(spieler1.punkte, spieler2.punkte);
```

Auch wenn beide Instanzen aus derselben Klasse `Spieler` stammen: eine Methode, die `this.punkte`
verändert, betrifft immer nur **die eine** Instanz, über die sie aufgerufen wurde – die andere
bleibt unberührt.
