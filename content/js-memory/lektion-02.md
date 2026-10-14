# Verdeckt und aufgedeckt

Beim Memory liegen alle Karten zuerst verdeckt. Unsere Rückseite ist ein Fragezeichen. Damit du es nicht immer wieder kopieren musst, legen wir es einmal in eine Variable:

```js
const rueckseite = '❓';
```

Aufdecken heißt dann: Bei einem Klick ändert die Karte ihren Text. Das kennst du aus Woche 7 – `addEventListener('click', ...)` funktioniert bei selbst gebauten Elementen genauso wie beim fertigen Knopf.

## Das Programm merkt sich etwas

Eine Karte hat zwei **Zustände**: verdeckt oder offen. Damit dein Programm weiß, was beim nächsten Klick passieren soll, muss es sich den Zustand merken – in einer Variable, die **außerhalb** der Klick-Funktion steht:

```
offen = false                 (am Anfang ist die Karte verdeckt)

bei jedem Klick:
  wenn offen:  Karte verdecken, offen = false
  sonst:       Karte aufdecken, offen = true
```

Das zweite Beispiel zeigt dasselbe Prinzip mit einem Lichtschalter: Die Variable `an` merkt sich, ob das Licht brennt.

> 💡 Eine Variable mit nur zwei Werten (`true` oder `false`) ist wie ein Schalter. Solche Schalter stecken in fast jedem Spiel: „Ist das Spiel vorbei?“, „Hat die Figur einen Schlüssel?“, „Liegt die Karte offen?“
