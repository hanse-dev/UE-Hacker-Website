# Schleifen und Bedingungen kombinieren

Die größte Stärke einer Schleife zeigt sich, wenn du sie mit einer Bedingung kombinierst – so
wertest du viele Werte aus und zählst oder summierst nur die, die zu einem Kriterium passen:

```js
let anzahlGerade = 0;
for (let i = 1; i <= 10; i++) {
  if (i % 2 === 0) {
    anzahlGerade++;
  }
}
console.log(`Gerade Zahlen: ${anzahlGerade}`);
```

Der Ablauf: die Schleife zählt `i` von 1 bis 10 hoch, und bei **jedem** Durchlauf prüft das `if`,
ob die aktuelle Zahl gerade ist. Nur dann wird `anzahlGerade` erhöht – die ungeraden Zahlen
werden einfach übersprungen, ohne dass die Schleife selbst unterbrochen wird.

Dieses Muster – Schleife durchlaufen, pro Durchlauf mit `if` prüfen, bei Treffer etwas zählen oder
summieren – begegnet dir in der Programmierung ständig, egal ob du Zahlen, Texte oder später
ganze Listen auswertest.
