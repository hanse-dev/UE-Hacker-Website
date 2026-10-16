# Über mehrere Spalten

Ein Item im Grid darf mehr als eine Zelle belegen:

```css
.gross {
  grid-column: span 2;     /* zwei Spalten breit */
}
.banner {
  grid-column: 1 / -1;     /* von der ersten bis zur letzten Linie: ganze Breite */
}
```

- `span 2` – „überspanne zwei Spalten“
- `1 / -1` – von **Linie** 1 bis zur letzten Linie. Gezählt werden die Linien **zwischen** den Spalten: Bei drei Spalten gibt es die Linien 1 bis 4; `-1` ist immer die letzte.

Für Zeilen gibt es dasselbe mit `grid-row`.

So entstehen Layouts wie bei Nachrichtenseiten: ein großer Aufmacher und mehrere kleine Meldungen daneben.
