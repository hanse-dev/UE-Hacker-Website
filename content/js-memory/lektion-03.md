# Ein ganzes Brett mit einer Schleife

Ein Memory braucht viele Karten. Acht Karten einzeln zu bauen wäre mühsam – das erledigt eine Schleife für dich.

Zuerst legst du fest, welche Symbole es gibt. Jedes Symbol steht **zweimal** in der Liste, denn es sollen ja Paare sein:

```js
const karten = ['🐶', '🐱', '🦊', '🐸', '🐶', '🐱', '🦊', '🐸'];
```

Dann läuft eine `for`-Schleife durch die Liste. Bei jedem Durchgang entsteht eine neue Karte – genau wie in Lektion 1, nur eben achtmal:

```
für jede Stelle i in der Liste:
  erzeuge einen button
  gib ihm die id 'karte' + i        (also karte0, karte1, karte2, ...)
  zeige die Rückseite
  hänge ihn an die Übungsfläche
```

`'karte' + i` klebt Text und Zahl zusammen. Beim ersten Durchgang ist `i` gleich 0, die id heißt also `karte0`.

## Jede Karte kennt ihre Nummer

Jetzt kommt ein praktischer Trick: Die Klick-Funktion steht **in** der Schleife. Dadurch weiß jede Karte, welches `i` zu ihr gehört. Klickst du später auf die dritte Karte, schaut sie in `karten[2]` nach, welches Symbol sie zeigen soll.

Ab dieser Lektion beginnt jede Aufgabe mit ein paar Zeilen „Vorbereitung“. Sie schreiben „Memory“ in die Überschrift und räumen weg, was wir gerade nicht brauchen (`.remove()` löscht ein Element von der Seite). Diese Zeilen musst du nicht ändern.

> 💡 Mit `karte.style.width = '80px'` werden alle Karten gleich breit. Dann passen genau vier nebeneinander.
