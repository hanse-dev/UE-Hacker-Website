# Eine Karte entsteht

Willkommen in der Memory-Werkstatt! In sieben Lektionen baust du ein Memory, das du wirklich spielen kannst. Wir fangen klein an: mit einer einzigen Karte.

In [Woche 7 des JS-Grundkurses](/kurs/js-grundkurs?week=7) hast du Elemente **gefunden** und **verändert**. Die Übungsfläche kennst du schon: eine Überschrift, ein Text, ein Knopf und eine Anzeige. Jetzt lernst du etwas Neues – du **erzeugst** eigene Elemente.

Das geht in drei Schritten:

```js
const zettel = document.createElement('p');   // 1. erzeugen
zettel.textContent = 'Hallo!';                // 2. beschriften
flaeche.appendChild(zettel);                  // 3. auf die Seite hängen
```

- `document.createElement('p')` baut ein neues Element – hier einen Absatz (`p`). Für unsere Karten nehmen wir `'button'`, denn Knöpfe kann man anklicken.
- Solange du das Element nicht anhängst, ist es unsichtbar. Erst `appendChild` setzt es ans Ende der Übungsfläche. Die Übungsfläche selbst findest du mit `document.querySelector('#dom-uebung')`.

Zwei Dinge machen die Karte noch besser:

- `karte.id = 'hund'` gibt ihr einen Namen. Damit findest du sie später mit `document.querySelector('#hund')` wieder.
- `karte.style.fontSize = '28px'` macht die Schrift größer. Über `.style` änderst du das Aussehen eines Elements.

> 💡 Die Symbole auf den Karten sind Emojis. Für JavaScript sind das ganz normale Textzeichen – du kannst sie einfach kopieren und zwischen Anführungszeichen setzen: `'🐶'`.
