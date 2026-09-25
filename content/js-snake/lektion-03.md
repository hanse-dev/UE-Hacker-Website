# Steuerung: Pfeiltaste wird Richtung

Die Schlange bewegt sich immer in eine **Richtung** – nach oben, unten, links oder rechts. Eine Richtung lässt sich super als Objekt mit `x` und `y` darstellen: `{x: 1, y: 0}` bedeutet "ein Kästchen nach rechts", `{x: 0, y: -1}` bedeutet "ein Kästchen nach oben" (nach oben wird `y` kleiner, nicht größer!).

Das Muster dahinter: eine Kette aus `if`s, die je nach Eingabe einen anderen Wert zurückgibt. Zum Beispiel bei der Anzahl Beine verschiedener Tiere:

```js
function anzahlBeine(tier) {
  if (tier === 'spinne') return 8;
  if (tier === 'hund') return 4;
  if (tier === 'vogel') return 2;
  return 0;
}

console.log(anzahlBeine('hund'));
```

Genauso baust du `richtungFuerTaste(taste)`: für jede Pfeiltaste ein eigenes `if`, das ein Richtungs-Objekt zurückgibt.

Hast du die aktuelle Richtung, berechnest du die neue Kopf-Position ganz einfach durch Addition. So läuft das Prinzip ab:

```
function naechsterKopf(kopf, richtung) {
  gib ein neues Objekt zurück: x = kopf.x + richtung.x, y = kopf.y + richtung.y
}
```

> 💡 Das Muster "Taste → neuer Wert" kennst du schon aus [Lektion 2 der JS-Spielewerkstatt](/kurs/projekt-js-spielewerkstatt) (`bewegeSchlaeger`) – dort war das Ergebnis eine einzelne Zahl, hier ist es ein ganzes Richtungs-Objekt.
