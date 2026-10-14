# Karten mischen

Bis jetzt liegen die Karten immer gleich: Hund, Katze, Fuchs, Frosch – und dann noch einmal. Das ist kein Spiel, das kann man auswendig! Also wird gemischt.

Dafür brauchst du zwei Bausteine.

## Baustein 1: Zwei Einträge tauschen

Stell dir vor, du hältst in jeder Hand einen vollen Becher und willst den Inhalt tauschen. Das geht nur mit einem dritten, leeren Becher. Beim Tauschen in einer Liste ist es genauso: Du brauchst eine **Merk-Variable**. Das erste Beispiel zeigt, wie das aussieht.

Ohne Merk-Variable geht ein Wert verloren – dann hättest du plötzlich zwei Katzen und keinen Hund mehr.

## Baustein 2: Eine zufällige Stelle

`Math.random()` liefert eine zufällige Kommazahl zwischen 0 und 1, zum Beispiel `0.4721`. Daraus machst du eine Stelle in der Liste:

```js
Math.floor(Math.random() * 8)   // eine ganze Zahl von 0 bis 7
```

`Math.random() * 8` ergibt eine Kommazahl zwischen 0 und 8. `Math.floor` schneidet alles hinter dem Komma ab. Statt der festen `8` schreibst du besser die Länge der Liste – dann stimmt es auch, wenn du später mehr Karten hast.

## Beides zusammen: mischen

```
für jede Stelle i in der Liste:
  wähle eine zufällige Stelle j
  tausche die Einträge an den Stellen i und j
```

So wandert jede Karte einmal an einen zufälligen Platz.

> 💡 Echte Zufallszahlen kann man nicht vorhersagen. Deshalb prüft der Test in der Aufgabe nur zwei Dinge: Liegen die Zahlen anders als vorher? Und sind noch alle da?
