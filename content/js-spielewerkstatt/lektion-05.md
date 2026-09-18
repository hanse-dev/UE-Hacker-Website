# Punkte und Game Over

Ein Spiel ohne Punktestand fühlt sich nicht wie ein richtiges Spiel an. Dafür brauchst du eine **Zustandsvariable** – eine Variable, die sich über die Zeit verändert und den aktuellen Spielstand merkt:

```js
let punkte = 0;
let leben = 3;
```

Bei jedem Treffer erhöhst du `punkte`, bei jedem verpassten Ball ziehst du `leben` ab. Deine Funktion `naechsterPunktestand(punkte, treffer)` kapselt genau diese Logik – so bleibt sie testbar, unabhängig vom Rest des Spiels.

Text auf dem Canvas gibt man mit `fillText` aus:

```js
ctx.font = '20px sans-serif';
ctx.fillText('Punkte: ' + punkte, 10, 25);
```

Für diese Lektion reicht aber `console.log` – die Ausgabe siehst du direkt unter deinem Code:

```js
console.log('Punkte: ' + punkte);
```

Ist `leben` bei `0` angekommen, ist das Spiel vorbei – „Game Over". Das prüfst du ganz normal mit einem `if`:

```js
if (leben <= 0) {
  console.log('Game Over!');
}
```

> 💡 In deinem fertigen Spiel würdest du bei Game Over die Animationsschleife stoppen, statt weiter `requestAnimationFrame` aufzurufen.
