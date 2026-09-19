# Klassen: Blaupausen für Objekte

In Woche 6 hast du Objekte einzeln von Hand geschrieben (`{ name: 'Alex', alter: 12 }`). Eine
**Klasse** ist eine **Blaupause** dafür – ein wiederverwendbares Muster, mit dem du beliebig viele
gleichartige Objekte erzeugst:

```js
class Haustier {
  constructor(name, art) {
    this.name = name;
    this.art = art;
  }
}

let bello = new Haustier('Bello', 'Hund');
console.log(bello.name, bello.art);
```

Der `constructor` läuft automatisch, sobald du mit `new Haustier(...)` ein **neues Objekt** aus
der Klasse erzeugst (eine **Instanz**). Die Parameter (`name`, `art`) landen über `this.name = ...`
als Properties auf der neuen Instanz – genau wie bei einem Objekt-Literal, nur diesmal
wiederverwendbar für beliebig viele Haustiere.

> ⚠️ Ohne `this.` davor legst du **keine** Property an, sondern veränderst nur den Parameter
> selbst – mehr dazu im Debug-Abschnitt dieser Woche.
