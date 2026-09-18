# Treffer! Kollision erkennen

Jetzt kommt das Herzstück jedes Fang-Spiels: Wie erkennt dein Code, ob der Ball wirklich auf dem Schläger gelandet ist? Das nennt man **Kollisionserkennung**.

Dafür brauchst du **Vergleiche** und **logische Verknüpfungen**:

```js
5 > 3          // true
5 === 5        // true (gleich)
true && false  // false – beide Seiten müssen wahr sein
true || false  // true – mindestens eine Seite muss wahr sein
```

Eine Funktion, die eine Bedingung prüft, kann das Ergebnis des Vergleichs direkt zurückgeben – du brauchst kein `if` dafür:

```js
function inBereich(x, links, rechts) {
  return x >= links && x <= rechts;
}
```

Probier das im ersten, schon fertigen Beispiel unten gleich selbst aus.

Für unseren Schläger gilt: Er ist 80 Pixel breit, seine linke Kante ist `schlaegerX`, seine rechte Kante also `schlaegerX + 80`. Ein Treffer liegt vor, wenn

- der Ball unten genug angekommen ist (`ballY >= 270`), **und**
- die x-Position des Balls zwischen der linken und der rechten Kante des Schlägers liegt.

Beide Bedingungen müssen gleichzeitig gelten – das ist also eine `&&`-Verknüpfung.

> 💡 Genau diese Funktion rufst du später in jedem Frame deiner Animationsschleife auf: Sobald `istTreffer(...)` `true` zurückgibt, zählst du einen Punkt.
