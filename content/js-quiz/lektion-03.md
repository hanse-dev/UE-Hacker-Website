# Richtig oder falsch?

Deine Knöpfe sehen gut aus, aber beim Klicken passiert noch nichts. Aus Woche 7 kennst du
`addEventListener('click', ...)`. Das funktioniert auch bei Knöpfen, die dein Code selbst erzeugt
hat – am besten gleich in der Schleife, in der sie entstehen.

Das Besondere: Jeder Knopf **merkt sich sein eigenes `i`**. Der erste Knopf kennt die 0, der zweite
die 1, der dritte die 2. Klickst du später auf einen Knopf, weiß er noch genau, welche
Nummer er hat.

```
für i von 0 bis 2:
  erzeuge den Knopf
  bei Klick auf diesen Knopf: mach etwas mit i
```

## Eine Funktion für die Antwort

Was bei einem Klick passieren soll, steckst du in eine eigene Funktion `antworte(i)`. Beim Klick
wird sie nur noch aufgerufen – mit der Nummer des Knopfs:

```js
k.addEventListener('click', () => {
  antworte(i);
});
```

So bleibt die Schleife kurz, und die ganze Quiz-Logik steht übersichtlich an einer Stelle.

## Wann ist eine Antwort richtig?

In jeder Frage steht unter `richtig` die Nummer der richtigen Antwort. Du musst also nur zwei
Zahlen vergleichen: die Nummer des angeklickten Knopfs und die Nummer aus der Frage.

```
wenn die angeklickte Nummer gleich der richtigen Nummer ist:
  zeige eine Erfolgsmeldung
sonst:
  zeige eine Fehlermeldung
```

Die Rückmeldung schreibst du in `#anzeige` – das Element steht direkt unter den Knöpfen.

> 💡 Nimm zum Vergleichen `===`. Ein einzelnes `=` wäre eine Zuweisung und würde die richtige
> Antwort überschreiben, statt sie zu vergleichen.
