# Die Auswertung

Bisher endet dein Quiz mit einem schlichten „Quiz beendet!“. Ein richtiges Quiz zeigt am Schluss
das Ergebnis – und sagt etwas dazu.

## Ein Kommentar zum Ergebnis

Welcher Kommentar passt, hängt vom Punktestand ab. Solche Entscheidungen mit mehreren Stufen
schreibst du als kleine Funktion, die mehrere Grenzen **der Reihe nach** prüft:

```
wetterTipp(grad):
  wenn grad mindestens 25 ist: gib 'Ab ins Freibad!' zurück
  wenn grad mindestens 10 ist: gib 'Eine Jacke reicht.' zurück
  sonst: gib 'Mütze auf!' zurück
```

Die Reihenfolge ist wichtig. `return` beendet die Funktion sofort – die zweite Zeile wird also nur
erreicht, wenn die erste Bedingung **nicht** zutraf. Deshalb steht die strengste Bedingung ganz
oben.

Deine Bewertungs-Funktion bekommt zwei Werte: wie viele Antworten richtig waren und wie viele
Fragen es gab. So funktioniert sie für ein Quiz mit 3 Fragen genauso wie für eines mit 10.

> 💡 „Mindestens die Hälfte“ rechnest du mit `anzahl / 2` aus. Bei 3 Fragen ist die Hälfte 1,5 –
> mit 2 richtigen Antworten liegst du darüber, mit 1 darunter.

Wie in den Spiele-Projekten testest du die Funktion zuerst für sich mit `console.log`, bevor du
sie ins Quiz einbaust.

## Der Schlussbildschirm

Die Auswertung bekommt wieder eine eigene Funktion. Sie räumt die Seite um:

- Die Überschrift zeigt, dass das Quiz vorbei ist.
- In `#text` steht statt einer Frage das Ergebnis.
- Die Antwort-Knöpfe verschwinden – es gibt ja nichts mehr zu beantworten.

Zum Verstecken nimmst du `hidden`, das du schon vom alten Knopf kennst. Die drei Antwort-Knöpfe
stecken im Array `knoepfe`, du gehst sie also mit einer Schleife durch:

```js
for (const k of knoepfe) {
  k.hidden = true;
}
```

Den Ergebnis-Satz setzt du aus Texten und Variablen zusammen. Achte auf die Leerzeichen an den
Nahtstellen: `'Du hast ' + punkte` braucht das Leerzeichen hinter „hast“, sonst kleben Wort und
Zahl zusammen.
