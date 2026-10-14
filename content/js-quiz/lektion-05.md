# Punkte zählen

Ein Quiz ohne Punkte ist nur halb so spannend. Du brauchst dafür zwei Dinge: eine Variable, die
mitzählt, und eine Stelle auf der Seite, an der man den Stand sieht.

## Die Zähl-Variable

```js
let punkte = 0;
```

Wie bei `nummer` gilt: `let`, weil sich der Wert ändert. Einen Zähler um 1 erhöhen kennst du aus
Woche 7 – `punkte++` ist die Kurzform von `punkte = punkte + 1`.

Wichtig ist nur die **Stelle**, an der gezählt wird: Einen Punkt gibt es nicht für jeden Klick,
sondern nur für eine richtige Antwort.

## Ein neues Element für die Anzeige

Die Übungsfläche hat kein freies Element mehr: In `#text` steht die Frage, in `#anzeige` die
Rückmeldung. Für den Punktestand erzeugst du deshalb ein neues Element – so wie die Knöpfe in
Lektion 2, nur diesmal einen Textabsatz:

```js
const stand = document.createElement('p');
```

`'p'` steht für *paragraph*, also Absatz. Auch dieses Element ist zuerst unsichtbar. Diesmal soll
es nicht vor einem bestimmten Element landen, sondern ganz unten. Dafür hängst du es an die
Übungsfläche selbst an:

```js
const flaeche = document.querySelector('#dom-uebung');
flaeche.appendChild(stand);
```

`#dom-uebung` ist der Kasten, in dem Überschrift, Text, Knopf und Anzeige stecken.
`appendChild` hängt ein Element als **letztes Kind** hinein – es erscheint also unter allem
anderen.

> 💡 `before` und `appendChild` machen fast dasselbe: Beide setzen ein neues Element auf die Seite.
> Der Unterschied ist nur der Ort – `before` vor einem bestimmten Element, `appendChild` ganz am
> Ende eines Kastens.

## Zählen und anzeigen gehören zusammen

Eine Variable zu ändern, ändert noch nichts auf der Seite. Nach jedem `punkte++` musst du den
neuen Stand auch in das Element schreiben – sonst zählt dein Quiz heimlich richtig, zeigt aber
weiter den alten Wert.
