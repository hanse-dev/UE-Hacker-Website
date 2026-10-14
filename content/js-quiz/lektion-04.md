# Weiter zur nächsten Frage

Bisher steht in deinem Code überall `fragen[0]` – dein Quiz kennt nur die erste Frage. Jetzt
bekommt es ein Gedächtnis: eine Variable, die sich merkt, **welche Frage gerade dran ist**.

```js
let nummer = 0;
```

Überall, wo bisher `fragen[0]` stand, schreibst du ab jetzt `fragen[nummer]`. Solange `nummer` 0
ist, ändert sich nichts. Erhöhst du `nummer` aber auf 1, meint derselbe Code plötzlich die zweite
Frage.

> 💡 `nummer` wird mit `let` angelegt, nicht mit `const` – ihr Wert soll sich ja ändern.

## Die Knöpfe bleiben, nur ihr Text wechselt

Für die nächste Frage brauchst du keine neuen Knöpfe. Die drei vorhandenen bekommen einfach eine
neue Beschriftung. Dafür musst du sie später wiederfinden – deshalb merkt sich die Schleife jeden
Knopf in einem Array:

```js
const knoepfe = [];
// ... in der Schleife, nachdem der Knopf erzeugt wurde:
knoepfe.push(k);
```

Danach ist `knoepfe[0]` der erste Antwort-Knopf, `knoepfe[1]` der zweite und so weiter.

## Eine Funktion, die anzeigt, was dran ist

Alles, was zum Anzeigen einer Frage gehört, kommt in eine eigene Funktion. Sie schaut nach, welche
Frage gerade dran ist, und bringt die Seite auf diesen Stand:

```
zeigeFrage:
  hole die Frage mit der aktuellen Nummer
  schreibe ihren Text in #text
  beschrifte jeden der drei Knöpfe mit der passenden Antwort
```

Der Vorteil: Immer wenn sich `nummer` ändert, rufst du nur diese eine Funktion auf, und die Seite
stimmt wieder.

## Und nach der letzten Frage?

Irgendwann sind die Fragen aufgebraucht. Das Muster dafür kennst du schon vom Durchklicken eines
Arrays: Vor dem Anzeigen prüfst du, ob es den nächsten Eintrag überhaupt noch gibt.

```
erhöhe die Nummer um 1
wenn die Nummer kleiner ist als die Anzahl der Einträge:
  zeige den nächsten Eintrag
sonst:
  zeige eine Schlussmeldung
```
