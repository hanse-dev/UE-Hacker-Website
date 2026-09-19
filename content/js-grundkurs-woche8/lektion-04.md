# Ein Array aus Instanzen

Genau wie ein Array aus Objekt-Literalen (Woche 6) kannst du ein Array aus Klassen-Instanzen
bauen – praktisch, wenn du viele gleichartige Dinge verwalten willst:

```js
class Tier {
  constructor(name, art) {
    this.name = name;
    this.art = art;
  }
}

let tiere = [
  new Tier('Bello', 'Hund'),
  new Tier('Mimi', 'Katze'),
];

for (const tier of tiere) {
  console.log(`${tier.name}: ${tier.art}`);
}
```

`for...of` funktioniert hier genau wie gewohnt – bei jedem Durchlauf ist `tier` einfach eine ganze
Instanz mit ihren eigenen Properties, aus der du dir wie gewohnt mit der Punkt-Notation einzelne
Werte holst.
