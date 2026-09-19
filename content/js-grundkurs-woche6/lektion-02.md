# Properties ändern und hinzufügen

Mit der Punkt-Notation kannst du eine Property nicht nur lesen, sondern auch **verändern** oder
eine ganz neue hinzufügen:

```js
let auto = { marke: 'VW', farbe: 'rot' };
auto.farbe = 'blau';
auto['baujahr'] = 2020;
console.log(auto);
```

`auto.farbe = 'blau'` überschreibt die bestehende Property, `auto['baujahr'] = 2020` legt eine
komplett neue an – beide Schreibweisen (`auto.baujahr` und `auto['baujahr']`) funktionieren
gleichwertig, solange der Name direkt als Text dasteht.

> 💡 Nur die **eckige** Klammer-Schreibweise (`auto['baujahr']`) funktioniert auch, wenn der
> Property-Name in einer **Variable** steht (z.B. `auto[meineVariable]`) – dazu mehr im
> Debug-Abschnitt dieser Woche.
